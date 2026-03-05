"""Pipeline d'ingestion : PDF -> chunks -> embeddings -> ChromaDB.

Utilise les embeddings ONNX natifs de ChromaDB (all-MiniLM-L6-v2)
pour eviter la dependance a torch/sentence-transformers (~6 Go).
"""
from __future__ import annotations

import os

import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from config import CHROMA_PATH, CHUNK_OVERLAP, CHUNK_SIZE


def get_embedding_function() -> DefaultEmbeddingFunction:
    """Retourne la fonction d'embedding ONNX native de ChromaDB."""
    return DefaultEmbeddingFunction()


def get_chroma_client() -> chromadb.PersistentClient:
    """Retourne le client ChromaDB persistant."""
    os.makedirs(CHROMA_PATH, exist_ok=True)
    return chromadb.PersistentClient(path=CHROMA_PATH)


def get_or_create_collection(
    client: chromadb.PersistentClient,
    collection_name: str = "normes",
) -> chromadb.Collection:
    """Retourne (ou cree) la collection specifiee."""
    return client.get_or_create_collection(
        name=collection_name,
        metadata={"hnsw:space": "cosine"},
        embedding_function=get_embedding_function(),
    )


def ingest_pdf(pdf_path: str, collection_name: str = "normes") -> int:
    """Indexe un PDF dans ChromaDB. Retourne le nombre de chunks crees."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(pages)

    if not chunks:
        return 0

    client = get_chroma_client()
    collection = get_or_create_collection(client, collection_name)

    filename = os.path.basename(pdf_path)

    texts = [c.page_content for c in chunks]
    metadatas = [
        {
            "source": filename,
            "page": c.metadata.get("page", 0),
        }
        for c in chunks
    ]
    ids = [f"{filename}__chunk_{i}" for i in range(len(chunks))]

    # ChromaDB calcule les embeddings automatiquement via la embedding_function
    collection.upsert(
        ids=ids,
        documents=texts,
        metadatas=metadatas,
    )

    return len(chunks)


def ingest_directory(
    dir_path: str, collection_name: str = "normes"
) -> dict[str, int]:
    """Indexe tous les PDFs d'un dossier. Ignore ceux deja presents.

    Returns
    -------
    dict[str, int]
        {filename: n_chunks} pour chaque fichier effectivement indexe.
    """
    if not os.path.isdir(dir_path):
        return {}

    # Fichiers deja indexes
    stats = get_db_stats(collection_name)
    existing = set(stats["sources"])

    results: dict[str, int] = {}
    for fname in sorted(os.listdir(dir_path)):
        if not fname.lower().endswith(".pdf"):
            continue
        if fname in existing:
            continue
        pdf_path = os.path.join(dir_path, fname)
        # Ignorer les fichiers trop petits (< 1 Ko = probablement vides)
        if os.path.getsize(pdf_path) < 1024:
            continue
        n = ingest_pdf(pdf_path, collection_name=collection_name)
        if n > 0:
            results[fname] = n
    return results


def get_db_stats(collection_name: str = "normes") -> dict:
    """Retourne des statistiques sur la base vectorielle."""
    client = get_chroma_client()
    try:
        collection = client.get_collection(
            collection_name,
            embedding_function=get_embedding_function(),
        )
        count = collection.count()
        all_meta = collection.get(include=["metadatas"])
        sources = set()
        for m in all_meta["metadatas"]:
            sources.add(m.get("source", "inconnu"))
        return {"documents": len(sources), "chunks": count, "sources": sorted(sources)}
    except Exception:
        return {"documents": 0, "chunks": 0, "sources": []}


def delete_document(filename: str, collection_name: str = "normes") -> int:
    """Supprime tous les chunks d'un document. Retourne le nombre supprime."""
    client = get_chroma_client()
    try:
        collection = client.get_collection(
            collection_name,
            embedding_function=get_embedding_function(),
        )
        results = collection.get(where={"source": filename}, include=[])
        if results["ids"]:
            collection.delete(ids=results["ids"])
            return len(results["ids"])
    except Exception:
        pass
    return 0
