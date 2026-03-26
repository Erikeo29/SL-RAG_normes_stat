"""Module de generation : contexte + question -> reponse LLM avec sources."""
from __future__ import annotations

import os

from groq import Groq

from config import LLM_MODEL, MAX_CONTEXT_CHUNKS, SYSTEM_PROMPT
from core.retrieval import format_context, retrieve_relevant_chunks


def get_groq_client() -> Groq | None:
    """Retourne le client Groq si la cle API est disponible."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GROQ_API_KEY", None)
        except Exception:
            pass
    if api_key:
        return Groq(api_key=api_key)
    return None


def _translate_query_to_en(query: str, client: Groq | None) -> str | None:
    """Translate a French query to English for better retrieval."""
    if not client:
        return None
    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a translator. Translate the user message "
                        "from French to English. Output ONLY the English "
                        "translation, nothing else."
                    ),
                },
                {"role": "user", "content": query},
            ],
            max_tokens=200,
            temperature=0,
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        return None


def stream_rag_response(
    user_message: str,
    chat_history: list[dict],
    collection_name: str = "normes_statistique",
):
    """Genere une reponse RAG en streaming.

    Yields
    ------
    tuple[str, list[dict]]
        (text_chunk, source_chunks) -- les sources sont renvoyees avec le dernier chunk.
    """
    # 1. Retrieval - bilingual query (embedding model is EN-centric)
    client = get_groq_client()
    en_query = _translate_query_to_en(user_message, client)
    queries = [user_message]
    if en_query and en_query.lower() != user_message.lower():
        queries.append(en_query)

    seen_ids: set[str] = set()
    chunks: list[dict] = []
    for q in queries:
        for c in retrieve_relevant_chunks(
            q, n_results=MAX_CONTEXT_CHUNKS, collection_name=collection_name
        ):
            chunk_id = f"{c['source']}_{c['page']}_{hash(c['text'][:80])}"
            if chunk_id not in seen_ids:
                seen_ids.add(chunk_id)
                chunks.append(c)
    chunks.sort(key=lambda c: c["distance"])
    chunks = chunks[:MAX_CONTEXT_CHUNKS]
    context = format_context(chunks)

    # 2. Construire le prompt augmente
    augmented_prompt = (
        f"Contexte extrait des normes :\n\n{context}\n\n"
        f"---\n\nQuestion de l'utilisateur : {user_message}"
    )

    if not client:
        yield "Clé API Groq non configurée.", chunks
        return

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for msg in chat_history[-10:]:
        messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": augmented_prompt})

    try:
        stream = client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=2048,
            stream=True,
        )

        full_response = ""
        for chunk_resp in stream:
            if chunk_resp.choices[0].delta.content:
                text = chunk_resp.choices[0].delta.content
                full_response += text
                yield text, chunks

    except Exception as e:
        yield f"Erreur : {str(e)[:100]}", chunks
