# Product Requirements

## Functional requirements

| ID | Requirement |
|---|---|
| FR-001 | Accept exactly one image per request. |
| FR-002 | Accept image content only as a Base64 data URL. |
| FR-003 | Support `image/jpeg`, `image/png`, and `image/webp` in Release 0. |
| FR-004 | Authenticate each API request with one fixed bearer API key. |
| FR-005 | Provide `GET /v1/models` and `GET /v1/models/{model_id}` for local model discovery. |
| FR-006 | Provide `POST /v1/responses` as the primary image-detection interface. |
| FR-007 | Provide limited `POST /v1/chat/completions` compatibility for vision clients. |
| FR-008 | Return image width, image height, class ID, class name, confidence, and bounding box for each detection. |
| FR-009 | Return detections in a documented, schema-versioned JSON payload. |
| FR-010 | Return OpenAI-style error envelopes and request IDs. |
| FR-011 | Reject unsupported OpenAI features explicitly. |
| FR-012 | Run inference synchronously in the request lifecycle. |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-001 | Production inference must execute without GPU dependencies. |
| NFR-002 | Raw request images and API keys must not be persisted or logged. |
| NFR-003 | Input must be bounded by request bytes, decoded bytes, dimensions, and total pixel count. |
| NFR-004 | Default operation must have no database, job queue, or worker process. |
| NFR-005 | Public compatibility claims must match contract tests. |
| NFR-006 | Public latency and capacity claims must match reproducible benchmarks. |
| NFR-007 | Model artifacts must have approved provenance, license review, and checksums. |
| NFR-008 | The API must fail closed for invalid authentication and unsupported input modes. |

## Detection-result requirements

- Bounding box convention: `bbox_xyxy = [x_min, y_min, x_max, y_max]` in original-image pixel coordinates.
- Coordinates are clamped to image bounds.
- `x_max > x_min` and `y_max > y_min`.
- Confidence is a number in `[0.0, 1.0]`.
- Results are sorted by descending confidence after non-maximum suppression.
- No temporal data, masks, polygons, keypoints, or track IDs are present.

## Deferred product decisions

The following require explicit owner approval before implementation:

- exact YOLO-family model and version;
- model/license provenance;
- supported class set and label map;
- model input size and preprocessing;
- calibrated confidence/NMS thresholds;
- target CPU architecture and performance target;
- container/base image policy;
- public exposure model and reverse-proxy/TLS configuration.
