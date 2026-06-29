# Benchmark Method

## Purpose

Measure the detector only on the actual intended CPU deployment class before publishing latency, throughput, resource, or “real-time” statements.

## Preconditions

- Approved ONNX model, checksum, labels, and preprocessing policy.
- Clean or documented target host.
- Fixed container/runtime version.
- Fixed `YOLO_CPU_THREADS` and `MAX_CONCURRENT_INFERENCES`.
- Representative, lawful, non-sensitive fixture images.
- No competing workload that would invalidate results.

## Required environment record

- CPU model and core/thread count;
- RAM capacity;
- operating system/kernel;
- container/base image digest;
- Python and ONNX Runtime versions;
- model ID, SHA-256, and input resolution;
- detector configuration and thresholds;
- concurrency setting.

## Measurements

| Metric | Requirement |
|---|---|
| Cold start | Time from process start to first completed successful detection. |
| Warm p50 / p95 | At least 30 measured requests after warm-up. |
| CPU utilization | Process/system context documented. |
| Peak memory | Maximum observed process resident memory. |
| Error rate | All failed requests classified. |
| Overload behavior | Confirm busy requests are rejected, not queued. |
| Image classes | Test at least small, medium, and near-limit images. |

## Reporting rules

- State exact conditions, not generic claims.
- Do not call the system “real-time” unless a defined input/resolution/CPU/SLO supports that statement.
- Do not compare to GPU performance unless methodology is explicit and the comparison is useful.
- Keep raw benchmark outputs out of Git unless sanitized and intentionally versioned.

## Acceptance output

Store a dated benchmark report outside Git or in a sanitised release evidence location. Link it in the release decision brief.
