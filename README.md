# New Jersey Behavioral Health Access Navigator

This repository is the shared technical home for the AI Campus Team 3 final project.

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
  src/
    # reusable pipeline/model code if needed
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
- large raw SAMHSA or HRSA files
- large ZIP archives
- local databases
- cache folders
- files containing secrets or API keys

## Technical Direction

Use K-Means clustering, not KNN, for the facility tiering model.

KNN is a supervised nearest-neighbor method. K-Means is the unsupervised clustering method that groups facilities into care-bundle or service-complexity tiers.

The navigator can combine:

- rule-based filtering or ranking for location, care need, payment, and service fit
- source-confidence labels from corroboration across data sources
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
