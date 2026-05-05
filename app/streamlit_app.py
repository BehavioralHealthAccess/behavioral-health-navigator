from pathlib import Path

import pandas as pd
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "final_nj_facility_sample.csv"

TEXT_COLUMNS = [
    "facility_name",
    "city",
    "zip",
    "type_of_care",
    "service_setting",
    "facility_type",
    "pharmacotherapies",
    "treatment_approaches",
    "emergency_services",
    "payment_funding",
    "payment_assistance",
    "special_programs_groups",
    "assessment_pretreatment",
    "testing",
    "recovery_support",
    "education_counseling",
    "age_groups_accepted",
    "language_services",
    "ancillary_services",
    "tier_name",
]

NEED_KEYWORDS = {
    "Any": [],
    "Crisis or urgent support": ["crisis", "emergency", "suicide"],
    "Outpatient therapy": ["outpatient", "individual psychotherapy", "group therapy", "telemedicine"],
    "Co-occurring mental health and substance use": ["co-occurring", "substance use", "integrated"],
    "Case management and care coordination": ["case management", "care coordination", "intensive case management"],
    "Housing or employment support": ["housing", "supported employment", "vocational"],
    "Peer or recovery support": ["peer support", "recovery", "mentoring"],
    "Youth or young adult support": ["children", "adolescents", "young adults", "family"],
    "Older adult support": ["seniors", "older adults"],
}

PAYMENT_OPTIONS = [
    "Any",
    "Medicaid",
    "Medicare",
    "Private health insurance",
    "Cash or self-payment",
    "State-financed health insurance plan other than Medicaid",
    "Federal military insurance",
]


@st.cache_data
def load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_PATH, dtype={"zip": "string"})
    data = data.fillna("")
    data["zip"] = data["zip"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(5)
    data["_search_text"] = data.apply(build_search_text, axis=1)
    return data


def build_search_text(row: pd.Series) -> str:
    values = [str(row.get(column, "")) for column in TEXT_COLUMNS]
    return " | ".join(values).lower()


def unique_values(data: pd.DataFrame, column: str) -> list[str]:
    if column not in data:
        return []
    values = sorted(value for value in data[column].dropna().astype(str).unique() if value)
    return values


def score_row(row: pd.Series, keywords: list[str], payment: str, query: str) -> tuple[int, str]:
    score = 0
    matches = []
    text = row["_search_text"]

    for keyword in keywords:
        if keyword in text:
            score += 2
            matches.append(keyword)

    if payment != "Any" and payment.lower() in str(row.get("payment_funding", "")).lower():
        score += 3
        matches.append(payment)

    if query and query.lower() in text:
        score += 3
        matches.append(query)

    return score, ", ".join(dict.fromkeys(matches)) if matches else "General match"


def apply_filters(
    data: pd.DataFrame,
    cities: list[str],
    setting: str,
    tiers: list[str],
    care_need: str,
    payment: str,
    query: str,
) -> pd.DataFrame:
    filtered = data.copy()

    if cities:
        filtered = filtered[filtered["city"].isin(cities)]

    if setting != "Any":
        filtered = filtered[filtered["service_setting"] == setting]

    if tiers:
        filtered = filtered[filtered["tier_name"].isin(tiers)]

    keywords = NEED_KEYWORDS[care_need]
    scored = filtered.apply(lambda row: score_row(row, keywords, payment, query), axis=1)
    filtered = filtered.assign(
        match_score=[score for score, _ in scored],
        match_signals=[signals for _, signals in scored],
    )

    if keywords or payment != "Any" or query:
        filtered = filtered[filtered["match_score"] > 0]

    return filtered.sort_values(["match_score", "facility_name"], ascending=[False, True])


def show_result_card(row: pd.Series) -> None:
    with st.container(border=True):
        left, right = st.columns([2, 1])
        with left:
            st.subheader(row["facility_name"])
            st.write(f"{row['city']}, NJ {row['zip']}")
            st.write(row.get("type_of_care", ""))
        with right:
            st.metric("Match score", int(row["match_score"]))
            st.caption(row.get("tier_name", ""))

        st.write(f"**Service setting:** {row.get('service_setting', '')}")
        st.write(f"**Matched signals:** {row.get('match_signals', '')}")
        st.write(f"**Payment/funding:** {row.get('payment_funding', '')}")
        st.write(f"**Ancillary services:** {row.get('ancillary_services', '')}")
        if row.get("phone", ""):
            st.write(f"**Phone:** {row.get('phone', '')}")
        st.caption(row.get("source_confidence", ""))


def main() -> None:
    st.set_page_config(
        page_title="NJ Behavioral Health Access Navigator",
        page_icon="",
        layout="wide",
    )

    st.title("New Jersey Behavioral Health Access Navigator")
    st.caption(
        "Decision-support prototype using processed public facility data. "
        "Verify availability, eligibility, insurance, and clinical fit directly with facilities."
    )

    if not DATA_PATH.exists():
        st.error(f"Missing data file: {DATA_PATH}")
        st.stop()

    data = load_data()

    with st.sidebar:
        st.header("Navigator Filters")
        care_need = st.selectbox("Care need", list(NEED_KEYWORDS.keys()))
        payment = st.selectbox("Payment/funding signal", PAYMENT_OPTIONS)
        setting = st.selectbox("Service setting", ["Any"] + unique_values(data, "service_setting"))
        tiers = st.multiselect("Care-bundle tier", unique_values(data, "tier_name"))
        cities = st.multiselect("City", unique_values(data, "city"))
        query = st.text_input("Search services or facility name")
        max_results = st.slider("Results shown", min_value=5, max_value=50, value=15, step=5)

    results = apply_filters(data, cities, setting, tiers, care_need, payment, query.strip())

    metric_a, metric_b, metric_c, metric_d = st.columns(4)
    metric_a.metric("Facilities in extract", len(data))
    metric_b.metric("Matching results", len(results))
    metric_c.metric("Cities represented", data["city"].nunique())
    metric_d.metric("Care tiers", data["tier_name"].nunique())

    st.divider()

    if results.empty:
        st.warning("No matching facilities found. Try broadening the filters.")
        return

    st.download_button(
        "Download filtered results",
        results.drop(columns=["_search_text"]).to_csv(index=False),
        file_name="filtered_nj_behavioral_health_facilities.csv",
        mime="text/csv",
    )

    tab_results, tab_data, tab_tiers = st.tabs(["Results", "Data Table", "Tier Counts"])

    with tab_results:
        for _, row in results.head(max_results).iterrows():
            show_result_card(row)

    with tab_data:
        display_columns = [
            "facility_name",
            "city",
            "zip",
            "phone",
            "service_setting",
            "type_of_care",
            "payment_funding",
            "tier_name",
            "match_score",
            "match_signals",
        ]
        st.dataframe(results[display_columns], use_container_width=True, hide_index=True)

    with tab_tiers:
        tier_counts = (
            results["tier_name"]
            .value_counts()
            .rename_axis("tier_name")
            .reset_index(name="facilities")
        )
        st.bar_chart(tier_counts, x="tier_name", y="facilities")
        st.dataframe(tier_counts, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
