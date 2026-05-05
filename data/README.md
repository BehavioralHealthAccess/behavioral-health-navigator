# Data Documentation

This folder documents the data used by the New Jersey Behavioral Health Access Navigator. It should contain documentation and small processed or demo files only.

The navigator is a decision-support prototype. It helps care coordinators, social workers, discharge planners, community health workers, and other navigators interpret plausible behavioral health facility options. It does not show real-time appointment availability, book care, determine clinical appropriateness, or replace professional judgment.

## Data Storage Rule

Do not upload raw GB-scale data to GitHub.

Use GitHub for:

- documentation
- notebooks and source code
- small processed or demo datasets
- source links and reproducibility notes
- plots or screenshots needed for the report

Do not use GitHub for:

- full raw source workbooks or national exports
- large raw SAMHSA, NPPES, HRSA, payer, or quality files
- ZIP archives
- local databases
- cache folders
- secrets, API keys, or private credentials

Raw source files should live in the team's shared Google Drive or be re-downloaded from official public sources.

## Final Data Story

The final integrated dataset is centered on SAMHSA National Mental Health Directory 2024 facility directory material. The team used the source workbook, especially the `Facilities List` worksheet and service-code reference fields, to build a cleaned and decoded facility file.

The GitHub-safe final review extract is:

```text
data/processed/final_nj_facility_sample.csv
```

That file contains 213 New Jersey facility rows, decoded service descriptions, payment/funding signals, recovery and ancillary support fields, and K-Means-derived tier labels. It is a processed extract suitable for prototype review, not a raw source file.

## Current Pipeline Summary

High-level flow:

1. Store the raw SAMHSA National Mental Health Directory 2024 workbook in shared Google Drive, not GitHub.
2. Load the `Facilities List` worksheet and service-code reference material in `notebooks/SAMHSA.ipynb`.
3. Clean and decode service, setting, payment/funding, recovery support, age group, and ancillary-service fields.
4. Export the cleaned facility file used for modeling.
5. Use `notebooks/Modeling.ipynb` to explore filtering, rule scoring, semantic matching, and K-Means service-tier labels.
6. Filter the processed artifact to New Jersey records.
7. Commit the 213-row New Jersey processed extract to GitHub for final review and prototype use.
8. Use the tier label as interpretation context, not as a clinical recommendation or quality score.

More detailed pipeline notes are in `docs/data_pipeline.md`.

## Source 1: SAMHSA National Mental Health Directory 2024

Primary source used in the final integration:

- SAMHSA National Mental Health Directory 2024 workbook, stored in the team's shared Google Drive.
- Main worksheet used: `Facilities List`.
- Reference material used: service-code reference fields where available.

Official context:

- SAMHSA data portal: https://www.samhsa.gov/data/
- FindTreatment.gov public facility lookup context: https://findtreatment.gov/

What it provides:

- Behavioral health facility names and New Jersey location fields.
- Facility service setting and type of care.
- Treatment approaches, recovery support, emergency services, payment/funding, age groups, special programs, and ancillary services.
- Public facility directory information that can support a bounded navigator prototype.

Main use in this project:

- Primary facility-level source for the navigator.
- Main input for service-fit filters, precomputed K-Means care-bundle tier labels, and prototype display.

Known limitations:

- The directory is not a real-time availability feed.
- It does not confirm whether a facility is accepting new clients today.
- It does not prove clinical appropriateness for a specific person.
- It does not confirm a specific person's current insurance eligibility.
- Multiple-response service fields require careful decoding and interpretation.
- Records may be stale, incomplete, or inconsistent.

## Optional Future Source: NPPES Provider Registry

Possible source: CMS National Plan and Provider Enumeration System downloadable files.

Official link:

- NPPES downloadable files: https://download.cms.gov/nppes/NPI_Files.html

Possible future use:

- Provider or organization identity context.
- National Provider Identifier (NPI), taxonomy/specialty codes, and address context.
- Corroboration where facility names and addresses can be matched in a transparent way.

Current status:

- Treat as future enrichment unless the team can show exact matching logic and resulting fields.
- Do not claim that NPPES integration is complete unless the final artifact contains explainable NPPES-derived columns.

Known limitations:

- Issuance of an NPI does not validate licensure, credentialing, service availability, or behavioral health access.
- NPPES records do not map one-to-one to treatment facilities.
- Address and organization matching can be ambiguous.

## Optional Future Source: HRSA Mental Health Shortage Area Data

Possible source: HRSA Data Warehouse shortage-area downloads.

Official links:

- HRSA Data Downloads: https://data.hrsa.gov/data/download/
- HRSA shortage-area downloads: https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas

Possible future use:

- Geographic access context through Mental Health HPSA designations, scores, and shortage-area status.
- County, ZIP, or geospatial enrichment if the matching method is defensible.

Current status:

- Treat as future enrichment unless the team can show exact matching logic and resulting fields.
- HRSA context should not be described as facility quality, facility capacity, or appointment availability.

## Optional Future Source: Payer or Quality Data

Current status:

- Optional and only if feasible.
- Do not use payer or quality data unless the team can explain the source, matching method, update date, and limitations.

Possible official sources:

- CMS Provider Data Catalog / Care Compare: https://data.cms.gov/provider-data/

Known limitations:

- Public quality measures may not be specific to behavioral health access.
- Payer directories can be stale.
- These sources usually do not prove that a specific facility accepts a specific patient today.

## Processed Data

The final prototype and review workflow should use a small processed file under `data/processed/`.

Primary review file:

- File name: `data/processed/final_nj_facility_sample.csv`
- Rows: 213
- Purpose: final New Jersey extract for the Streamlit prototype, report walkthrough, and coach review.
- Source lineage: SAMHSA National Mental Health Directory 2024 processing plus derived K-Means tier labels.

Small classroom demo file:

- File name: `data/processed/facility_service_demo.csv`
- Rows: 15
- Purpose: compact input for `notebooks/final_facility_tier_model.ipynb`.

## What The Data Cannot Reliably Tell Us

The data cannot reliably tell us:

- whether a facility has appointments available today
- whether a facility is accepting new clients
- whether a facility accepts a specific person's insurance today
- whether a facility is clinically appropriate for a specific person
- whether public records are fully current or complete
- whether a high service-complexity tier is better than a focused outpatient tier
- whether a facility is accessible for a specific person's transportation, language, disability, or cultural needs unless directly supported by current data

Use these data as bounded navigation support. Human review, direct facility verification, and professional judgment remain necessary.
