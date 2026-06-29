# Explicit Non-Goals

The following are intentionally out of scope for Release 0. Any proposal to add one requires an architecture decision, changed security/test plan, and explicit human approval.

## Vision scope exclusions

- Object tracking, track IDs, trajectory calculation, temporal smoothing, re-identification.
- Video, camera, RTSP, webcam, uploaded movie, frame extraction, or frame batching.
- Segmentation, masks, polygon outlines, instance contours, panoptic segmentation.
- Pose, keypoints, landmarks, OCR, face recognition, face matching, age/gender inference, or biometric identification.
- Image annotation, annotated image download, image modification, or image generation.

## API and state exclusions

- Background jobs, queues, task workers, polling, callbacks, webhooks, response retrieval, cancellation, or deletion.
- Database, cache, request history, user history, artifact storage, image storage, or audit event database.
- Streaming, SSE, WebSockets, Realtime API, server-side conversation state.
- Multiple images per request, batch inference, multi-image comparison.
- Files API, file IDs, multipart upload, external URL fetch, and client filesystem paths.

## Platform exclusions

- GPU/CUDA/TensorRT paths.
- Auto-downloading or dynamic replacement of model artifacts.
- Multi-tenant authentication, API-key UI, billing, subscriptions, or user accounts.
- Kubernetes, distributed queues, horizontal scaling claims, generic inference gateway behavior.
- Full OpenAI API compatibility.

## Why these are excluded

Every excluded feature adds one or more distinct trust boundaries: storage retention, remote retrieval/SSRF, temporal identity, concurrent state, GPU runtime, billing/accountability, or complex OpenAI endpoint semantics. The first release must establish a provable, constrained core before any such expansion.
