# Processed Demo Data

This folder stores small processed/demo files only. Do not place full raw SAMHSA, NPPES, HRSA, payer, ZIP, database, or cache files here.

## `final_nj_facility_sample.csv`

- Rows: 213
- Columns: 57
- Source: New Jersey subset of the team's processed `clustered_dataframe_final.csv` artifact from Google Drive.
- Primary source lineage: SAMHSA National Mental Health Directory 2024 workbook, especially the `Facilities List` worksheet and decoded service-code fields.
- Purpose: final GitHub-safe data extract for the Streamlit prototype, report walkthrough, and coach review.
- Scope: New Jersey behavioral health facilities only.
- Important note: this is processed public facility data. It is not a real-time appointment, capacity, quality, or insurance-eligibility feed.

Tier distribution in this extract:

| Tier | Rows |
| --- | ---: |
| Essential Support Services | 69 |
| Structured Clinical & Family Support | 56 |
| Peer & Community-Led Services | 53 |
| Specialized Chronic Care | 19 |
| Comprehensive Support Hub | 16 |

The extract keeps the decoded facility service fields used by the team notebooks, including service setting, treatment approaches, emergency services, payment/funding signals, special programs, recovery support, age groups, ancillary services, original `cluster_label`, and plain-language `tier_name`.

Two review helper fields were added during final integration:

- `source_confidence`: explains that the row comes from SAMHSA National Mental Health Directory 2024 processing with decoded services and derived K-Means tier.
- `data_scope`: marks the file as a New Jersey processed extract for final prototype review.

## `facility_service_demo.csv`

- Rows: 15
- Columns: 15
- Source: small New Jersey sample derived from the local processed file `clustered_dataframe_final.csv` in Downloads.
- Full local file shape: 8,319 rows and 55 columns.
- New Jersey subset in the local file: 213 rows.
- Purpose: runnable model input for `notebooks/final_facility_tier_model.ipynb`.
- Scope: demonstrates service-feature engineering, K-Means clustering, tier labeling, and plain-language model interpretation.
- Important note: this is a small processed sample, not a raw source extract and not a claim of real-time facility availability.

The committed sample is balanced across the five tier names already present in the processed local file:

- Comprehensive Support Hub
- Essential Support Services
- Peer & Community-Led Services
- Specialized Chronic Care
- Structured Clinical & Family Support

The columns include:

- facility name and New Jersey location fields
- type of care
- service setting
- facility type
- treatment approaches
- emergency services
- payment/funding signals
- recovery support
- age groups accepted
- ancillary services
- original `cluster_label` and `tier_name` from the local processed file

## Generated Output

When the notebook runs, it writes `facility_tiers_demo.csv` with the added `model_cluster` and `model_tier_name` fields. That output can be used for the prototype or report if the team wants a static demo result.

## Full Data Rule

The full national `clustered_dataframe_final.csv` file should stay outside GitHub unless the team explicitly decides it is small, processed, non-sensitive, and appropriate to commit. For final review, GitHub keeps the New Jersey processed extract and the small notebook demo file.

## Replacement Path

When the final cleaned data is available, replace this sample with a small processed SAMHSA-centered New Jersey extract that keeps the same service-oriented columns. Re-run the notebook, inspect the cluster profiles, and revise the tier names if the actual feature patterns differ from this demo sample.
