# Next-session handoff - Nigeria avian influenza systematic review

**Prepared:** 19 September 2026  
**Purpose:** resume the review without rediscovery, methodological drift, or accidental manuscript edits.

## Start here

Read these files in order:

1. `AGENTS.md` - binding scope, safety, and phase-order instructions.
2. `Workbench/50_END_TO_END_WORKPLAN.md` - full phase map and gate criteria.
3. `Workbench/15_RUN_LOG.md` - current dated evidence and gate record.
4. `Workbench/53_CANONICAL_REGISTER.json` - current identity register.
5. `Workbench/19_SEARCH_run_sheets.md` - source strings, dates, exports, and limitations.

The manuscript source of truth is `Avian_review_paper_fellow.docx`. It is frozen and unchanged.
Do not edit it until a paste-ready change is explicitly approved after the required gates.

## Current state

- Review question: emergence, temporal/geographic/host-range, molecular/clade, and reassortment dynamics of avian influenza viruses in Nigeria, 2006-2026.
- Framework: CoCoPop/PEO; reporting: PRISMA 2020, PRISMA-S, and SWiM.
- Default synthesis: SWiM narrative synthesis without forced meta-analysis.
- PROSPERO: skipped; do not claim prospective registration.
- Operational cutoff: 19 September 2026. The 16 September library is historical; the WoS layer is dated 19 September.
- Roles: R1 primary reviewer; Epicurus independent Reviewer 2; main Codex agent arbiter.

### Gates

- **Gate A - passed:** protocol truth, cutoff amendment, roles, and review route are recorded.
- **Gate B - conditionally closed for source audit:** PubMed, Scopus, ScienceDirect, OpenAlex/Crossref, and the WoS base query are recorded; Scholar is supplementary; AJOL is blocked/not run; corrected WoS facet retries returned HTTP 429. Do not claim complete database coverage.
- **Gate C - open for screening reconciliation:** the canonical identity register is complete, but record-level adjudication and replacement of the historical upper-bound queue remain open.
- **Gate D onward - not started:** full-text eligibility, extraction, RoB, certainty, synthesis, manuscript reporting, and final checklist audit.

## Verified evidence checkpoint

`Workbench/53_CANONICAL_REGISTER.json` currently contains:

- 2,288 raw input rows;
- 1,845 provisional canonical identity groups;
- 443 collapsed duplicate rows;
- source rows: PubMed 140, OpenAlex/Crossref 1,744, Scopus 204, ScienceDirect 25, WoS 175;
- 151 WoS rows matched a pre-existing source group and 24 remain provisional-new;
- all final statuses deliberately remain non-final.

The 160-record full-text queue is an upper bound only. It is not a final screening denominator or a final included-study count. Full-text assessment, extraction, and RoB remain zero.

## Web of Science status

- Valid base query: `TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026)`.
- Result: 175 raw records across four pages (50/50/50/25), all HTTP 200, 175 unique UIDs.
- Raw response exports are preserved in `.playwright-cli/`; do not share or commit that directory.
- The 24-record provisional-new queue is in `Workbench/52_WOS_PROVISIONAL_NEW.json`.
- Reviewer 2 provisional title/metadata result: 2 `include_main`, 6 `background_only`, 14 `exclude`, 2 `unclear`.
- Corrected molecular, epidemiological/spatial/temporal, and wild-bird facet retries returned HTTP 429. Their exploratory artifacts are not protocol-valid facet totals.
- Next WoS action: wait for the documented quota-reset window, then run one corrected facet test at no more than one request per second; log the response before any pagination.

## Exact next actions

1. Recompute/remap screening decisions from raw records to canonical IDs. Do not inherit pre-collapse aggregate votes silently.
2. Manually adjudicate title/year discrepancies and identifier-missing records; retain source lineage.
3. Link WoS correction record `WOS:000255508300044` to parent PMID `18394282`.
4. Keep PMID `27677611` as a non-Nigeria Iran record in the audit trail; do not delete it.
5. Rebuild the full-text queue from the canonical register and freeze the Gate C screening denominator.
6. Only after Gate C, run the controlled screening workflow with R1 primary review, R2 independent verification, and main-agent adjudication.
7. Do not start extraction or edit the manuscript before full-text eligibility and the extraction pilot are complete.

## Security and repository state

- `woskey.txt`, `.playwright-cli/`, `.playwright-mcp/`, and the local Python environment are ignored by Git.
- Never print, commit, paste, or place API keys in Workbench files, the manuscript, or command output. Rotate any key that appeared in chat or browser snapshots.
- Public GitHub repository: `https://github.com/batestguy/avian-influenza-nigeria-systematic-review`.
- Latest pushed commit before this handoff: `194e8a2`.
- The workflow PDF was regenerated locally at `output/pdf/AvianInfluenzaSysRev.pdf` for 19 September status. The PDF update and its generator are currently uncommitted; commit/push them only when explicitly requested.

## Do not do

- Do not edit `Avian_review_paper_fellow.docx`.
- Do not treat exploratory WoS facet files as corrected search results.
- Do not use the 160-record queue for final PRISMA counts.
- Do not claim AJOL or Google Scholar as completed primary searches.
- Do not use a scraper, CAPTCHA solver, proxy rotation, paywall bypass, or unauthorised full-text route.
- Do not create CSV/BibTeX/Zotero sidecars or new screening databases unless explicitly authorised.

## Handoff acceptance check

Before beginning work, confirm that the current session can state: Gate B is conditionally closed with limitations; Gate C is open; the canonical register is the identity source; the manuscript is frozen; and the next deliverable is a reconciled screening denominator, not extraction.

