# Project Context

Project: New Jersey Behavioral Health Access Navigator

Team context: AI Campus Team 3 is in the final integration stage. Team members have explored data, built prototype pieces, worked on a pitch, and now need to bring everything together into one coherent final submission.

## Final Deliverables

The final submission should include:

- GitHub codebook/codebase
- 13-15 page project report
- Streamlit or similar prototype
- final cohort presentation on May 13, 2026

The final submission deadline is May 8, 2026.

## Core Purpose

This project helps users identify plausible behavioral health facilities in New Jersey using public data. It is intended to reduce navigation friction for people such as care coordinators, social workers, discharge planners, community health organizations, and other navigators.

The tool does not claim real-time appointment availability. It does not book appointments. It does not replace clinical or professional judgment. It is a decision-support prototype.

## Final Project Story

We built a behavioral health access navigator using public New Jersey data. The system helps users narrow and interpret facility options by service fit, location, payment or insurance signals, source confidence, and a K-Means care-bundle tier that summarizes facility service complexity.

The honest value of the project is not that it knows everything. The value is that it makes fragmented public data more usable, explainable, and bounded.

## Data Sources

The final integrated artifact is centered on one defensible public source:

- SAMHSA National Mental Health Directory 2024 facility directory material, especially the `Facilities List` worksheet and service-code reference fields.

The current practical center of the project is the cleaned and decoded SAMHSA-centered facility dataset. NPPES, HRSA, payer, and quality data remain useful future enrichment paths, but they should not be described as completed production integrations unless the team can show the exact matching logic and resulting fields.

## Data Rule

Do not upload raw GB-scale data to GitHub.

GitHub should store:

- code
- notebooks
- documentation
- small sample/demo datasets
- reproducibility instructions
- plots or screenshots needed for the report

GitHub should not store:

- full raw NPPES monthly files
- large raw source files
- ZIP archives
- local databases
- caches
- secrets or API keys

If large raw data is needed, document where it lives, how it was obtained, and how the processed demo file was created.

## Current Technical Direction

Use cleaned and decoded SAMHSA National Mental Health Directory facility data to support a behavioral health navigator prototype.

Modeling direction:

- Use K-Means clustering, not KNN, to group facilities into care-bundle or service-complexity tiers.
- Engineer features from service-related fields, such as service setting, type of care, treatment approaches, recovery support, emergency services, payment/funding, age groups, and ancillary services.
- Use tools such as pandas, scikit-learn, MultiLabelBinarizer, matplotlib, and seaborn where useful.
- Use elbow and/or silhouette plots to justify the number of clusters.
- Rename numeric clusters into plain-language tier names after inspecting their feature profiles.

Navigator direction:

- Use simple filtering or rule-based ranking for care need, location, payment/insurance, and service fit.
- Add the K-Means tier label as an interpretation layer.
- Add source-confidence labels where available to communicate provenance and uncertainty.

## Terminology Correction

Use "K-Means" consistently for the clustering model.

Do not describe the clustering model as KNN. KNN is a supervised nearest-neighbor method for classification or regression. K-Means is an unsupervised clustering method.

## Suggested Repo Layout

```text
notebooks/
  # final model notebook and exploratory notebooks
src/
  # reusable Python code if needed
app/
  # Streamlit prototype
data/
  README.md
  samples/
  processed/
docs/
  project_context.md
  responsible_ai_memo.md
  deployment_readiness.md
  source_agreement_evaluation.md
```

## Report Structure

The project report should follow the AI Campus Participant Guide rather than the pitch deck structure.

Suggested sections:

1. Problem statement and intended user
2. Data understanding
3. Data cleaning and processing
4. Baseline model or ranking logic
5. K-Means care-bundle clustering
6. Interpretation walkthrough
7. Human-in-the-loop design
8. Responsible AI memo
9. Deployment readiness
10. Limitations and next steps

## Role Lanes

Sarthak and Sangeetha: data/model work. The end goal is one notebook that runs top-to-bottom and produces facility tiers with plots and plain-language explanations.

Sarthak: prototype work. The end goal is a simple Streamlit app or demo path that shows facility results, tier labels, and honest confidence/source labels where available.

Sangeetha: data documentation. The end goal is a clear `data/README.md` explaining sources, file sizes, important columns, processed/demo files, and data limitations.

Caity: responsible AI and healthcare interpretation. The end goal is documentation that explains intended use, limitations, bias and missing-data risks, misuse scenarios, and human override rules.

Joseph: report assembly and presentation/demo narrative. The end goal is a coherent report outline and a clear 5-7 minute presentation script for other cohorts.

## Responsible AI Boundaries

The tool should be framed as a plausibility navigator, not a source of truth.

It should not claim:

- appointment availability
- provider acceptance of a specific patient today
- clinical appropriateness of a facility for a specific person
- complete or current insurance network status unless directly supported by data

The project should explain:

- where data may be missing, stale, or biased
- how source disagreement affects confidence
- when a user should reject or override the output
- why human judgment remains necessary
- how AI assistants were used responsibly during the project

## Coach Standard

Every output should be explainable in plain language by the team.

If a non-coder cannot explain the model at a high level, the model section is incomplete. If a coder cannot explain the user risk and responsible AI boundaries, the responsible AI section is incomplete.

Prefer simple, working, defensible artifacts over ambitious fragile features.
