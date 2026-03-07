"""RAG normes statistiques — Point d'entree Streamlit."""
import os

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

from config import CSS_PATH
from components.sidebar import render_sidebar
from components.chat_page import render_chat_page
from components.upload_page import render_upload_page
from components.about_page import render_about_page
from components.normes_page import render_normes_statistique_page
from utils.translations import t


# --- Page config ---
st.set_page_config(
    page_title="RAG Normes Statistiques",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Authentication ---
_cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml")
with open(_cfg_path) as _f:
    _auth_config = yaml.load(_f, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    _auth_config["credentials"],
    _auth_config["cookie"]["name"],
    _auth_config["cookie"]["key"],
    _auth_config["cookie"]["expiry_days"],
)

authenticator.login()

if not st.session_state.get("authentication_status"):
    if st.session_state.get("authentication_status") is False:
        st.error("Identifiants incorrects / Invalid credentials")
    else:
        st.info("Entrez vos identifiants / Enter your credentials")
    st.stop()

authenticator.logout(location="sidebar")

try:
    with open(_cfg_path, "w") as _f:
        yaml.dump(_auth_config, _f, default_flow_style=False)
except OSError:
    pass

# --- Session state init ---
if "lang" not in st.session_state:
    st.session_state.lang = "fr"
if "current_page" not in st.session_state:
    st.session_state.current_page = "about"
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
if "chat_sources" not in st.session_state:
    st.session_state.chat_sources = []


# --- CSS + boutons de navigation ---
def load_custom_css(path: str) -> str:
    """Charge le CSS et retourne le HTML complet (CSS + boutons navigation)."""
    try:
        with open(path, encoding="utf-8") as f:
            css_content = f.read()
    except FileNotFoundError:
        css_content = ""

    nav_buttons_html = (
        '<a href="#top" class="nav-button back-to-top"'
        ' title="Retour en haut / Back to top">&#9650;</a>'
        '<a href="#bottom" class="nav-button scroll-to-bottom"'
        ' title="Aller en bas / Go to bottom">&#9660;</a>'
        '<div id="top"></div>'
    )
    return f"<style>{css_content}</style>{nav_buttons_html}"


st.markdown(load_custom_css(CSS_PATH), unsafe_allow_html=True)


# --- Sidebar ---
render_sidebar()


# --- Routing ---
page = st.session_state.current_page

if page == "chat":
    render_chat_page()
elif page == "upload":
    render_upload_page()
elif page == "normes_statistique":
    render_normes_statistique_page()
elif page == "about":
    render_about_page()

# Ancre de bas de page
st.markdown('<div id="bottom"></div>', unsafe_allow_html=True)
