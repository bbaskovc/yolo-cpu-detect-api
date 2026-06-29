# Decision Log

Architecture decisions are durable project memory. Do not replace an approved decision silently; supersede it with a new dated decision entry.

## ADR-001 — Single-image CPU object detection

- **Status:** Accepted
- **Date:** 2026-06-29
- **Decision:** Build CPU-only, synchronous, one-image object detection.
- **Consequences:** No GPU runtime, video, tracking, background jobs, or persistent state in Release 0.

## ADR-002 — OpenAI-compatible subset

- **Status:** Accepted
- **Date:** 2026-06-29
- **Decision:** Support a limited `/v1` contract with bearer authentication, model listing, Responses image input, and Chat Completions image-input compatibility.
- **Consequences:** The service remains compatible with selected client conventions but does not claim full OpenAI API equivalence.

## ADR-003 — Base64 data URLs only

- **Status:** Accepted
- **Date:** 2026-06-29
- **Decision:** Accept exactly one Base64 data URL image per request.
- **Consequences:** No multipart upload, remote URLs, Files API, or file IDs. This avoids storage and SSRF scope in Release 0.

## ADR-004 — Stateless synchronous service

- **Status:** Accepted
- **Date:** 2026-06-29
- **Decision:** Process inference in the HTTP request lifecycle with bounded active concurrency and no queue.
- **Consequences:** Busy requests receive an explicit error; no job polling or artifact retrieval is required.

## ADR-005 — ONNX Runtime CPU target

- **Status:** Proposed, pending exact model approval
- **Date:** 2026-06-29
- **Decision:** Use ONNX Runtime CPU execution provider as the intended production inference runtime.
- **Consequences:** Exact model/export, license, checksum, labels, and target CPU benchmark remain approval gates.
