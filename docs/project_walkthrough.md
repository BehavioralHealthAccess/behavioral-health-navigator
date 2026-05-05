# Project Walkthrough

This guide is for anyone opening the repository who wants to understand the project quickly.

## Fast Reading Path

1. Start with this guide and the root `README.md`.
2. Read `docs/final_report.md` or download `docs/final_report.docx`.
3. Open `data/processed/final_nj_facility_sample.csv` to inspect the final New Jersey data extract.
4. Review `app/streamlit_app.py` to understand the prototype.
5. If running locally, use:

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

6. Review `docs/responsible_ai_memo.md` and `docs/deployment_readiness.md` before judging readiness claims.

## What The Project Is

The Behavioral Health Access Navigator is a decision-support prototype for New Jersey behavioral health navigation. It helps care coordinators, social workers, discharge planners, and community health navigators inspect public facility data and identify plausible facilities to review or contact.

The completed technical package uses processed SAMHSA National Mental Health Directory 2024 facility data. The GitHub-safe extract contains 213 New Jersey facility records with decoded service fields and derived K-Means care-bundle tier labels.

## What The Project Is Not

The prototype does not:

- confirm appointment availability
- confirm whether a facility is accepting new clients
- verify a specific person's insurance
- decide clinical appropriateness
- measure provider quality
- replace professional judgment

## Key Artifacts

| Reader Question | Artifact |
| --- | --- |
| What is the project and how should I read it? | `README.md`, `docs/project_walkthrough.md` |
| What is the polished report draft? | `docs/final_report.md`, `docs/final_report.docx` |
| What data is included in GitHub? | `data/processed/final_nj_facility_sample.csv` |
| Where is the prototype? | `app/streamlit_app.py` |
| How was the source data processed? | `notebooks/SAMHSA.ipynb`, `data/README.md`, `docs/data_pipeline.md` |
| What modeling work is included? | `notebooks/Modeling.ipynb`, `notebooks/final_facility_tier_model.ipynb` |
| What are the responsible AI boundaries? | `docs/responsible_ai_memo.md` |
| Is this deployable? | `docs/deployment_readiness.md` |

## Useful Questions

- Does the documentation explain why SAMHSA National Mental Health Directory 2024 is the completed primary source?
- Does the project distinguish K-Means tiering from KNN?
- Does the report explain what the tier labels do and do not mean?
- Does the app run from the committed 213-row extract?
- Does the data documentation explain why large raw files are not committed to GitHub?
- Does the prototype clearly identify what it cannot safely claim?

## Current Readiness

Ready as a classroom prototype: yes.

Ready for production deployment: no. The prototype needs formal data-refresh logic, user testing, accessibility review, privacy/security review, and live verification sources before it could be considered operational.
