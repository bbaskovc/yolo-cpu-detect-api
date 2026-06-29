# Agent Constitution — yolo-cpu-detect-api

## 1. Mission

Build a secure, CPU-only HTTP service that performs **one-shot object detection on exactly one image** supplied through a deliberately constrained, OpenAI-compatible API subset.

The project is an object detector, not a general-purpose model-serving platform. It must return bounding boxes, class labels, class IDs, and confidence scores for one image per synchronous request.

## 2. Product invariants

These rules are non-negotiable unless the human project owner changes this constitution explicitly.

1. One request processes exactly one image.
2. Processing is synchronous and stateless: the response is returned in the original request lifecycle.
3. The service performs object detection only.
4. Production inference is CPU-only. Do not add CUDA, TensorRT, GPU execution providers, GPU containers, or a GPU fallback.
5. API access requires `Authorization: Bearer <fixed-key>`.
6. The input image is accepted only as a Base64 data URL in an OpenAI-style image item.
7. Raw image bytes, Base64 image strings, bearer tokens, secret values, and model credentials must never be committed, logged, emitted in errors, placed in fixtures, or sent to telemetry.
8. Remote image URLs, OpenAI file IDs, multipart image uploads, and filesystem paths supplied by clients are rejected.
9. Model weights are deploy-time artifacts, excluded from Git, pinned by checksum, and never downloaded during an API request.
10. The API contract, detection-result schema, class mapping, preprocessing policy, and model ID are versioned.
11. Documentation may not claim compatibility, safety, accuracy, capacity, latency, or production readiness without test or benchmark evidence.

## 3. Explicit non-goals

The following are forbidden in Release 0 and must not be introduced as an incidental “improvement”:

- Object tracking, temporal IDs, re-identification, or video processing.
- Segmentation, masks, polygons, keypoints, pose, OCR, classification-only endpoints, or annotated-image output.
- Background jobs, queues, workers, polling, callbacks, persistence, databases, caching, stored requests, or stored artifacts.
- Multiple images per request, batch processing, streaming, WebSockets, server-sent events, or realtime sessions.
- User accounts, per-user keys, API-key management UI, billing, quotas by user, or tenant separation.
- Remote image URL downloading, URL allowlists, file-ID retrieval, or multipart uploads.
- Full OpenAI API emulation.
- Automatic model download, custom model training, model-selection UI, or unreviewed model replacement.
- Kubernetes, distributed processing, or generalized model serving.

## 4. Compatibility scope

The service is **OpenAI-compatible by selected client contract**, not by semantic equivalence to a language model.

Supported endpoints:

- `GET /v1/models`
- `GET /v1/models/{model_id}`
- `POST /v1/responses` — primary interface
- `POST /v1/chat/completions` — limited image-input compatibility interface
- `GET /healthz` — unauthenticated liveness endpoint
- `GET /readyz` — unauthenticated readiness endpoint

The service must accept exactly one Base64 data URL using:

- Responses: `input_image.image_url`
- Chat Completions: `image_url.url`

The service may accept `input_text` or `text` only for client-shape compatibility and must ignore it for detection behavior. It must reject unsupported features explicitly instead of silently ignoring them when their use could mislead the client.

Unsupported: `store=true`, `stream=true`, `background=true`, response retrieval/cancellation/deletion, conversations, tools/function calls, files, batches, and all non-listed endpoints.

## 5. Required architecture

Use a deliberately small architecture:

- Python 3.11+.
- FastAPI application layer, introduced only in the API-skeleton work order.
- ONNX Runtime CPU execution provider for production inference, introduced only after the model/license decision gate.
- One process by default with a bounded active-inference semaphore; no queue.
- In-memory image decoding. Avoid files; where a library forces a temporary file, delete it in a `finally` path and document why.
- Detector abstraction so API code does not depend on a particular YOLO package.
- Model and label artifacts supplied by explicit deployment paths and checksums.
- Structured, redacted logs with a request ID but no request payload recording.

Do not implement production inference before the project owner approves the exact model weights, their license, the class map, the ONNX export provenance, and the checksum policy.

## 6. Security rules

- Read the fixed bearer key only from a runtime secret such as `YOLO_API_KEY`.
- Use constant-time secret comparison.
- Reject missing, malformed, and invalid bearer authorization.
- Cap encoded body size before full Base64 decode.
- Validate the data URL prefix and media-type allowlist before decode.
- Enforce decoded-byte, width, height, and pixel-count limits after decode.
- Configure image decoding defensively against malformed and decompression-bomb-style images.
- Never fetch client-provided URLs.
- Never log `Authorization`, body content, Base64 data, image metadata beyond safe dimensions, or model-path secrets.
- Add request ID to all success and error responses.
- Treat model weights and third-party model licenses as supply-chain inputs requiring review.

## 7. Testing rules

Every PR must add or update tests that prove its changed behavior. Tests are evidence, not decoration.

Required eventual test layers:

- Unit tests: configuration, authentication, request IDs, data URL parser, image validation, output schemas, NMS, coordinate invariants.
- Contract tests: supported OpenAI response and error envelopes; unsupported feature rejection.
- SDK smoke tests: OpenAI Python SDK with a configured `base_url` against both supported request styles.
- Integration tests: fixture image through the HTTP API to stable structured detections.
- Security tests: invalid key, malformed headers, invalid Base64, bad image, unsupported MIME, remote URL, file ID, multiple images, body/byte/pixel limit, and busy-service rejection.
- Operational tests: CPU-only container startup, readiness behavior, model-load failure behavior.
- Benchmark harness: reproducible cold/warm latency and memory measurements on the target CPU.

Never describe a skipped test as passed. Do not weaken assertions simply to make CI green.

## 8. Work-order discipline

The execution agent receives one PR-sized work order at a time. A work order must state:

- verified current state;
- exact goal;
- constraints and explicit non-goals;
- relevant files/areas;
- required behavior;
- tests to add or run;
- documentation updates;
- permitted dependency or local-environment changes;
- branch/commit instructions;
- required executor report.

Before editing, inspect the current repository state and this constitution. Do not modify unrelated files. Do not refactor adjacent code unless explicitly in scope.

## 9. Execution environment

Execution may happen with broad permissions only inside a disposable, rebuildable VM, container, or devcontainer that contains no production secrets, irreplaceable state, personal data, or uncommitted project truth.

The agent may install development dependencies and local test tooling inside that boundary when the work order allows it. It must not ask the human to perform ordinary dependency installation or command execution that can safely happen in that boundary.

Remote Git branches, pull requests, CI logs, docs, decision records, and release evidence are the durable project truth.

## 10. Definition of done

A change is complete only when all applicable conditions hold:

1. It satisfies the bounded work order and preserves every product invariant.
2. It does not add any explicit non-goal.
3. Required tests pass and skipped checks are stated honestly.
4. Documentation and examples match the actual behavior.
5. No raw image, model weight, secret, generated artifact, or unrelated change is committed.
6. Static checks and project validation pass.
7. The executor returns the required final report.
8. The human project owner, guided by strategic review, decides whether to merge or release.

## 11. Required executor report

Use `docs/templates/executor-report.md` and include:

- summary of completed work;
- changed files and why;
- commands run and outcomes;
- tests and evidence;
- skipped/unavailable checks;
- compatibility impact;
- security and privacy impact;
- dependency and license impact;
- risks, uncertainties, and recommended next work;
- confirmation that no non-goal was added.
