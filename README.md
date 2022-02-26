# xontrib-langenv

[xonsh](https://xon.sh) integration with:

* [Pyenv](https://github.com/pyenv/pyenv)
* [Nodenv](https://github.com/nodenv/nodenv)
* [Goenv](https://github.com/syndbg/goenv)
* [Rbenv](https://github.com/rbenv/rbenv)

## Install

Install using pip

```
pip install xontrib-langenv
```

## Usage

Add to your `.xonshrc` as follows:

### Pyenv

```sh
xontrib load pyenv
```

This xontrib initializes `pyenv` when `xonsh` is started.
After initialization `pyenv` commands works as they would do in any *classic* shell.

Also supports [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).

### Nodenv

```sh
xontrib load nodenv
```

This xontrib initializes `nodenv` when `xonsh` is started.
After initialization `nodenv` commands works as they would do in any *classic* shell.

### Goenv

```sh
xontrib load goenv
```

This xontrib initializes `goenv` when `xonsh` is started.
After initialization `goenv` commands works as they would do in any *classic* shell.

### Rbenv

```sh
xontrib load rbenv
```

This xontrib initializes `rbenv` when `xonsh` is started.
After initialization `rbenv` commands works as they would do in any *classic* shell.
