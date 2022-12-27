"""Initialize pyenv at xonsh start
"""
import builtins
import os
from .langenv_common import get_bin, create_alias

__all__ = ()

PYENV = get_bin('pyenv')
if PYENV:
    PYENV_VENV = None

    PYENV_PATH = $(@(PYENV) init --path)
    PYENV_ENV = $(@(PYENV) init - --no-rehash)
    PYENV_VENV = $(@(PYENV) virtualenv-init - 2> /dev/null)

    # add shims to path
    source-bash -n --suppress-skip-message @(PYENV_PATH) e>/dev/null

    # init pyenv
    source-bash -n --suppress-skip-message @(PYENV_ENV) e>/dev/null

    if PYENV_VENV:
        # init pyenv-virtualenv
        source-bash -n --suppress-skip-message @(PYENV_VENV) e>/dev/null

    create_alias("pyenv", PYENV, PYENV_ENV)
