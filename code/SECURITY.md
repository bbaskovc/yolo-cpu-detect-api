# Security Policy

## Scope

This policy covers the repository, released container images, API contract, request parsing, authentication, image handling, model artifact handling, and deployment guidance.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability involving API-key exposure, image parsing, request smuggling, denial of service, dependency compromise, model artifact compromise, or unauthorized access.

Report privately to the repository owner through the designated project contact channel. Include:

- affected version or commit;
- impact and attack preconditions;
- reproduction steps or a safe proof of concept;
- suggested remediation, if known.

The project owner will acknowledge receipt, assess severity, and coordinate a fix before public disclosure.

## Security invariants

- No API key, image payload, model credential, or production secret may be committed or logged.
- No remote image URL fetching is allowed.
- No multipart image uploads or client filesystem paths are accepted.
- Requests are bounded by encoded-byte, decoded-byte, image dimension, and pixel limits.
- The service must run CPU-only and without optional GPU execution providers.
- Model weights must be provenance-reviewed and checksum-pinned.
- Images are processed in memory and not persisted by default.
- Security claims require test evidence.

See [`docs/06-security.md`](docs/06-security.md) for the complete implementation policy.
