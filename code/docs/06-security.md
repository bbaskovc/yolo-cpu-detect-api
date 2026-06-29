# Security and Privacy Design

## Security objectives

1. Only holders of the configured server-side bearer secret may invoke inference.
2. Client image data does not persist after the request and does not enter logs.
3. The API never performs network fetches based on client input.
4. Malformed, oversized, or decompression-bomb-style images cannot consume unbounded memory or CPU.
5. Model artifacts and dependencies are controlled supply-chain inputs.
6. The service fails closed when auth, input validation, or model readiness fails.

## Authentication

- Header required: `Authorization: Bearer <fixed-key>`.
- Parse only the bearer scheme; reject alternative schemes.
- Normalize no secret material into error responses.
- Compare key material with a constant-time primitive.
- Read key from environment variable or container secret at startup.
- Do not permit a query parameter, request body field, or browser-visible key.
- Test invalid/missing/malformed credentials.

## Image input safety

### Accepted transport

Only `data:<allowed-mime>;base64,<payload>` is permitted.

### Rejections

- `http://`, `https://`, `file://`, `ftp://`, and custom schemes.
- OpenAI file IDs.
- Multipart requests.
- Multiple image items.
- Unsupported MIME prefix.
- Empty Base64 payload.
- Invalid Base64 alphabet/padding.
- Decoded bytes above the configured limit.
- Invalid decoder output.
- Width, height, or total pixels above configured limits.
- Animated/multi-frame formats unless explicitly added and tested later.

### Baseline defaults

| Limit | Baseline |
|---|---:|
| Encoded JSON request | 12 MiB |
| Decoded image source bytes | 8 MiB |
| Total pixels | 16,000,000 |
| Image side | 8,192 px |
| Active inferences per process | 1 |

These are initial policy values. They require performance and security validation before becoming a released capacity guarantee.

## Logging and observability

Allowed logs:

- request ID;
- endpoint;
- response status;
- safe elapsed time;
- safe image dimensions after validation;
- selected public model ID;
- error code without payload.

Forbidden logs:

- authorization header;
- API key or any secret;
- Base64 payload;
- image pixels, filenames, client-supplied URLs, or full request body;
- local model path if it exposes protected filesystem structure;
- raw exception trace if it may contain payload data.

## Model and dependency supply chain

- Pin Python dependencies with a lock strategy selected in an approved later work order.
- Record detector model provenance, exporter version, license, checksum, and label-map checksum.
- Do not download model weights in response to a request.
- Do not commit weights to Git.
- Scan dependencies and container images before release.

## Deployment hardening

- Deploy behind TLS when reachable outside a trusted network.
- Prefer non-root container user.
- Prefer read-only application filesystem.
- Mount model artifacts read-only.
- Set memory and CPU resource limits appropriate to the target host.
- Bind to private interfaces by default unless public exposure is explicitly approved.
- Place rate limiting at reverse proxy and/or application layer before public access.

## Security release gate

Release requires passing security tests, secret scan, dependency/model provenance review, image-limit validation, log redaction review, and deployment configuration review.
