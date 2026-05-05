# Notebooks

This folder contains both final review notebooks and Drive-origin notebooks from the team's exploratory work.

## Notebook Inventory

| Notebook | Role | Notes |
| --- | --- | --- |
| `SAMHSA.ipynb` | Source cleaning and decoding | Copied from the team's Google Drive work as `SAMHSA_3.ipynb`. It reads the SAMHSA National Mental Health Directory 2024 workbook, loads the `Facilities List` and code reference material, decodes service fields, and exports `samhsa_filtered_data.csv`. |
| `Modeling.ipynb` | Filtering, ranking, embeddings, and tier work | Copied from the team's Google Drive work as `Modeling.ipynb`. It explores user-input filtering, semantic matching, rule scoring, K-Means tier labels, and optional Gemini-generated explanations. |
| `final_facility_tier_model.ipynb` | Small reproducible K-Means demo | Uses the committed small demo CSV so reviewers can run a compact version without raw Drive files. |

## Running Notes

The Drive-origin notebooks were developed in Google Colab and include Google Drive paths and package-install cells. To run them outside Colab, update the file paths to point to local copies of the Drive data.

The GitHub-safe processed extract for final review is:

```text
data/processed/final_nj_facility_sample.csv
```

That file is intentionally much smaller than the raw source materials and should be enough for the prototype and reviewer walkthrough.

## Data Boundary

Do not commit the full raw workbook, large national exports, local cache folders, API keys, or private credentials. Keep those materials in the shared Google Drive and document how the processed extract was created.
