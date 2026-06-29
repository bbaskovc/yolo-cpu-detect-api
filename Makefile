PYTHON ?= python

.PHONY: check compile diff-check format format-check lint test type-check verify

check: verify test lint format-check type-check compile diff-check

format:
	$(PYTHON) -m ruff format .

format-check:
	$(PYTHON) -m ruff format --check .

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

type-check:
	$(PYTHON) -m mypy src

verify:
	$(PYTHON) scripts/verify_initial_repository.py

compile:
	PYTHONPYCACHEPREFIX=/tmp/yolo-cpu-detect-api-pycache $(PYTHON) -m compileall -q src

diff-check:
	git diff --check
