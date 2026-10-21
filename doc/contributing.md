# Contributing guide (humans and agents)

## Prerequisites

- Python 3.13
- Poetry
- pre-commit

## Setup

```bash
poetry install
pre-commit install --install-hooks
```

## Quality commands

```bash
poetry run poe format
poetry run poe check
```

## Conventional commits (required)

Commit messages must follow Conventional Commits. Examples:

- `feat: add energy sensor entity`
- `fix: handle missing statistics metadata`
- `docs: clarify HACS installation steps`

The commit message format is enforced by pre-commit using Commitizen.

## Versioning and tagging

Use `bump-my-version` to update semantic versions consistently:

```bash
poetry run bump-my-version bump patch
```

This updates `pyproject.toml`, `custom_components/ha_energy_informations/manifest.json`, and
`custom_components/ha_energy_informations/__init__.py`, and creates a `vX.Y.Z` tag.
