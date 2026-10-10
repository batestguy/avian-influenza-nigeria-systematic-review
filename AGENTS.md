# AvianInfluenzaSysRev

Single-manuscript systematic review of avian influenza in Nigeria, 2006–2026. This is
not a software project: no package manager, test suite, build system, or CI. Do not
scaffold any. There is no code only two historical PubMed helper scripts and one-off
Python pipeline scripts run with bare `python`.

**Current state (10 October 2026).** The review is complete and the October cycle is
committed (close-out commit of 10 October; nothing pushed).
`Avian_review_paper_submission_ready.docx`: 127 reports = 113 studies; 145 references
(4 flagged); 96 pages; abstract 290 words. Remaining before submission: author items
(six highlighted placeholders, the Reviewer 1 line, the journal choice) and the internal
Sunday checks (reporting audits re-run, reviewer blind re-score). Registration is
honestly capped at about 7 (never backdate it; file 17 records the decision not to
misregister).

**Author deadline: Sunday 11 October 2026** (decision D7, logged in file 15; the dated Sunday
critical path and checkpoints are at the top of file 15).

## Read first, in this order
1. `Workbench/57_NEXT_SESSION_HANDOFF_20260922.md` — read the top section only; newest first.
2. `Workbench/59_IMPROVEMENT_PLAN_20261008.md` — the current plan; its progress log (bottom) is the session record.
3. `Workbench/15_RUN_LOG.md` — top checkpoints; the only place author decisions are logged.
4. `Workbench/56_SCREENING_RECONCILIATION.json` — the controlling record (register, screening, linkage).
5. `Workbench/00_INDEX.md` — file map; audit files `01`–`08` (PRISMA 2020, PRISMA-S, protocol, SWiM, JBI RoB, GRADE-prognosis, molecular check, formats).

**Warning:** `README.md` and `FILE_INVENTORY.md` carry dated updates (10 October 2026) and
keep their historical sections; where they conflict with files 15/56/57/59, the ledger
wins. Older handoff sections in file 57 are historical; do not act on them.

## Workspaces
- `D:\AvianInfluenzaSysRev` — this repository: handoffs, run log, audit files, search artifacts, the register, both `.docx` files.
- `D:\AvianInfluenzaSysRev_retrieval_20260927\` — the working data and build tree (outside the repo):
  - `manuscript\` — section files, `assemble.py`, `verify.py`, `render_check.py`, dated backups, `refs_verified_20261008.json`
  - `extraction\` → `consensus_all.json`; `rob\` → `consensus_rob_all.json`; `synthesis\` → `run_all.py`, tables S1–S5, `SWIM_NARRATIVE.md`
  - `linkage\` → report-to-study linkage, `prisma_flow.py`; `fulltext\`, `votes\`, `work\`
  - `retrieval_pass2\` — W4: `build_log.py`, `gen_loan.py`, `LOAN_REQUEST_LIST.md`, `retrieval_log_20261008.json`
  - `human_check\` — W6: `make_sample.py` (seed 20261008), `sample_public.json` (blinded), `sample_key.json` (**never publish**)
  - `scholar_rerun\` — 28 Sep Scholar run (`reconcile.py` may be re-run; `run_q1q4.py` must not)
- If the retrieval workspace is missing, stop and ask; do not rebuild it from scratch.

## Commands (no build, test, or lint exists)
Manuscript rebuild, from `...\manuscript\`:
1. `python assemble.py --target` — writes `D:\AvianInfluenzaSysRev\Avian_review_paper_submission_ready.docx`
2. `python verify.py` — references/citations, all 113 studies cited, first-citation order, no stray STU ids, word counts, placeholders
3. `python <docx skill>\scripts\office\validate.py <docx> --original backup_submission_ready_20261007.docx` — the `docx` skill ships `scripts/office/validate.py`
4. `python render_check.py` — needs LibreOffice (`soffice`) and PyMuPDF; renders PDF/pages into `render\`

- Synthesis: in `...\synthesis\`, `python run_all.py` rebuilds tables and sensitivity; every assertion must pass.
- Retrieval pass 2: in `...\retrieval_pass2\`, `python build_log.py` then `python gen_loan.py`. Edit `OVERRIDES` in `build_log.py`, not the JSON, so reviewer fixes survive re-runs.
- **Never re-run** `linkage\adjudicate_linkage.py` or `apply_linkage.py` after extraction: they renumber study IDs. Re-running `prisma_flow.py` is fine.
- SerpApi (Google Scholar): check quota before use; the 8 Oct run exhausted it.

## Pipeline (data flow)
Search outputs (files `30`–`55`) → canonical register + screening (file 56; `CAN-xxxx` ids)
→ report-to-study linkage (`report_linkage` in file 56; CAN → STU) → extraction
(`consensus_all.json`; 113 studies, 379 rows) → RoB (`consensus_rob_all.json`) → synthesis
(`run_all.py` → S1–S5 tables) → narrative + certainty (`SWIM_NARRATIVE.md`) → manuscript
sections → `assemble.py` → verify/validate/render → audits (files `01`/`02`/`04`).

## Review identity
- Question: emergence, temporal/geographic/host-range, molecular/clade/reassortment dynamics of AIVs in Nigeria, 2006–2026.
- Standards: PRISMA 2020 (27 items + 12-item abstract), PRISMA-S (16), SWiM where meta-analysis is not justified — do not force meta-analysis. Framework is CoCoPop/PEO, not PICO.
- Eligibility anchor: Nigeria-specific HPAI/LPAI with epi, molecular/phylogenetic, or spatial/temporal data. Exclude non-Nigeria work without Nigeria data, non-avian influenza work, and surveys without laboratory testing. Never infer full-text eligibility from abstracts or snippets.
- RoB: JBI Prevalence / Analytical Cross-sectional / Cohort / Case Series, plus the custom molecular check (file 07): a `No` on M4 (accessions) or M5 (phylogeny method/support) caps that study's molecular claims at "suggestive". No ROBINS-I/RCT tools, no score sums. Certainty is narrative (GRADE-prognosis, file 06); never invent grades.
- Current numbers: register **2,157** = 1,803 title-excluded + 342 full-text candidates (127 retain / 117 exclude / 98 not retrieved) + 12 duplicates. RoB item agreement 79.3%; 14 high-risk studies (kept in the main synthesis, removed only in sensitivity); 13 molecular caps. Certainty: narrative per claim (GRADE-prognosis, file 06; 7 Oct pass recorded 9 Low, 14 Very low, 1 not gradable).

## Language rules (enforced; files 15, 57)
- subtype vs clade/sublineage vs reassortant vs new introduction stay distinct; never conflate.
- antibody = exposure only; "suggests" for the 13 capped studies; "first" claims attributed to their authors; wording follows certainty.
- British English throughout; names and date ranges stay consistent.

## Author protocol (how to work with Mayowa Olabode)
- Yes/no questions, one at a time, with a recommended option. Log every decision in file 15.
- Act as scribe: transcribe only what the author has actually said; never enter a decision the author has not given, and never invent decisions or human checks (file 14 records the accessibility wording).
- **Commit only when the author asks.** The October close-out commit (10 October 2026) includes the ledger and the whole October cycle; afterwards, commit again only on a fresh request.
- The protocol is "available from the corresponding author on request" (author decision). Any OSF/Zenodo registration is retrospective and says so; never backdate (file 17).

## Retrieval rules (binding)
- Legal routes only: publisher/repository open access, Crossref, OpenAlex, Europe PMC, Unpaywall, CORE, BASE, AJOL, institutional repositories. Never Sci-Hub or any shadow library.
- No author contact unless decision D3 is approved. Never send the author's email or any identifier in a request.
- **One attempt per bot gate** (CAPTCHA/login wall): never retry, never auto-pass. Log it and move the record to the author-download/loan list.
- Retrieval attempts, strings, counts and errors belong in files 15 and 19; never credentials or session material. `woskey.txt` and `.playwright-*` are git-ignored — keep them so.

## Agent workflow pattern
- Executor does the work; a separate reviewer agent checks it before anything is reported. Fan-out is at most 3.
- Agents return JSON/text to the main session; only the main session edits the `.docx` or the register. Use blind R1/R2 votes with fixed JSON schemas, then adjudicate conflicts against the source text.
- Agents save after each unit (usage limits interrupt runs); before relaunching a batch, check for partial R1/R2 files and reuse them.

## Current work (file 59) - status 10 October 2026
- **All work packages executed:** W1 (search rebuild) done; W2 (citation chasing, 88/123 seeds) done; W3 (screen + integrate, register now 2,157) done; W4 (retrieval pass 2; reports not retrievable legally are recorded as not retrieved) closed at what legal open routes yielded; W5 (figures) built and embedded; W6 (independent human check) **AI-only per the author's 9 Oct directive** - no external helper; the manuscript discloses AI-only screening; W7 (extraction/RoB/synthesis for the new studies) done, coverage 113; W8 preparation is the OSF/Zenodo retrospective deposit (never backdated, file 17); **W9 remains: re-run the reporting audits (files 01/02/04) against the updated manuscript and the reviewer blind re-score**, both on the Sunday path.
- The author's D1/D2 were superseded by the 9 Oct author directive: no tasks are delegated to the author, retrieval closes at legal routes, and questions go only via the final deliverable (file 15). W6 helper questions (D1 follow-up, D4) are therefore closed.
- W6 page status: built, but the only run so far was done by the author and is a **calibration pilot only — never report it as the independent check**. Before a helper uses it: add Stage 1 worked examples, and make Stage 2 require opening the paper and recording the page relied on. Share by email as Editor (Contributor only if same organisation), **never by public link**. `sample_key.json` (the AI decisions) is never published.

## Manuscript rules
- Edit target: `Avian_review_paper_submission_ready.docx` **only**, via the build pipeline above, using the `docx` skill. `Avian_review_paper_fellow.docx` (~2,783 words) stays frozen.
- Preserve Times New Roman, numeric bracket citations, and the highlight conventions the build uses (yellow = author placeholder).
- Section files `sections\01_title_abstract.txt`–`10_appendix_cdef.txt`; citations are keys (`{B:...}` and study keys); `assemble.py` numbers them in first-citation order. Tables: `tables_gen.py`. References: `build_refs.py` → `refs_reports.json`; `refs_verified_20261008.json` is applied after OVR (search for `VER`).
- If any number changes: update upstream data first (extraction/rob/synthesis), rerun `run_all.py` with all assertions passing, then rebuild the manuscript. Take a dated backup before editing; validate against the previous backup with `--original`.
- Open author items (highlighted in the docx): declarations (funding — also in the abstract — competing interests, contributions, acknowledgements, data availability); Reviewer 1 identity before 27 Sep; target journal choice (main text 8,530 words including table notes must fit its limit).

## Skills
- `docx` — required for any `.docx` edit (`thesis-to-journal` is not installed; author decision 7 Oct).
- `academic-paper-review` — manuscript critique.
- `systematic-literature-review` — method reference only; its scripts are arXiv-only and must not be used for this PubMed/Scopus review.

## Git
- Branch `main` only; `origin` = `https://github.com/batestguy/avian-influenza-nigeria-systematic-review.git`. Commit only when the author asks.
- Commit style: plain sentence summaries, sometimes tagged `(reviewer-verified)` or `(author decision)`; e.g. `RoB batch 3 consensus (28 studies; 78.8% item agreement); conventions A10-A12`.
- Never commit secrets, browser state, or environments; `.gitignore` already covers them.

## Tips for AI agents
- **Reports ≠ studies:** 127 reports map to 113 studies via file 56 `report_linkage`; never renumber `STU-xxx` after extraction.
- Normalise DOIs (strip non-alphanumerics) before matching — older register records store them without punctuation.
- `Workbench\` file numbers are chronological; never reuse an old number for a new topic. The current state lives only in the tops of files 57/59/15 and in file 56.
- `wos_facet_*.json` are exploratory/rate-limited artifacts; interpret only through files 15/19/33 — never infer counts from them directly.
- Unrelated untracked root files (`25min-alternating-exercise.html`, `app.png`) are not part of the review; leave them out of commits.
