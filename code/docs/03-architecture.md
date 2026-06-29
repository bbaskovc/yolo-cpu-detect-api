# Target Architecture

## Overview

```text
Client
  |
  | HTTPS, Authorization: Bearer <fixed key>
  | JSON: exactly one Base64 data URL
  v
Reverse proxy or private network boundary
  v
FastAPI application (single process by default)
  |- request ID middleware
  |- bearer authentication
  |- OpenAI Responses adapter
  |- OpenAI Chat Completions adapter
  |- request policy validation
  |- data URL parsing / safe in-memory decode
  |- active-inference semaphore
  |- detector interface
  |- ONNX Runtime CPU detector implementation
  |- post-processing / NMS / label mapping
  `- OpenAI-style response/error serializer
```

## Trust boundaries

| Boundary | Trust rule |
|---|---|
| Client to API | Client input is untrusted; bearer authentication is required. |
| Image payload | Treat as hostile binary input; validate, bound, decode defensively, discard after response. |
| API to detector | Detector receives a validated in-memory image representation only. |
| Model artifact | Deploy-time trusted artifact only after license, checksum, and provenance approval. |
| Runtime configuration | Server-owned secret/configuration; never returned to client. |
| Network | API never makes outbound fetches based on client input. |

## Component responsibilities

### API adapters

Translate supported OpenAI request shapes to one internal `DetectionRequest`. They must not know detector-specific preprocessing or YOLO package details.

### Request policy

Enforce exactly one image, reject unsupported modes, and normalize applicable request parameters.

### Image module

Parse `data:<mime>;base64,<data>`, validate the media type, limit encoded/decode size, decode safely, enforce dimensions/pixels, and return an in-memory image.

### Detector interface

A stable abstraction that accepts a validated image and returns internal detection records. The ONNX implementation is one adapter, not an API contract.

### Post-processing

Perform detection-output parsing, coordinate conversion, confidence filtering, class filtering, NMS, coordinate clamping, and deterministic sorting.

### Response serializer

Render the canonical detection JSON into OpenAI-style Responses or Chat Completions envelopes. It must never add invented token counts.

## Concurrency policy

Release 0 permits a bounded number of active synchronous inference executions, defaulting to one. When no inference slot is available, return an explicit `429` error. Do not queue, persist, or later resume work.

## No-database rationale

A one-shot synchronous request has no durable job or conversation state. Adding storage would create retention, cleanup, privacy, availability, and schema obligations without supporting the core product.
