"""Utilitaire de chargement de fichiers markdown depuis docs/."""
import os

import streamlit as st

from config import ROOT_DIR


def load_file_content(relative_path: str) -> str:
    """Charge un fichier markdown depuis docs/<lang>/<relative_path>.

    Pas de cache Streamlit pour permettre les mises a jour live.
    """
    lang = st.session_state.get("lang", "fr")
    full_path = os.path.join(ROOT_DIR, "docs", lang, relative_path)
    try:
        with open(full_path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"*Fichier introuvable : `{full_path}`*"
