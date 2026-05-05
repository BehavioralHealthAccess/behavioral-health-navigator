# Source Agreement Evaluation

## Current Source Position

The final GitHub review artifact is centered on one primary public source: SAMHSA National Mental Health Directory 2024 facility directory material.

The processed New Jersey extract should be described as:

- SAMHSA-centered
- decoded into readable service fields
- filtered to New Jersey
- augmented with derived K-Means tier labels
- appropriate for a classroom prototype and report walkthrough

It should not be described as a complete multi-source provider registry unless additional source-matching fields are added and documented.

## Current Source-Confidence Label

The final extract includes:

```text
SAMHSA National Mental Health Directory 2024; decoded services; derived K-Means tier
```

This means the facility information and service descriptions come from the SAMHSA-centered processed data, while the care-bundle tier is derived from the team's modeling workflow.

## Agreement Claims That Are Safe

Safe language:

- The prototype uses processed public facility directory data.
- The source includes facility service, setting, payment/funding, age-group, and ancillary-service fields.
- The K-Means tier summarizes patterns in available service fields.
- The data should be verified before any referral or care-planning decision.

## Agreement Claims To Avoid

Avoid language such as:

- NPPES confirms every facility.
- HRSA confirms facility-level shortage status.
- The model knows which facility is best.
- The tool verifies insurance acceptance.
- The tool knows current availability.
- The tier label measures care quality.

## Future Multi-Source Agreement Method

If the team later adds NPPES, HRSA, payer, or quality data, use transparent match labels:

- `not_attempted`
- `matched_exact`
- `matched_probable`
- `ambiguous_multiple_matches`
- `not_matched`

For each added source, document:

- source URL
- download date
- raw file name and size
- matching fields used
- match rate
- fields added to the processed extract
- known false-positive and false-negative risks

Only use strong source-confidence language when the match can be explained and defended.
