# Agent operating procedure — systematic review tasks

**Current workflow (9 October 2026).** Supersedes the gate text further below, which is kept as historical.

- **Roles.** An *executor* agent does each work unit; a fresh, independent *reviewer* agent checks it before anything is reported; the main session adjudicates and is the only writer of the `.docx` and of the register (file 56). Agents return JSON/text; the main session integrates it into Workbench files.
- **Fan-out.** At most 3 agents at once. Agents save after each unit; before relaunching, check for partial outputs and reuse them.
- **Work queues.** W1–W9 in file 59; its progress log is the session record. Startable without further author decisions: W1 (all sources except Scopus/ScienceDirect), W2, the W4 open-route re-sweep, W5, W8 preparation.
- **Author gate.** Yes/no questions, one at a time, recommended option first; log every answer in file 15. Never enter a decision the author has not given; never invent a human check.
- **Boundaries.** Legal retrieval routes only; one attempt per bot gate, never retried or auto-passed; no author contact unless D3 is approved; commit only when the author asks.
- **Verification habits.** Number checks by script (counts reconcile; `run_all.py` assertions pass; `verify.py` PASS); every claim cites file/row; disagreements adjudicated against the source text.
- **Blind spots to preserve.** Appraisers and the W9 re-scorer must not read file 59 (targets) or file 57 (baseline); the W6 `sample_key.json` is never published; the author's 8 Oct page run is a calibration pilot only, never the independent check.

---

## Historical — gate text as at 2026-09-20 (superseded)

**Current gate (2026-09-20):** AJOL import/canonical matching is complete and Gate C screening
reconciliation is initialized in `56_SCREENING_RECONCILIATION.json`. Agents may perform title/abstract
verification only through that register. They must not start extraction or RoB, and all prior screening
votes remain provisional until independently verified and adjudicated.

## Which agent for what (this repo has no code)

- `general` — screening votes, extraction, RoB pre-reads, synthesis drafting. Only type used for review tasks.
- `explore` — repo/file discovery only. Not for literature judgments.
- `data-explorer` / `ml-builder` / `ship-reviewer` — NOT used (no datasets, no models, no code diffs here).

## Rules (enforced)

1. **Batches of ~5 papers**, max 3 subagents per turn, rounds sequential. Subagents get pure text (titles/abstracts or pasted excerpts) — never ask them to re-run database searches.
2. **Blinded independence:** same batch goes to 2 agents without seeing each other's output when a decision matters (screening include/exclude, outcome extraction). Conflicts resolved by main session or arbiter, logged.
3. **Self-contained prompts:** subagents start with zero conversation context. Every dispatch includes: task, eligibility/form verbatim, papers as text, exact JSON schema, "JSON only" instruction.
4. **JSON-only returns:** strip `Task Succeeded. Result:` prefix before parsing. Failed/unparseable batch = logged, affected papers re-queued — never fail the whole run.
5. **Verification, not trust:** agent output is a pre-read. Main session spot-checks 20% + all includes + all excludes before freezing any table. Agent votes never enter T1–T7 directly.
6. **No manuscript writes by agents:** agents return JSON/text to main session. Only main session edits the `.docx` (paste-approved) or workbench logs.

## Prompt skeleton

Task, eligibility or form, papers, schema, "return JSON array only". See 24_AGENT_BATCH_SEED1 for the live pilot.
