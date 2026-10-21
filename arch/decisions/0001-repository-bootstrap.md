# 1. Bootstrap repository for HA + HACS integration

Date: 2026-10-21

## Status

Accepted

## Context

The repository needs a consistent structure for:

- Home Assistant custom integration packaging and metadata.
- HACS Marketplace compatibility.
- Reliable local development and CI validation.
- Documented versioning and contribution workflow.

## Decision

- Use `custom_components/ha_energy_informations/` as integration root with a versioned `manifest.json`.
- Manage project configuration in `pyproject.toml` with Poetry.
- Use Poe the Poet tasks for common local commands.
- Enforce quality and policy checks using pre-commit hooks (Ruff, Black, markdownlint, and Conventional
  Commits via Commitizen).
- Add `bump-my-version` to keep semantic versions synchronized across `pyproject.toml`, `manifest.json`,
  and integration module version.
- Add a pull-request CI workflow that runs pre-commit.
- Provide a VS Code devcontainer for reproducible onboarding.
- Maintain architecture and contributor documentation in `arch/` and `doc/`.

## Consequences

- Contributors and automation share a single source of truth for formatting and versioning.
- Releases must follow semantic versioning and use version bump tooling.
- Commit messages must follow Conventional Commits format.
- Additional up-front tooling maintenance is required, but drift and review friction are reduced.
