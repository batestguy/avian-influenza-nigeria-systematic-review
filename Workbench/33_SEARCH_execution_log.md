# Search execution log — PubMed run 2026-09-16 (by assistant)

## What was actually run (reproducible)

- Source: PubMed via NLM E-utilities esearch + esummary. Date run: 2026-09-16.
- Query: `(avian influenza OR AIV OR HPAI OR H5N1) AND Nigeria`, datetype pdat, last ~20y (reldate 7300 ≈ 2006–2026 window).
- Translation as run: ("influenza in birds"[MeSH] OR ... OR "AIV" OR "HPAI" OR H5N1-MeSH...) AND (Nigeria[MeSH] OR Nigeria[All Fields]).
- Hits: **188 unique PMIDs** after dedupe (raw 276 across two pages → 188 unique). Saved: `30_PUBMED_idlist.txt`, titles/years/journals/DOIs: `31_PUBMED_candidates.json`.
- Title triage: 146/188 mention avian/influenza/H5/H9/AIV/HPAI/LPAI; of those, **72 mention Nigeria in title** (file 32 subset basis).

## Screening Round 1 (agents, 2026-09-16) — first 15 Nigeria-in-title records

Includes (10): 42046457 (2026 reassortant 2.3.4.4b), 41200728 (captive wild-bird screening), 39553779 (H9N2 commercial poultry 2024), 38896308 (H5N1 molecular epi 2006–2021), 38314064 (Hadejia-Nguru wild-bird 2.3.4.4b), 37376688 (H5 poultry evolution 2021–22), 37363241 (North-central resurgence), 34452311 (LBM H9N2 reservoir), 33480188 (H5Nx introductions), 32236814 (H5N1 re-emergence 2014–16).
Excludes (5): 42376503 Akanbi review (no primary data, background), 39939962 paramyxovirus (non-AIV), 37775596 vaccination perspective (no primary data), 36146628 human flu/COVID (non-AIV), 34996333 metaavulavirus (non-AIV).
Remaining: 57 Nigeria-in-title + 74 AIV-title without Nigeria-in-title + 42 off-title → screen in next rounds.

## v3 adoption (2026-09-16) — new base 140, MOL 53 first

- v1 All-Fields pulled ~1/3 off-topic (Newcastle, SARS-CoV-2, Zika, swine H1N1). v2 tiab-only lost KAP 19305431. v3 adopted: AIV block [tiab] AND Nigeria[Mesh]/tiab/Nigerian AND 2006/01/01–2026/09/30[dp] = 140 records (35_PUBMED_v3_base.txt). MOL 53, EPI ~100, WILD ~37. Full log file 36.
- R1 10 Includes all retained in v3. Screening base = v3 140, NOT v1 188.

## Screening R2–R5 (2026-09-16) — PubMed title/abs complete

- R2 MOL 4–6 (15): main 1 (29104094 2.3.2.1c) + supp 1 (29651056 pig → context only); unsure 2 (36268570, 32312185); excludes 11. File 38.
- R3 MOL 7–9 (15): main 6 (28710829, 27873070, 27677611, 26664747, 26079193, 25671118) + supp 1 (24677113 workers); unsure 3 (24885233, 22001877, 21248176); excludes 5. File 39.
- R4 MOL 10–12 (15, MOL closed): main 10 (20071565, 19290041, 19239760, 18976562, 18976556, 18704172 H5N2 wild-bird, 18631423, 18394282 reassortant, 17622635, 17479371 Kaduna index); excludes 5 (20335251 Austria, 19618621/19618617 reviews, 18837987 Sweden, 17498292 Denmark).
- Unsure resolution via abstracts: include 32312185 H5N6 Nigeria, 22001877 NG n=106 vaccination dynamics, 21248176 H5N2 reassortant Hadejia-Nguru; exclude 36268570 SA/Namibia; full-text check 24885233.
- R5 remainder 82 v3: main 43 (EPI/spatial/KAP/LBM/wild-bird/costs — e.g. 32193749, 29631310, 29152316, 29067212, 30255048, 27603430, 27317323, 28337492, 25923926, 26949793, 25328630, 24880626, 27379256, 24001574, 23936731, 23308319, 23074668, 23038077, 22925404, 22869337, 22530694, 22476732, 22469078, 22079423, 21553559, 21205255, 21146235, 20846589, 20521661, 19653927, 19331751, 19305431, 19021104, 18926110, 18575062, 18343470, 19738338, 22761900, 17542958, 16863071, 41438164, 33040313, 29920398) + supp 2 (23400898, 18008254 workers); excludes 37 (7× 2006 news + reviews/human-only/non-Nigeria/no AIV data — full list in chat 2026-09-16).
- Cumulative PubMed: screened 142 (140 v3 + 2 v1-only), main 73, supp 4, excludes 64, full-text check 1.

## Cross-database status update — 2026-09-20

The PubMed counts above remain source-specific and unchanged. Scopus and ScienceDirect were
imported on 16 September; Scholar was searched as a supplement on 17 September; WoS has a
175-record imported API layer plus 20 September count-only browser totals of 206/77/154/70; AJOL
was searched on 20 September and yielded 79 unique article URLs from 144 query rows. Next:
independently verify the completed AJOL import, secure a legitimate WoS export if available,
and complete screening reconciliation before full-text work.

- Run file 19 strings verbatim in library portals; record date, filters, hits, export filename in file 19 + Gate 1 table file 15. Dedupe vs PubMed 140 (auto + manual) before full-text. Do NOT edit PubMed strings mid-run; amendments = new version + date.
