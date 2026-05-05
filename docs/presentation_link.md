# Presentation Notes

Known presentation materials are in the team's shared Drive. The public GitHub repository does not include direct Drive links; share those privately with the team or reviewers only when needed.

## Presentation Storyline

Use the presentation to show a clear, bounded project:

1. Behavioral health navigation is hard because public facility data are fragmented and hard to interpret.
2. The team built a New Jersey prototype using processed SAMHSA National Mental Health Directory 2024 data.
3. The notebook pipeline decodes service fields and creates a GitHub-safe New Jersey extract.
4. The modeling notebook uses K-Means to group facilities into care-bundle tiers based on service patterns.
5. The Streamlit prototype loads those precomputed tiers and lets a navigator filter and interpret plausible facility options.
6. The tool does not confirm appointment availability, clinical fit, or insurance acceptance.
7. Future work would add transparent NPPES/HRSA enrichment, stronger refresh workflows, and user testing.
