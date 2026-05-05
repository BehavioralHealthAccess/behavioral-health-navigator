# New Jersey Behavioral Health Access Navigator

This repository is the shared technical home for the AI Campus Team 3 final project.

## Coach / Reviewer Start Here

If you are reviewing this project for another team or cohort, use this path:

1. Read `docs/coach_review_guide.md` for the one-page navigation map.
2. Read the polished report draft in `docs/final_report.md` or download `docs/final_report.docx`.
3. Inspect the final GitHub-safe data extract: `data/processed/final_nj_facility_sample.csv`.
4. Review the prototype code in `app/streamlit_app.py`.
5. Run the prototype locally if desired:

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

6. Check the responsible-use boundaries in `docs/responsible_ai_memo.md` and deployment notes in `docs/deployment_readiness.md`.

This project is ready to review as a bounded classroom prototype once the repository is visible to reviewers. It is not a production healthcare system and does not verify real-time appointment availability, insurance acceptance, clinical appropriateness, or provider quality.

Final deliverables:

- GitHub codebook/codebase
- 13-15 page project report
- Streamlit or similar prototype
- Final cohort presentation on May 13, 2026

## Project Purpose

This project helps users identify plausible behavioral health facilities in New Jersey using public data. It does not claim real-time appointment availability, does not book care, and does not replace professional judgment.

The intended first users are care coordinators, social workers, discharge planners, community health workers, and other navigators who help people find behavioral health care.

## Final Project Story

We built a behavioral health access navigator using public New Jersey behavioral health data. The system helps users narrow and interpret facility options by service fit, location, payment or insurance signals, source confidence, and a K-Means care-bundle tier that summarizes facility service complexity.

This is a decision-support prototype, not a clinical authority or booking system.

## Current Review Artifacts

The final integration branch contains the core artifacts needed for coach and cohort review:

- `data/processed/final_nj_facility_sample.csv`: a GitHub-safe New Jersey extract with 213 facilities, decoded service fields, source-confidence language, and K-Means tier labels.
- `notebooks/SAMHSA.ipynb`: the Drive-origin notebook that reads the SAMHSA National Mental Health Directory 2024 workbook and creates the cleaned service file.
- `notebooks/Modeling.ipynb`: the Drive-origin notebook that explores filtering/ranking, embeddings, and tier generation.
- `notebooks/final_facility_tier_model.ipynb`: a smaller classroom-friendly notebook using the committed demo file.
- `app/streamlit_app.py`: a lightweight Streamlit prototype that runs from the committed New Jersey extract.
- `docs/final_report.docx` and `docs/final_report.md`: polished final report draft prepared from the team's Drive report and final integration artifacts.
- `docs/`: final documentation for reviewer navigation, pipeline, responsible AI, deployment readiness, source limits, report link, and presentation link.

To run the local prototype:

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Repository Structure

Use this structure as the shared working layout:

```text
behavioral-health-navigator/
  README.md
  notebooks/
    # exploration, data/model notebooks, plots
  data/
    README.md
    samples/
      # small sample/demo data only
    processed/
      # small processed demo files only
  app/
    # Streamlit prototype
  docs/
    project_context.md
    responsible_ai_memo.md
    deployment_readiness.md
    source_agreement_evaluation.md
```

## Data Rule

Do not upload raw GB-scale data files to GitHub.

GitHub should contain code, notebooks, documentation, small sample/demo data, and reproducibility instructions. Raw files should stay in the shared Drive or be referenced by official source links and download instructions.

Good to commit:

- notebooks
- Python scripts
- Streamlit app files
- documentation
- small sample/demo CSV files
- screenshots and plots needed for the report

Do not commit:

- full NPPES monthly raw files
- large raw SAMHSA, HRSA, workbook, or archive files
- large ZIP archives
- local databases
- cache folders
- files containing secrets or API keys

## Technical Direction

Use K-Means clustering, not KNN, for the facility tiering model.

KNN is a supervised nearest-neighbor method. K-Means is the unsupervised clustering method that groups facilities into care-bundle or service-complexity tiers.

The navigator can combine:

- rule-based filtering or ranking for location, care need, payment, and service fit
- source-confidence labels that describe provenance and data limitations
- K-Means tier labels that summarize facility service complexity

## Codex Instructions

Before starting any role-specific task, ask Codex to read:

- `README.md`
- `docs/project_context.md`

Treat those files as the source of truth for scope, terminology, data rules, and final deliverables.

Codex can help organize, code, clean, draft, and document. Every team member still needs to understand and defend what Codex produces. If you cannot explain a notebook cell, report paragraph, or model choice in plain language, revise it.

## Coach Standard

Prefer simple, working, defensible artifacts over ambitious fragile features.

The final submission should make clear:

- what problem the project addresses
- what public data was used
- how the data was cleaned and processed
- what the model does
- what the model does not do
- how humans should interpret or override outputs
- where the prototype fails or remains incomplete
- what the team would improve next
