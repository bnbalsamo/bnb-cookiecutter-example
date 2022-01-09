# bnb-cookiecutter-example [![v0.1.0](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/bnbalsamo/bnb-cookiecutter-example/releases)

[![CI](https://github.com/bnbalsamo/bnb-cookiecutter-example/workflows/CI/badge.svg?branch=main)](https://github.com/bnbalsamo/bnb-cookiecutter-example/actions)
[![Coverage](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example/branch/main/graph/badge.svg)](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example/)
[![Documentation Status](https://readthedocs.org/projects/bnb-cookiecutter-example/badge/?version=latest)](http://bnb-cookiecutter-example.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example/shield.svg)](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A project.

See the full documentation at https://bnb-cookiecutter-example.readthedocs.io

# Installation

This project is currently only installable via development tooling.

- Install [poetry](https://python-poetry.org/)
- ```$ git clone https://github.com/bnbalsamo/bnb-cookiecutter-example.git```
- ```$ cd bnb-cookiecutter-example```
- ```$ poetry install --no-dev```

# Development

To install + configure a development environment...

- Install [poetry](https://python-poetry.org/)
- Clone the repository
    - `git clone git@github.com:bnbalsamo/bnb-cookiecutter-example.git`
- `cd` into the project directory
    - `cd bnb-cookiecutter-example`
- Install the project and development dependencies with poetry
    - `poetry install -E docs -E tests`
- Activate the project's virtual environment in your current shell
    - `poetry shell`
- Install the pre-commit hooks
    - `pre-commit install --install-hooks`

Development tasks are available via the `tasks.py` [invoke](http://www.pyinvoke.org/)
script. After installation you can view the help via `inv --list`

## Running Tests
```
$ inv test
```

## Running autoformatters
```
$ inv format
```

## Upgrading Dependencies
```
$ poetry update
```

# Author
First Last <you@provider.com>

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.48.0_
