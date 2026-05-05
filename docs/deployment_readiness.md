# Deployment Readiness

## Current Status

The repository is ready for final review as a prototype, not as a production healthcare system.

Working review artifacts:

- GitHub-safe processed New Jersey extract: `data/processed/final_nj_facility_sample.csv`
- Streamlit prototype: `app/streamlit_app.py`
- Source cleaning notebook: `notebooks/SAMHSA.ipynb`
- Modeling notebook: `notebooks/Modeling.ipynb`
- Small reproducible classroom notebook: `notebooks/final_facility_tier_model.ipynb`
- Data, pipeline, responsible AI, and deployment documentation in `docs/`

## Local Run Instructions

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

The app runs from the committed New Jersey processed extract and does not require API keys.

## What Is Ready

- Small data artifact suitable for GitHub review.
- Clear source lineage to SAMHSA National Mental Health Directory 2024 processing.
- Search/filter prototype for service setting, care need, payment/funding signal, city, and tier.
- Source-confidence and responsible-use language.
- K-Means tier labels available in the processed data.

## What Is Not Production Ready

- No real-time appointment or capacity feed.
- No live insurance verification.
- No clinical appropriateness model.
- No authenticated user accounts, audit logging, or privacy review.
- No production data refresh workflow.
- No formal accessibility, security, or clinical safety review.
- No validated NPPES, HRSA, payer, or quality-data integration in the final review extract.

## Review Checklist

Before final submission, confirm:

- the GitHub repository is public or otherwise shared with reviewers
- no raw large files, secrets, `.env` files, API keys, or private credentials are committed
- the notebooks have outputs stripped or are small enough for GitHub review
- the report accurately describes SAMHSA as the completed primary source
- optional sources are framed as future work unless supported by final fields
- the presentation uses the prototype as a bounded demonstration, not a production claim

## Suggested Next Improvements

- Add a reproducible script that converts the Drive source workbook into the committed processed extract.
- Add latitude/longitude or county fields if available and verified.
- Add a controlled data-refresh manifest with source URL, download date, file size, and preparer.
- Add explainable NPPES or HRSA enrichment only after transparent matching and quality checks.
- Add usability testing with likely navigator users.
