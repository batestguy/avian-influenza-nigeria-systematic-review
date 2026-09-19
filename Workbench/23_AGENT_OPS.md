# Agent operating procedure — systematic review tasks

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
