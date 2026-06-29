# Project Charter

## Mission

Provide CPU-only, one-shot object detection for exactly one image through a secure, synchronous, OpenAI-compatible API subset.

## Problem statement

Consumers that already use OpenAI-style HTTP clients or SDK configuration should be able to send a Base64-encoded image to a local service using a familiar `/v1` base path and bearer authentication, then receive deterministic machine-readable detection results. The service must run on machines without a GPU.

## Intended users

- Internal services that need local object detection.
- Edge or offline-adjacent deployments without GPU hardware.
- Developers who want OpenAI-shaped client integration without deploying a general model-serving platform.

## Success criteria for Release 0

1. A client configured with an OpenAI SDK `base_url` can call the documented endpoint subset.
2. The service authenticates a fixed server-side bearer key without leaking it.
3. Exactly one Base64 image data URL is accepted and processed synchronously.
4. A CPU-only detector returns stable schema-versioned detections.
5. Input validation rejects unsafe or unsupported image forms.
6. Benchmark results on the actual target CPU support all public performance claims.
7. The project makes no false claim of full OpenAI API compatibility, tracking, segmentation, video support, or production-scale capacity.

## Governance

- Human owner: owns product intent, accepted risk, merges, and releases.
- Strategic layer: owns architecture synthesis, work-order creation, evidence review, handoffs, and readiness briefs.
- Execution agent: owns one bounded implementation task at a time inside a controlled environment.
- Durable truth: repository history, PRs, CI, docs, decisions, release evidence, and handoffs.

## Release vocabulary

| Label | Meaning |
|---|---|
| Draft | Documents or code are incomplete and unverified. |
| Prototype | Demonstrates a narrow behavior; no security or performance implication. |
| Alpha | Core path exists with known gaps; not for broad users. |
| Beta | Defined scope is test-backed, but operational and compatibility limits remain. |
| Release candidate | All stated release gates are passing; awaiting final approval. |
| Production-ready | Only after owner-approved release evidence supports the actual deployment context. |
