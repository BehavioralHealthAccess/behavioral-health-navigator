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


## Requirements Alignment

The AI Campus project structure asks teams to produce both technical artifacts and communication artifacts. This report is therefore written as a bridge between the code repository and the final presentation. It does not replace the notebooks, data documentation, prototype, or responsible AI memo. Instead, it explains how those artifacts fit together and what claims can be safely made from them.

The technical artifacts are represented in the public repository through the working notebooks, the Streamlit prototype, the processed New Jersey data extract, and the pipeline documentation. The notebooks show the team's data cleaning, service-field decoding, ranking exploration, and tiering work. The application shows a lightweight review workflow that can be launched locally. The data documentation explains why raw multi-gigabyte files are not committed to GitHub and why a smaller processed extract is used for review.

The communication artifacts are represented through this report, the project walkthrough, the deployment readiness brief, the responsible AI memo, and the final presentation deck. Together, these materials answer the demo-day questions: what was rebuilt, what it does, where it fails, and what future steps would be necessary before broader use. The intended standard is not simply that the model runs, but that the team can explain the purpose, assumptions, limits, and review path across disciplines.

This alignment matters because the project should be evaluated as an integrated prototype, not as a single algorithm. A technically impressive model would be weak if it could not be explained, audited, or bounded. Conversely, a clear prototype with modest modeling can still be valuable when it organizes public information in a way that is easier for people to inspect and challenge.


## System Map

The project can be read as a small information system with four layers: source data, processing, interpretation, and presentation. Each layer has a different job and a different risk. Keeping those layers separate makes the project easier to explain and prevents the final prototype from implying more certainty than it has.

| Layer | Main Artifact | Purpose | Primary Risk |
| --- | --- | --- | --- |
| Source data | SAMHSA directory workbook in Drive | Provides public facility records and service-code fields. | Source may be stale, incomplete, or inconsistently coded. |
| Processing | `notebooks/SAMHSA.ipynb` and data docs | Cleans fields, decodes service codes, and produces a readable extract. | Cleaning steps may not yet be fully automated from raw source to final CSV. |
| Interpretation | `notebooks/Modeling.ipynb` and tier fields | Explores ranking and groups facilities by service-pattern signals. | Users may overread tiers as quality rankings or clinical recommendations. |
| Presentation | Streamlit app, README, report, slides | Helps readers search, inspect, and explain the project. | A polished interface may create false confidence if limits are not visible. |

The intended flow is simple: raw source files remain in Drive, processed review data lives in GitHub, notebooks document the team's technical reasoning, and the Streamlit app gives readers a lightweight way to inspect records. The project deliberately avoids a complex deployment stack because the final two-week priority is a defensible artifact package, not a production launch.

The visual system map for presentation can show this flow as: public directory source to cleaning and decoding notebook, to New Jersey extract, to tiering and ranking exploration, to Streamlit app, to human verification. The human verification box should be the final step, not a footnote. This communicates that the project is a support tool inside a human workflow.


## Problem Statement and Intended Users

Access to behavioral health care is constrained not only by supply, but also by navigation friction. Individuals seeking mental health or substance use treatment often depend on professionals who must translate incomplete directory information into a short list of possible contacts. During discharge planning or community referral work, delays can increase risk, create unnecessary repeated calls, and make already strained systems harder to use.

The intended users are not patients acting alone. The primary users are care coordinators, social workers, discharge planners, community health workers, and related professionals who need a faster way to review public facility information. The project aims to support these users by making facility records easier to filter, rank, and interpret while preserving human responsibility for final judgment.

The project also has a broader classroom and public-facing audience. A reader should be able to open the GitHub repository, understand the source data and model boundaries, run or inspect a small prototype, and see exactly where the larger raw files remain outside GitHub.


## Use Case Boundary

The practical use case is a first-pass navigation screen. A user may know that a client needs outpatient mental health services, may have a payment constraint such as Medicaid or self-pay, and may want facilities in a specific city or broader service tier. The tool helps convert those criteria into a smaller set of records to inspect. It is designed to reduce search friction, not to make a referral decision.

The user still has to confirm whether a facility is open, accepting new clients, appropriate for the person's age and needs, reachable by transportation, and compatible with payer or insurance constraints. A phone call, official website check, or professional referral pathway remains necessary. This is why the prototype frames outputs as plausible records to review rather than recommendations to follow.

The tool is also not designed for emergency triage. Crisis situations require established emergency protocols, hotlines, mobile crisis teams, emergency departments, or other appropriate crisis response channels. The project should never be presented as a substitute for those systems.


## Decision Supported

The system supports a bounded navigation decision: given a care need and a small set of practical criteria, which facilities appear plausible enough to review or contact first? This is a prioritization and information-design problem rather than a clinical prediction problem.

The navigator does not choose a facility for a person. It does not infer diagnosis, predict treatment success, or determine eligibility. Instead, it helps users move from an unwieldy directory toward a shorter, more interpretable list that can be checked by phone, official websites, or professional referral channels.

Because there is no labeled outcome variable for successful referrals, the project emphasizes transparent filtering, rule scoring, semantic matching exploration, and unsupervised service-pattern tiering rather than supervised prediction.


## Data Source and Processed Extract

The primary completed source is SAMHSA National Mental Health Directory 2024 facility directory material, especially the Facilities List worksheet and related service-code reference material. This source is distinct from N-SUMHSS survey microdata. The team used the directory workbook as a public facility inventory, not as a real-time operations feed.

The processed New Jersey extract committed to GitHub is data/processed/final_nj_facility_sample.csv. It contains 213 New Jersey records, 57 columns, decoded service descriptions, payment and funding signals, recovery support fields, age-group fields, ancillary services, original cluster labels, plain-language tier labels, and source-confidence language.

The raw workbook and large intermediate files should remain in the team Google Drive. GitHub is used for code, notebooks, documentation, small processed project data, and reproducibility instructions. This protects the repository from becoming a dumping ground for large raw data while still giving readers a runnable project package.


## Data Feature Families

The processed extract is useful because it converts a dense public directory into feature families that are easier to reason about. The project does not depend on every field being perfect. Instead, it uses groups of related fields to help the reader understand what kind of facility record they are seeing.

| Feature Family | Examples In The Extract | How It Supports Navigation |
| --- | --- | --- |
| Facility identity and location | facility name, city, state, ZIP, phone, intake phone | Lets users recognize and contact records. |
| Care type and setting | type of care, service setting, facility type | Helps distinguish outpatient, residential, inpatient, and multi-setting options. |
| Treatment approaches | CBT, DBT, group therapy, individual therapy, telehealth therapy | Helps users inspect whether a record mentions relevant clinical modalities. |
| Payment and funding | Medicaid, Medicare, private insurance, self-pay, sliding fee, payment assistance | Helps users screen for practical affordability signals. |
| Age groups and populations | adults, young adults, seniors, children/adolescents, special programs | Helps users avoid obvious population mismatches. |
| Recovery and ancillary supports | case management, peer support, education services, suicide prevention services | Helps summarize broader supports beyond a basic facility listing. |
| Derived tier labels | five plain-language care-bundle tiers | Helps readers compare service-pattern breadth without treating tiers as rankings. |

The feature families also make limitations easier to see. For example, the payment fields can indicate that a facility reports Medicaid or payment assistance, but they do not prove current acceptance for a specific person. A service-setting field may say outpatient, but it does not prove the facility has immediate openings. This distinction between useful signal and verified fact is central to the responsible use of the prototype.


## Data Processing Workflow

The Drive-origin notebook notebooks/SAMHSA.ipynb documents the cleaning path. It reads the SAMHSA workbook, retains facility identity, city, state, ZIP, phone and intake fields, combines available name fields into a facility_name field, standardizes ZIP values as text, clears placeholder street values, and decodes compact service-code strings into more readable service categories.

The resulting columns describe type of care, service setting, facility type, pharmacotherapies, treatment approaches, emergency services, facility operation, payment/funding, special programs, recovery support, education and counseling, accepted age groups, language services, and ancillary services. For modeling, ancillary and recovery-support mentions were converted into binary multi-label indicators that can be compared across facilities.

The current final extract should be viewed as a reader-ready processed artifact. It is enough for a prototype demonstration, but it is not a fully automated production data pipeline. A future version should include a reproducible command-line script that rebuilds the GitHub extract from the Drive workbook and records source file dates, checksums, and row counts.


## Pipeline And Reproducibility

The project pipeline can be understood as five stages. First, the raw public workbook and supporting files remain in the shared Drive because they are too large and too source-like for GitHub. Second, the notebook workflow extracts and cleans the fields needed for navigation. Third, the team filters the processed data to New Jersey and keeps a compact GitHub-safe extract. Fourth, notebooks explore ranking and tiering logic. Fifth, the Streamlit app loads the prepared extract and provides a user-facing way to filter and inspect records.

This structure is intentionally conservative. It gives the public repository enough material to run and review the project without turning GitHub into raw-data storage. It also lets readers understand the exact relationship among Drive, notebooks, processed data, app, and report.

The main reproducibility gap is that the current repository does not yet contain a single command that rebuilds the 213-row extract from the raw workbook. That is acceptable for a classroom prototype if it is disclosed clearly, but it should be fixed before any operational claim. A stronger version would include a `scripts/build_nj_extract.py` file, source-file checksum logging, row-count validation, and a short data contract that explains which columns the app expects.


## Modeling and Ranking Approach

The modeling work combines transparent ranking ideas with unsupervised tiering. In notebooks/Modeling.ipynb, candidate facilities can be filtered by user-supplied care need, setting, age or payer preferences, and location fields where available. Facility attributes are also combined into text descriptions so semantic matching can be explored with sentence-transformer embeddings.

The exploratory ranking approach combines a semantic similarity score with a rule-based score. Semantic similarity provides flexibility when users describe needs in natural language. Rule scoring keeps important structured fields visible, such as care modality, outpatient or residential wording, payer alignment, counseling services, and payment assistance. This mix is appropriate for a prototype because it is easier to explain than a black-box model trained without ground-truth referral outcomes.

Facility tiering in the notebook workflow uses K-Means clustering on binarized ancillary and recovery-support service indicators. The resulting tier labels are care-bundle summaries. They should not be read as quality scores, provider rankings, or clinical recommendations.

The committed Streamlit prototype is intentionally simpler than the full exploratory notebook. It does not rerun K-Means, KNN, or semantic embeddings at runtime. Instead, it loads the 213-row New Jersey extract, applies deterministic filters and keyword/payment/query match scoring, and displays the precomputed tier label as interpretation context.


## Evaluation and Explainability

Because there is no verified ground-truth label for a successful behavioral health referral, the project cannot honestly report accuracy, sensitivity, or precision for referral success. This is an important modeling constraint. A supervised evaluation would require historical referral outcomes, confirmation of facility availability, payer acceptance, appropriateness of match, and follow-up results. The current public directory does not contain those labels.

Instead, the project uses a defensible prototype evaluation standard: transparency, traceability, and plausibility. Transparency means a reader can see which source fields contribute to the app display and the tier labels. Traceability means the app result can be traced back to a row in the processed extract. Plausibility means the output should make sense as a short list for human review, not as an automated clinical answer.

The tier labels support explainability because they summarize service-pattern groupings in plain language. A user can see that a facility is tagged as "Peer & Community-Led Services" or "Comprehensive Support Hub" and then inspect the underlying service fields. The label is useful only when paired with the source fields. If the label is separated from the underlying evidence, it becomes too easy to overinterpret.

The ranking and filter logic in the app is also explainable by design. Rather than hiding a score behind a model endpoint, the app shows practical match signals such as query terms, payment/funding text, service setting, and source-confidence language. This makes the prototype more modest but easier to defend.


## Results

The final GitHub extract contains 213 New Jersey behavioral health facility records. All rows in the committed extract are New Jersey records, and the file includes both decoded facility attributes and derived K-Means tier labels. This gives readers a concrete artifact to inspect rather than a purely conceptual proposal.

The Streamlit prototype uses the extract to filter and display facilities by care need, service setting, payment/funding signal, city, and tier. It also shows simple match signals so a user can see why a facility appeared in the results. Those match signals are deterministic keyword and field matches, not live model predictions. The default filter path loads all 213 records, and narrower filters produce smaller review lists.

The most important result is the integrated workflow: the team moved from scattered Drive files and exploratory notebooks toward a single reviewable repository that contains data documentation, notebooks, a GitHub-safe data extract, a prototype, responsible AI documentation, deployment notes, and a polished report draft.


## Interpretation

The K-Means tiers should be interpreted as service-pattern summaries. A facility in a more comprehensive tier may report a broader mix of supports, but that does not mean it is better for every person or clinically appropriate for a specific case. A focused outpatient or essential-support facility may be the best practical option depending on the person, urgency, eligibility, transportation, payer status, and professional judgment.

The project demonstrates that better information organization can reduce navigation friction even without increasing the number of providers. A human navigator can use the tool to narrow a search, inspect service and payment signals, review a tier label, and then verify details directly with a facility.

The strongest interpretation is therefore modest and useful: public facility data can be turned into a clearer workflow for human review. The system should not be described as a clinical matching engine or an automated referral system.


## Repository Navigation

The GitHub repository is part of the final product. A reader should not have to know the team's Slack or Drive history to understand the submission. The README provides the front door, and the docs folder gives the supporting explanation.

A good review path is: start with the README, open the project walkthrough, inspect the final report, review the data README, skim the notebooks, and then run or inspect the Streamlit app. The processed CSV is small enough to open directly, and the app is simple enough to run with the listed Python requirements.

This structure also helps the team present the work. Instead of walking through code line by line, the team can show the repository as an evidence base: what data was used, what notebooks were created, what the app does, what the responsible-use boundaries are, and where the final report and slides live. The repository is therefore both a technical package and a communication artifact.


## Artifact Inventory

The repository contains several types of artifacts because the project has to be understandable from more than one angle. A technical reader may start with the notebooks and app. A general reader may start with the README, walkthrough, and report. A coach or program lead may focus on whether the team can explain limits and integration choices. The table below shows how the artifacts support those different reading paths.

| Artifact | Location | Reader Question It Answers |
| --- | --- | --- |
| Repository README | `README.md` | What is this project, how do I start, and what is included? |
| Project walkthrough | `docs/project_walkthrough.md` | What should I click first and how do the parts fit together? |
| Final report | `docs/final_report.docx`, `docs/final_report.pdf`, `docs/final_report.md` | What did the team build and how should it be interpreted? |
| Data README | `data/README.md` | What data is included, what is excluded, and why? |
| Data pipeline memo | `docs/data_pipeline.md` | How does the raw source become the GitHub-safe extract? |
| Processed extract | `data/processed/final_nj_facility_sample.csv` | What concrete records power the app and final analysis? |
| Cleaning notebook | `notebooks/SAMHSA.ipynb` | How were source fields cleaned and decoded? |
| Modeling notebook | `notebooks/Modeling.ipynb` | What ranking and similarity ideas did the team explore? |
| Tiering notebook | `notebooks/final_facility_tier_model.ipynb` | How can K-Means be used to demonstrate care-bundle tiering? |
| Streamlit app | `app/streamlit_app.py` | What does the user-facing prototype look like? |
| Responsible AI memo | `docs/responsible_ai_memo.md` | What are the intended uses, misuses, and human override rules? |
| Deployment readiness | `docs/deployment_readiness.md` | What would need to happen before the tool could be used beyond a demo? |
| Presentation draft | `docs/final_presentation_draft.pptx` | What story should the team present on demo day? |

This inventory is useful because it prevents the report from carrying all the burden. The final report should explain the project at a high level, while the repository preserves the evidence trail. If a reader wants proof that the processed extract exists, they can open the CSV. If they want to understand responsible-use boundaries, they can read the memo. If they want to see the product experience, they can open the app or presentation screenshots.


## Design Tradeoffs

The project required several late-stage tradeoffs. These tradeoffs should be named clearly because they show judgment rather than weakness. A final demo is stronger when the team can say why a simpler path was chosen.

| Decision | Chosen Path | Alternative | Rationale |
| --- | --- | --- | --- |
| Data hosting | Keep raw and large files in Drive; commit a processed NJ extract to GitHub. | Upload full raw files to GitHub. | GitHub remains fast, public, and reviewable while Drive preserves larger source material. |
| App scoring | Use deterministic filters and keyword/payment/query matches. | Require live embeddings or API-backed scoring. | The app runs locally without secrets or quota issues and is easier to explain. |
| Model framing | Present K-Means as service-pattern tiering. | Present the model as a clinical recommender. | Tiering is defensible from source fields; clinical recommendation would overclaim. |
| Evaluation | Use transparency, traceability, plausibility, and limitation review. | Claim predictive accuracy without outcome labels. | Referral-success labels are not available in the public directory data. |
| Presentation | Use screenshots and brief methodology. | Walk through code during the final demo. | Program guidance favors a concise methodology and visible product evidence. |

These choices make the final project more modest, but also more credible. The team can show that it understands the difference between an exploratory notebook, a reproducible app, a final presentation, and a production healthcare system.


## Prototype Walkthrough

The prototype lives in app/streamlit_app.py and runs from the committed New Jersey processed extract. It can be launched locally with pip install -r requirements.txt followed by streamlit run app/streamlit_app.py.

The sidebar allows a user to select care need, payment or funding signal, service setting, care-bundle tier, city, and a free-text search query. The main view displays facility cards with facility name, location, type of care, service setting, matched signals, payment/funding text, ancillary services, phone where available, and source-confidence language.

This lightweight prototype runs without API keys, external services, or raw Drive files, making it suitable for classroom review and final presentation.


## Presentation Demo Plan

The final demo should not try to prove that the system solves behavioral health access. That would be too broad and too strong. The demo should show a bounded workflow that makes public data more usable.

A strong presentation sequence is: introduce the access-navigation problem, explain the data source and GitHub-safe extract, show the tier distribution, show screenshots of the Streamlit app, then close with responsible-use boundaries and future work. The presentation can use screenshots rather than a live code walkthrough. This matches the program guidance that a brief methodology is enough and that screenshots of the product are appropriate.

Each team member should be able to answer basic questions about the full workflow, even if they owned different pieces. For example, a report lead should understand why the app avoids live model calls, and a modeling lead should understand why the responsible AI memo warns against clinical overreach. The final artifact is strongest when the team can explain the whole project together.


## Responsible AI and Human-in-the-Loop Use

The navigator must be framed as bounded decision support. It is appropriate for trained professionals who can verify details and incorporate contextual knowledge. It is inappropriate as a fully automated decision-maker, direct-to-patient triage authority, diagnostic tool, or guarantee of provider suitability.

The main responsible AI risks are data staleness, missing service details, uneven reporting across geographies or provider types, overinterpretation of tier labels, and automation overreach. The user interface and report should repeatedly make clear that availability, eligibility, insurance acceptance, and clinical fit must be verified outside the tool.

The human override rule is simple: if professional judgment, crisis status, lived context, accessibility needs, or updated facility information conflicts with the prototype output, the human should override the tool. The model provides evidence to inspect, not an instruction to follow.


## Limitations and Assumptions

The SAMHSA directory is a public snapshot. It may contain stale records, missing optional fields, inconsistent service coding, incomplete intake information, and records that lag real-world changes. It does not include live appointment availability, wait times, staffing levels, bed capacity, or confirmation that a facility is accepting new clients.

The current extract does not include validated NPPES, HRSA, payer, or quality-data integration. Those are reasonable future enrichment directions, but they should not be claimed as completed integrations unless transparent matching fields and quality checks are added.

The prototype also has technical limits. It relies on simple filters and text matching, and the committed app does not perform live semantic embedding calls, K-Means clustering, or KNN. The notebooks explore richer ranking ideas, but the review app favors simplicity and local reproducibility.


## Governance and Misuse Scenarios

The most important misuse scenario is overreliance. A user could treat a displayed facility as the "right" answer even when the record is stale, the facility is full, the payment field is outdated, or the person needs a different level of care. The mitigation is repeated boundary language in the app, README, report, and presentation: verify before action.

A second misuse scenario is treating tier labels as quality rankings. The tiers are service-pattern summaries, not performance measures. A facility with fewer listed supports may still be clinically appropriate, geographically accessible, culturally trusted, or practically available. A facility with a broader service profile may still be unavailable, unsuitable, or outside a person's payer network.

A third misuse scenario is expanding the tool to direct patient use without support. A person in distress may interpret incomplete output as exhaustive or definitive. The safer framing is professional decision support for navigators who can combine public data with updated local knowledge.

Governance for a production version would require named owners for data refresh, validation, user support, incident reporting, accessibility, and escalation. Without those owners, the tool should remain a classroom prototype and public demonstration artifact.


## Ethical Review Questions

The project should be evaluated with questions that match its real risk profile. The most important questions are not only about whether the notebook runs. They are about what a person might assume after seeing the output.

One question is whether the user can tell the difference between a facility record and a verified care option. The app and report should make that difference explicit. A record means the facility appears in the public dataset with certain reported fields. A verified option requires updated confirmation and professional review.

A second question is whether the tool makes hidden exclusions. If a facility lacks a field, the tool may fail to surface it for a specific query even though it could still be useful. Missing data should be treated as uncertainty, not as proof that the service is absent. This is especially important in public health data where reporting practices may vary.

A third question is who bears the cost of error. If a facility is wrongly treated as suitable, the burden may fall on the person seeking care, a caregiver, a discharge planner, or a community organization. The tool must therefore keep the cost of uncertainty visible. A future version should include feedback mechanisms so users can report stale records or misleading fields.

A fourth question is whether the tool would behave differently across regions or populations. The current extract is New Jersey only, and the source fields may not reflect lived access barriers such as transportation, language fit, cultural trust, disability access, or real-time capacity. These limitations should be named rather than hidden behind a clean interface.


## Deployment Readiness

The project is ready to read and inspect as a prototype package once the repository is made accessible. It is not ready for production healthcare deployment.

Before sharing broadly, the repository should be public or intended readers should be added with explicit access. The README should be the first stop, followed by the project walkthrough, final report, app, notebooks, data documentation, and responsible AI memo.

A production pathway would require a formal data-refresh workflow, accessibility testing, security and privacy review, user testing with navigators, clearer source licensing documentation, and a real plan for data currency and operational verification.


## Submission Readiness

The final submission package should include the public GitHub link, this report as a PDF, and the final presentation slides. The GitHub link is the best single entry point because it connects readers to the README, notebooks, data extract, app, documentation, report files, and presentation draft.

Before submission, the team should click through the repository as a reader. They should confirm that the README makes sense, that the report opens, that the processed CSV is visible, that the notebooks are present, and that the slides identify where screenshots should be inserted. If a team member does not understand a notebook, they can copy sections into ChatGPT and ask for a plain-language explanation, then return to the repository with a clearer map.

The last-minute priority is not adding more features. The priority is fluency: every team member should be able to explain the data source, the model boundary, the prototype workflow, the responsible AI limits, and why GitHub contains processed review data rather than raw multi-gigabyte files.


## Future Work

The highest-value next step is a reproducible data-build script that starts from the raw SAMHSA workbook and produces the committed New Jersey extract with row-count checks. This would make the project easier to rerun and defend.

Future source enrichment could add NPPES identity context, HRSA shortage-area context, or payer and quality data, but only with transparent matching logic and clear uncertainty labels. Real-time availability and insurance verification would require data sources beyond the static directory.

Future modeling could incorporate validated feedback from navigators, successful referral outcomes, or user interaction logs. Until such labels exist, transparent filtering and unsupervised service-pattern summaries are more defensible than predictive claims.


## Final Checklist

The final project should be considered ready for submission when the following checks are satisfied:

| Check | Status In Current Package | Notes |
| --- | --- | --- |
| Public repository is accessible | Complete | The repository has been made public for review. |
| README provides a reader path | Complete | The README gives a start-here sequence and explains the major folders. |
| Final report is available as PDF | Complete | The report is stored in `docs/final_report.pdf`. |
| Slides are available | Draft complete | The presentation draft includes screenshot-needed boxes for the team to replace. |
| Processed data is GitHub-safe | Complete | The committed extract has 213 NJ records and avoids raw GB-scale data. |
| App can run without API keys | Complete | The Streamlit app loads the committed extract and uses local deterministic logic. |
| Raw data is not committed | Complete | Large raw files remain in Drive. |
| Responsible AI limits are documented | Complete | Limits appear in the README, report, app framing, and responsible AI memo. |
| Team can explain the full workflow | Needs live review | Each member should click through the repo and understand the notebooks, data, app, and report before presentation. |

The final checklist intentionally includes team fluency. A repository can be technically complete and still fail in presentation if the team cannot explain why choices were made. The last step before demo day should therefore be a shared walkthrough where each person practices explaining one technical artifact and one limitation outside their own assigned lane.


## Glossary For Presentation

The following terms should be used consistently in the report and presentation. Consistent language matters because small wording changes can make the project sound more automated or more clinically authoritative than it is.

| Term | Recommended Meaning |
| --- | --- |
| Navigator | A tool that helps users inspect and narrow public facility records. It is not an automated referral system. |
| Facility record | A row from the processed public dataset. It is evidence to inspect, not proof that care is available. |
| Care-bundle tier | A plain-language grouping based on service-pattern indicators. It is not a quality rating. |
| K-Means | An unsupervised clustering method used here to demonstrate service-pattern grouping. It does not learn from referral outcomes. |
| KNN | A nearest-neighbor method. It should not be described as the final runtime method unless the team adds and documents it. |
| Semantic similarity | A way to compare natural-language text descriptions. It was explored in notebooks but is not required by the final app. |
| Deterministic filtering | Rule-based filtering that gives the same output for the same data and inputs. This is what the Streamlit app uses. |
| Source confidence | Language that reminds users whether a field comes from static public data and needs verification. |
| Human-in-the-loop | A requirement that professionals verify and override the tool when context or updated information requires it. |
| Deployment readiness | A statement about what works for demonstration and what would be required before operational use. |

The team should avoid saying that the model "finds the best facility" or "recommends treatment." Better language is that the system "surfaces plausible facility records for human review." The difference is not cosmetic. It protects the project from overstating the data, and it helps the audience understand why human verification is part of the design.

The team should also avoid saying that the app "uses AI" in a vague way. The final app is a lightweight prototype built from processed public data, deterministic filters, keyword matching, payment and setting fields, and precomputed tier labels. The AI-related work is better described as exploratory modeling and workflow design rather than autonomous decision-making.


## Conclusion

The Behavioral Health Access Navigator turns scattered public facility information into a more usable review workflow for New Jersey behavioral health navigation. The final GitHub package gives readers a coherent path through the project: source documentation, processed data, notebooks, prototype, responsible AI boundaries, deployment readiness, and a polished report draft.

The project is strongest when described modestly: it reduces uncertainty for human navigators by organizing public data and surfacing plausible facility options. It does not replace professional judgment, verify real-time access, or make clinical decisions. That bounded framing makes the work both more honest and more useful.
