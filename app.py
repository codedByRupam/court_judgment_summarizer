import streamlit as st

from utils import extract_text_from_pdf, clean_text
from summarizer import summarize_text
from bullet_summary import generate_bullets
from verdict import extract_verdict
from ner import extract_entities
from section_extractor import extract_sections
from legal_summarizer import summarize_section

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Court Judgment Analyzer",
    page_icon="🏛️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    text-align:center;
}

.metric-card {
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🏛️ Legal AI")

    st.markdown("""
### AI Features

✅ PDF Text Extraction

✅ Transformer Summarization

✅ 5-Point Summary

✅ Verdict Detection

✅ Named Entity Recognition

✅ Legal Section Extraction

✅ Litigation Risk Assessment

---

### Technologies

- Python
- Streamlit
- HuggingFace Transformers
- spaCy
- PyMuPDF
""")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏛️ AI Court Judgment Analyzer")

st.markdown("""
Analyze Indian court judgments using NLP and Transformer-based AI.

### Features
- ⚖ Final Verdict Detection
- 📋 5-Point Case Summary
- 📝 AI Generated Summary
- 📚 Legal Section Analysis
- 👨‍⚖ Named Entity Recognition
- ⚠ Litigation Risk Assessment
""")

st.divider()

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Court Judgment PDF",
    type=["pdf"]
)

# --------------------------------------------------
# PROCESS PDF
# --------------------------------------------------

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF Uploaded Successfully")

    text = extract_text_from_pdf("temp.pdf")
    text = clean_text(text)

    with st.spinner("🤖 Analyzing Judgment..."):

        # -----------------------
        # SUMMARY
        # -----------------------

        summary = summarize_text(text)

        bullets = generate_bullets(text)

        # -----------------------
        # LEGAL SECTIONS
        # -----------------------

        sections = extract_sections(text)

        facts = summarize_section(
            sections["facts"]
        )

        petitioner = summarize_section(
            sections["petitioner"]
        )

        respondent = summarize_section(
            sections["respondent"]
        )

        reasoning = summarize_section(
            sections["reasoning"]
        )

        # -----------------------
        # VERDICT
        # -----------------------

        verdict = extract_verdict(text)

        if "dismissed" in verdict.lower():
            risk = "High"

        elif "allowed" in verdict.lower():
            risk = "Low"

        else:
            risk = "Medium"

        # -----------------------
        # ENTITIES
        # -----------------------

        entities = extract_entities(text)

    # --------------------------------------------------
    # METRICS
    # --------------------------------------------------

    entity_count = (
        len(entities["persons"])
        + len(entities["organizations"])
        + len(entities["dates"])
        + len(entities["locations"])
    )

    page_count = max(
        1,
        len(text.split()) // 500
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📄 Pages",
            page_count
        )

    with c2:
        st.metric(
            "🔍 Legal Entities",
            entity_count
        )

    with c3:
        st.metric(
            "⚖ Verdict",
            verdict
        )

    with c4:
        st.metric(
            "⚠ Litigation Risk",
            risk
        )

    st.divider()

    # --------------------------------------------------
    # VERDICT
    # --------------------------------------------------

    st.header("⚖ Final Verdict")

    if "dismissed" in verdict.lower():

        st.error(
            "⚖️ " + verdict.upper()
        )

    elif "allowed" in verdict.lower():

        st.success(
            "⚖️ " + verdict.upper()
        )

    else:

        st.warning(verdict)

    st.divider()

    # --------------------------------------------------
    # BULLET SUMMARY
    # --------------------------------------------------

    st.header("📋 5-Point Case Summary")

    for bullet in bullets:

        st.success(bullet)

    st.divider()

    # --------------------------------------------------
    # DETAILED SUMMARY
    # --------------------------------------------------

    with st.expander(
        "📝 Detailed AI Summary"
    ):

        st.write(summary)

    st.divider()

    # --------------------------------------------------
    # ADVANCED LEGAL ANALYSIS
    # --------------------------------------------------

    analysis_available = False

    for item in [
        facts,
        petitioner,
        respondent,
        reasoning
    ]:

        if item and item != "Section not found.":

            analysis_available = True
            break

    if analysis_available:

        with st.expander(
            "📚 Advanced Legal Analysis"
        ):

            if (
                facts
                and
                facts != "Section not found."
            ):

                st.subheader("📌 Facts")

                st.write(facts)

            if (
                petitioner
                and
                petitioner != "Section not found."
            ):

                st.subheader(
                    "👨‍💼 Petitioner Arguments"
                )

                st.write(petitioner)

            if (
                respondent
                and
                respondent != "Section not found."
            ):

                st.subheader(
                    "🏛 Respondent Arguments"
                )

                st.write(respondent)

            if (
                reasoning
                and
                reasoning != "Section not found."
            ):

                st.subheader(
                    "⚖ Court Reasoning"
                )

                st.write(reasoning)

    st.divider()

    # --------------------------------------------------
    # ENTITY ANALYSIS
    # --------------------------------------------------

    st.header(
        "📚 Extracted Legal Entities"
    )

    with st.expander(
        "👨‍⚖️ Parties / People"
    ):

        st.write(
            entities["persons"][:20]
        )

    with st.expander(
        "📅 Important Dates"
    ):

        st.write(
            entities["dates"][:20]
        )

    with st.expander(
        "🏢 Organizations"
    ):

        st.write(
            entities["organizations"][:20]
        )

    with st.expander(
        "📍 Locations"
    ):

        st.write(
            entities["locations"][:20]
        )

    st.divider()

    # --------------------------------------------------
    # REPORT
    # --------------------------------------------------

    report = f"""
========================================
AI COURT JUDGMENT ANALYSIS REPORT
========================================

FINAL VERDICT
-------------
{verdict}

LITIGATION RISK
---------------
{risk}

5 POINT SUMMARY
---------------
{chr(10).join(bullets)}

DETAILED SUMMARY
----------------
{summary}

FACTS
-----
{facts}

PETITIONER ARGUMENTS
--------------------
{petitioner}

RESPONDENT ARGUMENTS
--------------------
{respondent}

COURT REASONING
---------------
{reasoning}

PERSONS
-------
{entities['persons'][:20]}

DATES
-----
{entities['dates'][:20]}

ORGANIZATIONS
-------------
{entities['organizations'][:20]}

LOCATIONS
---------
{entities['locations'][:20]}
"""

    st.download_button(
        label="📥 Download Analysis Report",
        data=report,
        file_name="court_judgment_report.txt",
        mime="text/plain"
    )