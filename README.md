# xontrib-langenv

[xonsh](https://xon.sh) integration with:

* [Pyenv](https://github.com/pyenv/pyenv)
* [Nodenv](https://github.com/nodenv/nodenv)
* [Goenv](https://github.com/syndbg/goenv)
* [Rbenv](https://github.com/rbenv/rbenv)

This xontrib replaces the slow `langenv` initialization with a faster python version (and skips the `rehash` step), which could save up to ~0.5s for each `lang`

The only two exceptions are:

  - `goenv`, which requires an extra `rehash --only-manage-paths` [init step](https://github.com/syndbg/goenv/blob/e1007619dbb180c8f8032a9dcdb7afbeb88e848a/libexec/goenv-init#L167) to set some more [environment variables](https://github.com/syndbg/goenv/blob/e1007619dbb180c8f8032a9dcdb7afbeb88e848a/libexec/goenv-sh-rehash#L24)
  - `virtualenv-init`

so if you rewrite that `goenv` env var setting and `pyenv` `virtualenv` init logic in python and xontribute to this xontrib, you could eliminate the last sources of xonsh langenv startup delay!

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

## Compatibility notes

If you are using `xonsh` v0.11 (or older) and you have issues with the latest version of this xontrib, try to downgrade it to version 1.0.6.
