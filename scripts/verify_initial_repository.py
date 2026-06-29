"""Validate the architecture/governance baseline before implementation begins."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "LICENSE-STATUS.md",
    "pyproject.toml",
    ".env.example",
    "docs/00-project-charter.md",
    "docs/01-product-requirements.md",
    "docs/02-non-goals.md",
    "docs/03-architecture.md",
    "docs/04-openai-compatibility.md",
    "docs/05-api-contract.md",
    "docs/06-security.md",
    "docs/07-test-and-validation.md",
    "docs/08-benchmark-method.md",
    "docs/10-work-plan.md",
    "docs/11-release-readiness.md",
    "docs/13-licensing-and-model-policy.md",
    "docs/templates/work-order.md",
    "docs/templates/executor-report.md",
    "examples/requests/responses-base64.json",
    "examples/requests/chat-completions-base64.json",
)

FORBIDDEN_SOURCE_TOKENS = (
    "tracking",
    "segmentation",
    "background jobs",
    "multipart",
    "remote image",
    "cuda",
)


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        print("Missing required files:", file=sys.stderr)
        for path in missing:
            print(f"- {path}", file=sys.stderr)
        return 1

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    if agents != claude:
        print("AGENTS.md and CLAUDE.md must be exactly equivalent.", file=sys.stderr)
        return 1

    required_constitution_terms = (
        "One request processes exactly one image.",
        "Production inference is CPU-only.",
        "Object tracking",
        "Background jobs",
        "Base64 data URL",
    )
    absent = [term for term in required_constitution_terms if term not in agents]
    if absent:
        print("Constitution is missing required policy terms:", file=sys.stderr)
        for term in absent:
            print(f"- {term}", file=sys.stderr)
        return 1

    source_root = ROOT / "src"
    unexpected_runtime_files = [
        path
        for path in source_root.rglob("*.py")
        if path.name not in {"__init__.py", "_version.py"}
    ]
    if unexpected_runtime_files:
        print("Initial baseline must not contain implementation modules yet:", file=sys.stderr)
        for path in unexpected_runtime_files:
            print(f"- {path.relative_to(ROOT)}", file=sys.stderr)
        return 1

    print("Initial repository baseline is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
