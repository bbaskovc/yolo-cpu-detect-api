# yolo-cpu-detect-api

A CPU-only, synchronous, single-image object-detection service with a deliberately constrained OpenAI-compatible HTTP API.

> **Repository state:** architecture and governance baseline only. No detector, API server, model weights, or production deployment is implemented in this initial package.

## What this project will do

- Receive exactly one image encoded as a Base64 data URL.
- Authenticate with one server-side fixed bearer API key.
- Perform one CPU YOLO-family object-detection inference.
- Return bounding boxes, labels, class IDs, and confidence scores as JSON inside OpenAI-style response envelopes.
- Support a selected subset of `/v1/models`, `/v1/responses`, and `/v1/chat/completions`.

## What it will not do

- Tracking, video, segmentation, masks, polygons, keypoints, or annotated-image output.
- Background work, job queues, polling, databases, persistence, stored images, or stored outputs.
- Remote URL fetching, OpenAI Files API compatibility, or multipart uploads.
- GPU or CUDA inference.
- Full OpenAI API emulation.

See [`docs/01-product-requirements.md`](docs/01-product-requirements.md) and [`docs/02-non-goals.md`](docs/02-non-goals.md).

## Start here

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Binding rules for coding agents and contributors |
| [`docs/00-project-charter.md`](docs/00-project-charter.md) | Mission, success criteria, governance |
| [`docs/03-architecture.md`](docs/03-architecture.md) | Target architecture and trust boundaries |
| [`docs/04-openai-compatibility.md`](docs/04-openai-compatibility.md) | Supported API subset and compatibility matrix |
| [`docs/05-api-contract.md`](docs/05-api-contract.md) | Input, output, errors, and schema policy |
| [`docs/06-security.md`](docs/06-security.md) | Security and privacy requirements |
| [`docs/10-work-plan.md`](docs/10-work-plan.md) | Ordered PR-sized implementation sequence |

## Repository layout

```text
.
├── AGENTS.md                         # Binding agent constitution
├── CLAUDE.md                         # Equivalent constitution for Claude Code
├── docs/                             # Product, architecture, API, security, evidence
├── examples/                         # Contract examples; no real images or secrets
├── models/                           # Documentation only; weights must not be committed
├── scripts/                          # Validation and later benchmark helpers
├── src/yolo_cpu_detect_api/          # Package skeleton; no detector implemented yet
├── tests/                            # Contract, integration, security, and fixture structure
└── .github/                          # CI, issue forms, PR template, Dependabot
```

## Initial verification

This baseline intentionally validates repository governance before product code exists.

```bash
python scripts/verify_initial_repository.py
python -m compileall -q src
```

After creating a virtual environment and installing development dependencies:

```bash
python -m pip install -e ".[dev]"
make check
```

## OpenAI-compatible client shape

The final service will accept a Base64 data URL supplied through the current OpenAI image-input conventions. The primary interface is `POST /v1/responses` with `input_image.image_url`; a limited `POST /v1/chat/completions` adapter accepts `image_url.url`.

The service does **not** claim OpenAI model equivalence. It is a local detector that intentionally adopts a limited OpenAI-style transport, authentication, endpoint, object, and error contract.

See [`docs/04-openai-compatibility.md`](docs/04-openai-compatibility.md) and [`docs/15-references.md`](docs/15-references.md).

## License status

No software license is granted by this starter repository until the project owner selects one. See [`LICENSE-STATUS.md`](LICENSE-STATUS.md) and [`docs/13-licensing-and-model-policy.md`](docs/13-licensing-and-model-policy.md).
