# Improvement plan: raise every appraisal domain to 8/10 or above (8 Oct 2026)

**Goal (author, 8 Oct 2026):** "thoroughly improve on all weak areas so we are high (8 and above) on every section".

**Baseline:** the appraisal given in chat on 8 Oct 2026, at commit `1a17393`. Overall, the deliverable scored about 6.5 and the workflow about 8.

**Governing rules still apply:** AGENTS.md; author decisions are yes/no questions, one at a time, logged in file 15; no invented decisions; legal retrieval routes only; executor does the work and the reviewer checks it before anything is reported.

## 1. Baseline and targets

| Domain | Now | Target | Main gap | Can AI close it alone? |
|---|---|---|---|---|
| Question and framing | 8 | 8.5 | The title promises spatiotemporal dynamics, but there is no map | Yes (figures, W5) |
| Protocol and registration | 4 | **7 (ceiling)** | Not registered; protocol "on request" | Partly. Needs the author's OSF account |
| Search | 5 | 8 | Scopus/ScienceDirect strings undocumented; 1,000-record caps; no citation chasing; no search peer review | Mostly. Scopus/ScienceDirect re-runs need someone with access |
| Selection | 5 | 8 | AI-only reviewers; human check relied on AI summaries; Reviewer 1 unknown before 27 Sep | **No. Needs a second human** |
| Retrieval | 4 | 8 | 88 reports not retrieved (27%), about 33 of them likely relevant | **No. Needs library or institutional access, or author contact** |
| Extraction and RoB | 8 | 8.5 | New studies from W1–W4 need the same treatment; add a human spot-check | Yes, plus a human sample |
| Synthesis and certainty | 8.5 | 8.5+ | Re-run with any new studies; add figures | Yes |
| Transparency and reporting | 8.5 | 9 | Data availability; reproducible search appendix | Yes, plus the author's deposit account |
| Workflow engineering | 9 | 9 | Keep it | Yes |

**Honest ceiling for registration.** A review cannot become *prospectively* registered after the fact. File 17 records the decision not to backdate. The best honest state is:
- a protocol that is pre-specified, publicly archived and verifiably timestamped (git history, first commit 19 Sep 2026);
- a retrospective OSF registration that states plainly that it is retrospective.

Appraisers usually score that as "partial yes", about 7. Getting above 7 would need a new, prospectively registered review. Every other domain can reach 8 or more.

## 2. Author decisions needed (yes/no, one at a time; recommended option first)

| # | Decision | Recommended | Unlocks |
|---|---|---|---|
| D1 | Can a second person (colleague or student) give about 4–6 hours to screen a random sample independently? | Yes | Selection to 8 (W6) |
| D2 | May we re-open retrieval through legal paid or loan routes: interlibrary loan, British Library On Demand, a colleague's institutional login, or Research4Life through a partner institution? This reverses the 28 Sep retrieval-gate closure. | Yes | Retrieval to 8 (W4) |
| D3 | May we contact authors for the about 33 likely-relevant unretrieved reports (one email each, 14-day window)? This reverses the 27 Sep "no author contact" policy. | Yes if D2 leaves more than 10 relevant gaps | Retrieval to 8 |
| D4 | Can someone with Scopus/ScienceDirect access paste our exact strings and export the results (about 30 minutes)? | Yes | Search to 8 (W1) |
| D5 | Publish the protocol versions and data on OSF or Zenodo, and register on OSF as retrospective? This needs the author's account; I prepare everything. | Yes | Registration to 7; transparency to 9 |
| D6 | Who was Reviewer 1 before 27 Sep, or state that it was not recorded? | State the facts | Selection, transparency |
| D7 | Is there still a hard deadline? It sets how far W2–W4 can go. | Answer | Sequencing |

## 3. Work packages

### W1. Search rebuilt and fully documented (Search 5 → 8)
1. Write final line-by-line strings for every source, with the facets on separate lines (AIV) AND (Nigeria) AND (2006–2026), as required by AGENTS.md and PRISMA-S. For OpenAlex/Crossref, page with cursors so there is no 1,000-record cap.
2. Re-run all sources with an end date of October 2026:
   - **By AI:** PubMed, OpenAlex, Crossref, AJOL, Web of Science Starter API, and Google Scholar through SerpApi.
   - **Through D4:** Scopus and ScienceDirect, as a pasted string and an exported RIS file.
3. Self-assess the strings against PRESS 2015 and document it. If D1's helper or a librarian can do it, get an independent PRESS review: the reviewer completes the PRESS form, and that is reported as search peer review.
4. Deduplicate against the 2,105-record register. Only new records go to screening. Log hits, dates and exports in files 19 and 33.
- **Done when:** PRISMA-S items 8, 9, 13 and 14 are fully reported, the caps are gone, and every string is reproducible from Appendix A.

### W2. Citation chasing (Search; PRISMA-S item 6)
- Do backward and forward citation searches on all 123 included reports, using the OpenAlex and Crossref reference and citation APIs (the citationchaser method). Screen the new records under the same rules.
- **Done when:** the limitation "citation chasing not done" is removed, and the counts appear in the PRISMA "other methods" arm.

### W3. Screening of new records (Selection)
- Dual independent AI screening, as before.
- Add a human sample under W6, and add any new studies to W4/W7.

### W4. Retrieval second pass (Retrieval 4 → 8; depends on D2/D3)
1. Re-sweep all 88 unretrieved reports through every legal open route: Unpaywall, Europe PMC, CORE, OpenAlex OA locations, institutional repositories (UILSpace, ABU Kubanni, UI repository, UP repository) and journal sites. Several have appeared since 28 Sep.
2. Then the D2 routes (loan or paid). Then D3 author contact if approved, logged with dates.
3. Priority order: the about 33 likely-relevant reports, with Laleye 2022 (clade 2.3.4.4b introductions) first.
4. Sensitivity: report what the synthesis would look like if the still-unretrieved relevant reports were added (direction-of-effect statement per synthesis area).
- **Done when:** no more than about 10% of the likely-relevant reports remain unretrieved, every attempt is logged, and the PRISMA box is updated.

### W5. Figures (Framing, Synthesis, Reporting)
- **Figure 2:** a choropleth map of laboratory-confirmed detections by state × epoch, using geoBoundaries ADM1 (an open licence).
- **Figure 3:** a timeline of first detections, waves and clade turnover (2.2 → 2.3.2.1c → 2.3.4.4b), with a certainty marker on each.
- **Figure 1:** export as a vector PDF or TIFF for submission, and keep the editable table version.
- **Built from:** `synthesis/` data, by script, with no hand-drawn numbers. Each figure is checked by the reviewer against Tables 2 and 4.

### W6. Independent human check (Selection 5 → 8; depends on D1)
**Sample** (random with a stated seed; the AI decisions are hidden from the helper):
- 20% of the title-stage exclusions (about 320 records);
- all 114 full-text exclusions;
- all 123 included reports, at eligibility level only.

**Steps:**
1. Prepare one-row-per-record sheets for the helper. Show only the title, abstract, link or PDF, and the criteria; show none of the AI's reasons.
2. Compute Cohen's kappa against the AI decisions.
3. Re-adjudicate any disagreement against the full text.
4. Report the kappa and the number of decisions overturned in the Methods and Results.
5. If kappa is below 0.6, widen the sample.

**Done when:** an independent human makes decisions on a defined sample, agreement is reported, and the "AI-only" limitation is narrowed to "AI-primary with independent human verification". The author's own reconfirmation stays reported as it is.

### W7. Extraction, RoB and synthesis update (all new studies)
- Process each new study the same way:
  - R1 executor and R2 reviewer;
  - consensus;
  - JBI checklists plus the molecular check;
  - `run_all.py` with its assertions;
  - re-rated certainty.
- A human spot-check (D1 helper, optional): 10 studies' key fields against the source, with agreement reported.
- Re-run the four sensitivity analyses. **Do not re-run `adjudicate_linkage.py`**, because it renumbers studies; add new studies with new IDs.

### W8. Registration and open data (Registration 4 → 7; Transparency → 9; depends on D5)
1. Prepare an OSF project with:
   - the frozen protocol (file 10) and every dated amendment (Appendix B source), with git commit hashes and timestamps;
   - the search exports and strings;
   - the screening register (file 56);
   - the extraction and RoB consensus JSON;
   - the synthesis scripts and the reference provenance (`refs_verified_20261008.json`).
2. Create an OSF retrospective registration (generalised systematic review template), stating plainly that it is retrospective.
3. Get a DOI through OSF, or through Zenodo from the GitHub repository.
4. Update the manuscript: the Registration statement, the Data availability statement (an author item, drafted for approval), and PRISMA 24a–c and 27.

### W9. Manuscript rebuild, audits and re-score
1. Update the Methods, Results, Figure 1 numbers, the abstract and the limitations.
2. Rebuild, then run `verify.py`, the docx validation and the render check.
3. Re-run the PRISMA 2020, PRISMA-S and SWiM audits (files 01, 02, 04), and do an AMSTAR-2 self-appraisal.
4. The reviewer agent re-scores every domain from scratch, without seeing this plan's targets.
5. Fill in the remaining author items: the declarations and D6.

## 4. Order and dependencies

```
D7 (deadline) ─┐
D1..D6 asked one at a time as each work package needs them
W1 search rebuild ─┬─> W3 screen new records ─┐
W2 citation chase ─┘                          ├─> W7 extract/RoB/synthesis ─> W5 figures ─> W9 rebuild+audit+re-score
W4 retrieval pass (D2/D3) ────────────────────┘
W6 human check (D1): runs in parallel once sheets are ready; results feed W9
W8 OSF (D5): prepare in parallel; register before submission
```

- **Can start now without any decision:** W1 (all sources except Scopus/ScienceDirect), W2, the W4 open-route re-sweep, W5 figures from the current data, and W8 preparation.
- **Fan-out:** at most 3 agents at a time. Every executor output goes to the reviewer before it is reported.

## 5. Risks

- **New studies change the conclusions.** That is the purpose of the work; certainty and the wording follow the evidence.
- **The helper is unavailable (D1 = no).** Selection stays at about 6. Say so plainly in the limitations, and do not invent a human check.
- **Paid retrieval or loans are refused (D2/D3 = no).** Retrieval stays at about 5 after the open re-sweep. Report it with the sensitivity statement.
- **Search volume rises** once the caps are removed. Screening load grows, but dual AI screening scales; the human sample stays proportional.
- **Registration cannot exceed about 7.** Disclose it honestly and never backdate it (file 17).

## 6. Progress log
- 2026-10-08: plan written; no work package started.
- 2026-10-09: **Agentic-execution session started** (author: "set up our agentic workflow ... make it publishable ready, first score what we have done").
  - **Fresh appraisal done** (file 60): two independent appraiser agents, blind to this file, plus main-session verification of every material claim. Fix list F1–F8 opened; F1 (file 56 summary blocks) executed and verified by the main session the same day. F2–F4, F8 dispatched to a fix executor; W5 figures dispatched; W1 search rebuild dispatched.
  - The appraisal confirmed the deliverable at about 62% submission-readiness with three genuine defects (stale file 56 summary; stale index/README; narrative missing the k4 rating block) — all agent-fixable and now queued — plus the honest ceilings (registration ≈7; no independent human screening yet; Scopus/ScienceDirect strings unrecoverable; 88 unretrieved).
  - When the manuscript is next rebuilt (W9), add: the D2 retrieval re-opening as a dated MAJOR amendment in Appendix B; the W4 second-pass results; any new studies from W1–W3; and the W5 figures (2 and 3) with captions.
- 2026-10-08: **D1 = yes** (author): a second person will screen, in a browser page.
  - **Sample resized** to fit about 6 hours. The original W6 sizes (20% of title exclusions plus all 237 full texts) would take about 25 hours.
    - Stage 1: 330 titles, stratified at seed 20261008. 250 drawn from the 1,768 title-excluded records and 80 from the 325 advanced to full text.
    - Stage 2: 40 full texts, 20 drawn from the 123 included and 20 from the 114 excluded.
    - Agreement will be weighted back to the population strata.
  - **Files:** sampling script and outputs in `D:\AvianInfluenzaSysRev_retrieval_20260927\human_check\`. `sample_public.json` is blinded and has no AI decisions or CAN IDs. `sample_key.json` holds the AI decisions and is never published.
  - **Page:** https://claude.ai/artifact/NT9auMwPRJ24xLjH4VPoD8. Decisions save to `decisions/<helper id>` in the page's database, with a backup in the browser. Only the owner can read them.
  - **Sharing:** invite the helper by email as Editor, or as Contributor if they are in the same organisation. Do not use a public link: outside visitors would be view-only, and the page would fall back to the backup text.
- 2026-10-08: **D2 = yes** (author): retrieval re-opened through legal loan or paid routes. The W4 open-route re-sweep starts now (executor), followed by an interlibrary loan request list for what remains.
- 2026-10-08: **W4 step 1 (open-route re-sweep) done and reviewer-checked.**
  - **Results:** 18 of the 88 now have a file: 10 full texts and 8 conference abstracts. 42 need a loan, 20 have no copy the agent could reach, and 8 have no identifier. Of the 33 priority reports, 5 are full text and 4 are abstracts. Laleye 2022 (CAN-0632) is closed at Wiley and is first on the loan list.
  - **Bot-gated files removed:** three files obtained after the browser auto-passed an anti-bot check (CAN-1291, 2023, 2040) were deleted, and those reports were moved to the author-download list. From now on: **one attempt per bot gate, never retried, never auto-passed.**
  - **Other reviewer fixes applied:** statuses corrected for CAN-0608, 1121 and 2095; Wiley "bronze" hints added for CAN-0607, 0609 and 0612; the CAN-0359 note reworded; the Wayback sweep limited to open-flagged records; overrides made permanent in `build_log.py`.
  - **Outputs:** `retrieval_pass2
etrieval_log_20261008.json` and `LOAN_REQUEST_LIST.md` (15 to download yourself, 19 priority loans, 33 other loans, 3 with nothing to request). Nothing has been screened yet.
- 2026-10-08: **The screening page was completed by the author, not by an independent second person.** The author said "I have answered". A copy is saved as `human_checkuthor_run_20261008.json`.
  - **Stage 1 (330 titles; 02:01-04:09 UTC):** agreement with the AI 57.3%, kappa 0.22 (0.16 weighted to the population). The author advanced or marked unsure 129 of the 250 titles the AI excluded, many plainly off-topic (Denmark wild birds, Ebola economics, Hubei influenza, producer constraints). 87 of the 330 records had been seen before in the author's 29-30 Sep verification.
  - **Stage 2 (40 full texts):** completed in about 7 minutes (about 10 seconds per paper), so these were not full-text reads. Agreement 75%, kappa 0.50. The author's includes conflict with the criteria (dromedary serology, a risk assessment without data, global models).
  - **Use:** this is **not** the W6 independent check and must not be reported as one. Treat it as a calibration pilot of the page and the instructions; whether and how to report it is decided later.
  - **Lessons for the helper version:** add worked examples for Stage 1 exclusions (other countries only, kits and vaccines, awareness and economics surveys without laboratory testing). Stage 2 must require opening the paper and noting the page or section relied on.
- 2026-10-09 (late; deadline): **D7 answered — "I need this by sunday": hard deadline Sunday 11 October 2026.** The Sunday critical path is at the top of file 15: figures + build today; W2 re-chase of the 43 quota-blocked seeds automated for Sat 01:10; Saturday W3 adjudication → register/flow integration → retrieval sweep → full-text screening → extraction/RoB/synthesis for new studies, with a **Saturday noon checkpoint** (any include not retrievable by then is reported as "not retrieved", not a silent drop); Sunday final rebuild, audits (files 01/02/04 + PRISMA-S), blind re-score, author items. Author questions queued one at a time: D1 follow-up, D4, D6, declarations (5 items), journal choice.
- 2026-10-09 (evening): **Author directive — the review work is the agent's job; no tasks delegated to the author except the final deliverable.** Retrieval closes at what legal open routes yield (loans optional); no author contact (D3 not pursued); no external helper for W6 (AI-only disclosure stands). **W5 figures fix round done and Figures 2–3 integrated; target rebuilt (94 pages, all checks passing).** **W3: 52 records dual-screened blind (agreement 92.3%, κ 0.852); 35 title-excluded, 17 advanced to full text; retrieval of the 17 running.** W2's 43 quota-blocked seeds queued for the 01:10 automation.

