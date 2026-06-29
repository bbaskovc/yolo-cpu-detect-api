# OpenAI Compatibility Contract

## Compatibility principle

This service implements a narrow local object-detection contract using selected OpenAI request and response conventions. It is not a language model and does not claim full OpenAI API coverage.

The purpose is client interoperability where it is meaningful:

- `/v1` base path;
- bearer authentication;
- model-list endpoints;
- Responses image input shape;
- Chat Completions image input shape;
- familiar response object/error envelope patterns;
- request IDs.

## Endpoint matrix

| Endpoint | Status | Release 0 behavior |
|---|---|---|
| `GET /v1/models` | Supported | Lists the local detector model. |
| `GET /v1/models/{model_id}` | Supported | Returns a local model descriptor or model-not-found error. |
| `POST /v1/responses` | Supported | Primary one-image detection endpoint. |
| `POST /v1/chat/completions` | Supported | Limited adapter for `image_url` clients. |
| `GET /healthz` | Extension | Liveness; no auth; no model-load requirement. |
| `GET /readyz` | Extension | Readiness; no auth; model must be usable. |
| All other `/v1/*` endpoints | Unsupported | Return OpenAI-style unsupported endpoint/error response. |

## Primary Responses request

```json
{
  "model": "yolo-cpu-detect-v1",
  "input": [
    {
      "role": "user",
      "content": [
        {
          "type": "input_image",
          "image_url": "data:image/jpeg;base64,<BASE64_IMAGE>"
        }
      ]
    }
  ],
  "store": false
}
```

### Responses policy

| Field | Policy |
|---|---|
| `model` | Required; must name a local detector. |
| `input` | Required; exactly one image item across all content. |
| `input_image.image_url` | Required image transport; Base64 data URL only. |
| `input_text` | Accepted but ignored for detection semantics. |
| `store` | Omitted or `false` only. `true` rejected. |
| `stream` | Omitted or `false` only. `true` rejected. |
| `background` | Omitted or `false` only. `true` rejected. |
| `tools`, `tool_choice` | Rejected as unsupported. |
| `conversation`, `previous_response_id` | Rejected as unsupported. |
| `metadata` | May be accepted as non-persisted opaque request metadata; not logged. |

## Chat Completions compatibility request

```json
{
  "model": "yolo-cpu-detect-v1",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64,<BASE64_IMAGE>"
          }
        }
      ]
    }
  ],
  "stream": false
}
```

### Chat Completions policy

| Field | Policy |
|---|---|
| `model` | Required local detector ID. |
| `messages` | Required; must contain exactly one supported Base64 image item overall. |
| `image_url.url` | Base64 data URL only. |
| text content | Accepted but ignored for detection semantics. |
| `stream` | Omitted or `false` only. `true` rejected. |
| `tools`, `response_format`, audio, reasoning fields | Rejected as unsupported. |

## Output policy

The canonical detection result is a JSON document encoded in:

- Responses: `output[0].content[0].text` with `type: output_text`.
- Chat Completions: `choices[0].message.content`.

This preserves a machine-readable response that common OpenAI client code can retrieve without the service inventing unsupported proprietary top-level fields.

See [`05-api-contract.md`](05-api-contract.md) for exact schemas.

## SDK smoke-test intent

The project will test a configured OpenAI Python SDK client using a local `base_url`. The test is evidence of the documented compatible subset only; it is not evidence of full SDK or full API feature support.
