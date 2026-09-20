# Calibration run SEED1 — adjudicated (2026-09-16)

**Status (2026-09-20):** calibration evidence remains valid for form interpretation only. Its
decisions do not replace canonical-record screening or full-text eligibility assessment.

Two `general` subagents screened 5 papers each, blinded, JSON-only. Main-session adjudication below. This validates file 18 forms before database screening.

## Adjudicated votes

| ID | Study | Agent vote | Final | Action |
|---|---|---|---|---|
| 1 | Kalonda 2020 SSA review | Exclude (no primary data) | **Exclude, background** | Citation-chase its Nigeria refs; not extracted |
| 2 | Olawuyi 2024 Hadejia-Nguru wild-bird 2.3.4.4b | Include | **Include** | Pilot extraction candidate (wild-bird + accession check) |
| 3 | Adesola 2024 H5N1 2006–2021 molecular epi | Include | **Include** | Pilot extraction candidate (temporal/clade) |
| 4 | Meseko 2023 poultry H5 2021–22 | Include | **Include** | Extraction (multi-subtype) |
| 5 | Shittu 2017 2015 WA2 2.3.2.1c | Include | **Include** | Extraction (clade replacement anchor) |
| 6 | Meseko 2021 H5Nx introductions | Include | **Include** | Extraction (introduction verdicts) |
| 7 | Akanbi & Lakes 2025 broad review | Exclude (no primary data) | **Exclude, background** | Positioning comparator in Introduction; not extracted |
| 8 | Akanbi 2024 H9N2 commercial poultry | Include | **Include** | Extraction (non-H5 anchor) |
| 9 | Abolnik 2025 Africa situation report | Exclude (non-Nigeria) | **Unsure → full-text check** | Agent over-excluded; verify Nigeria section before final Exclude |
| 10 | Meseko 2026 reassortant 2.3.4.4b | Include | **Include** | Extraction (reassortment flagship; apply M7 strictly) |

Agreement: 9/10 with adjudication; 1 downgraded to full-text check. Forms (file 18) behaved correctly on edge cases (reviews → background, continental report → verify).

## What this proves about agent use

- Batches of 5 + JSON-only + fixed reasons work; ~1 min per batch.
- Agents handle clear Includes well; edge cases (ID 9) need human full-text tiebreak — keep that rule.
- Next: reuse same prompt shape for database batches; 2 agents × 5 papers, main session adjudicates, verified votes only enter T-tables.
