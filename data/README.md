# Data Documentation

This folder documents the data used by the New Jersey Behavioral Health Access Navigator. It should contain documentation and small demo or processed files only.

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

- full raw NPPES monthly files
- large raw SAMHSA, HRSA, payer, or quality files
- ZIP archives
- local databases
- cache folders
- secrets, API keys, or private credentials

Raw source files should live in the team's shared Drive or be re-downloaded from the official source links below.

## Current Pipeline Summary

The practical center of the project is a cleaned, decoded SAMHSA-centered facility file. That file can be enriched where feasible with NPPES provider identity/address context, HRSA mental-health shortage-area context, and optional payer or quality context. The final prototype should use a small processed extract, not raw source files.

High-level flow:

1. Download or locate raw files outside GitHub.
2. Keep source files in shared Drive, not in this repository.
3. Clean and decode SAMHSA facility records.
4. Filter to New Jersey facilities.
5. Standardize names, addresses, county/city fields, service fields, payment fields, and age/service-population fields.
6. Optionally enrich with NPPES, HRSA, and payer/quality data if match quality is defensible.
7. Create source-confidence fields that describe whether a facility or attribute is supported by one source or multiple sources.
8. Export a small processed/demo file to `data/processed/` for the notebook and prototype.
9. Run the K-Means model notebook to create care-bundle or service-complexity tiers.
10. Use the tier label as interpretation context, not as a clinical recommendation.

More detailed pipeline notes are in `docs/data_pipeline.md`.

## Source 1: SAMHSA Facility Data

Recommended source: SAMHSA National Substance Use and Mental Health Services Survey (N-SUMHSS) public-use files and documentation.

Official links:

- SAMHSA data portal: https://www.samhsa.gov/data/
- N-SUMHSS public-use files: https://www.samhsa.gov/data/data-we-collect/n-mhss/datafiles
- FindTreatment.gov for public facility lookup context: https://findtreatment.gov/

Raw data location:

- Preferred local/shared location: team shared Drive, for example `Shared Drive/raw/samhsa/`.
- GitHub location: do not commit raw SAMHSA files.

Approximate size:

- Varies by year and download format. Public-use files are usually not GB-scale, but raw downloads and extracted files should still stay outside GitHub.
- Record the exact downloaded file name, year, format, and size in the shared Drive manifest when the team finalizes the extract.

What it provides:

- Behavioral health facility location and characteristics.
- Substance use and mental health treatment facility services.
- Service setting, type of care, treatment approaches, recovery support, emergency services, payment/funding, age groups, and ancillary/support services.

Important columns or concepts:

- Facility identifier or survey record identifier.
- Facility name.
- Street address, city, state, ZIP, county, latitude, longitude if available.
- Service setting, including outpatient, intensive outpatient, partial hospitalization, residential, crisis, or hospital-based settings where available.
- Type of care, including mental health treatment, substance use treatment, co-occurring care, and medication management signals where available.
- Treatment approaches and recovery supports.
- Emergency/crisis services.
- Payment, insurance, funding, sliding fee, Medicaid, Medicare, private insurance, and self-pay signals.
- Age groups or populations served.
- Ancillary services such as case management, housing support, employment support, transportation assistance, or care coordination.

Main use in this project:

- Primary facility-level source for the navigator.
- Main input for service-fit filters and K-Means care-bundle clustering.

Known limitations:

- N-SUMHSS is survey-based and may have nonresponse.
- It is not a real-time availability feed.
- It does not confirm whether a facility is accepting new clients today.
- It does not prove clinical appropriateness for a specific person.
- Multiple-response service fields require careful decoding and interpretation.
- Records may be stale, incomplete, or inconsistent across years.

## Source 2: NPPES Provider Registry

Recommended source: CMS National Plan and Provider Enumeration System (NPPES) downloadable files.

Official link:

- NPPES downloadable files: https://download.cms.gov/nppes/NPI_Files.html

Raw data location:

- Preferred local/shared location: team shared Drive, for example `Shared Drive/raw/nppes/`.
- GitHub location: do not commit full NPPES monthly files.

Approximate size:

- The CMS monthly NPPES Data Dissemination file is large. As of the April 13, 2026 Version 2 monthly release, the ZIP file is about 1,073 MB.
- Weekly incremental files are much smaller, but the monthly file is still too large for GitHub.

What it provides:

- Provider and organization identity data.
- National Provider Identifier (NPI).
- Provider type/entity type.
- Taxonomy/specialty codes.
- Mailing and practice addresses.
- Other names, practice locations, and endpoint reference files in the Version 2 release.

Important columns or concepts:

- NPI.
- Entity type code.
- Provider organization name or provider name fields.
- Provider business mailing address.
- Provider business practice location address.
- Provider taxonomy code and primary taxonomy switch.
- Enumeration date and last update date.
- Deactivation date if applicable.

Main use in this project:

- Optional enrichment for provider identity, specialty, and address context.
- Possible corroboration source when facility names, organization NPIs, or practice addresses match SAMHSA-centered records.

Known limitations:

- CMS notes that issuance of an NPI does not ensure or validate that a provider is licensed or credentialed.
- NPPES does not prove behavioral health service availability.
- NPPES does not show appointment capacity.
- Address matching can be messy, especially for organizations with multiple locations.
- Provider registry records may not map one-to-one to treatment facilities.

## Source 3: HRSA Mental Health Shortage Area Data

Recommended source: HRSA Data Warehouse shortage-area downloads, especially Mental Health HPSA files.

Official links:

- HRSA Data Downloads: https://data.hrsa.gov/data/download/
- HRSA shortage-area downloads: https://data.hrsa.gov/data/download?titleFilter=Shortage+Areas

Raw data location:

- Preferred local/shared location: team shared Drive, for example `Shared Drive/raw/hrsa/`.
- GitHub location: do not commit large HRSA raw files or shapefile bundles.

Approximate size:

- HRSA Mental Health HPSA `All HPSAs` CSV is about 14 MB.
- Mental Health HPSA shapefile and boundary downloads can be much larger, for example tens to more than 100 MB depending on the boundary file.

What it provides:

- Geographic shortage-area context for mental health provider access.
- HPSA designation details, scores, status, discipline class, and geography.

Important columns or concepts:

- HPSA ID or designation identifier.
- HPSA name.
- HPSA discipline class, especially Mental Health.
- Designation type.
- HPSA status.
- HPSA score.
- State, county, county FIPS, or geography fields.
- Designation date or last update date.

Main use in this project:

- Geographic context for access barriers and shortage areas.
- Possible county-level or geography-level enrichment in the navigator.

Known limitations:

- HRSA HPSA context is geographic, not facility-specific quality or availability.
- HPSA designation does not mean a specific facility has capacity.
- Matching by county can hide variation inside counties.
- Boundary files require geospatial handling and careful projection/geometry work.

## Source 4: Optional Payer or Quality Data

Current status:

- Optional and only if feasible. Do not use payer or quality data unless the team can explain the source, matching method, update date, and limitations.

Possible official sources:

- CMS Provider Data Catalog / Care Compare: https://data.cms.gov/provider-data/
- CMS Care Compare doctors and clinicians information: https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/Compare-DAC
- CMS Care Compare about the data: https://www.cms.gov/medicare/quality/physician-compare-initiative/about-data

Raw data location:

- Preferred local/shared location if used: team shared Drive, for example `Shared Drive/raw/cms_provider_data/`.
- GitHub location: do not commit large raw provider-data exports.

Approximate size:

- Varies widely by file. Some CMS Provider Data Catalog files are small enough to inspect locally; archives and full downloadable datasets can be hundreds of MB.
- Record exact file names, download dates, and sizes if the team uses any payer or quality data.

What it may provide:

- Clinician or group demographics.
- Medicare provider affiliations.
- Publicly reported quality or performance data, if available for a relevant provider type.
- Facility or clinician identifiers that may support matching.

Important columns or concepts if used:

- NPI or CMS Certification Number where applicable.
- Provider or organization name.
- Practice location.
- Group affiliation.
- Measure identifiers and scores, if quality measures are used.
- Reporting period and data refresh date.

Main use in this project if used:

- Optional context, not the core navigator source.
- Possible corroboration for provider identity, affiliations, or public quality indicators.

Known limitations:

- CMS quality data may not be specific to behavioral health access needs.
- Quality measures are not the same as appointment availability, insurance acceptance, or clinical fit.
- Public performance data may lag current practice.
- Payer directories can be stale and should not be treated as proof that a specific patient will be accepted today.

## Processed Demo Data

The final prototype and model notebook should use a small processed/demo file under `data/processed/`.

Expected processed file:

- File name: `data/processed/facility_service_demo.csv`
- Created by: cleaned SAMHSA-centered extraction pipeline or model-prep notebook/script.
- Purpose: small runnable input for the prototype and K-Means care-bundle tier notebook.
- Size target: small enough for GitHub and classroom review, ideally a few KB to a few MB.
- Rows: enough to demonstrate filters, source confidence, and K-Means tiering; not the full raw source universe.

Expected columns:

- `facility_id`
- `facility_name`
- `county`
- `city`
- `state`
- `zip`
- `latitude`
- `longitude`
- `service_setting`
- `care_types`
- `treatment_approaches`
- `recovery_support`
- `emergency_services`
- `payment_options`
- `age_groups`
- `ancillary_services`
- `source_confidence`
- Optional enrichment fields such as `nppes_match_status`, `hrsa_mental_health_hpsa_status`, or `payer_quality_context` if defensible.

What should be removed or simplified:

- Raw source-only columns not needed for the demo.
- Very large text fields or code columns that are not decoded.
- Duplicate records after facility-level standardization.
- Any private credentials, local paths, cache metadata, or sensitive data.

## Reproducibility Notes

When the final data extract is ready, update this section with exact file names and dates.

1. Download or locate raw SAMHSA, NPPES, HRSA, and optional payer/quality files outside GitHub.
2. Save raw files in the shared Drive raw-data folder.
3. Record source URL, download date, file name, and file size in a shared manifest.
4. Clean and decode SAMHSA facility fields.
5. Filter to New Jersey.
6. Standardize names and addresses.
7. Match NPPES records only where the match logic is explainable.
8. Add HRSA shortage-area context by county, FIPS, ZIP, or geospatial match depending on available processed fields.
9. Add optional payer/quality context only if the source is clear and useful.
10. Create source-confidence fields to show whether important attributes are supported by one or multiple sources.
11. Export a small processed demo file to `data/processed/`.
12. Run the model notebook and prototype using the processed file.

## What The Data Cannot Reliably Tell Us

The data cannot reliably tell us:

- whether a facility has appointments available today
- whether a facility is accepting new clients
- whether a facility accepts a specific person's insurance today
- whether a facility is clinically appropriate for a specific person
- whether public records are fully current or complete
- whether a matched NPPES provider and a SAMHSA facility are definitely the same operational entity without human review
- whether a high service-complexity tier is better than a focused outpatient tier
- whether a facility is accessible for a specific person's transportation, language, disability, or cultural needs unless directly supported by current data

Use these data as bounded navigation support. Human review, direct facility verification, and professional judgment remain necessary.
