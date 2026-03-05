"""Systeme de traduction bilingue FR/EN — Normes statistiques."""
import streamlit as st

TRANSLATIONS: dict[str, dict[str, str]] = {
    # --- App ---
    "app_title": {
        "fr": "Normes statistiques",
        "en": "Statistical Standards",
    },
    "app_subtitle": {
        "fr": "Assistant intelligent pour l'analyse de normes statistiques",
        "en": "Intelligent assistant for statistical standards analysis",
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
        "fr": "A propos",
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
        "fr": "Documents indexes",
        "en": "Indexed documents",
    },
    "lang_label": {
        "fr": "Langue / Language",
        "en": "Language / Langue",
    },
    "version_info": {
        "fr": (
            "**Version 1.0.0** — Mars 2026\n\n"
            "**App dediee normes statistiques**\n"
            "- Base vectorielle pre-indexee\n"
            "- Synchronisation depuis dossier"
        ),
        "en": (
            "**Version 1.0.0** — Mar 2026\n\n"
            "**Dedicated statistical standards app**\n"
            "- Pre-indexed vector store\n"
            "- Directory sync"
        ),
    },
    # --- Upload page ---
    "upload_title": {
        "fr": "Charger des documents PDF",
        "en": "Upload PDF documents",
    },
    "upload_help": {
        "fr": "Glissez vos fichiers PDF ici (ISO, ASTM, JCGM, NIST...)",
        "en": "Drop your PDF files here (ISO, ASTM, JCGM, NIST...)",
    },
    "upload_domain_hint": {
        "fr": "Les documents seront indexes dans le domaine **normes statistiques**.",
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
        "fr": "fichier(s) indexe(s) depuis le dossier",
        "en": "file(s) indexed from directory",
    },
    "upload_sync_uptodate": {
        "fr": "Tous les documents du dossier sont deja indexes.",
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
        "fr": "documents indexes avec succes",
        "en": "documents indexed successfully",
    },
    "upload_processing": {
        "fr": "Indexation en cours...",
        "en": "Indexing in progress...",
    },
    "upload_done": {
        "fr": "Termine !",
        "en": "Done!",
    },
    "upload_delete": {
        "fr": "Supprimer",
        "en": "Delete",
    },
    "upload_deleted": {
        "fr": "supprime",
        "en": "deleted",
    },
    # --- Chat page ---
    "chat_placeholder": {
        "fr": "Posez une question sur les normes statistiques...",
        "en": "Ask a question about statistical standards...",
    },
    "chat_welcome": {
        "fr": (
            "Posez une question sur les documents statistiques charges. Exemples :\n"
            "- Quel est le plan d'echantillonnage pour un NQA de 1.0 selon l'ISO 2859-1 ?\n"
            "- Comment calculer les limites de controle d'une carte X-barre ?\n"
            "- Quels sont les indices de capabilite Cp et Cpk selon l'ISO 22514 ?"
        ),
        "en": (
            "Ask a question about the uploaded statistical documents. Examples:\n"
            "- What is the sampling plan for an AQL of 1.0 per ISO 2859-1?\n"
            "- How to compute control limits for an X-bar chart?\n"
            "- What are the Cp and Cpk capability indices per ISO 22514?"
        ),
    },
    "chat_clear": {
        "fr": "Effacer la conversation",
        "en": "Clear conversation",
    },
    "chat_error": {
        "fr": "Erreur lors de la generation",
        "en": "Error during generation",
    },
    "chat_api_missing": {
        "fr": "Cle API Groq non configuree. Ajoutez GROQ_API_KEY dans les secrets.",
        "en": "Groq API key not configured. Add GROQ_API_KEY in secrets.",
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
        "fr": "Aucun document indexe. Chargez des PDFs via Annexes > Gestion des documents.",
        "en": "No documents indexed. Upload PDFs via Annexes > Document management.",
    },
    # --- Matrix page ---
    "matrix_title": {
        "fr": "Matrice de compliance",
        "en": "Compliance matrix",
    },
    "matrix_help": {
        "fr": "Croisez les exigences d'un referentiel avec vos procedures internes.",
        "en": "Cross-reference standard requirements with your internal procedures.",
    },
    "matrix_standard": {
        "fr": "Referentiel",
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
        "fr": "Ecart identifie",
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
        "fr": "Synthese",
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
        "fr": "A evaluer",
        "en": "To evaluate",
    },
    "matrix_search_title": {
        "fr": "Recherche dans les documents indexes",
        "en": "Search in indexed documents",
    },
    "matrix_search_placeholder": {
        "fr": "ex: plan d'echantillonnage, NQA, carte de controle, capabilite...",
        "en": "e.g.: sampling plan, AQL, control chart, capability...",
    },
    "matrix_search_label": {
        "fr": "Rechercher dans les documents charges",
        "en": "Search in uploaded documents",
    },
    "matrix_searching": {
        "fr": "Recherche en cours...",
        "en": "Searching...",
    },
    "matrix_no_results": {
        "fr": "Aucun resultat. Verifiez que des documents sont indexes.",
        "en": "No results. Check that documents are indexed.",
    },
    "matrix_custom_empty": {
        "fr": "Personnalise (vide)",
        "en": "Custom (empty)",
    },
    # --- About page ---
    "about_domain_statistique_desc": {
        "fr": (
            "Normes statistiques industrielles : echantillonnage (ISO 2859, ISO 3951), "
            "cartes de controle SPC (ISO 7870), capabilite des procedes (ISO 22514), "
            "interpretation statistique des donnees (ISO 16269)."
        ),
        "en": (
            "Industrial statistical standards: sampling (ISO 2859, ISO 3951), "
            "SPC control charts (ISO 7870), process capability (ISO 22514), "
            "statistical interpretation of data (ISO 16269)."
        ),
    },
}


def t(key: str) -> str:
    """Retourne la traduction pour la langue courante."""
    lang = st.session_state.get("lang", "fr")
    entry = TRANSLATIONS.get(key, {})
    return entry.get(lang, entry.get("fr", key))
