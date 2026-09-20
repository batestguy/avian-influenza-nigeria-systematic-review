# Phase 1 — Search rebuild skeleton (DRAFT, per-database strings to finalise)

**Execution amendment (2026-09-20):** the architecture below remains the design record. The
actual AJOL and Web of Science strings run on 20 September are frozen verbatim in files 15 and
19. AJOL required nine short mandatory-term queries rather than one Boolean mega-query. Web of
Science used the full AIV block plus Nigeria block, with three separate facet lines and a
publication-date window of 2006-01-01 to 2026-09-20. Do not retrofit these executed strings into
the 16 September historical layer.

## Architecture (replaces current `And Nigeria`-in-every-block)

`(AIV block) AND (Nigeria block) AND (date 2006–2026 block)`, then facet lines for molecular / epi-spatial-temporal / wild-bird run as SEPARATE restricted queries, not fused into one unreproducible string.

## PubMed via NLM (master — adapt syntax per platform)

Line 1 (AIV): ("Influenza in Birds"[Mesh] OR "Influenzavirus A"[Mesh] OR "avian influenza"[tiab] OR "avian influenza virus"[tiab] OR AIV[tiab] OR "highly pathogenic avian influenza"[tiab] OR HPAI[tiab] OR "low pathogenic avian influenza"[tiab] OR LPAI[tiab] OR H5N1[tiab] OR H5N2[tiab] OR H5N6[tiab] OR H5N8[tiab] OR H9N2[tiab])
Line 2 (Nigeria): (Nigeria[Mesh] OR Nigeria[tiab] OR Nigerian[tiab])
Line 3 (date): ("2006/01/01"[dp] : "2026/09/30"[dp])
Line 4 (base set): #1 AND #2 AND #3
Line 5 (molecular facet): (genome[tiab] OR molecular[tiab] OR phylogen*[tiab] OR clade[tiab] OR lineage[tiab] OR sublineage[tiab] OR reassort*[tiab] OR mutation[tiab] OR evolution[tiab] OR "genetic diversity"[tiab] OR "genetic characterisation"[tiab])
Line 6 (epi-spatial facet): (outbreak[tiab] OR surveillance[tiab] OR prevalence[tiab] OR distribution[tiab] OR spatial[tiab] OR geographic[tiab] OR temporal[tiab] OR emergence[tiab] OR re-emergence[tiab] OR spread[tiab] OR introduction[tiab])
Line 7 (wild-bird facet): ("wild bird*"[tiab] OR waterfowl[tiab] OR migratory[tiab] OR wetland[tiab] OR wildlife[tiab])
Final sets: #4 AND #5 | #4 AND #6 | #4 AND #7 — record hits per line, date run, filters (English, 2006–2026).

## Scopus via Elsevier — adapt

`TITLE-ABS-KEY("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H5N2 OR H5N6 OR H5N8 OR H9N2) AND TITLE-ABS-KEY(Nigeria OR Nigerian) AND PUBYEAR > 2005 AND PUBYEAR < 2027` + facet AND-lines as above. Record exact string as run.

## Web of Science — adapt

`TS=("avian influenza" OR AIV OR HPAI OR LPAI OR H5N1 OR H9N2) AND TS=(Nigeria OR Nigerian) AND PY=(2006-2026)` + facets. Record collection (SCIE etc.) + date.

## ScienceDirect / Google Scholar / AJOL

- ScienceDirect: title-abs-key variant, record filters; export capped — log cap.
- Google Scholar: relevance-ranked, first 200 screened, query + date + cap logged. Never sole source.
- AJOL: free-text variants (`avian influenza Nigeria`, `H5N1 Nigeria`, `H9N2 Nigeria`, `poultry Nigeria wild birds`), record per-query hits.

## Supplementaries (log per item)

Reference lists of all includes + Kalonda 2020 + Akanbi & Lakes 2025; forward/backward citation chasing; WOAH reports + theses considered grey with sensitivity analysis.

## Logging rule (PRISMA-S)

Per source: platform, date, exact string, filters, hits, exports retained in workbench log. Amendments dated.
