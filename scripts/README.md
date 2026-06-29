# Scripts

This directory contains repository validation and, later, reproducible maintenance/benchmark helpers.

Rules:

- Scripts must not contact external services based on user input.
- Scripts must not read, print, or write secrets.
- Benchmark scripts must keep raw output outside Git unless explicitly sanitized.
- A script must document inputs, outputs, and failure behavior.
