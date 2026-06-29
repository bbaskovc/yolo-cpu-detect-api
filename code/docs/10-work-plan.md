# Work Plan and PR Sequence

The initial repository baseline is deliberately established outside a PR because it is the project constitution and planned contract. All subsequent code changes use PR-sized work orders.

| Order | PR title | Goal | Must not include | Evidence required |
|---:|---|---|---|---|
| 001 | `build(repo): establish implementation baseline` | Add package/tooling baseline after owner imports initial repository. | API server, detector, model. | Repository validation, formatting/lint/type/test configuration passing. |
| 002 | `feat(api): add safe app skeleton and auth` | Implement FastAPI skeleton, config validation, health endpoints, request IDs, bearer auth, safe logging. | Image decode, OpenAI adapter, inference. | Auth and redaction tests; startup/readiness tests. |
| 003 | `feat(api): add OpenAI model and request adapters` | Implement `/v1/models`, Responses adapter, Chat Completions adapter, errors, and unsupported-feature policy using a fake detector. | Real image decoder/model. | Contract tests and OpenAI SDK smoke tests. |
| 004 | `feat(image): add Base64 image validation` | Parse data URLs, apply byte/MIME/pixel limits, decode safely in memory. | ONNX inference. | Malformed/oversized/remote/multiple image tests. |
| 005 | `decision(model): approve detector artifact` | Record model selection, license, source, export process, labels, checksums, and validation fixtures. | API behavior change. | Owner-approved decision record. |
| 006 | `feat(inference): add ONNX CPU detector` | Implement detector interface, ONNX CPU adapter, preprocessing, postprocessing, NMS, class map. | New endpoints, tracking, segmentation. | CPU-only integration tests and model fixture evidence. |
| 007 | `feat(runtime): add bounded inference concurrency` | Add semaphore, busy response, resource/health behavior, container/deployment artifact. | Queue, persistence, worker. | Busy/overload tests, CPU-only container proof. |
| 008 | `docs(release): add benchmark and release evidence` | Run benchmark, validate docs/runbook, prepare release decision. | New features. | Benchmark report, security/compatibility/test evidence. |

## Work-order rule

Every PR starts from [`templates/work-order.md`](templates/work-order.md). The strategic layer updates only the narrow work order required by the next row.
