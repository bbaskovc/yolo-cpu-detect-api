# Release Readiness Checklist

A release decision is evidence-based. A checkbox marked “not applicable” must include a rationale.

## Product and scope

- [ ] Implemented behavior matches the approved product requirements.
- [ ] No tracking, video, segmentation, masks, queue, persistence, remote URL, multipart upload, or GPU dependency exists.
- [ ] Supported OpenAI-compatible endpoint subset is documented exactly.
- [ ] Unsupported features fail explicitly and are documented.

## API and compatibility

- [ ] `/v1/models` and `/v1/models/{id}` contract tests pass.
- [ ] `/v1/responses` Base64 image contract test passes.
- [ ] `/v1/chat/completions` Base64 image compatibility test passes.
- [ ] OpenAI Python SDK smoke tests pass with local `base_url`.
- [ ] Error envelopes and request IDs are tested.
- [ ] No false usage/token accounting is returned.

## Detection and model

- [ ] Approved model/label artifact provenance is recorded.
- [ ] Model and label checksums are verified.
- [ ] Model license and intended deployment use were reviewed.
- [ ] Golden/fixture detection tests pass with documented tolerances.
- [ ] Bounding-box invariants and NMS behavior are tested.

## Security and privacy

- [ ] API key handling and redaction tests pass.
- [ ] Image payload/URL/file-ID rejection tests pass.
- [ ] Request/decoded-image/dimension/pixel limit tests pass.
- [ ] No image persistence path exists by default.
- [ ] Secret scan is clean.
- [ ] Dependency/model supply-chain review is complete.
- [ ] Deployment TLS/network exposure configuration is reviewed.

## Operations and performance

- [ ] CPU-only deployment starts successfully on target class hardware.
- [ ] `/healthz` and `/readyz` behavior is tested.
- [ ] Busy overload produces rejection rather than a queue.
- [ ] Benchmark report covers target CPU, configuration, p50/p95 latency, memory, and overload behavior.
- [ ] Runbook and `.env.example` match actual deployment behavior.

## Governance

- [ ] Change log is updated.
- [ ] Executor reports are archived with PR evidence.
- [ ] Known limitations and validation debt are stated plainly.
- [ ] Human owner reviewed the release decision brief and approved the release.
