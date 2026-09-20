# PubMed improvement — v1 → v3 (2026-09-16)

**Source-status note (2026-09-20):** this historical PubMed optimisation log is unchanged. The
v3 base remains 140 and molecular facet 53; later AJOL/WoS updates do not alter these counts.

## Problem with v1 (base 188)

Query `(avian influenza OR AIV OR HPAI OR H5N1) AND Nigeria` used All-Fields mapping: pulled Newcastle disease, SARS-CoV-2, Ebola, Zika, H1N1-swine, Ochrobactrum — ~1/3 off-topic at title level.

## v2 test (base 134): tighter but lossy

tiab-only + subtypes + explicit dp range cut noise well (dropped 65, mostly junk) but LOST one relevant KAP paper (19305431, "avian flu" wording not in block) and gained 11× 2006 news blurbs + one Niger false hit.

## v3 adopted (base 140) — RECOMMENDED new base

Block: avian influenza / avian flu / bird flu / fowl plague / AIV / HPAI / LPAI / H5N1 H5N2 H5N6 H5N8 H9N2 H7N9 H5Nx [tiab] AND Nigeria[Mesh]/tiab/Nigerian AND 2006/01/01–2026/09/30[dp].
Result: 140 records; recovers the KAP paper; drops 62 v1 off-topic; +14 vs v1 (early news, screened out at title stage).
Facets on v3: MOL 53, EPI ~100, WILD ~37 (re-run values in 34/35 files; MOLv3 = 53).

## Recommendation (locked)

- New screening base = **v3 140** (`35_PUBMED_v3_base.txt`), NOT v1 188.
- Prioritise: MOL 53 first (molecular/clade core of your Q1 claim), then EPI, then WILD, then remainder.
- Round 1's 10 Includes all retained in v3 (verify on next screen round — re-check PMIDs 42046457, 41200728, 39553779, 38896308, 38314064, 37376688, 37363241, 34452311, 33480188, 32236814).
- v1-only orphans: spot-checked, off-topic except recovered KAP — no further action.
- Exact v3 strings are PRISMA-S appendix-ready; file 11 skeleton superseded for PubMed (Scopus/WoS adaptations unchanged).
