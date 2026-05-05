# Responsible AI Memo

## Intended Use

The New Jersey Behavioral Health Access Navigator is a decision-support prototype for people who help others locate behavioral health services, such as care coordinators, social workers, discharge planners, community health workers, and community-based navigators.

The tool is meant to make public facility directory data easier to search and interpret. It is not a clinical decision system, referral authority, appointment system, or insurance-verification system.

## What The System Does

- Filters and ranks New Jersey behavioral health facilities using decoded public directory fields.
- Shows service setting, type of care, payment/funding signals, age-group fields, and ancillary supports where available.
- Adds a K-Means care-bundle tier that summarizes service-pattern complexity.
- Communicates source and scope limits through source-confidence language.

## What The System Must Not Claim

- A facility has appointments available today.
- A facility is accepting new clients.
- A facility accepts a specific person's insurance today.
- A facility is clinically appropriate for a specific person.
- A higher service-complexity tier means higher quality.
- Public directory records are complete, current, or error-free.

## Key Risks

Data staleness: public directory records can lag real-world changes in staffing, services, eligibility, and availability.

Coverage gaps: some facilities may be missing, have incomplete service information, or have records that do not reflect all programs.

Misinterpretation: users may confuse a model tier with quality, clinical fit, or urgency.

Equity concerns: people with language, transportation, disability, insurance, cultural, or crisis needs may require details that are missing or incomplete in the public data.

Automation overreach: AI-generated summaries or explanations could sound more certain than the source data allows.

## Human-In-The-Loop Rules

Human users should:

- verify availability, eligibility, location, payment, and insurance details directly with the facility
- use professional judgment for clinical fit and urgency
- treat tier labels as interpretation aids, not recommendations
- override the tool when lived context, crisis status, accessibility needs, or updated facility information conflicts with the output
- document uncertainty when sharing a suggested option with another person

## Model Interpretation

The K-Means tier is an unsupervised grouping of facilities based on service patterns. It is not a supervised prediction, quality score, or medical recommendation.

Plain-language tier names should be explained as summaries of common service bundles. They should not be used to imply that one tier is better than another.

## AI Assistant Use

The team used AI assistants to help organize code, documentation, notebooks, and final integration work. AI-generated artifacts should be reviewed by team members before submission. Every notebook, model choice, limitation, and report claim should be explainable by the team in plain language.

## Minimum User-Facing Warning

Any prototype or presentation should include language equivalent to:

> This prototype uses processed public facility directory data for navigation support. It does not confirm appointment availability, insurance acceptance, clinical appropriateness, or real-time service status. Users should verify details directly with facilities and apply professional judgment.
