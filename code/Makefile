PYTHON ?= python

.PHONY: check format lint type test verify compile

check: verify compile lint type test

format:
	$(PYTHON) -m ruff format .

lint:
	$(PYTHON) -m ruff check .

type:
	$(PYTHON) -m mypy src tests scripts

test:
	$(PYTHON) -m pytest

verify:
	$(PYTHON) scripts/verify_initial_repository.py

compile:
	$(PYTHON) -m compileall -q src scripts tests
