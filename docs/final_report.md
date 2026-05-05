# Behavioral Health Access Navigator

**Final Project Report Draft**

**Team Members:** Caitlin Cohen, Sarthak Chandervanshi, Sangeetha Maheshwari, Joseph Thorpe
**Faculty Advisor:** Dr. Andrei Nikiforov
**Draft Date:** May 4, 2026

> This report is a polished review draft prepared from the team report document and the final GitHub integration artifacts.

## Reader Artifact Map

| Review Need | Artifact | What To Look For |
| --- | --- | --- |
| Start here | `README.md` | Project scope, review sequence, and run instructions. |
| Project walkthrough | `docs/project_walkthrough.md` | One-page map of the repository. |
| Report | `docs/final_report.docx and docs/final_report.md` | Polished report draft and GitHub-readable text version. |
| Prototype | `app/streamlit_app.py` | Streamlit app using the committed New Jersey extract. |
| Final data extract | `data/processed/final_nj_facility_sample.csv` | 213 New Jersey facility records with decoded service fields and K-Means-derived tiers. |
| Data documentation | `data/README.md and docs/data_pipeline.md` | Source lineage, processing steps, and limitations. |
| Notebooks | `notebooks/SAMHSA.ipynb and notebooks/Modeling.ipynb` | Drive-origin cleaning, filtering, ranking, and modeling work. |
| Responsible AI | `docs/responsible_ai_memo.md` | Intended use, misuse risks, and human override rules. |
| Deployment readiness | `docs/deployment_readiness.md` | Prototype status, gaps, and next improvements. |

## Tier Distribution In Final NJ Extract

| Tier | Facilities | Interpretation |
| --- | ---: | --- |
| Essential Support Services | 69 | Focused service profiles with essential support fields. |
| Structured Clinical & Family Support | 56 | Facilities with structured therapy, family, education, or rehabilitation signals. |
| Peer & Community-Led Services | 53 | Facilities where peer, recovery, mentoring, or community support signals are prominent. |
| Specialized Chronic Care | 19 | Facilities with more specialized chronic-care or intensive support patterns. |
| Comprehensive Support Hub | 16 | Broad service bundles with many ancillary and recovery-support indicators. |

## Executive Summary

The Behavioral Health Access Navigator is a decision-support prototype designed to help care coordinators, social workers, discharge planners, and community health navigators interpret public behavioral health facility data for New Jersey. The project addresses a practical access problem: behavioral health resources may exist, but finding plausible options quickly is difficult because public information is fragmented, inconsistently encoded, and often hard to search during time-sensitive care transitions.

The current GitHub package centers on a processed extract from SAMHSA National Mental Health Directory 2024 facility directory material. The team cleaned and decoded facility-level service fields, filtered the processed artifact to New Jersey, and added K-Means-derived care-bundle tier labels that summarize service patterns. The final committed review extract contains 213 New Jersey facility rows and 57 columns.

The prototype should be interpreted carefully. It helps users narrow and inspect plausible facility options, but it does not confirm real-time appointment availability, insurance acceptance, capacity, clinical appropriateness, or quality. Human verification and professional judgment remain necessary before any referral or care-planning decision.


## Problem Statement and Intended Users

Access to behavioral health care is constrained not only by supply, but also by navigation friction. Individuals seeking mental health or substance use treatment often depend on professionals who must translate incomplete directory information into a short list of possible contacts. During discharge planning or community referral work, delays can increase risk, create unnecessary repeated calls, and make already strained systems harder to use.

The intended users are not patients acting alone. The primary users are care coordinators, social workers, discharge planners, community health workers, and related professionals who need a faster way to review public facility information. The project aims to support these users by making facility records easier to filter, rank, and interpret while preserving human responsibility for final judgment.

The project also has a broader classroom and public-facing audience. A reader should be able to open the GitHub repository, understand the source data and model boundaries, run or inspect a small prototype, and see exactly where the larger raw files remain outside GitHub.


## Decision Supported

The system supports a bounded navigation decision: given a care need and a small set of practical criteria, which facilities appear plausible enough to review or contact first? This is a prioritization and information-design problem rather than a clinical prediction problem.

The navigator does not choose a facility for a person. It does not infer diagnosis, predict treatment success, or determine eligibility. Instead, it helps users move from an unwieldy directory toward a shorter, more interpretable list that can be checked by phone, official websites, or professional referral channels.

Because there is no labeled outcome variable for successful referrals, the project emphasizes transparent filtering, rule scoring, semantic matching exploration, and unsupervised service-pattern tiering rather than supervised prediction.


## Data Source and Processed Extract

The primary completed source is SAMHSA National Mental Health Directory 2024 facility directory material, especially the Facilities List worksheet and related service-code reference material. This source is distinct from N-SUMHSS survey microdata. The team used the directory workbook as a public facility inventory, not as a real-time operations feed.

The processed New Jersey extract committed to GitHub is data/processed/final_nj_facility_sample.csv. It contains 213 New Jersey records, 57 columns, decoded service descriptions, payment and funding signals, recovery support fields, age-group fields, ancillary services, original cluster labels, plain-language tier labels, and source-confidence language.

The raw workbook and large intermediate files should remain in the team Google Drive. GitHub is used for code, notebooks, documentation, small processed project data, and reproducibility instructions. This protects the repository from becoming a dumping ground for large raw data while still giving readers a runnable project package.


## Data Processing Workflow

The Drive-origin notebook notebooks/SAMHSA.ipynb documents the cleaning path. It reads the SAMHSA workbook, retains facility identity, city, state, ZIP, phone and intake fields, combines available name fields into a facility_name field, standardizes ZIP values as text, clears placeholder street values, and decodes compact service-code strings into more readable service categories.

The resulting columns describe type of care, service setting, facility type, pharmacotherapies, treatment approaches, emergency services, facility operation, payment/funding, special programs, recovery support, education and counseling, accepted age groups, language services, and ancillary services. For modeling, ancillary and recovery-support mentions were converted into binary multi-label indicators that can be compared across facilities.

The current final extract should be viewed as a reader-ready processed artifact. It is enough for a prototype demonstration, but it is not a fully automated production data pipeline. A future version should include a reproducible command-line script that rebuilds the GitHub extract from the Drive workbook and records source file dates, checksums, and row counts.


## Modeling and Ranking Approach

The modeling work combines transparent ranking ideas with unsupervised tiering. In notebooks/Modeling.ipynb, candidate facilities can be filtered by user-supplied care need, setting, age or payer preferences, and location fields where available. Facility attributes are also combined into text descriptions so semantic matching can be explored with sentence-transformer embeddings.

The exploratory ranking approach combines a semantic similarity score with a rule-based score. Semantic similarity provides flexibility when users describe needs in natural language. Rule scoring keeps important structured fields visible, such as care modality, outpatient or residential wording, payer alignment, counseling services, and payment assistance. This mix is appropriate for a prototype because it is easier to explain than a black-box model trained without ground-truth referral outcomes.

Facility tiering in the notebook workflow uses K-Means clustering on binarized ancillary and recovery-support service indicators. The resulting tier labels are care-bundle summaries. They should not be read as quality scores, provider rankings, or clinical recommendations.

The committed Streamlit prototype is intentionally simpler than the full exploratory notebook. It does not rerun K-Means, KNN, or semantic embeddings at runtime. Instead, it loads the 213-row New Jersey extract, applies deterministic filters and keyword/payment/query match scoring, and displays the precomputed tier label as interpretation context.


## Results

The final GitHub extract contains 213 New Jersey behavioral health facility records. All rows in the committed extract are New Jersey records, and the file includes both decoded facility attributes and derived K-Means tier labels. This gives readers a concrete artifact to inspect rather than a purely conceptual proposal.

The Streamlit prototype uses the extract to filter and display facilities by care need, service setting, payment/funding signal, city, and tier. It also shows simple match signals so a user can see why a facility appeared in the results. Those match signals are deterministic keyword and field matches, not live model predictions. The default filter path loads all 213 records, and narrower filters produce smaller review lists.

The most important result is the integrated workflow: the team moved from scattered Drive files and exploratory notebooks toward a single reviewable repository that contains data documentation, notebooks, a GitHub-safe data extract, a prototype, responsible AI documentation, deployment notes, and a polished report draft.


## Interpretation

The K-Means tiers should be interpreted as service-pattern summaries. A facility in a more comprehensive tier may report a broader mix of supports, but that does not mean it is better for every person or clinically appropriate for a specific case. A focused outpatient or essential-support facility may be the best practical option depending on the person, urgency, eligibility, transportation, payer status, and professional judgment.

The project demonstrates that better information organization can reduce navigation friction even without increasing the number of providers. A human navigator can use the tool to narrow a search, inspect service and payment signals, review a tier label, and then verify details directly with a facility.

The strongest interpretation is therefore modest and useful: public facility data can be turned into a clearer workflow for human review. The system should not be described as a clinical matching engine or an automated referral system.


## Prototype Walkthrough

The prototype lives in app/streamlit_app.py and runs from the committed New Jersey processed extract. It can be launched locally with pip install -r requirements.txt followed by streamlit run app/streamlit_app.py.

The sidebar allows a user to select care need, payment or funding signal, service setting, care-bundle tier, city, and a free-text search query. The main view displays facility cards with facility name, location, type of care, service setting, matched signals, payment/funding text, ancillary services, phone where available, and source-confidence language.

This lightweight prototype runs without API keys, external services, or raw Drive files, making it suitable for classroom review and final presentation.


## Responsible AI and Human-in-the-Loop Use

The navigator must be framed as bounded decision support. It is appropriate for trained professionals who can verify details and incorporate contextual knowledge. It is inappropriate as a fully automated decision-maker, direct-to-patient triage authority, diagnostic tool, or guarantee of provider suitability.

The main responsible AI risks are data staleness, missing service details, uneven reporting across geographies or provider types, overinterpretation of tier labels, and automation overreach. The user interface and report should repeatedly make clear that availability, eligibility, insurance acceptance, and clinical fit must be verified outside the tool.

The human override rule is simple: if professional judgment, crisis status, lived context, accessibility needs, or updated facility information conflicts with the prototype output, the human should override the tool. The model provides evidence to inspect, not an instruction to follow.


## Limitations and Assumptions

The SAMHSA directory is a public snapshot. It may contain stale records, missing optional fields, inconsistent service coding, incomplete intake information, and records that lag real-world changes. It does not include live appointment availability, wait times, staffing levels, bed capacity, or confirmation that a facility is accepting new clients.

The current extract does not include validated NPPES, HRSA, payer, or quality-data integration. Those are reasonable future enrichment directions, but they should not be claimed as completed integrations unless transparent matching fields and quality checks are added.

The prototype also has technical limits. It relies on simple filters and text matching, and the committed app does not perform live semantic embedding calls, K-Means clustering, or KNN. The notebooks explore richer ranking ideas, but the review app favors simplicity and local reproducibility.


## Deployment Readiness

The project is ready to read and inspect as a prototype package once the repository is made accessible. It is not ready for production healthcare deployment.

Before sharing broadly, the repository should be public or intended readers should be added with explicit access. The README should be the first stop, followed by the project walkthrough, final report, app, notebooks, data documentation, and responsible AI memo.

A production pathway would require a formal data-refresh workflow, accessibility testing, security and privacy review, user testing with navigators, clearer source licensing documentation, and a real plan for data currency and operational verification.


## Future Work

The highest-value next step is a reproducible data-build script that starts from the raw SAMHSA workbook and produces the committed New Jersey extract with row-count checks. This would make the project easier to rerun and defend.

Future source enrichment could add NPPES identity context, HRSA shortage-area context, or payer and quality data, but only with transparent matching logic and clear uncertainty labels. Real-time availability and insurance verification would require data sources beyond the static directory.

Future modeling could incorporate validated feedback from navigators, successful referral outcomes, or user interaction logs. Until such labels exist, transparent filtering and unsupervised service-pattern summaries are more defensible than predictive claims.


## Conclusion

The Behavioral Health Access Navigator turns scattered public facility information into a more usable review workflow for New Jersey behavioral health navigation. The final GitHub package gives readers a coherent path through the project: source documentation, processed data, notebooks, prototype, responsible AI boundaries, deployment readiness, and a polished report draft.

The project is strongest when described modestly: it reduces uncertainty for human navigators by organizing public data and surfacing plausible facility options. It does not replace professional judgment, verify real-time access, or make clinical decisions. That bounded framing makes the work both more honest and more useful.
