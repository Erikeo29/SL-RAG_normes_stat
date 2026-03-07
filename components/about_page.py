"""Page a propos : description du projet et architecture."""
import streamlit as st

from config import COLLECTION_NAME
from core.ingestion import get_db_stats
from utils.translations import t


def render_about_page():
    """Affiche la page a propos."""
    lang = st.session_state.get("lang", "fr")
    stats = get_db_stats(collection_name=COLLECTION_NAME)

    if lang == "fr":
        _render_fr(stats)
    else:
        _render_en(stats)


def _render_fr(stats: dict):
    st.header("À propos")

    st.subheader("Objectif")
    st.markdown(
        "Cette application est un **assistant intelligent** pour l'analyse de normes "
        "statistiques industrielles. Elle utilise la technologie **RAG** "
        "(Retrieval-Augmented Generation) pour permettre de poser des questions "
        "en langage naturel sur les documents chargés."
    )

    st.warning(
        "**Prototype** — Cette application est un outil exploratoire. Les normes "
        "indexées sont des documents publics dont l'actualité et l'exactitude doivent "
        "être vérifiées avant toute utilisation. L'assistant IA est un guide : il peut "
        "commettre des erreurs ou des omissions. Pour toute décision, référez-vous "
        "systématiquement aux textes normatifs officiels dans leur version en vigueur."
    )

    st.markdown("---")

    st.subheader("Domaine couvert")
    st.markdown(t("about_domain_statistique_desc"))
    st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.markdown("---")

    st.subheader("Fonctionnalités")
    st.markdown(
        "- **Chat RAG** : posez des questions en langage naturel, obtenez des réponses "
        "avec références aux documents sources\n"
        "- **Synthèse des normes** : vue d'ensemble structurée des normes statistiques\n"
        "- **Bilingue** : français et anglais"
    )

    st.markdown("---")

    st.subheader("Cas d'usage")
    st.markdown(
        "- Comprendre les méthodes d'évaluation de l'incertitude de mesure (GUM)\n"
        "- Consulter les recommandations NIST sur l'incertitude et la métrologie\n"
        "- Explorer les concepts statistiques fondamentaux (intervalles, propagation)\n"
        "- Parcourir la synthèse des normes statistiques industrielles (ISO, ASTM)"
    )

    st.markdown("---")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Découpage en chunks -> Embeddings -> ChromaDB\n"
        "                                                      |\n"
        "Question -> Embedding -> Recherche sémantique -> Chunks pertinents\n"
        "                                                      |\n"
        "               Chunks + Question -> LLM (Llama 3.3) -> Réponse sourcée",
        language=None,
    )

    st.markdown("---")

    st.subheader("Composants techniques")
    st.markdown(
        "| Composant | Technologie |\n"
        "|-----------|-------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Base vectorielle | ChromaDB (persistante, locale) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.markdown("---")

    st.caption(
        "Les documents chargés dans ce RAG sont des documents publics et gratuits "
        "(JCGM/BIPM, NIST)."
    )


def _render_en(stats: dict):
    st.header("About")

    st.subheader("Purpose")
    st.markdown(
        "This application is an **intelligent assistant** for analyzing industrial "
        "statistical standards. It uses **RAG** (Retrieval-Augmented Generation) "
        "technology to allow natural language questions on uploaded documents."
    )

    st.warning(
        "**Prototype** — This application is an exploratory tool. The indexed standards "
        "are public documents whose currency and accuracy must be verified before any "
        "use. The AI assistant is a guide: it may produce errors or omissions. For any "
        "decision, always refer to the official normative texts in their current version."
    )

    st.markdown("---")

    st.subheader("Domain covered")
    st.markdown(t("about_domain_statistique_desc"))
    st.caption(f"{stats['documents']} documents, {stats['chunks']} chunks")

    st.markdown("---")

    st.subheader("Features")
    st.markdown(
        "- **RAG Chat**: ask natural language questions, get answers with source references\n"
        "- **Standards overview**: structured summary of statistical standards\n"
        "- **Bilingual**: French and English"
    )

    st.markdown("---")

    st.subheader("Use cases")
    st.markdown(
        "- Understand measurement uncertainty evaluation methods (GUM)\n"
        "- Consult NIST recommendations on uncertainty and metrology\n"
        "- Explore fundamental statistical concepts (intervals, propagation)\n"
        "- Browse the overview of industrial statistical standards (ISO, ASTM)"
    )

    st.markdown("---")

    st.subheader("Architecture")
    st.code(
        "PDF Upload -> Chunking -> Embeddings -> ChromaDB\n"
        "                                           |\n"
        "Question -> Embedding -> Semantic search -> Relevant chunks\n"
        "                                           |\n"
        "            Chunks + Question -> LLM (Llama 3.3) -> Sourced answer",
        language=None,
    )

    st.markdown("---")

    st.subheader("Technical components")
    st.markdown(
        "| Component | Technology |\n"
        "|-----------|------------|\n"
        "| Interface | Streamlit |\n"
        "| Embeddings | ChromaDB ONNX (all-MiniLM-L6-v2) |\n"
        "| Vector store | ChromaDB (persistent, local) |\n"
        "| LLM | Llama 3.3 70B via Groq API |\n"
        "| PDF parsing | PyPDF |\n"
        "| Chunking | LangChain RecursiveCharacterTextSplitter |"
    )

    st.markdown("---")

    st.caption(
        "All documents loaded in this RAG are free, publicly available documents "
        "(JCGM/BIPM, NIST)."
    )
