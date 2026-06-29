# Deployment

Deployment artifacts are intentionally deferred until the API skeleton, authentication, image safety behavior, model policy, and CPU benchmark requirements have implementation evidence.

When deployment files are introduced, they must document:

- CPU-only runtime;
- non-root execution where practical;
- read-only application filesystem where practical;
- read-only model mount;
- server-side secret injection for `YOLO_API_KEY`;
- request and resource limits;
- private/TLS exposure policy;
- health and readiness endpoints;
- no writable persistent image or job storage.
