# Data Documentation

This folder is for data documentation and small demo/sample files only.

Do not upload raw GB-scale source files to GitHub. Raw source files should stay in the shared Drive or be referenced through official download links and reproducibility instructions.

## Data Storage Rule

Use GitHub for:

- source documentation
- data dictionaries
- small sample/demo files
- processed files small enough to run the prototype
- instructions for recreating processed data

Do not use GitHub for:

- full NPPES monthly files
- large raw SAMHSA or HRSA files
- ZIP archives
- local databases
- caches
- files with secrets or private credentials

## Expected Sources

Fill this section in as the pipeline is finalized.

### SAMHSA Facility Data

- Raw file name:
- Raw file location or official source link:
- Approximate size:
- What it provides:
- Important columns used:
- Known limitations:

### NPPES Provider Registry

- Raw file name:
- Raw file location or official source link:
- Approximate size:
- What it provides:
- Important columns used:
- Known limitations:

### HRSA Mental Health Shortage Area Data

- Raw file name:
- Raw file location or official source link:
- Approximate size:
- What it provides:
- Important columns used:
- Known limitations:

### Optional Payer or Quality Data

- Raw file name:
- Raw file location or official source link:
- Approximate size:
- What it provides:
- Important columns used:
- Known limitations:

## Processed Demo Data

Document the small file used by the notebook/prototype.

- Processed file name:
- Created by notebook/script:
- Number of rows:
- Number of columns:
- Purpose:
- Columns included:
- What has been removed or simplified:

## Reproducibility Notes

Add the exact steps needed to rebuild the processed demo file from raw data.

1. Download or locate raw source files.
2. Run cleaning/decoding notebook or script.
3. Match/enrich sources if applicable.
4. Create processed demo file.
5. Run model notebook and prototype.

## Data Limitations

Use this section to record what the data cannot reliably tell us, such as real-time availability, exact insurance acceptance for a specific patient, current appointment capacity, or clinical appropriateness.
