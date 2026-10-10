# 9 October fixes applied by the main session (F2, F3, F4, F8)

Two fix executor agents were dispatched but ran without write authority (Plan-mode posture) and
returned verified patch content instead. The main session applied and verified every item below.
All edits are outside the manuscript docx; nothing was rebuilt.

## F3 — SWIM_NARRATIVE.md, (k4) rating block added
- Before: 22 `^Rating:` blocks (9 Low + 13 Very low); `k4` appeared only in the publication-bias list.
- After: 23 blocks — inserted the (k4) block after (k3):
  "**(k4) The EA-2024-DV genotype (single study).** Rating: Very low – downgraded for imprecision;
  place of reassortment not shown (STU-039)."
- Check: `grep '^Rating:'` = 23 (verified by script). Matches manuscript Table 6 (9 Low + 14 Very low + 1 not gradable).
- No completion-count sentence added: no ratings summary exists in the narrative; nothing was invented.

## F4 — extraction/BATCH_BRIEF.md, per-report `access` semantics documented
- Before: the field was undocumented, leading to a spurious "7 vs 4 abstract-only" discrepancy.
- After: added the note: `reports_used[].access` is per report; abstract-only studies are
  STU-015, STU-025, STU-027, STU-029; STU-014, STU-022, STU-028 have both a full-text and an
  abstract-level report and are not abstract-only.
- Check: all seven study→report mappings re-verified against `consensus_all.json` (0 differences).

## F2 — orientation docs refreshed (dated, historical text kept)
- `Workbench/00_INDEX.md`: current-status block now carries the register numbers
  (2,105 = 1,768 + 325 [123/114/88] + 12) and the two-stage flow; the 20 Sep paragraph is
  marked historical.
- `README.md`: new "Current state — 9 October 2026" block; source-of-truth corrected to
  `Avian_review_paper_submission_ready.docx`; repository-map rows updated; "Superseded" notes on
  the 20 Sep state and Resume-order sections; stale "no GitHub remote" line replaced with the
  actual `origin`.
- `FILE_INVENTORY.md`: dated update note pointing to the current state; historical inventory kept.

## F8 — engineering hygiene
- `synthesis/run_all.py`: added `assert cov["n_studies"] == 110` before the final print, so the
  driver fails loudly if coverage changes.
- `synthesis/syn_common.py`: absolute roots now resolve as env var first
  (`AIV_RETRIEVAL_ROOT`, `AIV_REPO_ROOT`), then the recorded literal path, else `SystemExit` with
  a clear message. Check: module imports cleanly; `REGISTER.exists()` True; grep shows no other
  hard-coded roots in `synthesis/*.py`.
- `synthesis/run_manifest.json`: created — `git_head` `1a17393…`, Python 3.14.4, sha256 of the ten
  synthesis outputs (t1–t5, s5, tables, coverage, sensitivity, occurrence) and a note that the
  outputs predate the manifest and are unchanged by it.
- `human_check/README.md`: created — handling rules (public vs key vs author-run files; the
  author run is a calibration pilot only).

## Not applied (needs a writer and/or is queued)
- F1 was already applied by the main session earlier today (file 56 status/counts) — see file 15.

## Verification performed
- `python` checks above, run by the main session on 2026-10-09 from the working tree.
- `git status` in the repo: expected modified files only (no accidental writes).
