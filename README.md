# ha-energy-informations

A Home Assistant custom integration to expose information from the Energy dashboard for use in templates.

## Repository layout

- `custom_components/ha_energy_informations/`: Integration code and Home Assistant `manifest.json`
- `arch/`: Architecture requirements, overview, and ADRs
- `doc/`: User and contributor documentation
- `.devcontainer/`: Reproducible development environment for VS Code

## Development

Use Poetry to install dependencies and run tasks:

```bash
poetry install
poetry run poe check
```

For commit checks:

```bash
pre-commit install --install-hooks
pre-commit run --all-files
```
