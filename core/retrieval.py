"""Module de retrieval : query -> chunks pertinents depuis ChromaDB."""
from __future__ import annotations

from core.ingestion import get_chroma_client, get_or_create_collection
from config import MAX_CONTEXT_CHUNKS


def retrieve_relevant_chunks(
    query: str,
    n_results: int = MAX_CONTEXT_CHUNKS,
    collection_name: str = "normes",
) -> list[dict]:
    """Recherche les chunks les plus pertinents pour une question.

    ChromaDB calcule l'embedding de la query automatiquement
    via la embedding_function configuree sur la collection.

    Returns
    -------
    list[dict]
        Chaque dict contient 'text', 'source', 'page', 'distance'.
    """
    client = get_chroma_client()
    try:
        collection = get_or_create_collection(client, collection_name)
    except Exception:
        return []

    if collection.count() == 0:
        return []

    results = collection.query(
        query_texts=[query],
        n_results=min(n_results, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    chunks = []
    for i, doc in enumerate(results["documents"][0]):
        if not doc:
            continue
        meta = results["metadatas"][0][i] or {}
        distance = results["distances"][0][i]
        chunks.append(
            {
                "text": doc,
                "source": meta.get("source", "inconnu"),
                "page": meta.get("page", 0),
                "distance": distance,
            }
        )

    return chunks


def format_context(chunks: list[dict]) -> str:
    """Formate les chunks en contexte pour le LLM."""
    if not chunks:
        return "Aucun document pertinent trouve dans la base."

    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        context_parts.append(
            f"[Source {i}: {chunk['source']}, page {chunk['page'] + 1}]\n"
            f"{chunk['text']}"
        )
    return "\n\n---\n\n".join(context_parts)
