# Operations Runbook

## Scope

This runbook defines the intended operational behavior after the API and detector are implemented. It does not imply that deployment artifacts exist in the initial repository.

## Startup expectations

1. Runtime configuration is present and valid.
2. API key is available as a server-side secret.
3. Model path, label map path, and checksums are configured.
4. Model artifact integrity is verified before readiness becomes healthy.
5. CPU execution provider is selected explicitly.
6. `/healthz` becomes healthy when process initialization completes.
7. `/readyz` becomes healthy only after detector readiness passes.

## Common operational states

| Symptom | Likely status | Response |
|---|---|---|
| Process is reachable but model missing | `healthz` healthy, `readyz` unhealthy | Check configuration, model mount, checksum, and logs without exposing secrets. |
| Invalid API key | `401 invalid_api_key` | Confirm server-side client configuration; do not log the supplied key. |
| Request image too large | `413 image_too_large` | Client reduces encoded bytes or image dimensions; do not raise limits without resource review. |
| Unsupported image URL | `400 invalid_image_input` | Client must embed Base64 data URL; remote fetch remains forbidden. |
| Service busy | `429 server_busy` | Client retries with bounded backoff; do not queue server-side work. |
| Inference failure | `500 inference_error` | Correlate request ID with sanitized logs; validate model and runtime health. |

## Secret rotation

1. Create a new server-side secret.
2. Update approved deployment secret configuration.
3. Restart/roll service according to deployment policy.
4. Update authorized clients through secure configuration.
5. Verify old secret no longer works.
6. Confirm logs did not expose either secret.

## Incident evidence

Capture only safe evidence: request IDs, timestamps, endpoint, status/error code, sanitized stack location, deployment revision, and model ID/checksum. Never capture images, Base64 strings, bearer tokens, or full request bodies.
