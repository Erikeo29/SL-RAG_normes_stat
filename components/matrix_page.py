"""Page matrice de compliance : exigences norme vs procedures internes."""
import streamlit as st
import pandas as pd

from config import COLLECTION_NAME
from core.retrieval import retrieve_relevant_chunks
from utils.translations import t


REQUIREMENTS = {
    "ISO 2859-1 (échantillonnage par attributs)": [
        {"clause": "4", "requirement": "Termes et définitions (NQA, lot, échantillon)"},
        {"clause": "9", "requirement": "Niveaux de contrôle (I, II, III, S-1 à S-4)"},
        {"clause": "10", "requirement": "Code de dimension d'échantillon"},
        {"clause": "11", "requirement": "Plans d'échantillonnage simple"},
        {"clause": "12", "requirement": "Plans d'échantillonnage double"},
        {"clause": "13", "requirement": "Plans d'échantillonnage multiple"},
        {"clause": "14", "requirement": "Règles de passage (normal, renforcé, réduit)"},
    ],
    "ISO 2859-2 (plans pour lots isolés)": [
        {"clause": "5", "requirement": "Qualité limite (QL) et risque du consommateur"},
        {"clause": "6", "requirement": "Sélection du plan d'échantillonnage"},
        {"clause": "7", "requirement": "Procédures d'échantillonnage pour lots isolés"},
    ],
    "ISO 3951-1 (échantillonnage par mesures)": [
        {"clause": "5", "requirement": "NQA et niveaux de contrôle"},
        {"clause": "9", "requirement": "Méthode s (écart-type connu)"},
        {"clause": "10", "requirement": "Méthode sigma (écart-type inconnu)"},
        {"clause": "12", "requirement": "Plans pour limites de spécification bilatérales"},
        {"clause": "14", "requirement": "Règles de passage (normal, renforcé, réduit)"},
    ],
    "ISO 7870-1/-2 (cartes de contrôle SPC)": [
        {"clause": "7870-1:4", "requirement": "Concepts fondamentaux des cartes de contrôle"},
        {"clause": "7870-1:5", "requirement": "Éléments d'une carte de contrôle"},
        {"clause": "7870-2:4", "requirement": "Carte X-barre et R (moyennes et étendues)"},
        {"clause": "7870-2:5", "requirement": "Carte X-barre et S (moyennes et écarts-types)"},
        {"clause": "7870-2:6", "requirement": "Carte des individus et étendue mobile"},
        {"clause": "7870-2:7", "requirement": "Carte p (proportion de non-conformes)"},
        {"clause": "7870-2:8", "requirement": "Carte np (nombre de non-conformes)"},
        {"clause": "7870-2:9", "requirement": "Carte c (nombre de non-conformités)"},
        {"clause": "7870-2:10", "requirement": "Carte u (taux de non-conformités)"},
    ],
    "ISO 22514-1/-2 (capabilité des procédés)": [
        {"clause": "22514-1:3", "requirement": "Termes : capabilité, performance, Cp, Cpk, Pp, Ppk"},
        {"clause": "22514-1:5", "requirement": "Conditions préalables (stabilité, normalité)"},
        {"clause": "22514-2:5", "requirement": "Estimation de la capabilité machine (Cm, Cmk)"},
        {"clause": "22514-2:6", "requirement": "Estimation de la capabilité procédé (Cp, Cpk)"},
        {"clause": "22514-2:7", "requirement": "Estimation de la performance procédé (Pp, Ppk)"},
        {"clause": "22514-2:8", "requirement": "Intervalles de confiance des indices"},
        {"clause": "22514-2:A", "requirement": "Distributions non-normales et transformations"},
    ],
    "ISO 22514-7 (capabilité systèmes de mesure)": [
        {"clause": "5", "requirement": "Résolution et discrimination du système de mesure"},
        {"clause": "6", "requirement": "Incertitude de mesure (type A et type B)"},
        {"clause": "7", "requirement": "Étude de répétabilité et reproductibilité (R&R)"},
        {"clause": "8", "requirement": "Étude de linéarité et biais"},
        {"clause": "9", "requirement": "Étude de stabilité (dérive temporelle)"},
        {"clause": "10", "requirement": "Rapport capabilité système de mesure (Cg, Cgk)"},
    ],
    "ISO 16269 (interprétation statistique des données)": [
        {"clause": "16269-4:5", "requirement": "Tests de conformité d'une moyenne"},
        {"clause": "16269-6:5", "requirement": "Détermination d'un intervalle statistique de tolérance"},
        {"clause": "16269-6:6", "requirement": "Intervalle de tolérance pour loi normale"},
        {"clause": "16269-7:5", "requirement": "Intervalle de confiance de la médiane"},
        {"clause": "16269-8:5", "requirement": "Intervalles de prédiction"},
    ],
}


def _status_options() -> list[str]:
    """Retourne les options de statut dans la langue courante."""
    return [
        t("matrix_compliant"),
        t("matrix_partial"),
        t("matrix_non_compliant"),
        t("matrix_to_evaluate"),
    ]


def _get_empty_matrix(requirements: list[dict]) -> pd.DataFrame:
    """Cree un DataFrame vierge depuis une liste d'exigences."""
    if not requirements:
        return pd.DataFrame(
            columns=["clause", "requirement", "status", "gap", "action"]
        )
    df = pd.DataFrame(requirements)
    df["status"] = t("matrix_to_evaluate")
    df["gap"] = ""
    df["action"] = ""
    return df


def render_matrix_page():
    """Affiche la matrice de compliance interactive."""
    st.header(t("matrix_title"))
    st.caption(t("matrix_help"))

    # Choix du referentiel
    standard_names = list(REQUIREMENTS.keys()) + [t("matrix_custom_empty")]
    norme = st.selectbox(
        t("matrix_standard"),
        standard_names,
        key="matrix_norme",
    )

    # Reinitialiser la matrice si le referentiel change
    if st.session_state.get("_last_norme") != norme:
        st.session_state["_last_norme"] = norme
        reqs = REQUIREMENTS.get(norme, [])
        st.session_state["matrix_data"] = _get_empty_matrix(reqs)

    if "matrix_data" not in st.session_state:
        reqs = REQUIREMENTS.get(norme, [])
        st.session_state["matrix_data"] = _get_empty_matrix(reqs)

    st.subheader(f"{t('matrix_requirements_for')} — {norme}")

    if st.session_state["matrix_data"].empty:
        st.info(t("matrix_add_rows_hint"))

    edited_df = st.data_editor(
        st.session_state["matrix_data"],
        column_config={
            "clause": st.column_config.TextColumn("Clause", width="small"),
            "requirement": st.column_config.TextColumn(
                t("matrix_requirement"), width="large"
            ),
            "status": st.column_config.SelectboxColumn(
                t("matrix_status"),
                options=_status_options(),
                width="medium",
            ),
            "gap": st.column_config.TextColumn(t("matrix_gap"), width="large"),
            "action": st.column_config.TextColumn(
                t("matrix_corrective_action"), width="large"
            ),
        },
        hide_index=True,
        use_container_width=True,
        num_rows="dynamic",
        key="matrix_editor",
    )

    st.session_state["matrix_data"] = edited_df

    # Metriques de synthese
    st.markdown("---")
    st.subheader(t("matrix_summary"))
    if not edited_df.empty:
        col1, col2, col3, col4 = st.columns(4)
        counts = edited_df["status"].value_counts()
        col1.metric(
            t("matrix_compliant"),
            counts.get(t("matrix_compliant"), 0),
            border=True,
        )
        col2.metric(
            t("matrix_partial"),
            counts.get(t("matrix_partial"), 0),
            border=True,
        )
        col3.metric(
            t("matrix_non_compliant"),
            counts.get(t("matrix_non_compliant"), 0),
            border=True,
        )
        col4.metric(
            t("matrix_to_evaluate"),
            counts.get(t("matrix_to_evaluate"), 0),
            border=True,
        )

    # Recherche RAG
    st.markdown("---")
    st.subheader(t("matrix_search_title"))
    search_query = st.text_input(
        t("matrix_search_label"),
        placeholder=t("matrix_search_placeholder"),
    )
    if search_query:
        with st.spinner(t("matrix_searching")):
            chunks = retrieve_relevant_chunks(
                search_query, n_results=3, collection_name=COLLECTION_NAME
            )
        if chunks:
            for chunk in chunks:
                similarity = max(0, 1 - chunk.get("distance", 1))
                st.markdown(
                    f'<div class="source-card">'
                    f"<strong>{chunk['source']}</strong> — "
                    f"{t('sources_page')} {chunk['page'] + 1} "
                    f"({t('sources_relevance')} : {similarity:.0%})<br>"
                    f"{chunk['text'][:500]}"
                    f"</div>",
                    unsafe_allow_html=True,
                )
        else:
            st.info(t("matrix_no_results"))
