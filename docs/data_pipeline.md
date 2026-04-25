# Data Pipeline Notes

This document explains the intended data flow for the New Jersey Behavioral Health Access Navigator. It supports `data/README.md` and should be kept in plain language so the team can defend the pipeline in the report and presentation.

## Pipeline Goal

Create a small, explainable processed facility dataset that supports:

- service-fit filtering
- location and county context
- payment or insurance signals where available
- source-confidence labels
- K-Means care-bundle or service-complexity tiering
- a Streamlit or similar prototype

The pipeline should make fragmented public data more usable. It should not imply real-time availability, appointment booking, clinical appropriateness, or complete insurance network accuracy.

## Folder Contract

Use this layout:

```text
data/
  README.md
  processed/
    # small processed demo files only
  samples/
    # small sample/demo files only

docs/
  data_pipeline.md
```

Keep these outside GitHub:

```text
raw/
interim/
cache/
large ZIP files
local databases
full NPPES monthly extracts
full raw SAMHSA, HRSA, CMS, or payer exports
```

## Step 1: Source Intake

For each raw source, record this in a shared manifest or team notes:

- source name
- official URL
- download date
- file name
- approximate file size
- format
- where the raw file lives in shared Drive
- known update cadence if available
- person who downloaded or prepared it

Minimum expected sources:

- SAMHSA N-SUMHSS or facility data
- CMS NPPES provider registry
- HRSA Mental Health HPSA data

Optional sources:

- CMS Provider Data Catalog or Care Compare data
- payer directory or quality data, only if feasible and explainable

## Step 2: SAMHSA-Centered Cleaning

SAMHSA should be the practical center of the project because it is closest to the facility-level behavioral health use case.

Recommended cleaning steps:

1. Load the selected SAMHSA public-use or facility file outside GitHub.
2. Filter to New Jersey records.
3. Keep facility identity and location fields.
4. Decode service-related fields using the source codebook.
5. Convert multi-select service variables into readable semicolon-separated fields.
6. Standardize county, city, ZIP, latitude, and longitude fields.
7. Remove obvious duplicate facility rows only when the rule is explainable.
8. Preserve enough source identifiers to trace records back to the raw file outside GitHub.

Key cleaned feature groups:

- service setting
- type of care
- treatment approaches
- recovery support
- emergency or crisis services
- payment and funding options
- age groups or populations served
- ancillary services

## Step 3: NPPES Enrichment

NPPES can support identity, NPI, specialty, and address context. It should not become the core facility source unless the team has strong matching logic.

Possible matching fields:

- organization name
- practice address
- ZIP code
- city
- NPI, if already available from another source
- taxonomy codes related to behavioral health

Recommended match labels:

- `matched_exact`
- `matched_probable`
- `not_matched`
- `not_attempted`
- `ambiguous_multiple_matches`

Use `matched_probable` or `ambiguous_multiple_matches` carefully. If a match cannot be explained in plain language, do not use it for a strong source-confidence claim.

## Step 4: HRSA Context

HRSA Mental Health HPSA data should be used as geographic access context.

Possible matching levels:

- county or county FIPS
- ZIP code if available and defensible
- geospatial boundary match if the team has latitude/longitude and a reproducible GIS workflow

Recommended fields to carry into the processed file:

- mental health HPSA status
- HPSA score
- designation type
- geography used for the match
- HRSA source date

Do not describe HRSA shortage context as facility quality or facility capacity.

## Step 5: Optional Payer or Quality Context

Use optional payer or quality data only if the team can answer:

- What source is it?
- When was it updated?
- What entity does it describe: facility, clinician, group, hospital, or plan?
- What identifier supports the match?
- What does it not tell us?

If the answers are unclear, document the source as future work instead of adding it to the demo file.

## Step 6: Source Confidence

The prototype should communicate uncertainty. A simple confidence field is enough for the final project if it is easy to explain.

Example labels:

- `SAMHSA only`: facility and services come from SAMHSA-centered processing only.
- `SAMHSA + NPPES`: facility identity or address has a defensible NPPES match.
- `SAMHSA + HRSA geography`: facility has HRSA shortage-area context by county, ZIP, or geospatial match.
- `Multiple public sources`: more than one public source supports the facility identity or context.
- `Needs verification`: match is ambiguous or important access details are missing.

Source confidence is not the same as clinical confidence. It only describes data corroboration.

## Step 7: Processed Demo Export

The processed file should be intentionally small and reviewable.

Recommended output path:

```text
data/processed/facility_service_demo.csv
```

Recommended output fields:

```text
facility_id
facility_name
county
city
state
zip
latitude
longitude
service_setting
care_types
treatment_approaches
recovery_support
emergency_services
payment_options
age_groups
ancillary_services
source_confidence
```

Optional enrichment fields:

```text
nppes_match_status
npi
primary_taxonomy
hrsa_mental_health_hpsa_status
hrsa_hpsa_score
payer_quality_context
```

Keep full raw records and large intermediate files out of GitHub.

## Step 8: Model and Prototype Use

The K-Means notebook should use the processed file to engineer service features and assign care-bundle tiers. The tier label should summarize service complexity, not quality.

The prototype can combine:

- simple filters for location, service fit, payment, and age group
- source-confidence labels
- K-Means tier labels
- responsible-use language that tells users to verify details directly

## Data Quality Checks

Before using a processed file in the final prototype, check:

- record count
- duplicate facility names and addresses
- missing county/city/ZIP values
- missing latitude/longitude values
- unexpected non-New Jersey records
- service fields that are still coded instead of decoded
- payment fields with unclear meanings
- age-group fields with inconsistent labels
- match rates for NPPES and HRSA enrichments
- whether source-confidence labels are explainable

## Final Report Language

Use language like:

> We used public behavioral health facility data as a bounded decision-support resource. The processed demo file summarizes facility services, location, payment/access signals, and source-confidence context. K-Means clustering groups facilities into care-bundle tiers based on service patterns. These tiers help navigators interpret options but do not rank quality, confirm availability, or decide clinical fit.

Avoid language like:

> The model finds the best facility.

> The tool knows which facility accepts the patient.

> The cluster proves clinical appropriateness.

Those claims are outside the project scope and outside what the data can support.
