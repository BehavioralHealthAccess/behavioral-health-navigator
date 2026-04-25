# Processed Demo Data

This folder stores small processed/demo files only. Do not place full raw SAMHSA, NPPES, HRSA, payer, ZIP, database, or cache files here.

## `facility_service_demo.csv`

- Rows: 18
- Columns: 15
- Purpose: Small runnable model input for `notebooks/final_facility_tier_model.ipynb`.
- Scope: Demonstrates service-feature engineering, K-Means clustering, tier labeling, and plain-language model interpretation.
- Important note: This is a demo processed structure, not a raw source extract and not a claim of real-time facility availability.

The columns mirror the kind of cleaned SAMHSA-centered facility fields expected by the final navigator:

- facility identity and geography
- service setting
- care types
- treatment approaches
- recovery support
- emergency services
- payment options
- age groups
- ancillary services
- source-confidence notes

## Generated Output

When the notebook runs, it writes `facility_tiers_demo.csv` with the added `cluster` and `facility_tier` fields. That output can be used for the prototype or report if the team wants a static demo result.

## Replacement Path

When the final cleaned data is available, replace `facility_service_demo.csv` with a small processed SAMHSA-centered extract that keeps the same service-oriented columns. Re-run the notebook, inspect the cluster profiles, and revise the tier names if the actual feature patterns differ from the demo data.
