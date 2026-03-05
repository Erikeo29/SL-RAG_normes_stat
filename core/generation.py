"""Module de generation : contexte + question -> reponse LLM avec sources."""
from __future__ import annotations

import os

from groq import Groq

from config import LLM_MODEL, SYSTEM_PROMPT
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
    # 1. Retrieval
    chunks = retrieve_relevant_chunks(user_message, collection_name=collection_name)
    context = format_context(chunks)

    # 2. Construire le prompt augmente
    augmented_prompt = (
        f"Contexte extrait des normes :\n\n{context}\n\n"
        f"---\n\nQuestion de l'utilisateur : {user_message}"
    )

    client = get_groq_client()
    if not client:
        yield "Cle API Groq non configuree.", chunks
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
