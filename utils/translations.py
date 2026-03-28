"""Systeme de traduction bilingue FR/EN - Normes statistiques."""
import streamlit as st

TRANSLATIONS: dict[str, dict[str, str]] = {
    # --- App ---
    "app_title": {
        "fr": "RAG Normes statistiques",
        "en": "RAG Statistical Standards",
    },
    "app_subtitle": {
        "fr": "Assistant intelligent pour l'analyse de normes statistiques",
        "en": "Intelligent assistant for statistical standards analysis",
    },
    "hero_subtitle": {
        "fr": "Assistant RAG pour les normes statistiques, incertitudes de mesure et métrologie - GUM, ISO, ASTM",
        "en": "RAG assistant for statistical standards, measurement uncertainty and metrology - GUM, ISO, ASTM",
    },
    # --- Sidebar ---
    "sidebar_title": {
        "fr": "Navigation",
        "en": "Navigation",
    },
    "page_chat": {
        "fr": "Chat documents",
        "en": "Document chat",
    },
    "page_upload": {
        "fr": "Gestion des documents",
        "en": "Document management",
    },
    "page_matrix": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "page_about": {
        "fr": "À propos",
        "en": "About",
    },
    "page_normes": {
        "fr": "Normes statistiques",
        "en": "Statistical standards",
    },
    "annexes_title": {
        "fr": "Annexes",
        "en": "Annexes",
    },
    "db_stats_title": {
        "fr": "Base de connaissances",
        "en": "Knowledge base",
    },
    "db_docs": {
        "fr": "Documents",
        "en": "Documents",
    },
    "db_chunks": {
        "fr": "Chunks",
        "en": "Chunks",
    },
    "db_indexed_docs": {
        "fr": "Documents indexés",
        "en": "Indexed documents",
    },
    "lang_label": {
        "fr": "Langue / Language",
        "en": "Language / Langue",
    },
    "version_info": {
        "fr": (
            "**Version 1.0.0** - Janv 2026\n\n"
            "**Nouveautés :**\n"
            "- Base vectorielle pré-indexée\n"
            "- Synchronisation depuis dossier"
        ),
        "en": (
            "**Version 1.0.0** - Jan 2026\n\n"
            "**New features:**\n"
            "- Pre-indexed vector store\n"
            "- Directory sync"
        ),
    },
    "upload_locked_hint": {
        "fr": "Réservé à l'administrateur",
        "en": "Administrator only",
    },
    # --- Upload page ---
    "upload_title": {
        "fr": "Charger des documents PDF",
        "en": "Upload PDF documents",
    },
    "upload_help": {
        "fr": "Glissez vos fichiers PDF ici (JCGM, NIST, documents publics...)",
        "en": "Drop your PDF files here (JCGM, NIST, public documents...)",
    },
    "upload_domain_hint": {
        "fr": "Les documents seront indexés dans le domaine **normes statistiques**.",
        "en": "Documents will be indexed in the **statistical standards** domain.",
    },
    "upload_sync_button": {
        "fr": "Synchroniser depuis le dossier",
        "en": "Sync from directory",
    },
    "upload_sync_processing": {
        "fr": "Synchronisation en cours...",
        "en": "Syncing...",
    },
    "upload_sync_done": {
        "fr": "fichier(s) indexé(s) depuis le dossier",
        "en": "file(s) indexed from directory",
    },
    "upload_sync_uptodate": {
        "fr": "Tous les documents du dossier sont déjà indexés.",
        "en": "All documents from the directory are already indexed.",
    },
    "upload_sync_no_dir": {
        "fr": "Dossier source introuvable.",
        "en": "Source directory not found.",
    },
    "upload_button": {
        "fr": "Indexer les documents",
        "en": "Index documents",
    },
    "upload_success": {
        "fr": "documents indexés avec succès",
        "en": "documents indexed successfully",
    },
    "upload_processing": {
        "fr": "Indexation en cours...",
        "en": "Indexing in progress...",
    },
    "upload_done": {
        "fr": "Terminé !",
        "en": "Done!",
    },
    "upload_delete": {
        "fr": "Supprimer",
        "en": "Delete",
    },
    "upload_deleted": {
        "fr": "supprimé",
        "en": "deleted",
    },
    # --- Chat page ---
    "chat_placeholder": {
        "fr": "Posez une question sur l'incertitude de mesure, la métrologie...",
        "en": "Ask a question about measurement uncertainty, metrology...",
    },
    "chat_welcome": {
        "fr": (
            "Posez une question sur les documents statistiques chargés. Exemples :\n"
            "- Comment évaluer l'incertitude de type A et de type B selon le GUM ?\n"
            "- Quelle est la méthode de propagation des incertitudes (loi de propagation) ?\n"
            "- Que recommande le NIST TN 1297 pour l'expression de l'incertitude ?"
        ),
        "en": (
            "Ask a question about the uploaded statistical documents. Examples:\n"
            "- How to evaluate Type A and Type B uncertainty per the GUM?\n"
            "- What is the uncertainty propagation method (law of propagation)?\n"
            "- What does NIST TN 1297 recommend for expressing uncertainty?"
        ),
    },
    "chat_clear": {
        "fr": "Effacer la conversation",
        "en": "Clear conversation",
    },
    "chat_error": {
        "fr": "Erreur lors de la génération",
        "en": "Error during generation",
    },
    "chat_api_missing": {
        "fr": "Clé API Groq non configurée. Ajoutez GROQ_API_KEY dans les secrets.",
        "en": "Groq API key not configured. Add GROQ_API_KEY in secrets.",
    },
    "ai_disclaimer": {
        "fr": (
            "⚠️ Réponse générée par IA - peut contenir des erreurs ou omissions. "
            "Vérifiez toujours les informations auprès des textes normatifs officiels."
        ),
        "en": (
            "⚠️ AI-generated response - may contain errors or omissions. "
            "Always verify information against the official normative texts."
        ),
    },
    "sources_title": {
        "fr": "Sources",
        "en": "Sources",
    },
    "sources_relevance": {
        "fr": "pertinence",
        "en": "relevance",
    },
    "sources_page": {
        "fr": "page",
        "en": "page",
    },
    "no_documents": {
        "fr": "Aucun document indexé. Chargez des PDFs via Annexes > Gestion des documents.",
        "en": "No documents indexed. Upload PDFs via Annexes > Document management.",
    },
    # --- Matrix page ---
    "matrix_title": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "matrix_help": {
        "fr": "Croisez les exigences d'un référentiel avec vos procédures internes.",
        "en": "Cross-reference standard requirements with your internal procedures.",
    },
    "matrix_standard": {
        "fr": "Référentiel",
        "en": "Standard",
    },
    "matrix_requirements_for": {
        "fr": "Exigences",
        "en": "Requirements",
    },
    "matrix_requirement": {
        "fr": "Exigence",
        "en": "Requirement",
    },
    "matrix_status": {
        "fr": "Statut",
        "en": "Status",
    },
    "matrix_gap": {
        "fr": "Écart identifié",
        "en": "Gap identified",
    },
    "matrix_corrective_action": {
        "fr": "Action corrective",
        "en": "Corrective action",
    },
    "matrix_add_rows_hint": {
        "fr": "Ajoutez des lignes avec le bouton '+' en bas du tableau.",
        "en": "Add rows with the '+' button at the bottom of the table.",
    },
    "matrix_summary": {
        "fr": "Synthèse",
        "en": "Summary",
    },
    "matrix_compliant": {
        "fr": "Conforme",
        "en": "Compliant",
    },
    "matrix_partial": {
        "fr": "Partiel",
        "en": "Partial",
    },
    "matrix_non_compliant": {
        "fr": "Non conforme",
        "en": "Non-compliant",
    },
    "matrix_to_evaluate": {
        "fr": "À évaluer",
        "en": "To evaluate",
    },
    "matrix_search_title": {
        "fr": "Recherche dans les documents indexés",
        "en": "Search in indexed documents",
    },
    "matrix_search_placeholder": {
        "fr": "ex: incertitude de mesure, propagation, GUM, type A, type B...",
        "en": "e.g.: measurement uncertainty, propagation, GUM, type A, type B...",
    },
    "matrix_search_label": {
        "fr": "Rechercher dans les documents chargés",
        "en": "Search in uploaded documents",
    },
    "matrix_searching": {
        "fr": "Recherche en cours...",
        "en": "Searching...",
    },
    "matrix_no_results": {
        "fr": "Aucun résultat. Vérifiez que des documents sont indexés.",
        "en": "No results. Check that documents are indexed.",
    },
    "matrix_custom_empty": {
        "fr": "Personnalisé (vide)",
        "en": "Custom (empty)",
    },
    # --- About page ---
    "about_domain_statistique_desc": {
        "fr": (
            "Normes statistiques industrielles et métrologie : incertitude de mesure "
            "(GUM - JCGM 100:2008), métrologie statistique (NIST SP 260-135), "
            "expression de l'incertitude (NIST TN 1297). La page de synthèse couvre "
            "également les normes ISO/ASTM (échantillonnage, SPC, capabilité)."
        ),
        "en": (
            "Industrial statistical standards and metrology: measurement uncertainty "
            "(GUM - JCGM 100:2008), statistical metrology (NIST SP 260-135), "
            "expression of uncertainty (NIST TN 1297). The overview page also covers "
            "ISO/ASTM standards (sampling, SPC, capability)."
        ),
    },
}


def t(key: str) -> str:
    """Retourne la traduction pour la langue courante."""
    lang = st.session_state.get("lang", "fr")
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get("fr", key))
