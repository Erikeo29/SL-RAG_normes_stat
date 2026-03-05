"""Page de gestion des documents : upload, indexation, suppression."""
from __future__ import annotations

import os
import tempfile

import streamlit as st

from config import COLLECTION_NAME, DOC_SOURCE_PATH
from core.ingestion import delete_document, get_db_stats, ingest_directory, ingest_pdf
from utils.translations import t


def render_upload_page():
    """Affiche la page de gestion des documents."""
    st.header(t("page_upload"))
    st.info(t("upload_domain_hint"))

    # Sync depuis dossier local
    if os.path.isdir(DOC_SOURCE_PATH):
        if st.button(t("upload_sync_button"), type="primary"):
            with st.spinner(t("upload_sync_processing")):
                results = ingest_directory(DOC_SOURCE_PATH, collection_name=COLLECTION_NAME)
            if results:
                total = sum(results.values())
                st.success(
                    f"{len(results)} {t('upload_sync_done')} ({total} chunks)"
                )
                for fname, n in results.items():
                    st.caption(f"  - {fname} ({n} chunks)")
                st.rerun()
            else:
                st.info(t("upload_sync_uptodate"))

    st.markdown("---")

    # Upload manuel
    uploaded_files = st.file_uploader(
        t("upload_help"),
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_uploader",
    )

    if uploaded_files:
        if st.button(t("upload_button"), type="primary"):
            total_chunks = 0
            progress = st.progress(0, text=t("upload_processing"))

            for i, uploaded_file in enumerate(uploaded_files):
                progress.progress(
                    (i) / len(uploaded_files),
                    text=f"{t('upload_processing')} {uploaded_file.name}",
                )

                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".pdf"
                ) as tmp:
                    tmp.write(uploaded_file.getvalue())
                    tmp_path = tmp.name

                try:
                    n_chunks = ingest_pdf(tmp_path, collection_name=COLLECTION_NAME)
                    total_chunks += n_chunks
                finally:
                    os.unlink(tmp_path)

            progress.progress(1.0, text=t("upload_done"))
            st.success(
                f"{len(uploaded_files)} {t('upload_success')} ({total_chunks} chunks)"
            )
            st.rerun()

    st.markdown("---")

    # Documents indexes
    stats = get_db_stats(collection_name=COLLECTION_NAME)
    if stats["sources"]:
        st.subheader(t("db_indexed_docs"))
        for source in stats["sources"]:
            col1, col2 = st.columns([4, 1])
            col1.write(f"📄 {source}")
            if col2.button(
                t("upload_delete"), key=f"del_{source}", type="secondary"
            ):
                n = delete_document(source, collection_name=COLLECTION_NAME)
                st.toast(f"{source} {t('upload_deleted')} ({n} chunks)")
                st.rerun()
    else:
        st.info(t("no_documents"))
