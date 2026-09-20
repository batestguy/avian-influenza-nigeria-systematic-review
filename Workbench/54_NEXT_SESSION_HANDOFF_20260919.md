# Next-session handoff - Nigeria avian influenza systematic review

**Prepared:** 19 September 2026; **updated:** 20 September 2026 (Gate C handoff)
**Purpose:** resume the review without rediscovery, methodological drift, or accidental manuscript edits.

## Start here

Read these files in order:

1. `AGENTS.md` - binding scope, safety, and phase-order instructions.
2. `Workbench/50_END_TO_END_WORKPLAN.md` - full phase map and gate criteria.
3. `Workbench/15_RUN_LOG.md` - current dated evidence and gate record.
4. `Workbench/53_CANONICAL_REGISTER.json` - current identity register.
5. `Workbench/19_SEARCH_run_sheets.md` - source strings, dates, exports, and limitations.
6. `Workbench/56_SCREENING_RECONCILIATION.json` - controlled Gate C screening queue and pilot.

The manuscript source of truth is `Avian_review_paper_fellow.docx`. It is frozen and unchanged.
Do not edit it until a paste-ready change is explicitly approved after the required gates.

## Current state

- Review question: emergence, temporal/geographic/host-range, molecular/clade, and reassortment dynamics of avian influenza viruses in Nigeria, 2006-2026.
- Framework: CoCoPop/PEO; reporting: PRISMA 2020, PRISMA-S, and SWiM.
- Default synthesis: SWiM narrative synthesis without forced meta-analysis.
- PROSPERO: skipped; do not claim prospective registration.
- Operational search-update date: 20 September 2026. The 16 September library and 19 September
  WoS API layer are historical imported layers; AJOL and WoS browser runs are dated 20 September.
- Roles: R1 primary reviewer; Epicurus independent Reviewer 2; main Codex agent arbiter.

### Gates

- **Gate A - passed:** protocol truth, cutoff amendment, roles, and review route are recorded.
- **Gate B - search execution complete with export limitations:** all six named databases have a
  documented run. Scholar has no persistent export; AJOL now has a persistent browser-derived
  citation-metadata file rather than a vendor bulk export; and WoS Free View supplied the
  20 September counts without a reliable complete export.
- **Gate C - open and operationally initialized:** file 56 contains the controlled 1,877-record queue and 40-record R1/R2 pilot. Record-level title/abstract decisions and adjudication remain open.
- **Gate D onward - not started:** full-text eligibility, extraction, RoB, certainty, synthesis, manuscript reporting, and final checklist audit.

## Verified evidence checkpoint

`Workbench/53_CANONICAL_REGISTER.json` currently contains:

- 2,367 raw input rows;
- 1,877 provisional canonical identity groups;
- 490 collapsed duplicate rows;
- source rows: PubMed 140, OpenAlex/Crossref 1,744, Scopus 204, ScienceDirect 25, WoS 175, AJOL 79;
- 151 WoS rows matched a pre-existing source group and 24 remain provisional-new;
- AJOL contributes 79 rows: 47 existing matches and 32 new identities; six are outside the 2006-2026 window and remain date flags, not substantive eligibility decisions;
- all final statuses deliberately remain non-final.

The historical 160-record full-text queue is superseded as an operational queue by file 56. It remains an audit snapshot only. The controlled screening denominator is 1,877 canonical identities; full-text assessment, extraction, and RoB remain zero.

## Web of Science status

- Historical imported layer: 175 UIDs from the 19 September API query, represented in file 53.
- Browser update on 20 September: 206 base, 77 molecular, 154 epidemiology/spatial/temporal,
  and 70 wild-bird/host, all date-filtered 2006-01-01 to 2026-09-20.
- Free View prevented a reliable complete record export. The new counts are not additional
  canonical records and must not be summed with 175.

- Valid base query: `TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026)`.
- Result: 175 raw records across four pages (50/50/50/25), all HTTP 200, 175 unique UIDs.
- Raw response exports are preserved in `.playwright-cli/`; do not share or commit that directory.
- The 24-record provisional-new queue is in `Workbench/52_WOS_PROVISIONAL_NEW.json`.
- Reviewer 2 provisional title/metadata result: 2 `include_main`, 6 `background_only`, 14 `exclude`, 2 `unclear`.
- The 19 September HTTP-429 facet attempts are superseded for count documentation by the
  successful 20 September browser queries, but not by a record-level export.

## Exact next actions

1. Start the 40-record pilot in file 56 using `Workbench/18_SCREENING_forms.md`.
2. Retrieve or verify title/abstract evidence for each pilot record; record evidence, not just a decision label.
3. Run R1 primary and R2 independent screening on the same pilot records without sharing votes.
4. Adjudicate disagreements in the main session and record the reason code and supporting evidence.
5. After pilot QA, expand title/abstract screening in controlled batches; keep all decisions provisional until adjudication.
6. Seek a legitimate full WoS export only if account access permits. If unavailable, retain the count-only limitation; do not scrape around access controls.
7. Link WoS correction record `WOS:000255508300044` to parent PMID `18394282` during screening QA.
8. Keep PMID `27677611` as a non-Nigeria Iran record in the audit trail; do not delete it.
9. Do not start extraction, RoB, or manuscript editing before full-text eligibility and the extraction pilot.

## Security and repository state

- `woskey.txt`, `.playwright-cli/`, `.playwright-mcp/`, and the local Python environment are ignored by Git.
- Never print, commit, paste, or place API keys in Workbench files, the manuscript, or command output. Rotate any key that appeared in chat or browser snapshots.
- Public GitHub repository: `https://github.com/batestguy/avian-influenza-nigeria-systematic-review`.
- Latest repository commit before this documentation update: `d96ed8c`.
- The workflow PDF was regenerated locally at `output/pdf/AvianInfluenzaSysRev.pdf` for 19 September status. The PDF update and its generator are currently uncommitted; commit/push them only when explicitly requested.

## Do not do

- Do not edit `Avian_review_paper_fellow.docx`.
- Do not add the 206 WoS count to the 175 imported UIDs or treat facet counts as separate records.
- Do not use the 160-record queue for final PRISMA counts.
- Do not treat file 56 pilot placeholders as screening decisions; it contains no substantive votes yet.
- Do not claim AJOL retrieval candidates or Google Scholar supplementary records as screened studies.
- Do not use a scraper, CAPTCHA solver, proxy rotation, paywall bypass, or unauthorised full-text route.
- Do not create CSV/BibTeX/Zotero sidecars or new screening databases unless explicitly authorised.

## Handoff acceptance check

Before beginning work, confirm that the current session can state: Gate B search execution is complete with export limitations; Gate C is open but initialized in file 56; file 53 is the identity source for the imported layers; the controlled denominator is 1,877; the manuscript is frozen; and the next deliverable is the dual-review title/abstract pilot, not extraction.
