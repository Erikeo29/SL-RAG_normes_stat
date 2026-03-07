"""Page principale : chat RAG avec les documents statistiques."""
import streamlit as st

from config import COLLECTION_NAME
from core.generation import stream_rag_response
from core.ingestion import get_db_stats
from utils.translations import t


def render_chat_page():
    """Affiche l'interface de chat RAG."""
    stats = get_db_stats(collection_name=COLLECTION_NAME)
    if stats["chunks"] == 0:
        st.warning(t("no_documents"))
        return

    if st.button(t("chat_clear"), type="secondary"):
        st.session_state.chat_messages = []
        st.session_state.chat_sources = []
        st.rerun()

    if not st.session_state.chat_messages:
        st.info(t("chat_welcome"))

    with st.container(height=500):
        for i, msg in enumerate(st.session_state.chat_messages):
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg["role"] == "assistant":
                    st.caption(t("ai_disclaimer"))
                    if i < len(st.session_state.chat_sources):
                        sources = st.session_state.chat_sources[i]
                        if sources:
                            _render_sources(sources)

        if prompt := st.chat_input(t("chat_placeholder")):
            st.session_state.chat_messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            st.session_state.chat_sources.append(None)

            with st.chat_message("assistant"):
                response_chunks = []
                source_chunks = []

                def response_generator():
                    for text_chunk, sources in stream_rag_response(
                        prompt,
                        st.session_state.chat_messages,
                        collection_name=COLLECTION_NAME,
                    ):
                        response_chunks.append(text_chunk)
                        if sources:
                            source_chunks.clear()
                            source_chunks.extend(sources)
                        yield text_chunk

                st.write_stream(response_generator())
                st.caption(t("ai_disclaimer"))

                if source_chunks:
                    _render_sources(source_chunks)

            full_response = "".join(response_chunks)
            st.session_state.chat_messages.append(
                {"role": "assistant", "content": full_response}
            )
            st.session_state.chat_sources.append(source_chunks)


def _render_sources(chunks: list[dict]):
    """Affiche les sources utilisees pour une reponse."""
    with st.expander(f"{t('sources_title')} ({len(chunks)})"):
        for i, chunk in enumerate(chunks, 1):
            similarity = max(0, 1 - chunk.get("distance", 1))
            st.markdown(
                f'<div class="source-card">'
                f"<strong>[{i}] {chunk['source']}</strong> — "
                f"{t('sources_page')} {chunk['page'] + 1} "
                f"({t('sources_relevance')} : {similarity:.0%})<br>"
                f"<em>{(chunk.get('text') or '')[:200]}...</em>"
                f"</div>",
                unsafe_allow_html=True,
            )
