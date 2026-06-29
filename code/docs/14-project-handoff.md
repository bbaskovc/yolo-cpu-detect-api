# Project Handoff

Update this document after every merged PR or strategic review so a new strategic session can reconstruct the project without relying on chat history.

## Current truth

- Default branch state: Initial repository baseline only.
- Open PRs: None.
- Recently merged PRs: None.
- CI status: Not yet connected to a remote repository.
- Current model artifact: Not selected.
- Current API implementation: Not implemented.

## Product goal

CPU-only, synchronous object detection for exactly one Base64 data URL image through a constrained OpenAI-compatible API subset.

## Implemented

- Product constitution in `AGENTS.md` and equivalent `CLAUDE.md`.
- Requirements, non-goals, architecture, compatibility, API, security, testing, benchmark, release, and model-policy documents.
- Empty source/test structure and initial quality configuration.

## Missing

- Remote Git repository and protected-branch configuration.
- Actual Python runtime dependencies and lockfile.
- FastAPI app/auth implementation.
- Image validation implementation.
- Model selection and license approval.
- ONNX detector implementation.
- Docker/deployment assets.
- Test fixtures, benchmarks, release evidence.

## Non-negotiable rules

- No tracking, video, segmentation, queue, persistence, remote URL, multipart upload, or GPU dependency.
- One Base64 image per synchronous request.
- Fixed bearer API key from server-side configuration only.
- No logging/persisting images or secrets.
- Explicit OpenAI compatibility subset only.

## Next recommended work

After importing this baseline into the new repository, create the first implementation work order for `PR-001: build(repo): establish implementation baseline` from `docs/10-work-plan.md`.

## Do not do next

- Do not start detector/model implementation before model/license approval.
- Do not add FastAPI or ONNX Runtime merely because the architecture names them; the next work order must define exact dependency versions and validation.
- Do not expand compatibility endpoints before primary contract tests exist.
