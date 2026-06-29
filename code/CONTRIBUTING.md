# Contributing

## Operating model

This repository uses a strategic-control-plane workflow:

- The human project owner owns product intent, risk acceptance, merge decisions, and release decisions.
- The strategic agent turns goals into architecture, narrow work orders, review questions, and evidence summaries.
- The execution agent implements one bounded work order at a time in a rebuildable environment.

`AGENTS.md` and `CLAUDE.md` are binding repository instructions. Read them before proposing or making a change.

## Contribution rules

1. Work only on an approved, PR-sized work order.
2. Start from a clean, current branch and report any existing uncommitted state.
3. Preserve product invariants and explicit non-goals.
4. Add or update evidence-producing tests for changed behavior.
5. Keep documentation synchronized with behavior and compatibility claims.
6. Do not commit image data, model weights, API keys, `.env` files, generated artifacts, or benchmark output with sensitive host information.
7. Do not merge directly to the protected default branch.
8. Complete the executor report template before requesting review.

## Local checks

```bash
python scripts/verify_initial_repository.py
python -m compileall -q src
make check
```

## Commit convention

Use Conventional Commits:

```text
feat(api): add OpenAI responses request adapter
fix(image): reject malformed data URL
security(auth): redact authorization header
build(ci): add repository validation job
docs(contract): clarify unsupported streaming behavior
test(api): cover invalid model error envelope
```

## Pull request standards

A PR must contain:

- a bounded problem statement;
- explicit non-goals;
- implementation summary;
- tests and evidence;
- compatibility impact;
- security/privacy impact;
- documentation changes;
- known limitations and follow-up work.

Use the repository PR template and `docs/templates/executor-report.md`.
