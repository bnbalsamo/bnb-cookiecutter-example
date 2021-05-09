# bnb-cookiecutter-example [![v0.0.1](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://github.com/bnbalsamo/bnb-cookiecutter-example/releases)

[![CI](https://github.com/bnbalsamo/bnb-cookiecutter-example/workflows/CI/badge.svg?branch=master)](https://github.com/bnbalsamo/bnb-cookiecutter-example/actions)
[![Coverage](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example/branch/master/graph/badge.svg)](https://codecov.io/gh/bnbalsamo/bnb-cookiecutter-example/)
 [![Documentation Status](https://readthedocs.org/projects/bnb-cookiecutter-example/badge/?version=latest)](http://bnb-cookiecutter-example.readthedocs.io/en/latest/?badge=latest) 
[![Updates](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example/shield.svg)](https://pyup.io/repos/github/bnbalsamo/bnb-cookiecutter-example/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A project.

See the full documentation at https://bnb-cookiecutter-example.readthedocs.io

# Installation
- ```$ git clone https://github.com/bnbalsamo/bnb-cookiecutter-example.git```
- ```$ cd bnb-cookiecutter-example```
    - If you would like to install the pinned dependencies, run ```pip install -r requirements.txt```
- ```$ python -m pip install .```

# Development

## Quickstart

To quickly install + configure a development environment...

Install [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv),
and [xxenv-latest](https://github.com/momo-lab/xxenv-latest) and copy the following into your terminal while
in the repository root.

```bash
[[ `type -t pyenv` ]] && \
[ -s "$PYENV_ROOT/plugins/pyenv-virtualenv" ] && \
[ -s "$PYENV_ROOT/plugins/xxenv-latest" ] && \
pyenv latest install -s 3.8 && \
PYENV_LATEST_38=$(pyenv latest -p 3.8) && \
pyenv latest install -s 3.7 && \
PYENV_LATEST_37=$(pyenv latest -p 3.7) && \
pyenv latest install -s 3.6 && \
PYENV_LATEST_36=$(pyenv latest -p 3.6) && \
pyenv virtualenv "$PYENV_LATEST_38" "bnb-cookiecutter-example" && \
pyenv local "bnb-cookiecutter-example" "$PYENV_LATEST_38" "$PYENV_LATEST_37" "$PYENV_LATEST_36" && \
pip install -e .[dev,tests,docs]
```

## Manual Configuration

If you choose not to use the quickstart script you will need to...

- Create a virtual environment
- Install the development dependencies
    - `pip install -e .[dev,tests,docs]`
- Configure tox so that it can access all relevant python interpreters

## Running Tests
```
$ inv run.tests
```

## Running autoformatters
```
$ inv run.autoformatters
```

## Pinning Dependencies
```
$ inv pindeps
```

# Author
First Last <you@provider.com>

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.40.0_
