from __future__ import annotations

from pathlib import Path

from yolo_cpu_detect_api import __version__

ROOT = Path(__file__).resolve().parents[1]


def test_initial_version_is_pre_alpha() -> None:
    assert __version__ == "0.0.0"


def test_agent_constitutions_are_equivalent() -> None:
    assert (ROOT / "AGENTS.md").read_text(encoding="utf-8") == (ROOT / "CLAUDE.md").read_text(
        encoding="utf-8"
    )


def test_initial_docs_state_the_core_non_goals() -> None:
    text = (ROOT / "docs/02-non-goals.md").read_text(encoding="utf-8").lower()
    for term in ("tracking", "video", "segmentation", "background jobs", "gpu"):
        assert term in text
