# Final Report Link

Current working report draft:

- Google Drive document: https://docs.google.com/document/d/1aUuMP8MsYjMD5R-L2QtOFB3krbYvulr3/edit
- GitHub polished report draft: `docs/final_report.docx`
- GitHub-readable report draft: `docs/final_report.md`

## Integration Notes

The current Drive file is an Office-format document opened through Google Drive, not a native Google Doc. If connector-based editing is needed, convert it to native Google Docs or edit the `.docx` directly in Drive.

The GitHub report draft was prepared locally from the Drive report text plus the final integration artifacts. It fixes the advisor-name spelling and replaces generic Results/Interpretation language with project-specific language based on the 213-row New Jersey extract and five K-Means care-bundle tiers.

The final report should align with this repository's current data story:

- Primary completed source: SAMHSA National Mental Health Directory 2024.
- Final GitHub data extract: `data/processed/final_nj_facility_sample.csv`.
- Model framing: K-Means care-bundle tiering, not KNN.
- Prototype framing: bounded navigation support, not clinical recommendation or real-time availability.
- Advisor name spelling: Dr. Andrei Nikiforov.

## Suggested Report Sections

1. Problem statement and intended users
2. Source data and data limitations
3. Cleaning and decoding workflow
4. Navigator ranking and filtering logic
5. K-Means care-bundle tiering
6. Prototype walkthrough
7. Responsible AI and human override rules
8. Deployment readiness
9. Limitations and next steps

## Ready-To-Paste Results Language

The final GitHub review extract contains 213 New Jersey behavioral health facility records derived from the team's processed SAMHSA National Mental Health Directory 2024 workflow. The extract keeps decoded service fields that are useful for navigation, including facility type, type of care, service setting, treatment approaches, emergency services, payment/funding signals, recovery support, age groups accepted, and ancillary services.

The K-Means tiering workflow assigns each facility to one of five plain-language care-bundle tiers. In the final New Jersey extract, the tier distribution is:

| Tier | Facilities |
| --- | ---: |
| Essential Support Services | 69 |
| Structured Clinical & Family Support | 56 |
| Peer & Community-Led Services | 53 |
| Specialized Chronic Care | 19 |
| Comprehensive Support Hub | 16 |

The Streamlit prototype uses this processed extract to let a navigator filter facilities by care need, service setting, payment/funding signal, city, and tier. It also provides simple match signals so the user can see why a facility appeared in the results. The prototype is intentionally bounded: it demonstrates search, filtering, and interpretation of public facility data, but it does not confirm appointment availability, insurance acceptance, clinical fit, or real-time service status.

## Ready-To-Paste Interpretation Language

The K-Means tiers should be interpreted as service-pattern summaries, not as quality scores. A facility in a more comprehensive tier may report a broader mix of supports, but that does not mean it is better for every person or clinically appropriate for a specific case. Similarly, a focused outpatient or essential-support facility may be exactly the right option depending on the person's needs, location, eligibility, and urgency.

The most important project result is not the model alone. The value of the navigator is that it turns a hard-to-read public directory into a more usable review workflow for human navigators. A user can narrow the list of facilities, inspect service and payment signals, see the care-bundle tier, and then verify details directly with the facility. This keeps the human in the loop and prevents the model from being treated as a referral authority.

The current source-confidence language should be read as a provenance statement: the facility data come from SAMHSA National Mental Health Directory 2024 processing, service fields were decoded for readability, and the tier label was derived from the team's K-Means workflow. Future versions could add NPPES provider identity context, HRSA shortage-area context, or payer/quality data, but those should be described as future work unless transparent matching fields are added to the final dataset.
