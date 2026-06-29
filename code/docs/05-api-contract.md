# API Contract

## Common HTTP rules

- Base path: `/v1` for OpenAI-compatible endpoints.
- Content type: `application/json`.
- Authentication: `Authorization: Bearer <YOLO_API_KEY>`.
- All responses include `x-request-id`.
- Input image content is never written to logs or responses.
- The service is synchronous and stateless.

## Model descriptor

```json
{
  "id": "yolo-cpu-detect-v1",
  "object": "model",
  "created": 0,
  "owned_by": "local"
}
```

`created` may be `0` until a project policy defines a stable model-artifact release timestamp. It must not claim an unknown upstream model creation date.

## Canonical detection result

```json
{
  "schema_version": "1.0",
  "model": "yolo-cpu-detect-v1",
  "image": {
    "width": 1920,
    "height": 1080
  },
  "detections": [
    {
      "class_id": 0,
      "class_name": "person",
      "confidence": 0.9421,
      "bbox_xyxy": [412, 96, 620, 704]
    }
  ]
}
```

### Field constraints

| Field | Constraint |
|---|---|
| `schema_version` | Semantic contract version, initially `1.0`. |
| `model` | Public local model ID used for this inference. |
| `image.width`, `image.height` | Positive original-image dimensions. |
| `class_id` | Non-negative integer valid for the approved label map. |
| `class_name` | Approved label-map string. |
| `confidence` | Finite number from 0.0 to 1.0 inclusive. |
| `bbox_xyxy` | Four integer pixels `[x_min, y_min, x_max, y_max]`. |

## Responses success envelope

```json
{
  "id": "resp_det_<opaque-id>",
  "object": "response",
  "created_at": 1782720000,
  "status": "completed",
  "model": "yolo-cpu-detect-v1",
  "output": [
    {
      "id": "msg_det_<opaque-id>",
      "type": "message",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "{...canonical detection JSON...}",
          "annotations": []
        }
      ]
    }
  ],
  "store": false,
  "usage": null
}
```

`usage` is `null` because no meaningful token accounting exists for this local detector. Do not fabricate token usage.

## Chat Completions success envelope

```json
{
  "id": "chatcmpl_det_<opaque-id>",
  "object": "chat.completion",
  "created": 1782720000,
  "model": "yolo-cpu-detect-v1",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{...canonical detection JSON...}"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": null
}
```

## Error envelope

```json
{
  "error": {
    "message": "Exactly one Base64 image is required.",
    "type": "invalid_request_error",
    "param": "input",
    "code": "invalid_image_input"
  }
}
```

| HTTP | Type | Code | Meaning |
|---:|---|---|---|
| 400 | `invalid_request_error` | `invalid_image_input` | Missing, multiple, malformed, remote, or otherwise invalid image input. |
| 400 | `invalid_request_error` | `unsupported_parameter` | A parameter requests unsupported behavior. |
| 401 | `authentication_error` | `invalid_api_key` | Bearer credential missing, malformed, or wrong. |
| 404 | `invalid_request_error` | `model_not_found` | Requested model is not present. |
| 413 | `invalid_request_error` | `image_too_large` | Encoded/request/decoded/pixel limit exceeded. |
| 415 | `invalid_request_error` | `unsupported_image_type` | Data URL media type is outside allowlist. |
| 422 | `invalid_request_error` | `invalid_image_data` | Decoding failed or decoded image violates safety rules. |
| 429 | `rate_limit_error` | `server_busy` | No active inference slot is available. |
| 500 | `server_error` | `inference_error` | Detector or runtime failure. |
| 503 | `server_error` | `model_not_ready` | Model unavailable or failed readiness validation. |

## Health endpoints

| Endpoint | Auth | Meaning |
|---|---|---|
| `GET /healthz` | No | Process is alive. It must not imply model readiness. |
| `GET /readyz` | No | Detector configuration and model are ready to serve. |
