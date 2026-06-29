# Licensing and Model Policy

## Repository license

No source-code license is selected in the initial repository. The project must remain private until the owner selects an explicit license.

## Model approval gate

No YOLO-family model, weights, export, labels, or dataset-derived artifact may be adopted until a decision record includes:

1. model family and exact version;
2. upstream source URL or trusted internal source;
3. source code and weights license terms;
4. intended use: internal, commercial, hosted, redistributed, embedded, or other;
5. ONNX export method and tool versions;
6. SHA-256 checksum for ONNX weight artifact;
7. SHA-256 checksum for label map;
8. input resolution and preprocessing rules;
9. class list and label-map version;
10. benchmark/test fixture plan;
11. any attribution or notice requirement.

## Artifact handling

- Weights and model outputs are not committed to Git.
- Deployment receives immutable, checksum-verified model artifacts through a documented delivery method.
- A model replacement is a controlled compatibility decision, not a silent package update.
- If detection semantics, preprocessing, labels, or expected quality change materially, publish a new model ID.

## Dependency policy

- Initial Python dependencies are deliberately minimal.
- Add runtime dependencies only in a work order that states purpose, license, security impact, and test coverage.
- Select and document a lockfile strategy before deployment.
- Review dependencies and container base images before release.
