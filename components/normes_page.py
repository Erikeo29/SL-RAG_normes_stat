"""Page de contenu normatif statistique."""
import os
import re

import streamlit as st

from config import ASSETS_PATH
from utils.data_loaders import load_file_content


def _render_markdown_with_images(content: str, image_dir: str):
    """Rendu markdown avec support des marqueurs <!-- IMG:filename.png -->."""
    parts = re.split(r"<!-- IMG:(\S+?) -->", content)
    for i, part in enumerate(parts):
        if i % 2 == 0:
            text = part.strip()
            if text:
                st.markdown(text, unsafe_allow_html=True)
        else:
            img_path = os.path.join(image_dir, part)
            if os.path.exists(img_path):
                st.image(img_path)


def render_normes_statistique_page():
    """Affiche la page de synthese des normes statistiques."""
    content = load_file_content("statistique/statistique_overview.md")
    image_dir = os.path.join(ASSETS_PATH, "images", "statistique")
    _render_markdown_with_images(content, image_dir)
