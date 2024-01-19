# Jedha CLI

Practice your Cybersecurity skills with Jedha CLI.

You can launch our labs directly from your terminal.

## Requirements

- Python 3.10+
- Docker
- Docker Compose
- AMD64 CPU (preferably, otherwise some labs may not work)

This CLI is build to be used on [Kali Linux](https://www.kali.org/) priorly. It may work on other Linux distributions, but we don't support them. Also it may work on Windows and MacOS but we don't support them either.

## Installation

Be sure you meet all the requirements before installing the CLI. Then:

```bash
pip install jedha-cli
```

Sometimes you may need to add it to the `PATH` variable. You can do it by adding the following line to your `.bashrc` or `.zshrc`:

```bash
export PATH="/home/kali/.local/bin:$PATH"
```

## Usage

## How does it work?

The CLI will download the lab you want to launch from our servers, and then launch it using Docker Compose.

## Development

If you want to try the project from the source code, you can clone this repository and install it using:

```bash
poetry install
```

> You can install `poetry` using `pipx install poetry`.

Start the virtual environment using:

```bash
poetry shell
```

Then, you can run the CLI using:

```bash
python -m src.main --help
```

To test locally the `pip install` you can use:

```bash
poetry build
pip install dist/*.tar.gz
```

## What is Jedha?

[Jedha](https://www.jedha.co) is a Cybersecurity and Data Science bootcamp based in France. If you are interested in learning more about our bootcamps, you can visit our [website](https://www.jedha.co).
