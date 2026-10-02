# PRISMA 2020 flow + final audit sheet

**Status (2026-09-20, superseded 2026-09-30):** was unfilled pending cross-source reconciliation. That reconciliation is done; the flow below is filled from the register.

## Flow (numbers from `prisma_flow.py`, reconciled with file 56 on 2026-09-30; diagram drawn at write stage)

**Status (2026-09-30):** filled, including the author's exclusion of CAN-1610 (rule Q1).

**Identification - databases and registers**
- Records identified: 2,367. OpenAlex 1,000 and Crossref 1,000 exports together gave 1,744 rows. PubMed 140, Scopus 204, Web of Science 175, ScienceDirect 25, AJOL 79 unique article pages (from 144 query rows).
- The Web of Science browser update (206 base) is count-only and is not added.
- Duplicates removed before screening: 490. Identity rule: DOI, PMID, or normalised title plus year.

**Identification - other methods**
- Google Scholar dated update search (2026-09-28, Q1-Q4, cap 200 per query): 800 rows, 519 unique.
- 291 were already identified by the database search, leaving 228 new records. Of these, 12 were later found to be duplicates of existing records and were removed.

**Screening - databases**
- Records screened: 1,877.
- Excluded on title/metadata: 1,578, including 6 outside the 2006-2026 window.
- Reports sought for retrieval: 299. Not retrieved: 80.
- Reports assessed for eligibility: 219. Excluded: 108:
  - non-Nigeria, no Nigeria data: 54 (includes CAN-0356 and CAN-1558, excluded by the author at extraction on 2026-10-02)
  - no laboratory-confirmed avian AIV: 19
  - no avian-host field data: 17
  - no primary data: 13
  - no epidemiological/molecular/spatial-temporal data: 2
  - duplicate dataset: 1
  - non-AIV: 1
  - experimental only: 1

**Screening - other methods**
- Records screened: 216. Excluded on title/snippet: 190.
- Reports sought: 26. Not retrieved: 8.
- Reports assessed: 18. Excluded: 6:
  - non-Nigeria: 2
  - no primary data: 2
  - no laboratory-confirmed avian AIV: 1
  - experimental only: 1

**Included**
- Reports: 123 (databases 111 + other methods 12).
- **Studies: 110** (report-to-study linkage, file 15, 2026-09-30; STU-032 and STU-070 retired 2026-10-02 when CAN-0356 and CAN-1558 were excluded, IDs not renumbered).
- Included in syntheses (temporal / geographic / host / molecular): ____ (after extraction).

## Final audit (score with files 01/02/04 — paste location per item)

- PRISMA 2020 27 + abstract 12: list any Partial/No with fix owner.
- PRISMA-S 16: strings + caps + chasing all Yes or justified.
- SWiM 9: groupings, metric, method, prioritisation, heterogeneity, certainty-link, presentation, results, limits.
- Bar: zero unjustified No on PRISMA 1–9/24–27, PRISMA-S 4–9, SWiM 1–4 — else not submission-ready.
