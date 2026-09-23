# Next-session handoff — Nigeria avian influenza systematic review

**Prepared:** 22 September 2026  
**Purpose:** resume screening and document production without rediscovery, methodological drift, or accidental edits to the frozen source manuscript.

## Start here

1. `AGENTS.md` — binding scope and safety rules.
2. `Workbench/15_RUN_LOG.md` — search and gate history.
3. `Workbench/53_CANONICAL_REGISTER.json` — identity source.
4. `Workbench/56_SCREENING_RECONCILIATION.json` — pilot/register screening source.
5. `Avian_review_paper_submission_ready.docx` — current deliverable.

The source manuscript `Avian_review_paper_fellow.docx` is frozen and must not be overwritten.

## Current repository state

- Branch: `main`, five local commits ahead of `origin/main`.
- Latest committed screening document: `a9ed430 Record adjudicated screening batch B4`.
- Previous commits: `9ad412c Record adjudicated screening batch B2`; `d4848d2 Advance systematic review screening status`.
- A user-owned untracked file, `25min-alternating-exercise.html`, was observed and left untouched. Do not add or delete it.
- No push has been performed.

## Review and search gates

- Gate A/protocol: closed.
- Gate B/search execution: closed with export limitations.
- Gate C/title/metadata screening: open and progressing in independent R1/R2 batches.
- Gates D onward — full text, extraction, RoB, certainty, synthesis and final reporting — not started.
- PROSPERO was skipped; do not claim prospective registration.
- Full-text inventory in the workspace currently contains no article PDFs; only the manuscript/output PDF is local. Retrieval must be targeted and legitimate; do not bypass paywalls or access controls.

## Verified identity and screening arithmetic

Source reconciliation remains:

`2,367 source rows → 1,877 provisional identity groups → 490 collapsed duplicates`.

Committed document state through B5:

| Batch | Screened | Excluded | Retained for full text | Verification |
|---|---:|---:|---:|---|
| R1/R2 pilot | 40 | 25 | 15 | Adjudicated; two disagreements resolved conservatively |
| B1 | 100 | 73 | 27 | R1/R2 exact agreement, 100/100 |
| B2 | 100 | 83 | 17 | Eight disagreements adjudicated |
| B3 | 100 | 87 | 13 | Six uncertainty disagreements resolved conservatively |
| B4 | 100 | 89 | 11 | Exact R1/R2 aggregate agreement |
| B5 | 100 | 79 | 21 | Fourteen disagreements retained conservatively |
| **Committed cumulative** | **540** | **436** | **104** | **1,337 identities unresolved** |

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

## Exact next actions

1. Continue title/metadata screening in 100-record R1/R2 batches using the same conservative rules; Batch B6 is the next unresolved block after B5. Keep uncertain records in the full-text queue.
2. Begin legitimate, targeted retrieval for the 104 provisional full-text candidates. Record full-text inclusion/exclusion reasons only after evidence is available.
3. Preserve the submission-stage wording: the document is not yet a final systematic-review manuscript.
4. Do not start extraction, RoB, certainty, synthesis or final PRISMA reporting until full-text eligibility is reconciled.

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

