# Test and Validation Strategy

## Principle

A claim is only as strong as the evidence attached to it. Green CI is not sufficient if it does not exercise the changed risk.

## Test pyramid

### Unit tests

- configuration parsing and invalid configuration;
- bearer-header parsing and constant-time comparison wrapper behavior;
- request ID generation/propagation;
- Base64 data URL parsing;
- MIME allowlist;
- body/byte/dimension/pixel validation;
- canonical detection schema validation;
- coordinate clamping and ordering;
- NMS behavior;
- error serialization.

### Contract tests

- `/v1/models` and `/v1/models/{model_id}` shapes;
- `/v1/responses` supported image request;
- `/v1/chat/completions` supported image request;
- success envelopes;
- all documented error envelopes;
- unsupported streaming/background/storage/tool/conversation behavior.

### Integration tests

- one valid fixture image travels through HTTP request parsing, safe decode, a deterministic detector fixture/double, serialization, and response parsing;
- after model approval, approved fixture images execute real ONNX CPU inference under controlled tolerances.

### Security tests

- absent/wrong/malformed bearer key;
- malformed/empty Base64;
- remote URL and file ID rejection;
- unsupported type;
- corrupted image;
- multiple images;
- oversized body, bytes, side, and pixels;
- busy semaphore behavior;
- log capture proving no secret/payload leakage.

### SDK interoperability tests

A test configures the OpenAI Python SDK with the local `base_url` and calls both documented endpoint subsets. The assertions cover only the explicitly documented compatibility subset.

## Fixture policy

- Fixtures must be small, lawful, non-sensitive, and documented.
- No real customer/user images.
- Binary image fixtures require provenance and must be intentionally included rather than casually copied.
- Synthetic images are preferred for parser/limit tests.
- Golden detection fixtures must record model ID, preprocessing, label map, output tolerance, and reason for change.

## Validation debt

Skipped tests, unavailable hardware, missing model artifact, or unrun benchmark are reported as open validation debt. They are never converted into a passing conclusion.
