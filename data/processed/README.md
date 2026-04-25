# Processed Demo Data

This folder stores small processed/demo files only. Do not place full raw SAMHSA, NPPES, HRSA, payer, ZIP, database, or cache files here.

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

The full `clustered_dataframe_final.csv` file should stay outside GitHub unless the team explicitly decides it is small, processed, non-sensitive, and appropriate to commit. For now, GitHub keeps only this small sample so the notebook is reproducible without uploading the larger national processed file.

## Replacement Path

When the final cleaned data is available, replace this sample with a small processed SAMHSA-centered New Jersey extract that keeps the same service-oriented columns. Re-run the notebook, inspect the cluster profiles, and revise the tier names if the actual feature patterns differ from this demo sample.
