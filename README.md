# Xontrib-pyenv

[Pyenv](https://github.com/pyenv/pyenv) [xonsh](https://xon.sh) integration.

## Install

Install using pip

```
pip install xontrib-pyenv
```

Add to your `.xonshrc`:

```
xontrib load pyenv
```

## Usage

This xontrib initializes `pyenv` when `xonsh` is started.
After initialization `pyenv` commands works as they would do in any *classic* shell.

Also supports [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
