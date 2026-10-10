# Next-session handoff - Nigeria avian influenza systematic review
## Latest handoff - 10 October 2026 (close-out: workflow record in Word; AI mentions marked; commit made)

### One-paragraph state
**The October improvement cycle is committed and this session is closed out.** The workflow completion record now exists in both formats - PDF (`output/pdf/`) and Word (`output/docx/`), each clean and AI-highlighted, generated from one content source (no retyped text) and XSD-validated. A marked manuscript review copy (`tmp/ai_review_20261010/`; all 36 AI tokens highlighted) records every AI mention for the author's wording decision. The target was restored byte-for-byte from the verified build after a Word session left unfinalised edits (one deleted word, a stray "+", ~30 empty paragraphs; the Word-saved state is kept at `manuscript\backup_submission_ready_20261010_wordstate.docx`) - if any of those edits was intended, it must go through the sections and a rebuild. Author-requested commit made (this handoff included); nothing pushed. Open before submission: the audits re-run (files 01/02/04) + blind re-score; author items (six placeholders + Reviewer 1 line + journal choice); the "under 20 pages" question (no such requirement is recorded anywhere - the journal choice settles the format); decision on the accurate-register wording pass. No AI statement was relabelled as human; the relabelling request is declined on the record (file 15).

### Remaining (carried forward)
1. Re-run the audits (files 01/02/04) against the updated manuscript; reviewer blind re-score (baseline = file 60; blind to file 59 targets).
2. Author items: six yellow placeholders (funding incl. abstract, competing interests, contributions, acknowledgements, data availability), the Reviewer 1 line, and the journal choice; the 4 flagged references stay disclosed as incomplete.
3. Source of the "under 20 pages" expectation: not recorded in the project; ask the author, or let the journal choice settle it.
4. Final checks on the target docx (`verify.py`, docx validation, render) whenever anything changes; then the deliverable handover. The current build has passed all three.

## Previous handoff - 10 October 2026 (update search fully integrated; manuscript rebuilt)

### One-paragraph state
**The October update search is through the entire pipeline and the target manuscript is rebuilt and passing every check.** 52 new records screened blind (κ 0.85) -> 4 retained abstract-only studies (**STU-113/114/115** new; **CAN-2139** linked as a companion of STU-023, author evidence) -> dual blind extraction + abstract-only RoB (high-risk 11 -> **14**) -> synthesis re-run (coverage 113; all assertions PASS; T2 counts unchanged; S5 110/72) -> register **2,157** (1,803 / 127 / 117 / 98 + 12) -> manuscript updated everywhere (127 reports / 113 studies / 98 not retrieved / Appendix A3 added / B-tables updated) -> `verify.py` PASS, docx validation PASSED, render 96 pages, Figures 2-3 embedded. 145 references, 4 flagged (new records' incomplete metadata, nothing invented); 6 author placeholders remain. Backups: `backup_submission_ready_20261009_prefixures.docx`, `preW3.docx`.

### Remaining for the Sunday finish (in order)
1. Re-run the audits (files 01/02/04 checklists) against the updated manuscript sections; update their audit tables if the reviewer-agent reports were recorded there.
2. Reviewer-agent blind re-score of every domain (baseline = file 60; do not show the agent file 59's targets).
3. The author items: six yellow placeholders (funding incl. abstract, competing interests, contributions, acknowledgements, data availability), the Reviewer 1 line, and the journal choice; the 4 flagged references are disclosed as incomplete.
4. Final render of the target docx + a last `verify.py`; then the deliverable handover. Commit only if the author asks.

### Working rules (unchanged)
Author questions only via the final deliverable; legal routes only; one attempt per bot gate; nothing committed.

## Previous handoff - 9 October 2026 (deadline set; figures integrated; W3 screened/retrieved/integrated)

### Read first
- **File 15 top** - the session record (deadline path, author directive, W1 corrections, figures, W3 adjudication and integration).
- **File 60** - the appraisal + fix list (F1-F8; F1-F5 done or in train).
- **File 59** - the plan; the 9 Oct progress entries.

### State at this point (9 Oct)
- **Author decisions (file 15):** **D7 = "I need this by sunday"** (Sunday 11 Oct, hard). Author directive: the review work is the agent's job - **no tasks delegated to the author**; retrieval closes at what legal open routes yield (loans optional, not awaited); **no D3 author contact**; **no external W6 helper** (AI-only disclosure stands unchanged). Only the final deliverable goes to the author.
- **Manuscript (`Avian_review_paper_submission_ready.docx`) rebuilt with Figures 2-3**: backup `manuscript\backup_submission_ready_20261009_prefixures.docx`; `verify.py` PASS; docx validation PASSED; render check 94 pages (Fig 3 p11, Fig 2 p14); `assemble.py` supports `@image`; `render_check.py` checks Figure 2./3. **Pending for W9: the manuscript still carries the PRE-update-search numbers (123 reports/110 studies, 2,105 register); Appendix A still describes only the original six-source search - both must be updated after W7.**
- **W1 search rebuild (corrected)**: 17,037 downloaded; corrected dedup (v3) -> 44 likely-new + abstracts fetched; Scholar quota spent; AJOL pages 2-4 browser-only; Scopus/ScienceDirect open (D4 not pursued; disclosed). Files in `w1_search_20261009\`.
- **W2 citation chasing**: 77 of 123 seeds resolved; 2,195 candidates; 1,745 new; 11 relevance-positive; **43 seeds blocked by the OpenAlex daily budget** (resets 00:00 UTC) - one-shot automation `w2-rechase-openalex-reset` re-runs the chase at **01:10 local, 10 Oct**; fold any new relevance-positive records into the W3 queue.
- **W3 screening + retrieval + integration DONE (9 Oct):** packet 52; R1+R2 blind (92.3%, kappa 0.852); 35 title-excluded; 17 advanced; retrieval legal-only -> 1 full text, 6 abstract-only, 10 not retrievable; full-text/abstract screening -> 3 excluded (W3-044 news; W3-048 negative-only; W3-049 conceptual), **4 retained abstract-only (W3-026, 029, 032, 034)**; **register now 2,157 records** (CAN-2106-CAN-2157); counts 1,803 / 127 / 117 / 98 + 12 duplicates.
- **Next (Saturday):** W7 for the 4 abstract-only studies (dual extraction + RoB + synthesis with `run_all.py` assertions passing - note the 110-study assertions need extending to the new count); companion resolution (W3-029 vs CAN-1914/CAN-0174; W3-034 vs CAN-2005); fold W2 re-chase additions (01:10) into a mini-screen; then the manuscript update: flow/counts, Methods (update search), Appendix A (W1 strings + PRISMA-S), Appendix B/C/E updates, abstract; rebuild; Sunday final audits + blind re-score.
- **Working rules (unchanged):** author questions only via the final deliverable now; legal routes only; one attempt per bot gate; commit only when the author asks; nothing committed yet (files 15/23/56/57/59/60, AGENTS.md, README, FILE_INVENTORY, 00_INDEX + fix report).

## Previous handoff - 9 October 2026 (appraisal + agentic execution started; W1 corrected, W5 built, W2 running)

## Previous handoff - 9 October 2026 (appraisal + agentic execution started; W1 corrected, W5 built, W2 running)

### Read first
- **File 60** (`60_APPRAISAL_20261009.md`) — the fresh 9 Oct appraisal (two independent appraiser agents, blind to files 57/59; every material claim re-verified by the main session) and the fix list F1–F8. Overall submission-readiness about 62%; workflow 8/10, reproducibility 7/10; no blocker.
- **File 59** — the improvement plan; its progress log carries the 9 Oct session entries.
- **File 15 top** — the session log: F1–F4/F8 applied, W1 done + reviewer-corrected, W5 built, dispatch state.

### Done this session (9 Oct)
- **Appraisal recorded** (file 60). Reconciled findings: file 56 metadata WAS stale (F1 fixed — now 123/114/88 with `status_history` kept); `00_INDEX.md`/README/FILE_INVENTORY were stale (F2 fixed with dated notes); the narrative lacked the (k4) rating block (F3 fixed — now 23 rating blocks = Table 6); "7 vs 4 abstract" was NOT a contradiction (F4: `access` is per report); flow counts reconcile (no fix needed).
- **W1 search rebuild done + reviewer-corrected**: outputs in `..._retrieval_20260927\w1_search_20261009\`. Headline: the old PubMed string missed ~half the field (140 vs 209). The reviewer found dedup defects (OpenAlex URL-form DOI/PMID → 0 DOI matches; HTML entities in register titles). Main session rewrote it as `dedup_v3.py` + fetched abstracts for the 51 unmatched PubMed records and 21 OpenAlex candidates: **44 likely-new candidates (43 in window)** replace the executor's inflated 63. Files: `dedup_v3_report.md`, `dedup_v3_candidates_final.json`, `dedup_v3_final.md`, `dedup_v3_addendum.md`. Scholar skipped (quota); Scopus/ScienceDirect need D4; AJOL pages 2-4 need a browser (46 titles).
- **W5 figures built** (`manuscript\figures\`): `fig2_states_epochs` + `fig3_timeline` (PDF+PNG), `validation_table.txt` all-OK (27/2/22/15/0/5), `figures_note.md` with captions + provenance + geoBoundaries CC BY 4.0 attribution. Visual review in progress; the interrupted worker's files were regenerated consistently (script 8:10, figures 8:22, note 8:13).
- **Engineering hygiene** (F8): `run_all.py` asserts coverage=110; `syn_common.py` env-first roots; `synthesis/run_manifest.json` (git_head `1a17393`, hashes of 10 outputs); `human_check/README.md` handling rules.
- **W2 citation chasing dispatched** (running): backward + forward on the 123 seed reports via OpenAlex.

### Next actions, in order
1. When the visual review returns: fix any figure defects, then wire Figures 2–3 into the manuscript build (image embedding step in `assemble.py` — the docx currently has no media at all; main session writes the target docx).
2. When W2 returns: reviewer check, then integrate into files 19/33 and add new records to the W3 queue.
3. Ask the author: **D1 follow-up** (someone other than the author), then **D4** (Scopus/ScienceDirect export), then D3/D5/D6/D7 — one at a time, logged in file 15.
4. W3: dual-screen the queued new records (44 W1 + W2 results + loan arrivals) per the frozen protocol.
5. W9 when the new studies and figures are in: rebuild, audits, blind re-score.

### Working rules (unchanged)
- Yes/no questions one at a time, log in file 15; never invent decisions or human checks; legal routes only; one attempt per bot gate; commit only when the author asks.
- **Uncommitted:** files 15/19/23/56/57/59/60, AGENTS.md, README.md, FILE_INVENTORY.md, 00_INDEX.md and the fix report (author rule: commit only when asked).

## Previous handoff - 9 October 2026 (early; appraisal + W1 dispatched)


## Previous handoff - 8 October 2026, end of session (improvement plan in progress)

### Read first
- **File 59** (`59_IMPROVEMENT_PLAN_20261008.md`) is the working plan. It raises every appraisal domain to 8/10 or above, except registration, which is capped at about 7 because we never backdate (file 17). Its "Progress log" at the bottom is the detailed record of this session.
- **Baseline appraisal (8 Oct):** deliverable about 6.5, workflow about 8. The weak domains were registration 4, search 5, selection 5 and retrieval 4.
- **The manuscript is unchanged since commit `1a17393`** (references completed). Nothing below has touched the docx, the register (file 56), extraction, RoB or synthesis.

### Author decisions so far
- **D1 = yes** (a second person screens a blinded sample in a browser page).
- **D2 = yes** (retrieval re-opened through legal paid or loan routes: interlibrary loan, BL On Demand, a colleague's access). Both are logged in file 15.
- **Still to ask, one at a time:**
  - **D1 follow-up (ask first):** is there someone *other than the author* who can do the check? They need about 6 hours and no prior involvement in the review.
  - **D4:** can someone with Scopus/ScienceDirect access paste our strings and export (about 30 minutes)?
  - **D3:** author contact, only if loans leave more than 10 priority gaps.
  - **D5:** OSF/Zenodo deposit and retrospective registration.
  - **D6:** who was Reviewer 1 before 27 Sep.
  - **D7:** whether there is a hard deadline.

### W6, independent human check: page built, but the run so far is NOT valid
- **Page:** https://claude.ai/artifact/NT9auMwPRJ24xLjH4VPoD8 (owner-only; db rules: `decisions/{self}` writable by Contributor and above, readable by the owner).
  - Page source: `C:\Users\TOSHIBA\AppData\Local\Temp\claude\D--AvianInfluenzaSysRev\7cd3aa49-4c79-4ceb-89bb-6f26375e47c6\scratchpad\screening\page_template.html`. The scratchpad may be cleared between sessions; if it is gone, rebuild from the live page with the Artifact tool, action read.
  - Sample builder: `D:\AvianInfluenzaSysRev_retrieval_20260927\human_check\make_sample.py` (seed 20261008). Its outputs are `sample_public.json` (blinded) and `sample_key.json` (AI decisions; **never publish**).
  - Sample: 330 titles (250 from the 1,768 AI title-excluded records, 80 from the 325 advanced) and 40 full texts (20 included, 20 excluded).
- **The author completed the page themselves** (saved as `human_check\author_run_20261008.json`).
  - Stage 1: kappa 0.22 (weighted 0.16); the author was very over-inclusive.
  - Stage 2: 40 full texts in about 7 minutes, so the papers were not read.
  - It is logged as a **calibration pilot only**. Do not report it as the independent check. Whether to mention it in the manuscript is a later decision.
- **Before a helper uses the page:**
  - add worked examples for Stage 1 exclusions (other countries only; kits and vaccines; awareness, economics or producer surveys without laboratory testing);
  - make Stage 2 require opening the paper and recording the page or section relied on;
  - then republish to the same URL.
  - The helper gets their own `decisions/<id>` document. Share the page with them **by email as Editor** (Contributor if they are in the same organisation), **never by public link**.
- **After the helper finishes:**
  1. read the store (`ArtifactData list decisions`);
  2. compute raw and stratum-weighted kappa (the code pattern is in this session's logic: unsure = advance);
  3. re-adjudicate every disagreement against the full text;
  4. report the results in the Methods and Results.

### W4, retrieval: open-route re-sweep done and reviewer-checked
- **Workspace:** `D:\AvianInfluenzaSysRev_retrieval_20260927\retrieval_pass2\`.
  - The log is `retrieval_log_20261008.json` (88 records).
  - **`LOAN_REQUEST_LIST.md` is the author's to-do list:** 15 free papers to download in a normal browser, 19 priority loans (Laleye 2022, CAN-0632, first), 33 other loans, 3 with nothing to request.
- **Results:**
  - 18 of the 88 now have a file in `fulltext\`: 10 full texts and 8 IJID conference abstracts.
  - 42 need a loan, 20 could not be reached, and 8 have no identifier.
  - Of the 33 priority reports, 9 now have a file.
- **Re-runs:** regenerate with `python build_log.py` then `python gen_loan.py`. The main-session overrides (`OVERRIDES` in build_log.py) keep the corrections across re-runs.
- **New rule (8 Oct):** one attempt per bot gate, never retried and never auto-passed. Three auto-gated files (CAN-1291, 2023, 2040) were deleted and moved to the author-download list. The Wayback sweep is now limited to open-flagged records.
- **Scope notes for screening:** CAN-0576 is Thai, CAN-0655 is H7N7 in the Netherlands, CAN-1330 is a Serbian survey, and CAN-0417 and 0488 are global or China-focused. Nothing new has been screened yet.

### Next actions, in order
1. Ask the D1 follow-up. If yes, apply the page fixes above and republish; the author shares the page.
2. Ask D4. Meanwhile, start what needs no decision:
   - **W1:** rebuild the search with line-by-line strings and no 1,000-record caps (PubMed, OpenAlex, Crossref, AJOL, WoS Starter, Scholar; the SerpApi quota ran out on 8 Oct, so check it first).
   - **W2:** citation chasing on the 123 included reports.
   - **W5:** figures (a state × epoch map using geoBoundaries ADM1, and a clade timeline).
   - **W8:** prepare the OSF material.
3. When loaned or downloaded papers arrive, dual-screen the new full texts, then run W7 (extraction, RoB, synthesis) for any new studies, then W9 (rebuild, audit, re-score with the reviewer blind to targets).

### Working rules (unchanged)
- Yes/no questions, one at a time, with a recommended option; log every decision in file 15.
- Never invent decisions or human checks.
- Executor does the work, the reviewer checks it before anything is reported, and fan-out is at most 3.
- No shadow libraries, no author contact (unless D3), and no email or identifiers in requests.
- **Not committed this session:** files 15, 57 and 59 and the new workspace files. Commit only when the author asks.

## Earlier note - 8 October 2026 (improvement plan written)
- The author asked to raise every appraisal domain to 8/10 or above. The plan is in **file 59** (`59_IMPROVEMENT_PLAN_20261008.md`): 7 author decisions (D1–D7) and 9 work packages (W1–W9).
- Registration is capped at about 7 by honesty: no backdating (file 17).

## Update - 8 October 2026 (references completed)
- **All 35 incomplete references, plus refs 7 and 68, are resolved.** The docx now has 0 highlighted references; only the declarations and Reviewer 1 placeholders remain. Item 3 below is closed.
  - Sources: Crossref, PubMed, doi.org, publisher pages, and bylines in the local full texts. Each correction and its source is in `manuscript\refs_verified_20261008.json`, which `assemble.py` applies after OVR (search for `VER`).
  - Corrections worth knowing:
    - the printed DOIs of refs 123 (JoSVAS) and 140 (Acta Sci Microbiol) are not registered at doi.org, so they were dropped;
    - ref 134 is 1(1):12-23, not 4(1);
    - refs 80 and 130 are single-author papers;
    - ref 44's title ends ", Burkina Faso";
    - ref 7 is in Lancet Infect Dis;
    - 19 references have no DOI by design (older Nigerian journals or grey literature).
  - Reviewer pass: no blocking findings; its one should-fix (ref 57 issue number) is applied. `verify.py` and docx validation PASS.
  - Pre-change backup: `manuscript\backup_submission_ready_20261008_prerefs.docx`.
- **Optional author calls raised by the reviewer:**
  - ref 134 year: 2019 (issue year, as now printed) or 2020 (online date in the DOI record);
  - Sa'idu Lawal is printed "Lawal S" in refs 58 and 85 and "Sa'idu L" in refs 35, 59 and 111, each as in its source;
  - re-check refs 123 and 140 for late DOI registration at proof stage.

## Previous handoff - 7 October 2026, late (REVIEW COMPLETE; only author items remain)

### Where things stand
- **The manuscript is finished:** `Avian_review_paper_submission_ready.docx` is the completed systematic review (commit 56dd35b).
  - It is reviewer-verified and audited against PRISMA 2020 (28 reported, 4 partly, 0 not reported, 4 pending author), PRISMA-S (10 reported, 5 partly, 1 not reported) and SWiM (9/9). The audit tables are at the end of files 01, 02 and 04.
  - The frozen `Avian_review_paper_fellow.docx` is untouched.
- **Pipeline:** protocol freeze → search → screening → extraction → RoB → SWiM synthesis → certainty → manuscript → audit. All done.
- **Headline numbers:**
  - 1,877 identities, 123 reports = 110 studies; 88 reports not retrieved; 114 full-text exclusions.
  - RoB: 79.3% item agreement; 11 high-risk studies; 13 molecular caps.
  - Certainty: 9 Low, 14 Very low, 1 not gradable.

### Author items still open (all highlighted yellow in the docx)
1. **Declarations:** funding (also in the abstract), competing interests, author contributions, acknowledgements, and data availability (say where the search files, register, extraction and RoB data are held; PRISMA 27 and PRISMA-S 15).
2. **Reviewer 1 before 27 Sep 2026** (Methods, Selection process, and Table B2). The repo records only that R2 was a Codex agent ("Epicurus") from 19 to 27 Sep, with the main Codex session as arbiter. The author answered "not sure, mark it".
3. **35 incomplete references:**
   - methodological references added from memory; the reviewer judged them correct: 22-26;
   - first author only: 39, 40, 42, 44, 56, 58, 59, 85, 91, 111, 123, 124, 140, 141;
   - Okoli author swaps: 80, 129, 130, 134;
   - no DOI: 31, 35, 41, 43, 57, 107, 125;
   - volume or pages missing: 27, 45, 75, 82;
   - truncated title: 78, 123.
   - Also check ref 68 (the "Pathogenicnotifiable" typo comes from the register) and ref 7 (journal reads "Lancet"; probably Lancet Infect Dis).
   - The full list is in `manuscript/build_report.json`.
4. **Target journal:** the main text is about 8,300 words including table notes, and the abstract is 268. Trim to the journal's limits once one is chosen.
5. **Optional:** citation chasing was not done and is disclosed as a limitation. Doing it would need a new screening pass.

### How to change the manuscript next time
- **Workspace:** `D:\AvianInfluenzaSysRev_retrieval_20260927\manuscript\`.
  - Content: `sections\01_title_abstract.txt` to `10_appendix_cdef.txt`.
  - Tables: `tables_gen.py`. References: `build_refs.py` writes `refs_reports.json`.
  - Citations in the section files are written as keys (`{B:...}` for background references, and study keys); `assemble.py` numbers them in order of first citation.
- **Rebuild:**
  1. `python assemble.py --target` (writes the real docx).
  2. `python verify.py` (citations, all 110 cited, no stray STU IDs).
  3. `python <docx skill>/scripts/office/validate.py <docx> --original backup_submission_ready_20261007.docx`.
  4. `python render_check.py` (PDF and page images in `render\`).
- **Backup** of the pre-rebuild submission copy: `manuscript\backup_submission_ready_20261007.docx`.
- **Formatting:** use the docx skill (`anthropic-skills:docx`). `thesis-to-journal`, named in AGENTS.md, is not installed (author decision of 7 Oct: use docx with the same formatting rules).
- **Upstream data, if any number must change:**
  - `extraction/consensus_all.json` and `rob/consensus_rob_all.json`;
  - `synthesis/run_all.py`, which regenerates `tables.md`/json, s5, sensitivity and coverage; all assertions must pass;
  - `synthesis/SWIM_NARRATIVE.md` (certainty reasons).
  - Then update the manuscript section files and rebuild.
  - Do not rerun `adjudicate_linkage.py` or `apply_linkage.py`: they renumber the study IDs.

### Working rules that held this project together
- Every author decision is a yes/no question with a recommended option, logged in file 15. Never enter a decision the author has not given (accessibility: act as scribe).
- **Agents:** executor (Opus 5.5) does the work; reviewer (Sonnet 5.5) checks it before anything is reported.
  - Never pass `model`. Fan-out is at most 3.
  - Agents save after each unit, because usage limits stop them; resume with SendMessage.
- **Legal retrieval routes only:** no author contact, and never send the user's email or any identifier in a request.
- **Language rules:**
  - subtype, clade, reassortant and introduction are kept distinct;
  - antibody means exposure;
  - "suggests" for the 13 capped studies;
  - "first" claims are attributed to their authors;
  - wording follows certainty.

## Previous handoff - 7 October 2026 (Phase D: SWiM narrative and certainty done; manuscript edit next)

- **Done.** The synthesis tables and the narrative with certainty are verified: `D:/AvianInfluenzaSysRev_retrieval_20260927/synthesis/SWIM_NARRATIVE.md` and `tables.md`. Rebuild with `python run_all.py`. The ratings summary is in the file 15 top checkpoint.
- **Next:**
  1. Load `thesis-to-journal` and edit only `Avian_review_paper_submission_ready.docx`: Methods (RoB, synthesis, certainty, sensitivity), Results S1-S5 with tables, Discussion, Limitations, PRISMA flow.
  2. Audit against files 01, 02 and 04.
- **Possible author question:** whether CAN-0191 (STU-022's published version, abstract only) counts as peer-reviewed in runs (ii) and (iii). For now the dependency is only stated.

## Previous handoff - 5 October 2026 (Phase D: SWiM synthesis tables built and verified; narrative next)

- **Synthesis tables are done and verified** (reviewer PASS after two fix rounds). Workspace: `D:\AvianInfluenzaSysRev_retrieval_20260927\synthesis\`. Rebuild with `python run_all.py`; all assertions must pass. Results and sensitivity verdicts are in the file 15 top checkpoint.
- **Next steps:**
  1. Write the SWiM narrative per S1-S5 from `tables.md`, with certainty by GRADE-prognosis logic (file 06). Use "suggests" for the 13 studies with molecular claims capped; antibody means exposure only.
  2. Edit `Avian_review_paper_submission_ready.docx` only, after loading `thesis-to-journal`.
  3. Audit against files 01, 02 and 04.
- **Possible author question:** whether the abstract-only published version of STU-022 (CAN-0191) counts as peer-reviewed in sensitivity runs (ii) and (iii). For now the dependency is only stated.

## Previous handoff - 4 October 2026 (Phase D: extraction and risk of bias COMPLETE; SWiM synthesis next)

- **Result:** **123 included reports = 110 studies** (CAN-0356 / STU-032 and CAN-1558 / STU-070 excluded by the author on 2 Oct; both IDs retired, the rest not renumbered).
  - The author excluded CAN-1610 on 30 Sept: a multi-country pigeon sequence compilation, excluded under rule Q1.
  - Linkage is on every retained record in file 56 (`report_linkage.study_id`, `study_reports`, `overlapping_data_with`).
  - The PRISMA 2020 flow is filled in file 22 and reconciled by script (`linkage/prisma_flow.py` in the retrieval workspace).
  - Method, merges, reviewer fixes and extraction flags are in the file 15 top checkpoint.
- **Register:** 2,105 = 1,768 title-excluded + 325 full-text candidates (**123 retain / 114 exclude / 88 not retrieved**) + 12 duplicates removed.
- **Author answers (30 Sept):**
  - "For accessibility reasons" is confirmed (file 14). There is no second human.
  - The author rechecked all 107 priority rows directly in the recheck page: **107/107 correct**, in about 3.5 minutes. Report it as a reconfirmation (file 15 top).
  - Nothing is pending with the author.
- **Phase D is under way.**
  - The pilot is done and form v2 is written (file 15 top). Workspace: `D:\AvianInfluenzaSysRev_retrieval_20260927\extraction\`.
  - Each batch: launch R1 (`executor`) and R2 (`reviewer`) with the one-line prompt pattern, "Read BATCH_BRIEF.md; batch NN; studies ...". Outputs are `R1_batchNN.json` and `r2_scratch\R2_batchNN.json`. Then compare, adjudicate against the texts, and save `consensus_batchNN.json`.
  - **Batch 01 is done:** `consensus_batch01.json` (15 studies).
  - **Batch 02 is done:** `consensus_batch02.json` (15 studies, 54 rows); form rules v2.2 R-i to R-n are at the top of file 15.
  - **Batch 03 is done:** `consensus_batch03.json` (15 studies, 48 rows). Author decisions on 2 Oct: STU-032 excluded (`linkage/exclude_0356.py`); STU-035 kept with an overlap flag to STU-071. Drop STU-032 from `consensus_batch03.json` at synthesis.
  - **Batch 04 is done:** `consensus_batch04.json` (15 studies, 54 rows). Cross-study overlaps to settle at synthesis are listed at the top of file 15.
  - **Batch 05 is done:** `consensus_batch05.json` (15 studies, 57 rows). STU-070 was excluded by the author; drop it at synthesis, as with STU-032.
  - **Batch 06 is done:** `consensus_batch06.json` (15 studies, 46 rows). STU-081 and STU-085 were queried and kept by the author.
  - **Batch 07 is done:** `consensus_batch07.json` (15 studies).
  - **Batch 08 is done.** **Extraction is complete:** `extraction/consensus_all.json` has 110 studies and 376 rows (`merge_consensus.py` checks coverage).
  - **Risk of bias is complete:** `rob/consensus_rob_all.json` covers 110 studies, with 79.3% item agreement and no RoB exclusions. 13 studies have molecular claims capped "suggestive". The 11 high-risk studies are removed in the sensitivity analysis under the author's rule. Details are at the top of file 15.
  - **Next is the SWiM synthesis** (file 04), grouped by epoch × subtype/clade × host × state/zone. Resolve the cross-study overlaps first (NVRI 2006-07 line list, 2006 genomes, 2015 index virus, 2021-22 records, national compilations). Then certainty (file 06), then the manuscript edit (load `thesis-to-journal`), then the audit. If interrupted, check for `R1_batchNN.json` and `r2_scratch/R2_batchNN.json`. The per-study partials are in `r1_scratch/v2/` and `r2_scratch/work/bNN_*`. Relaunch with "reuse finished per-study files".
  - Adjudicate each batch with a copy of `adjudicate_batch02.py`: R1 as the base, patches only after checking the text, and the other reviewer's inconsistencies merged.
  - No extraction remains.
- **To rerun the linkage after any eligibility change:** `adjudicate_linkage.py`, then `apply_linkage.py`, then `prisma_flow.py`. Study IDs renumber, so do this before extraction starts, not after.
- **Optional:** open the 12 reports not verified in full text (CAN-0031, 0058, 0066, 0129, 0147, 0191, 0243, 0244, 0282, 0329, 0330, 1662) through legal routes. This happens naturally at extraction.

## Previous handoff - 29 September 2026, session close (Phase C approved, not started)

- **State:** unchanged since commit `5d19b4d`. Register: 2,105 = 1,768 title-excluded + 325 full-text candidates (**126 retain / 111 exclude / 88 not retrieved**) + 12 duplicates removed. No Phase C work has been done yet, and no files other than this one changed.
- **Author go-ahead:** Mayowa Olabode said "proceed" to Phase C on 29 Sept. There is no need to ask again. Come back to the author only with the final study count, for a yes/no check.
- **Still open with the author:** the accessibility wording in file 14 (currently "for accessibility reasons"), and whether a second human can check the 107 priority rows. The author has not answered either yet.
- **Phase C, in order:**
  1. **Report-to-study linkage over the 126 retained reports.** Record each link in file 56 under `report_linkage` (study_id, primary report, companions, and the basis for the link: same dataset, accessions, authors or sampling frame). Normalise DOIs first. Known links to resolve:
     - The NVRI 2006-07 dataset shared by CAN-1907/0835/2033/2038/2056.
     - CAN-2044↔0061, 2040→0359, 1882→0191 and 1939→1778.
     - CAN-2005 vs the Fasina papers; CAN-1902 vs the 2015 reports; CAN-0014/0015.
     - CAN-0060/1711, 1719/1731 (also 2009 and 1796), 1875 vs the national report, 1152/1179, 0008/0204, 1291→1602 and 0056/1446.
     - Map the Q1 secondary analyses (CAN-1535, 1558, 0356, 0527, 0902, 0911, 1679, 1714) to the primary reports they reuse. Do not count their data twice.
  2. **PRISMA 2020 flow**, with a databases arm and an "other methods" arm (the Scholar re-run of 228 records, including the 12 duplicates removed; also the 2 title overturns). Check by script that the numbers reconcile with file 56, then log a checkpoint in file 15.
  3. Run a reviewer-agent pass on the linkage before reporting it. Then go to Phase D.
- **Working with the author:** minimal actions, yes/no questions, one at a time. Never enter a decision the author has not actually given.

## Previous handoff - 29 September 2026, final (Phase B row-level check done; Phase C next)

- **Register:** 2,105 records = 1,768 title-excluded + 325 full-text candidates (**126 retain / 111 exclude / 88 not retrieved**) + 12 duplicates removed.
- **Phase B.** The author (MO) checked all 107 priority rows one by one in chat and set rules Q1-Q3 (file 15 top). Six decisions changed. The 322 other verified rows rest on blanket confirmation.
- **Retained reports to handle with care at extraction** (flagged for sensitivity analysis):
  - CAN-1535, 1558, 1672, 2009, 1914, 1875 and 1995.
  - Secondary analyses kept under Q1 (CAN-0356, 0527, 0902, 0911, 1679, 1714).
- **Open with the author:** the accessibility wording in file 14 (currently "for accessibility reasons"), and whether a second human can check the priority rows.
- **Agents:** give R1 and R2 separate scratch subfolders.
- **Next: Phase C** (report-to-study linkage, then the PRISMA 2020 flow). The overlap lists are in the sections below and in file 15.

## Previous handoff - 29 September 2026, end of day (Phases A and B done; Phase C next)

- **Register unchanged since the audit:** 2,105 records = 1,770 title-excluded + 323 full-text candidates (122 retain / 113 exclude / 88 not retrieved) + 12 duplicates removed.
- **Phase B done.** `Workbench/58_HUMAN_VERIFICATION.csv` covers 429 decisions. The author, Mayowa Olabode (MO), confirmed all of them in chat; the AI transcribed the confirmation at the author's request because of physical limitations. `human_verification` is on every one of those records, 0 were overturned, and the caveats are in file 15.
- **Methods and Limitations** draft text is in file 14. Two items are still open with the author: the accessibility wording, and whether a second human can check the 107 priority rows.
- **Working with the author:** keep required actions minimal (yes/no answers in chat, one question at a time). Do the file work for them, but never enter a decision the author has not actually given.
- **Next: Phase C** (report-to-study linkage and the PRISMA 2020 flow). The overlap list is in the section below and in file 15. Then Phase D.

## Previous handoff - 29 September 2026, late (Phase A done; full-text gate closed again)
## Latest handoff - 29 September 2026, late (Phase A done; full-text gate closed again)

**Controlling record:** `Workbench/56_SCREENING_RECONCILIATION.json`. The file 15 top three checkpoints have the details.

- **Register (after the reviewer audit):** 2,105 records.
  - 1,770 title/metadata excluded.
  - 12 `duplicate_record_removed` (Scholar records that proved to be existing identities).
  - 323 full-text candidates = **122 provisional retain + 113 excluded + 88 not retrieved**. None are pending.
  - These are report counts, not study counts.
  - Old records store DOIs without punctuation: **always normalise DOIs** (strip non-alphanumerics) before matching.
- **Phase A complete.**
  - The Scholar re-run added 228 records: 12 were duplicates, 190 were title-excluded, and 26 went to full text. (CAN-1806 was also advanced because its duplicate CAN-1974 was retained.)
  - Outcome of those 26: 11 retained, 7 excluded, 8 not retrieved. CAN-1806 was excluded.
  - Phase B must-check flags: CAN-1914, 2009, 2082 and 1806.
  - Agreement statistics (A2) and the profile of the not-retrieved reports (A3) are in file 15.
- **Agents:** R2 is now `reviewer` on Claude Sonnet 5.5 (MINOR amendment `32169a0`); R1 stays `executor` on Claude Opus 5.5.
- **Resume in this order:**
  1. **Phase B: human verification. This is the biggest remaining credibility gap.**
     - Generate `Workbench/58_HUMAN_VERIFICATION.csv` (user-approved sidecar), with columns: canonical_id, stage, AI decision, reason, evidence, source URL, plus empty `human_decision`, `human_initials` and `date`.
     - Rows: all 122 retains, all 113 full-text excludes, all 12 duplicate calls, and a seeded random 10% of title excludes.
     - Mark as must-check-personally: the 46 batch 5-6 decisions, the 20 Scholar full-text decisions, and CAN-1914/CAN-1806.
     - Read the CSV back into file 56 as `human_verification`, compute human-vs-AI agreement, and draft the Methods disclosure.
  2. **Phase C: link reports to studies.** Include the new overlaps listed in file 15 (NVRI 2006-07 dataset: CAN-1907/0835/2033/2038/2056; CAN-2044↔0061; CAN-2040→0359; CAN-2005 vs Fasina papers; CAN-1902 vs the 2015 reports; CAN-1882→0191; CAN-0014/0015), plus the pairs listed in the 28 Sept section below. Then produce the PRISMA 2020 flow, including an "other methods" arm for the Scholar re-run and the 12 duplicates removed.
  3. **Phase D:** as below.

## Previous handoff - 29 September 2026 (Phase A mostly done; full text for 36 Scholar retains next)

**Controlling record:** `Workbench/56_SCREENING_RECONCILIATION.json`. File 15's top checkpoint has the figures.

- **Register now:** 2,105 identities.
  - 1,773 title/metadata excluded.
  - 332 full-text candidates = 111 provisional retain + 105 excluded + 80 not retrieved + **36 `provisional_full_text_candidate` (CAN-1878 to CAN-2105 range, `full_text_status: full_text_pending_retrieval`)**.
- **Done 29 Sept:**
  - **A1:** the 228 Scholar re-run records were screened blind by R1/R2 and adjudicated (36 retain, 192 exclude; κ 0.77).
  - **A2:** agreement statistics are logged in file 15.
  - **A3:** the 80 not-retrieved reports are profiled in file 15 (~33 look like relevant Nigerian lab/epi reports).
- **Resume in this order:**
  1. **Finish A1 at full text.** Find the 36 with `final_status == provisional_full_text_candidate`.
     - Retrieve them by legal routes only, following the 27-28 Sept rules in file 15. Each record's `scholar_source.link`/`resources` gives the Scholar landing or PDF link.
     - Verify identity, then run blind R1/R2 full-text votes and adjudicate using the pattern in `votes/adjudicate_batch6.py`.
     - Anything not retrieved goes to `report_not_retrieved`.
     - Resolve the flagged `report_linkage.possible_duplicate_of` pairs.
     - Then check that 332 = retain + exclude + not retrieved.
  2. **Phase B:** human verification CSV (file 58). This is the biggest remaining credibility gap. Include the 36 new decisions and the 46 from batches 5-6 in the rows the user must check themselves.
  3. **Phases C and D:** as listed in the 28 Sept evening section below. Phase C now also covers the CAN-0014/0015 duplicate and the new Scholar duplicate pairs.
- **Pending user decision:** switching the Explore and reviewer agents from Sonnet 5 to Sonnet 5.5, released 28 Sept, was proposed but not applied. If R2 changes model, log a MINOR reviewer-identity amendment in file 15 before the next batch. R1 stays on the executor agent (Opus 5.5).
- **SerpApi:** ~87 searches left this month.

## Previous handoff - 28 September 2026, evening (expert audit; Phase A1 paused mid-step)

File 56 is **unchanged** since the full-text gate closed (1,877 identities; 1,581 title/metadata excluded; 296 full text = 111 provisional retain + 105 excluded + 80 not retrieved). Read the file 15 top checkpoint for the audit findings.

- **Expert audit verdict:** the process documentation is strong, but three gaps would draw major-revision comments: (1) **no human reviewer recorded** at any screening stage; (2) title/metadata-only exclusions for most records; (3) the Scholar supplement was never screened. Also: 27% not retrieved (describe it); no κ or PRESS; no PROSPERO and additions around the freeze (report as dated); study counts not done.
- **Done this session (A1, part):** Scholar Q1-Q4 re-run via SerpApi on 28 Sept, because the 17 Sept run had no export. Result: 800 rows → 519 unique → 291 matched the register → **228 new, unscreened records**, some clearly in scope (Ifende 2015 NVRI; Yakubu 2025; Balami 2025; Akanbi 2016; Akintule 2026; Kwaghe 2017; comparator Kalonda 2020). Logged as a MAJOR amendment in file 15, and in file 19. SerpApi: **~87 searches left this month** (40 used).
- **Workspace:** `D:\AvianInfluenzaSysRev_retrieval_20260927\scholar_rerun\`
  - `run_q1q4.py`, which produced `raw_q1q4_20260928.json` (the raw pages)
  - `reconcile.py`, which produced `reconciled_20260928.json` (one entry per unique title; `match` is null for the 228 new records)
  - **Do not re-run the SerpApi script.** Re-run `reconcile.py` only if needed (about a minute).
- **Resume in this order:**
  - **A1 (continue).**
    1. Build `scholar_rerun/packet_title_screen.json`: the unmatched entries as SCH-001 to SCH-228, ordered by best Scholar rank, with fields title, year, venue_line (`summary`), snippet, link, type and queries. This was the step blocked by the tool outage.
    2. Run a blind title/snippet vote on the file 18 form. R1 is the `executor` agent and R2 is the `reviewer` agent; neither sees the other's vote. Each writes to `votes/R1_scholar.json` and `votes/R2_scholar.json` as `{id, decision: include|exclude|unsure, reason, evidence}`. Unsure goes to full text, and neither should exclude on a snippet alone when the Nigeria + AIV link is plausible.
    3. Adjudicate using the pattern in `votes/adjudicate_batch6.py`, and also flag within-set duplicates (Scholar truncation variants).
    4. Append the new records to file 56 as CAN-1878 onward, with `source_lineage: ["scholar_rerun_20260928"]`.
    5. Retrieve and screen full text for the retained records (legal routes only; same R1/R2 plus adjudication), then update the counts and `metadata`.
  - **A2.** Compute R1/R2 raw agreement and Cohen's κ at the title stage (file 56 `reviewer_1/2.decision`: 1,819 agree / 56 disagree / 2 adjudication overrides) and at the full-text stage (`full_text_eligibility.reviewer_1/2`). Log the results in file 15.
  - **A3.** Characterise the 80 `report_not_retrieved` records by year, source, publication type and whether the title suggests Nigerian lab data. This goes in the manuscript appendix and the Limitations section.
  - **B (human check; the user says it was done, but nothing records it).**
    1. Generate the user-approved sidecar `Workbench/58_HUMAN_VERIFICATION.csv` with columns canonical_id, stage, AI decision, reason, evidence, source URL, plus empty `human_decision`, `human_initials` and `date`. Rows cover all retains, all full-text excludes and a seeded random 10% of title excludes.
    2. The user fills it in. **The 46 batch 5-6 decisions (27-28 Sept) need the user's own review.**
    3. Read it back into file 56 as `human_verification`, compute human-vs-AI agreement, log an amendment, and draft the Methods disclosure.
  - **C.** Link reports to studies: CAN-0060/1711, CAN-1719/1731, CAN-1875 vs the national surveillance report, CAN-1152/1179, CAN-0008/0204, CAN-1291→1602, CAN-0056/1446, plus shared NVRI line lists and accessions. Then produce the PRISMA 2020 flow, with the arithmetic checked by script against file 56.
  - **D.** Extraction pilot (file 20 T1-T5, ~10 studies) → full extraction → RoB (file 21 + 07; no score sums) → SWiM (file 04; epoch × subtype/clade × host × state/zone) → narrative certainty (file 06). Edit only `Avian_review_paper_submission_ready.docx`, and load `thesis-to-journal` first. Finish with the audit against files 01/02/04.
- **Checks after each phase:** file 56 must parse; candidates must equal retain + exclude + not retrieved; every exclusion must have one fixed reason. Pass the phase outputs to the `reviewer` agent before reporting.
- **Manuscript:** unedited.

## Previous handoff - 28 September 2026 (full-text gate closed)

The controlling record is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **Gate state:** 1,877 title/metadata identities; 1,581 excluded; 296 full-text candidates = **111 provisional retain + 105 excluded + 80 reports not retrieved**. No report remains unassessed. These are report counts, not study counts.
- **Done 28 Sept:** 32 candidates identity-verified and screened as batch 5 (13 retain / 19 exclude; `15c316e`). Sweeps 3-4 (OpenAlex/Europe PMC/Semantic Scholar/Crossref title search; Google Scholar via SerpApi with the "All versions" cluster; long-timeout repository retries; Chrome DevTools browser pass) gave 14 more texts; batch 6 = 6 retain / 8 exclude. The remaining 80 are `report_not_retrieved` (`2087a50`). CAN-1627 and CAN-1672 were excluded because the published text reports no laboratory-confirmed results. CAN-1291 (preprint) is not retrieved; its study is represented by the retained CAN-1602.
- **Amendment (file 15, 28 Sept MAJOR):** the ATBU institutional-access step was dropped because institutional access was unavailable to the team. ResearchGate, Academia.edu (login) and AgEcon Search were bot-gated; no CAPTCHA was bypassed, no login was used and no shadow library was used. Methods/Limitations must say so, and must give the 80 not-retrieved reports.
- **Workspace:** `D:\AvianInfluenzaSysRev_retrieval_20260927\` (full texts, OCR text, `work/` route logs, `votes/` R1/R2 JSON and adjudication scripts). SerpApi key file is on the user's Desktop (free plan; 127 searches left this month).
- **Resume in this order:**
  1. Resolve report/dataset overlaps among the 111 retained reports (companion reports, shared NVRI 2006-07 outbreak line lists, shared sequence accessions, e.g. CAN-0060/CAN-1711, CAN-1719/CAN-1731, CAN-1875 vs the national surveillance report, CAN-1152/CAN-1179 and CAN-0008/CAN-0204 pairs), then produce the study count and the PRISMA 2020 flow numbers.
  2. Extraction pilot (T1-T5, file 20), then full extraction.
  3. RoB (JBI plus custom molecular check, file 21), SWiM synthesis, manuscript update in the working copy only (the original `.docx` stays frozen), then the PRISMA/PRISMA-S/SWiM audit.
- **Manuscript:** unedited. No extraction, RoB or synthesis started.

## Previous handoff - 27 September 2026 (session paused mid-retrieval)

The controlling record is still `Workbench/56_SCREENING_RECONCILIATION.json`. **Its eligibility counts are unchanged:** 296 full-text candidates; 170 adjudicated (92 provisional retain; 78 exclude); 126 open.

- **Committed this session:** batches 2-4 (`dd30a10`); `full_text_status` normalised to match `final_status` for 28 records (`8d68ad2`). The register now shows 92 `full_text_eligible_provisional`, 78 `full_text_excluded`, and 126 candidates in retrieval states (84 identifier unresolved, 20 identifier missing, 18 metadata/subscription only, 4 free route located).
- **Protocol amendments logged in file 15 (27 Sept):** MAJOR, by user decision for deadline reasons. There is **no author contact and no waiting period.** Reports without verified full text after (a) a legal open-access sweep and (b) one time-boxed ATBU institutional-access attempt go to PRISMA "reports not retrieved". They are not content exclusions, and Methods/Limitations must state the deviation. MINOR: R1 = executor agent (Claude Opus 5.5) and R2 = a separate reviewer agent (Claude Sonnet 5), blind to R1; the main session adjudicates.
- **Retrieval policy:** only legal routes are allowed. The user asked about Sci-Hub; it was declined and **must not be used or claimed** in the Methods. The user agreed to the honest route. Routes in scope are Crossref, OpenAlex (all locations), Europe PMC/PMC, PubMed, Semantic Scholar, Unpaywall (all oa_locations), CORE, BASE, Internet Archive Scholar/Wayback, preprint servers, Nigerian university and FAO/WOAH/CGIAR repositories, AJOL/Nigerian journals, directly downloadable author uploads (no requests), and thesis repositories.
- **Retrieval sweep was stopped partway** (usage limit). It did **not** write to file 56. Its outputs are saved outside the repo at `D:\AvianInfluenzaSysRev_retrieval_20260927\`:
  - `fulltext/`: 32 candidate full texts, **not yet verified** as the correct publication: CAN-0006 CAN-0020 CAN-0055 CAN-0060 CAN-0071 CAN-0541 CAN-0630 CAN-0648 CAN-0943 CAN-0946 CAN-0947 CAN-0948 CAN-1033 CAN-1152 CAN-1296 CAN-1346 CAN-1416 CAN-1502 CAN-1627 CAN-1666 CAN-1667 CAN-1672 CAN-1710 CAN-1711 CAN-1712 CAN-1713 CAN-1714 CAN-1715 CAN-1745 CAN-1796 CAN-1817 CAN-1875.
  - `fulltext/_rejected/`: downloads that failed the identity check (CAN-0032, 0047, 0061, 0062, 0064, 0580, 0646, 1033, 1121, 1502, 1745 variants).
  - `work/`: `resolve.json` (identifier resolution), `attempts.json` (route log), `extra_urls.json`, `manual*.json`, and logs. The scripts (`common.py`, `resolve.py`, `discover2.py`, `fetch2.py`) sit at the folder root.
- **Resume in this order:**
  1. Verify the 32 candidates: title, first author, year and journal must match, with a Methods/Results body present. Write verified items and all attempts from `work/attempts.json` into each record's `retrieval` field (`fulltext_obtained`, `retrieval_attempts` dated 2026-09-27). Set `full_text_status` to `retrieval_fulltext_obtained_pending_screening`. Do not change `final_status`.
  2. Finish the sweep for the remaining ~94 open records using the routes above. Record the publisher URL for paywalled items.
  3. Give the user the paywalled list for one ATBU attempt: "Access through your institution", campus Wi-Fi, or the Research4Life login from the library.
  4. Screen retrieved texts with independent R1/R2 votes plus main adjudication, in batches. Resolve CAN-1627's laboratory evidence (a candidate file exists).
  5. Mark the remainder "not retrieved". Resolve report/dataset overlaps, then count studies. Then run the extraction pilot, RoB, SWiM, the manuscript update (working copy only; the original `.docx` stays frozen), and the PRISMA/PRISMA-S/SWiM audit.
- **Manuscript:** unedited. No extraction, RoB or synthesis has started.

## Previous handoff - 27 September 2026 (fourth batch)

The controlling record is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **Gate state:** 1,877 title/metadata identities; 1,581 excluded and 296 advanced to full text. Independent R1/R2 and main adjudication are complete for **170 reports (92 provisional retain; 78 exclude)**. **126 remain open (125 unassessed; CAN-1627 seek further info)**. These are report counts, not final studies or PRISMA counts.
- **Completed:** CAN-0244, CAN-0282, CAN-0329 and CAN-0330 provisionally retained; CAN-0416, CAN-0483, CAN-0485, CAN-0499 and CAN-0570 excluded. Original source URLs, two reviewer observations, fixed reasons and 23 other failed/abstract-only access routes are in file 56. CAN-0215 remains unassessed because the publisher URL returned 403 and snippets did not establish a full-text Nigeria-specific result. CAN-0541 remains unassessed pending independently verified matching full text.
- **Resume:** assess 125 unassessed original publications, resolve CAN-1627's laboratory evidence, and match reports, outbreak line lists and sequence accessions before final study count. Do not infer full-text eligibility from abstracts, snippets, or different papers. No author contact occurred; the frozen unretrievable rule still requires two attempts plus author contact.
- **Manuscript:** original `.docx` remains frozen and unedited. No extraction pilot, RoB or SWiM synthesis started.

## Previous handoff - 27 September 2026 (third batch)

The controlling record is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **Gate state:** 1,877 title/metadata identities; 1,581 excluded and 296 advanced to full text. Independent R1/R2 and main adjudication are complete for **161 reports (88 provisional retain; 73 exclude)**. Another **135 candidates remain open (134 unassessed; CAN-1627 seek further info)**. These are report counts, not final studies or PRISMA counts.
- **Completed:** CAN-0070 and CAN-0129 provisionally retained from original texts; CAN-0097 excluded for no Nigerian data; CAN-0187 excluded for no primary data. Eleven other records gained documented access attempts. CAN-0207's accessible 2021 JALSI article is a different publication from the indexed 2016 IJID record, so CAN-0207 remains unassessed. Conference abstracts CAN-0204/0205/0206 also remain unassessed pending matching full publication. Reviewer evidence, URLs and overlap cautions are in file 56.
- **Resume:** verify original full text and independently screen the 134 unassessed candidates; resolve CAN-1627 against an explicit laboratory source. Match report versions, outbreak line lists and sequence accessions before final study counting. No author contact occurred; do not invoke unretrievable exclusion without the frozen two-attempt-plus-author-contact process.
- **Manuscript:** original `.docx` remains frozen and unedited. No extraction pilot, RoB or SWiM synthesis started.

## Previous handoff - 27 September 2026 (second batch)

This checkpoint supersedes historical sections below. The controlling record is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **Gate state:** 1,877 title/metadata identities; 1,581 excluded and 296 advanced to full text. Independent R1/R2 and main adjudication are complete for **157 reports (86 provisional retains; 71 exclusions)**. Another **139 candidates remain open (138 unassessed; CAN-1627 seek further info)**. These are report counts, not final studies or PRISMA counts.
- **Completed:** six original full texts provisionally retained (CAN-0031, CAN-0033, CAN-0053, CAN-0058, CAN-0065, CAN-0066); CAN-0046 and CAN-0063 excluded. CAN-0033 is a secondary Nigerian-sequence reanalysis, not new isolate collection. CAN-0063's seasonal human influenza antigens do not establish AIV. CAN-0053 subtype attribution and CAN-0065 arithmetic need extraction QA. Full reviewer evidence, original URLs and adjudication are in file 56.
- **Resume:** independently screen the 138 unassessed candidates from verified original full texts. Seventeen of the latest 25 searched records remain unassessed after access leads or failed routes; do not infer eligibility from abstracts. Resolve CAN-1627 against an explicit laboratory source and report/dataset overlaps before study counting. Unretrievable exclusion still requires the frozen two-attempt-plus-author-contact process; no author contact has occurred.
- **Manuscript:** original `.docx` remains frozen and unedited. No extraction pilot, RoB or SWiM synthesis started.

## Previous handoff - 27 September 2026

This checkpoint supersedes historical sections below. The controlling file is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **End-of-session update:** a second independent R1/R2 batch added CAN-1347, CAN-1501, CAN-1637 and CAN-1737 as provisional retains. Counts now stand at **149 adjudicated (80 provisional retain; 69 exclude)** and **147 open (146 unassessed; CAN-1627 seek further info)**. CAN-1731 and CAN-1870 are among the 146 unassessed because the original PDFs did not open through attempted routes. CAN-1737 was retained after an R1/R2 disagreement: file 10 explicitly permits positive avian serology with a stated assay; record exposure only. Details and source URLs are in file 56 and the top of file 15.
- **Gate state:** 1,877 title/metadata identities; 1,581 excluded and 296 advanced to full text. Independent R1/R2 plus main-agent adjudication is complete for 149 reports: 80 provisional retains and 69 exclusions. Another 147 candidates remain open: 146 have no full-text assessment, and CAN-1627 has concordant `seek_further_info` votes because its Ogun surveillance totals lack explicit positive laboratory confirmation. These are report counts, not a final included-study or PRISMA count.
- **Completed 27 September:** original full texts and independent votes provisionally retained CAN-0147, CAN-0744, CAN-0745, CAN-0746 and CAN-1630. Original URLs, section evidence and assay cautions are recorded in file 56 and summarised at the top of file 15. Five additional records (CAN-0129, CAN-0189, CAN-0089, CAN-0006, CAN-0017) had legitimate access attempts but no original full text opened; they remain pending.
- **Resume:** assess the 146 untouched full-text candidates with original publisher, author-posted or repository copies, independent R1/R2 votes and main adjudication. Resolve CAN-1627 against laboratory source records. Reconcile confirmed report/version and surveillance-dataset overlap before any final included-study count or extraction pilot. Do not turn abstracts or blocked links into full-text votes. The frozen unretrievable rule still requires two attempts plus author contact; no author contact has occurred.
- **Manuscript:** original `.docx` remains frozen and unedited. No extraction pilot, RoB or SWiM synthesis started.

## Latest handoff - 26 September 2026
This checkpoint supersedes historical sections below. The controlling record is `Workbench/56_SCREENING_RECONCILIATION.json`.

- **Gate state:** 1,877 title/metadata identities, of which 1,581 were excluded and 296 advanced to full text. There are 140 independently adjudicated full-text reports (71 provisional retain; 69 exclude), with 156 still without full-text assessment. Thus 296 = 140 + 156. No first-pass report is awaiting R2. These are report-level numbers, not a final included-study count. The original `.docx` remains frozen and unedited.
- **Today:** closed independent R2 and main adjudication for 132 new reports on top of eight prior adjudications. The final 22 R2 full-text decisions were ten retain and twelve exclude. CAN-0423's original accepted manuscript was opened through the versioned HAL URL; R1/R2 both retained its Nigerian avian laboratory data. CAN-0146 was newly assessed and retained from the University of Ilorin original PDF. CAN-0113 was corrected to exclude after avian-host laboratory criterion QA, with history preserved. CAN-1734's year was corrected to 2021.
- **Identity and data overlap:** CAN-0056/CAN-1446 are confirmed the same report; CAN-0056 was excluded as a duplicate at full text but the title-identity denominator remains 1,877 pending formal PRISMA deduplication. CAN-0008/CAN-0204, CAN-1291/CAN-1602, and CAN-1152/CAN-1179 remain possible report/version pairs. Surveillance, sequence and serosurvey reports require accession, sampling-period, site and event-line-list matching before study-level synthesis counts.
- **Access gate:** 156 candidates still need original full-text assessment. Record publisher, repository and alternate legitimate routes. Metadata/abstract snippets cannot substitute for a full-text vote. Do not use the unretrievable exclusion reason before two documented attempts and author contact; no author contact has been made.
- **Ordered next work:** (1) retrieve and independently R1/R2 screen the 156 remaining candidates; (2) resolve report identity and dataset overlaps; (3) pilot extraction T1?T5, then RoB, SWiM synthesis and manuscript reporting. Keep serology, infection, subtype, clade, reassortment and introduction distinct.
- **Validation:** JSON parses; 1,877 unique IDs; 296 = 140 + 156; 71 + 69 = 140; all 69 adjudicated exclusions have a fixed reason. No repository preflight/build script exists.

### Session closed: resume from this point

- Resume directly from the **156 records whose `final_status` is `provisional_full_text_candidate` and which lack `full_text_eligibility`** in the controlling register. Do not repeat the 140 completed R1/R2 adjudications. The 2026-09-23 retrieval-category counts are historical access leads, not current eligibility totals.
- Start with original publisher or repository full texts already located in each record's `retrieval` field. Next revisit access-pending leads including CAN-0330's abstract-only publisher page, CAN-1291's probable preprint/published pair with CAN-1602, and the remaining AJOL-linked candidates. Record each legitimate access attempt; do not turn an abstract or a blocked link into a full-text exclusion.
- For each newly opened report, record independent R1 and R2 decisions, page or section evidence, an exact source URL, and one fixed reason for any exclusion. Main-agent adjudication follows the independent votes. Keep report-level eligibility separate from study-level counting and preserve the original paper as a single frozen `.docx`.
- The remaining access process may require institutional PDFs or author contact. No author contact or external message was sent this session. Obtain explicit user authorization before contacting authors; record the frozen two-attempt-plus-author-contact process before any unretrievable exclusion.
- After the 156 eligibility decisions and report/data overlaps are resolved, proceed in order to the T1-T5 extraction pilot, RoB, SWiM synthesis and reporting. No extraction or manuscript edit started this session.

## Current handoff — 24 September 2026
This section supersedes the 23 September snapshot preserved below. The controlling sources are
`Workbench/56_SCREENING_RECONCILIATION.json` for record-level decisions and retrieval attempts,
and the dated section at the top of `Workbench/15_RUN_LOG.md` for proceedings.

### Verified gate state
- 1,877 unique canonical records have title/metadata dispositions: 296 retained for full-text
  assessment and 1,581 excluded at that stage. Of the 296, **107 have full-text eligibility
  assessments**: eight earlier two-reviewer adjudications (five provisionally eligible, three
  excluded) and 99 first-pass assessments awaiting independent second review. **189 remain
  unassessed**. Do not use the historical 288-pending figure below.
- Retrieval categories in the register are 107 recorded free routes, 24 metadata or subscription
  only, 122 identifier unresolved, and 35 identifier missing; the remaining eight are the earlier
  adjudicated reports. A free route is an access lead, not an eligibility decision.
- No final included-study count, final PRISMA full-text exclusion tally, extraction pilot, RoB,
  certainty judgement, synthesis, or manuscript reporting update is supportable yet. The original
  `Avian_review_paper_fellow.docx` is frozen; `Avian_review_paper_submission_ready.docx` remains
  the provisional working output and was not edited this session.
- No independent second-review decision was fabricated for the 99 new first-pass records. The
  protocol's independent-review requirement remains open despite the user's delegation of the
  screening work. Preserve the existing eight adjudications as recorded.

### Work completed this session
- Eight first-pass assessments were added with source URL and page/section evidence:
  `CAN-0056` (2007 Nigerian H5N1 genomes and 2:6 reassortment), `CAN-0039` (17 turkey-flock
  submissions and reused NVRI outbreak map), `CAN-0025` (2015 resurgence; author-posted Results,
  publisher PDF returned 403), `CAN-1724` (32 affected/32 unaffected Kano farms; reported effect
  estimates need QA), `CAN-0007` (Jigawa H5 serology, 396 birds), `CAN-0008` (Kaduna wild-bird
  influenza A serology, H5/H7 and PCR negative), `CAN-0339` (113 H5N1-affected poultry farms and
  road proximity), and `CAN-1678` (northern Nigeria FAO interviews plus FAO/OIE outbreak maps).
  All eight are **first-pass retain**, subject to second review and dataset reconciliation; none
  is a final included study. Exact evidence and cautions are in each register record.
- Original journal PDFs were read for all above except `CAN-0025`, whose author-posted article
  text supplied Results evidence while the AJOL PDF returned 403. For `CAN-0007`/`CAN-0008`,
  African Union DSpace `/server/api/core/bitstreams/{id}/content` supplied the original issue PDFs.
  Cambridge and Geospatial Health publisher PDFs opened through the R document reader although
  browser fetches had failed. URLs are stored in the register and run log.
- Additional legitimate retrieval attempts were logged for `CAN-0007`, `CAN-0008`, `CAN-0017`,
  `CAN-0032`, and `CAN-0061`; unsuccessful routes remain documented. Four previously recorded
  free routes still need verified full text: `CAN-0191` (ScienceDirect 403), `CAN-0423`
  (Taylor & Francis PDF unavailable), `CAN-0485` (Oxford/CiteSeerX PDF unavailable), and
  `CAN-1610` (MDPI 429 and Europe PMC blocked). Do not mark them excluded for retrieval failure
  until the frozen two-attempt-plus-author-contact rule is satisfied.
- Dataset-overlap watchlists now cover 2006–2009 national outbreak line lists (`CAN-0039`,
  `CAN-0025`, `CAN-0339`, `CAN-1678` added), 2006–2008 genomes (`CAN-0056` added), the
  Métras conference/journal reports (`CAN-0061`/`CAN-0608`) with `CAN-1724` as a possible
  separate Kano sample, and the Aiki-Raji 2007 conference abstract (`CAN-0032`) versus the
  2008 full article DOI `10.3201/eid1411.080557`. These are hypotheses for accession,
  farm-ID, date, site, and author comparison; no duplicate exclusion has been declared.
- The screening form now labels human- or mammal-only data `no avian-host field data`, already
  implied by the frozen inclusion rule. Four provisional exclusions use that code; `CAN-1720`
  uses experimental-only/no-field-relevance. Five prior placeholder reasons are resolved, and
  all still await independent second review. This is a reason-label clarification, not a new
  eligibility criterion.

### Resume in this order
1. Validate the 296-candidate denominator against the register, then continue first-pass
   assessment of the four unverified free routes and other unresolved titles. Record authentic
   full-text source, page or section, decision, one fixed exclusion reason if applicable, and
   every failed retrieval attempt. Search original publisher/repository copies before treating
   index snippets as full text.
2. Obtain an independent second decision for each of the 99 first-pass records; adjudicate
   disagreements without relabelling a same-agent reread as independent. Keep 189 pending until
   their full text is assessed or a legitimate unretrievable determination is complete.
3. Match isolate accessions, sampling periods/sites, farm IDs and outbreak line lists within the
   overlap watchlists before counting studies. Separate report-level eligibility from study-level
   synthesis counts.
4. Only after eligibility and overlaps are resolved, pilot the existing T1–T5 extraction shells
   in `Workbench/20_EXTRACTION_T1_T5_shells.md`; then follow the frozen RoB/SWiM/reporting order.
   Do not infer clade, pathogenicity, or introduction from a subtype or antibody result.

### Reproducibility and validation
- No repository preflight/setup script exists. The register was parsed after editing: 1,877
  records with 1,877 unique IDs, 296 candidates, 107 assessed and 189 pending; the last
  verification also found zero assessed exclusion recommendations lacking a fixed reason.
- Terminal `exec_command` failed with `helper_unknown_error: setup refresh had errors`.
  `mcp__rmcp__execute_r_analysis` could read/write the JSON and read publisher PDFs through
  in-memory `url(..., 'rb')` + `readBin` + `pdftools::pdf_text`. `pdftools` was approved for this
  analysis session only; a later session may need to approve it again. Browser fetch errors
  should not be mistaken for proof that a source is unavailable through all legitimate routes.

**Prepared:** 23 September 2026  
**Purpose:** resume screening and document production without rediscovery, methodological drift, or accidental edits to the frozen source manuscript.

## Start here

1. `AGENTS.md` — binding scope and safety rules.
2. `Workbench/15_RUN_LOG.md` — search and gate history.
3. `Workbench/53_CANONICAL_REGISTER.json` — identity source.
4. `Workbench/56_SCREENING_RECONCILIATION.json` — pilot/register screening source.
5. `Avian_review_paper_submission_ready.docx` — current deliverable.

The source manuscript `Avian_review_paper_fellow.docx` is frozen and must not be overwritten.

## Current repository state

- Branch: `main`, synchronized with `origin/main` after the corrected B20 handoff push.
- Latest committed screening document/reconciliation: `7f7019d Record full-text eligibility batch 1`.
- Latest handoff commit: `4044b48` (`Update next-session handoff after full-text batch 1`); previous screening document/reconciliation commit is `7f7019d`.
- A user-owned untracked file, `25min-alternating-exercise.html`, was observed and left untouched. Do not add or delete it.
- Pushes have been performed to the configured remote; do not alter the user-owned untracked HTML file.

## Review and search gates

- Gate A/protocol: closed.
- Gate B/search execution: closed with export limitations.
- Gate C/record-level title/metadata screening: complete for all 1,877 canonical identities; 296 provisional full-text candidates are recorded with R1/R2/adjudication fields.
- Gate D/retrieval inventory: complete as a source-location pass; 107 free/open routes, 24 metadata/subscription-only routes and 165 unresolved or identifier-missing routes are recorded. Eight full texts have now been assessed: five are provisionally eligible, three are excluded, and 288 candidates remain pending full-text eligibility.
- Gates D full-text eligibility onward — extraction, RoB, certainty, synthesis and final reporting — remain incomplete.
- PROSPERO was skipped; do not claim prospective registration.
- Full-text inventory in the workspace currently contains no article PDFs; only the manuscript/output PDF is local. Retrieval must be targeted and legitimate; do not bypass paywalls or access controls.

## Verified identity and screening arithmetic

Source reconciliation remains:

`2,367 source rows → 1,877 provisional identity groups → 490 collapsed duplicates`.

Committed document state through B15:

| Batch | Screened | Excluded | Retained for full text | Verification |
|---|---:|---:|---:|---|
| R1/R2 pilot | 40 | 25 | 15 | Adjudicated; two disagreements resolved conservatively |
| B1 | 100 | 73 | 27 | R1/R2 exact agreement, 100/100 |
| B2 | 100 | 83 | 17 | Eight disagreements adjudicated |
| B3 | 100 | 87 | 13 | Six uncertainty disagreements resolved conservatively |
| B4 | 100 | 89 | 11 | Exact R1/R2 aggregate agreement |
| B5 | 100 | 79 | 21 | Fourteen disagreements retained conservatively |
| B6 | 100 | 83 | 17 | Eight disagreements retained conservatively |
| B7 | 100 | 82 | 18 | Seven disagreements retained conservatively |
| B8 | 100 | 90 | 10 | Four disagreements retained conservatively |
| B9 | 100 | 85 | 15 | Four disagreements retained conservatively |
| B10 | 100 | 91 | 9 | Seven disagreements retained conservatively |
| B11 | 100 | 92 | 8 | Five disagreements retained conservatively |
| B12 | 100 | 90 | 10 | Eight disagreements retained conservatively |
| B13 | 100 | 90 | 10 | Five disagreements retained conservatively |
| B14 | 100 | 91 | 9 | Exact R1/R2 agreement |
| B15 | 100 | 91 | 9 | Six disagreements retained conservatively |
| B16 | 100 | 82 | 18 | Five disagreements retained conservatively |
| B17 | 100 | 65 | 35 | Twelve disagreements retained conservatively |
| B18 | 97 | 78 | 19 | Nine disagreements retained conservatively |
| B19 | 40 | 0 new | 0 new | Duplicate-range audit of CAN-0241–CAN-0280; retrieval/extraction pilot only |
| B20 | 40 | 36 | 4 | True uncovered gap CAN-0341–CAN-0380; one two-record swap adjudicated |
| **Record-level reconstructed cumulative** | **1,877** | **1,581** | **296** | **R1/R2 lists and conservative adjudication recorded; full-text eligibility pending** |

## Current state after committed B4

Batch B4 covers 100 records, `CAN-0381–CAN-0480` (register gaps explain the jump after B3).

- R1: 0 clear includes, 11 uncertain/retain for full text, 89 exclusions.
- R2: exact aggregate agreement with R1; no disagreements reported.
- Final B4 disposition: 11 provisional full-text candidates, 89 exclusions.
- Committed cumulative status: 440 screened, 357 excluded, 83 provisional full-text candidates, 1,437 unresolved.
## Current state after committed B5

Batch B5 covers 100 records, `CAN-0481–CAN-0580`.

- R1 retained 10 and excluded 90; R2 retained 18 and excluded 82.
- The reviewers differed on 14 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B5 disposition: 21 provisional full-text candidates, 79 exclusions.
- Committed cumulative status: 540 screened, 436 excluded, 104 provisional full-text candidates, 1,337 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4 and B5 updates and is committed as `29e7322`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B6

Batch B6 covers 100 records, `CAN-0581–CAN-0680`.

- R1 retained 9 and excluded 91; R2 retained 17 and excluded 83.
- The reviewers differed on 8 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B6 disposition: 17 provisional full-text candidates, 83 exclusions.
- Committed cumulative status: 640 screened, 519 excluded, 121 provisional full-text candidates, 1,237 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4, B5 and B6 updates and is committed as `d762698`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B7

Batch B7 covers 100 records, `CAN-0681–CAN-0780`.

- R1 retained 15 and excluded 85; R2 retained 14 and excluded 86.
- The reviewers differed on 7 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B7 disposition: 18 provisional full-text candidates, 82 exclusions.
- Committed cumulative status: 740 screened, 601 excluded, 139 provisional full-text candidates, 1,137 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B7 updates and is committed as `504b282`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B8

Batch B8 covers 100 records, `CAN-0781–CAN-0880`.

- R1 retained 7 and excluded 93; R2 retained 9 and excluded 91.
- The reviewers differed on 4 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B8 disposition: 10 provisional full-text candidates, 90 exclusions.
- Committed cumulative status: 840 screened, 691 excluded, 149 provisional full-text candidates, 1,037 unresolved.
- A targeted retrieval pilot located authoritative or open full-text/metadata sources for CAN-0782, CAN-0825, CAN-0835 and CAN-0846. These remain provisional pending formal full-text eligibility and extraction checks.
- `Avian_review_paper_submission_ready.docx` contains the B4–B8 updates plus the retrieval-pilot note and is committed as `354406f`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B9

Batch B9 covers 100 records, `CAN-0881–CAN-0980`.

- R1 retained 12 and excluded 88; R2 retained 14 and excluded 86.
- The reviewers differed on 4 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B9 disposition: 15 provisional full-text candidates, 85 exclusions.
- Committed cumulative status: 940 screened, 776 excluded, 164 provisional full-text candidates, 937 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B9 updates plus the retrieval-pilot note and is committed as `8f8c72b`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B10

Batch B10 covers 100 records, `CAN-0981–CAN-1080`.

- R1 retained 2 and excluded 98; R2 retained 9 and excluded 91.
- The reviewers differed on 7 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B10 disposition: 9 provisional full-text candidates, 91 exclusions.
- Committed cumulative status: 1,040 screened, 867 excluded, 173 provisional full-text candidates, 837 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B10 updates plus the retrieval-pilot note and is committed as `fa17b0c`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B11

Batch B11 covers 100 records, `CAN-1081–CAN-1180`.

- R1 retained 4 and excluded 96; R2 retained 7 and excluded 93.
- The reviewers differed on 5 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B11 disposition: 8 provisional full-text candidates, 92 exclusions.
- Committed cumulative status: 1,140 screened, 959 excluded, 181 provisional full-text candidates, 737 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B11 updates plus the retrieval-pilot note and is committed as `81f3fc7`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B12

Batch B12 covers 100 records, `CAN-1181–CAN-1280`.

- R1 retained 6 and excluded 94; R2 retained 6 and excluded 94.
- The reviewers differed on 8 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B12 disposition: 10 provisional full-text candidates, 90 exclusions.
- Committed cumulative status: 1,240 screened, 1,049 excluded, 191 provisional full-text candidates, 637 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B12 updates plus the retrieval-pilot note and is committed as `939c527`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B13

Batch B13 covers 100 records, `CAN-1281–CAN-1380`.

- R1 retained 8 and excluded 92; R2 retained 7 and excluded 93.
- The reviewers differed on 5 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B13 disposition: 10 provisional full-text candidates, 90 exclusions.
- Committed cumulative status: 1,340 screened, 1,139 excluded, 201 provisional full-text candidates, 537 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B13 updates plus the retrieval-pilot note and is committed as `d6e00d5`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B14

Batch B14 covers 100 records, `CAN-1381–CAN-1480`.

- R1 and R2 had exact agreement: 9 retained and 91 excluded; no disagreements occurred.
- Final B14 disposition: 9 provisional full-text candidates, 91 exclusions.
- Committed cumulative status: 1,440 screened, 1,230 excluded, 210 provisional full-text candidates, 437 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B14 updates plus the retrieval-pilot note and is committed as `7c08fc1`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B15

Batch B15 covers 100 records, `CAN-1481–CAN-1580`.

- R1 retained 5 and excluded 95; R2 retained 8 and excluded 92.
- The reviewers differed on 6 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B15 disposition: 9 provisional full-text candidates, 91 exclusions.
- Committed cumulative status: 1,540 screened, 1,321 excluded, 219 provisional full-text candidates, 337 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B15 updates plus the retrieval-pilot note and is committed as `1125ed9`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B16

Batch B16 covers 100 records, `CAN-1581–CAN-1680`.

- R1 retained 16 and excluded 84; R2 retained 15 and excluded 85.
- The reviewers differed on 5 records. Applying the conservative rule, all disagreement records were retained for full-text assessment.
- Final B16 disposition: 18 provisional full-text candidates, 82 exclusions.
- Committed cumulative status: 1,640 screened, 1,403 excluded, 237 provisional full-text candidates, 237 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B16 updates plus the retrieval-pilot note and is committed as `1e9dff1`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B17

Batch B17 covers 100 records, `CAN-1681–CAN-1780`.

- R1 retained 35 and excluded 65; R2 retained 23 and excluded 77.
- The reviewers differed on 12 records; all disagreements were retained conservatively. The 23 R2 retains were also retained by R1.
- Final B17 disposition: 35 provisional full-text candidates, 65 exclusions.
- Committed cumulative status: 1,740 screened, 1,468 excluded, 272 provisional full-text candidates, 137 unresolved.
- `Avian_review_paper_submission_ready.docx` contains the B4–B17 updates plus the retrieval-pilot note and is committed as `9e8e42c`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Current state after committed B18

Batch B18 covers the final contiguous register range, `CAN-1781–CAN-1877` (97 records).

- R1 retained 18 and excluded 79; R2 retained 11 and excluded 86.
- The reviewers differed on 9 records; all disagreements were retained conservatively.
- Final B18 disposition: 19 provisional full-text candidates, 78 exclusions.
- Aggregate status before B20: 1,837 screened, 1,546 excluded, 291 provisional full-text candidates. The actual unresolved canonical gap was `CAN-0341–CAN-0380`; the earlier B19 pass on `CAN-0241–CAN-0280` was duplicate-range work.
- `Avian_review_paper_submission_ready.docx` contains the B4–B18 updates plus the retrieval-pilot note and is committed as `09cd968`; ZIP/XML, `python-docx`, and LibreOffice rendering checks passed. The source manuscript remains unchanged.

## Corrected current state after B19 audit, B20 and record-level reconstruction

The previous B19 label was corrected during this session. B19 screened `CAN-0241–CAN-0280`, a range already included in B3; it contributes zero new unique identities. Its eight-record retrieval/extraction pilot remains in the Word document as a method calibration and is not part of the canonical screening arithmetic.

Batch B20 screened the true uncovered range `CAN-0341–CAN-0380` (40 records).

- R1 retained 4 (`CAN-0344`, `CAN-0345`, `CAN-0359`, `CAN-0379`) and excluded 36.
- R2 retained 4 (`CAN-0344`, `CAN-0356`, `CAN-0359`, `CAN-0379`) and excluded 36.
- One two-record decision swap was adjudicated: `CAN-0345` was excluded after source verification found no Nigeria surveillance sites, while `CAN-0356` was retained because the primary geospatial analysis reports Nigerian H5N1 occurrence.
- Final B20 disposition: 4 provisional full-text candidates and 36 exclusions.
- Record-level reconstructed status: 1,877 screened, 1,581 exclusions, 296 provisional full-text candidates.
- Two independent title/metadata passes were completed across the full register in 100-record blocks. R1 retained 269 and R2 retained 277; the conservative union contained 302 before preserving the prior evidence-supported pilot/B20 adjudications. The final register records every R1/R2/adjudication field.
- `Avian_review_paper_submission_ready.docx` contains the correction, B20 audit table, non-additive B19 pilot note, prior extraction calibration pilot, record-level reconstruction, Gate D retrieval inventory, two pilot exclusions and the first six-record full-text batch; the validated document/reconciliation commit is `7f7019d`.

## Gate D retrieval inventory

- Retrieval inventory checked 296 provisional candidates through public Europe PMC metadata/full-text links, DOI routes and linked repository/Unpaywall routes on 23 September 2026.
- 107 candidates have a legitimate free/open source URL recorded; these are not yet full-text eligibility decisions.
- 24 candidates have a matched metadata or subscription-only route; no paywall or access control was bypassed.
- 165 candidates remain unresolved or lack a stored PMID/DOI; title-based legitimate retrieval and/or manual library retrieval remains required.
- Every candidate has `retrieval`, `full_text_status`, `eligibility_status` and `next_action` fields in `Workbench/56_SCREENING_RECONCILIATION.json`.

## Gate D full-text eligibility pilot

- CAN-0258: concordant R1/R2 full-text exclusion for `NO_NIGERIA_STUDY_DATA`; accessible PMC/PubMed evidence is an Egypt-only H5N8 ostrich study.
- CAN-0269: concordant R1/R2 full-text exclusion for `NOT_PRIMARY_RESEARCH`; accessible full text is a narrative review and Nigeria is only cited, not a primary study site.
- Pilot status: 2 assessed exclusions, 0 included studies, 294 candidates pending. The fixed decisions and source URLs are recorded in the reconciliation register and Word deliverable.

## Gate D full-text eligibility batch 1 — 23 September 2026

- Six legitimate PMC full texts were retrieved and assessed independently by R1 and R2.
- CAN-0087, CAN-0113, CAN-0114, CAN-0132 and CAN-0142 were adjudicated provisionally eligible for extraction. They are not final included studies until duplicate/dataset linkage, extraction and appraisal are complete.
- CAN-0151 was concordantly excluded for `NO_NIGERIA_STUDY_DATA`: the full text reports Egyptian chicken/duck genomes and phylogeny; Nigeria is contextual only.
- CAN-0113 was the sole disagreement. It was retained because the frozen scope includes epidemiologic/risk-factor evidence; extract it as awareness/biosecurity context, not infection, prevalence or outbreak-incidence evidence.
- CAN-0132 was retained because the Results identify Nigeria as an analysed national unit assigned to agro-ecological niche 3. Extract only the Nigeria-specific model result and do not count the reused international surveillance records as independent Nigerian events.
- Batch arithmetic: 6 assessed; 5 provisionally eligible; 1 new exclusion; 288 candidates pending; 0 final included studies claimed.
- Evidence URLs and R1/R2/adjudication fields are in `Workbench/56_SCREENING_RECONCILIATION.json`; the Word appendix is B24 in `Avian_review_paper_submission_ready.docx`.

## Exact next actions

1. Open/download the remaining located free/open routes (approximately 101 candidate routes after batch 1) and record full-text evidence; document legitimate outcomes for the 24 metadata/subscription-only and 165 unresolved/missing-identifier records.
2. Perform dual-review full-text eligibility assessment with explicit fixed exclusion reasons, legitimate retrieval-failure documentation, duplicate/dataset linkage checks and page/section evidence.
3. Reconcile the final eligible report set, then run the extraction pilot, JBI/custom molecular appraisal, narrative certainty plan, SWiM synthesis and PRISMA/PRISMA-S/SWiM audit in that order.
4. Preserve submission-stage wording until all gates are genuinely complete: no final included-study count, synthesis claim, certainty grade or PRISMA flow is supported yet.

## Frozen screening rules

Include for full-text review when the title/metadata supports Nigeria linkage, avian AIV/HPAI/LPAI relevance, and an eligible evidence type: epidemiology, prevalence, outbreak/surveillance, molecular/phylogenetic, spatial/temporal, or wild-bird finding.

Exclude only when clearly non-Nigeria, non-AIV/non-avian, general/editorial/news/review without primary data, lab-only/experimental without field relevance, or lacking eligible evidence. If the title/metadata is ambiguous, retain for full text.

All retained records remain provisional candidates, not final included studies. Never conflate subtype, clade, reassortant, or new introduction.

## Security and scope reminders

- Never print, commit, paste, or persist credentials, API keys, cookies, or private keys.
- Do not share `.playwright-cli/`, `.playwright-mcp/`, `woskey.txt`, or other credential-bearing artifacts.
- Keep the deliverable as a single Word document. Do not create CSV, BibTeX, Zotero, or new screening-database sidecars.
- Preserve Times New Roman, British English, numeric bracket citations, manual references, and the yellow `Abstract` heading style.
- The Word file must continue to state clearly that final screening, full-text assessment, extraction, RoB, synthesis and PRISMA flow are incomplete until they are genuinely complete.

