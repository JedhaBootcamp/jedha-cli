# Jedha CLI

## Development

We use [Poetry](https://python-poetry.org/) to manage dependencies and virtual environments.

Once Poetry is installed, run `poetry install` to install the dependencies.

To run pre-commit hooks, run `poetry run pre-commit run --all-files`. Or:

```bash
poetry shell
pre-commit install
pre-commit run --all-files
```
