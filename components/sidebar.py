"""Composant sidebar : langue, navigation, stats."""
import streamlit as st

from config import COLLECTION_NAME
from core.ingestion import get_db_stats
from utils.translations import t


def render_sidebar():
    """Affiche le sidebar avec navigation et informations."""
    with st.sidebar:
        st.title(t("app_title"))

        st.markdown("---")

        # Langue
        lang_options = {"Francais": "fr", "English": "en"}
        current_lang = st.session_state.get("lang", "fr")
        default_idx = 0 if current_lang == "fr" else 1
        selected = st.radio(
            t("lang_label"),
            options=list(lang_options.keys()),
            index=default_idx,
            horizontal=True,
            key="lang_radio",
        )
        new_lang = lang_options[selected]
        if new_lang != current_lang:
            st.session_state.lang = new_lang
            st.rerun()

        st.markdown("---")

        # Navigation
        current = st.session_state.get("current_page", "about")

        if st.button(
            t("page_about"),
            type="primary" if current == "about" else "secondary",
            use_container_width=True,
            key="btn_about",
        ):
            st.session_state.current_page = "about"
            st.rerun()

        if st.button(
            t("page_normes"),
            type="primary" if current == "normes_statistique" else "secondary",
            use_container_width=True,
            key="btn_normes",
        ):
            st.session_state.current_page = "normes_statistique"
            st.rerun()

        if st.button(
            t("page_chat"),
            type="primary" if current == "chat" else "secondary",
            use_container_width=True,
            key="btn_chat",
        ):
            st.session_state.current_page = "chat"
            st.rerun()

        st.markdown("---")

        # Stats base + documents indexes
        stats = get_db_stats(collection_name=COLLECTION_NAME)
        st.caption(t("db_stats_title"))
        st.caption(f"{stats['documents']} docs · {stats['chunks']} chunks")

        with st.expander(t("db_indexed_docs")):
            if stats["sources"]:
                for src in stats["sources"]:
                    st.caption(f"- {src}")
            st.markdown("---")
            st.button(
                t("page_upload"),
                key="btn_upload",
                use_container_width=True,
                disabled=True,
                help=t("upload_locked_hint"),
            )

        st.markdown("---")

        # Version
        st.markdown(t("version_info"))
        st.markdown("")
        st.markdown(
            "© 2025 Eric QUEAU — "
            "[MIT License](https://opensource.org/licenses/MIT)"
        )
