# New Jersey Behavioral Health Access Navigator

This repository contains the final project package for AI Campus Team 3's New Jersey Behavioral Health Access Navigator.

## Start Here

This repository is organized so a reader can move from project overview to working artifacts without needing outside context. A good path is:

1. Read `docs/project_walkthrough.md` for the one-page project map.
2. Read the polished report draft in `docs/final_report.md` or download `docs/final_report.docx`.
3. Inspect the final GitHub-safe data extract: `data/processed/final_nj_facility_sample.csv`.
4. Review the prototype code in `app/streamlit_app.py`.
5. Run the prototype locally if desired:

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

6. Check the responsible-use boundaries in `docs/responsible_ai_memo.md` and deployment notes in `docs/deployment_readiness.md`.

This project is a bounded classroom prototype. It is not a production healthcare system and does not verify real-time appointment availability, insurance acceptance, clinical appropriateness, or provider quality.

Project outputs:

- 13-15 page project report
- GitHub code, notebooks, and data documentation
- Streamlit prototype
- Final cohort presentation on May 13, 2026

## Project Purpose

This project helps users identify plausible behavioral health facilities in New Jersey using public data. It does not claim real-time appointment availability, does not book care, and does not replace professional judgment.

The intended first users are care coordinators, social workers, discharge planners, community health workers, and other navigators who help people find behavioral health care.

## Final Project Story

We built a behavioral health access navigator using public New Jersey behavioral health data. The system helps users narrow and interpret facility options by service fit, location, payment or insurance signals, source confidence, and a precomputed K-Means care-bundle tier that summarizes facility service complexity.

This is a decision-support prototype, not a clinical authority or booking system.

## Current Artifacts

The repository contains the core artifacts needed to understand, run, and evaluate the project:

- `data/processed/final_nj_facility_sample.csv`: a GitHub-safe New Jersey extract with 213 facilities, decoded service fields, source-confidence language, and K-Means tier labels.
- `notebooks/SAMHSA.ipynb`: the Drive-origin notebook that reads the SAMHSA National Mental Health Directory 2024 workbook and creates the cleaned service file.
- `notebooks/Modeling.ipynb`: the Drive-origin notebook that explores filtering/ranking, embeddings, and tier generation.
- `notebooks/final_facility_tier_model.ipynb`: a smaller classroom-friendly notebook using the committed demo file.
- `app/streamlit_app.py`: a lightweight Streamlit prototype that runs from the committed New Jersey extract.
- `docs/final_report.docx` and `docs/final_report.md`: polished final report prepared from the team's Drive report and final integration artifacts. The team should review the editable DOCX and export the final PDF manually before submission.
- `docs/`: final documentation for project navigation, pipeline, responsible AI, deployment readiness, source limits, report link, and presentation link.

## Repository Structure

```text
behavioral-health-navigator/
  README.md
  app/
    streamlit_app.py
  data/
    README.md
    processed/
      final_nj_facility_sample.csv
  notebooks/
    # exploration, data/model notebooks, plots
  docs/
    project_walkthrough.md
    final_report.md
    final_report.docx
    project_context.md
    responsible_ai_memo.md
    deployment_readiness.md
    source_agreement_evaluation.md
```

## Data Included

The repository includes a GitHub-safe processed New Jersey extract:

```text
data/processed/final_nj_facility_sample.csv
```

This file contains 213 New Jersey facility records derived from the team's SAMHSA National Mental Health Directory 2024 processing workflow. It includes decoded service fields, payment/funding signals, ancillary-service fields, source-confidence language, and K-Means care-bundle tier labels.

The full raw workbook and larger intermediate files are not included in this repository. See `data/README.md` and `docs/data_pipeline.md` for source details and reproducibility notes.

## Modeling Summary

The repository includes two different modeling ideas, and they should not be conflated:

- Facility tiering: `notebooks/Modeling.ipynb` trains K-Means on binarized service indicators and assigns five plain-language care-bundle tiers. The committed New Jersey extract stores those outputs as precomputed `cluster_label` and `tier_name` fields. `notebooks/final_facility_tier_model.ipynb` is a smaller runnable K-Means demonstration using the committed demo CSV.
- Ranking exploration: `notebooks/Modeling.ipynb` also explores sentence-transformer cosine similarity plus rule-based scoring for candidate ranking.
- Prototype runtime: `app/streamlit_app.py` does not rerun K-Means, KNN, or embedding similarity. It loads the committed 213-row extract, applies deterministic filters and keyword/payment/query match scores, and displays the precomputed tier label.

Use "K-Means tier labels" for the care-bundle clustering work. Do not describe the project as using KNN. KNN is a supervised nearest-neighbor method, while K-Means is the unsupervised clustering method used for the tier labels.

The tier labels summarize service bundles and service complexity. They are not quality scores, referral decisions, or clinical recommendations.

## Responsible Use

This project should be read as a navigation prototype. It can help a human user narrow a list of plausible facilities, but it cannot verify:

- real-time appointment availability
- whether a facility is accepting new clients
- insurance acceptance for a specific person
- clinical appropriateness
- provider quality
- current capacity or wait times

Human verification and professional judgment remain necessary before any referral or care-planning decision.
