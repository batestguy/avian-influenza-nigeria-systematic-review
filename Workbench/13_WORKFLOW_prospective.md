# Systematic-review workflow — Nigeria AIV 2006–2026 (operational phase map)

Status: unregistered systematic review, SWiM default. Re-audited 2026-09-19. The 2026-09-16 search library remains the locked historical layer; a Web of Science API update on 2026-09-19 added 175 raw records but has not been canonicalised or screened. Preliminary title/abstract screening exists for the earlier layer, while canonical reconciliation, full-text assessment, extraction and RoB are not complete. The master end-to-end plan is `50_END_TO_END_WORKPLAN.md`. Original manuscript frozen until paste-approved. See `17_SKIPPED_PROSPERO_note.md` for the registration decision.

## Gate rule (hard)

`Freeze → search run → screen → extract.` No screening before freeze files 10 + 11 are approved.

## Stage 0 — Freeze (this week, you + me)

- [ ] Approve `10_Phase0_protocol_freeze_DRAFT.md` (question, 4 objectives, groupings, eligibility).
- [ ] Approve `11_Phase1_search_rebuild_DRAFT.md` (per-database strings + caps + supplementaries).
- [x] Review roles operationalised for this unregistered review: R1 = primary reviewer; R2 = independent Reviewer-2 Codex agent (Epicurus); Arbiter = main Codex agent. All actions remain logged.
- **Gate 0 exit:** freeze files 10 + 11 approved and dated. Paste into Methods when ready.

**Re-audit status:** Gate 0 was re-frozen on 2026-09-19 after the cutoff and reviewer-role amendment.
Gate 1/source audit is conditionally closed with explicit Scholar/AJOL/WoS limitations. Gate 2
identity reconciliation is complete in `53_CANONICAL_REGISTER.json`, but screening reconciliation
and final candidate-queue adjudication remain open. The 2026-09-19 WoS retrieval does not itself
establish final eligibility.

## Stage 1 — Skip registration (logged)

- PROSPERO skipped per file 17. Use the "not prospectively registered" sentence from file 14/17.
- **Gate 1 exit:** decision file 17 exists. Searches may run immediately after Gate 0.

## Stage 2 — Search + dedupe

- [ ] Run each string AS WRITTEN, one database per day max to avoid mix-ups. Log: platform, date, exact string, filters, hits, export filename.
- [ ] Dedupe: tool + manual title/DOI check. Log auto vs manual duplicates (needed for PRISMA flow).
- [ ] Re-run/update search before analysis; log date.
- **Gate 2 exit:** per-source hit table complete; deduped library count fixed.

**WoS update completed:** base API query returned 175 raw records on 2026-09-19. Canonical identity
merge is now preserved in `53_CANONICAL_REGISTER.json`; facet coverage and source-level PRISMA
accounting remain incomplete.

## Stage 3 — Selection (dual)

- [ ] Pilot: same 30–50 abstracts, all screeners, calibrate form; revise eligibility notes if needed (dated amendment).
- [ ] Title/abstract: 2 independent votes, blinded. Conflicts → discussion → arbiter. Log reason at full-text stage only (one reason from fixed list).
- [ ] Full-text retrieve + dual assess; build excluded-with-reasons table (T6 shell in `08_formats`).
- [ ] PRISMA flow numbers: identified → deduped → screened → full-text → included.
- **Gate 3 exit:** flow diagram + T6 complete; include list frozen.

## Stage 4 — Extraction + RoB (piloted)

- [ ] Pilot extraction form on 3–5 diverse includes; revise; re-pilot if major change.
- [ ] Dual extraction for outcome fields (subtype/clade/host/temporal/spatial/molecular claims); single + verification for descriptive fields. No blanks.
- [ ] JBI RoB (2 appraisers) + 7-item molecular check per study; overall Include/Exclude/Seek. No sums.
- [ ] GRADE-prognosis certainty per synthesis grouping (narrative).
- **Gate 4 exit:** T1–T5 + T7 tables filled; certainty paragraphs drafted.

## Stage 5 — SWiM synthesis + write + audit

- [ ] One synthesis per grouping (temporal / geographic / host / molecular) with table + text + limits, every claim row-linked.
- [ ] Sensitivity: peer-only vs +grey; high-RoB-out re-read.
- [ ] Write Abstract last (12-item); Discussion splits evidence vs method limits.
- [ ] Audit: PRISMA 27 + S 16 + SWiM 9 using `01/02/04` scoring files. Zero `No` on gate items or justify.
- **Gate 5 exit:** audit sheet all Yes/justified; manuscript paste-ready.

## Amendment discipline

Any post-freeze change: date + what + why in `15_RUN_LOG.md` + Methods note. Minor (extra database) vs major (outcome/eligibility change) labelled.
