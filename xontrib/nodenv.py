"""Initialize nodenv at xonsh start
"""
import builtins
import os
from .langenv_common import get_bin, create_alias

__all__ = ()

NODENV = get_bin("nodenv")

# check if nodenv installed
if NODENV:
    NODENV_ENV = $(@(NODENV) init -)

    # init nodenv
    source-bash -n --suppress-skip-message @(NODENV_ENV) e>/dev/null

    create_alias("nodenv", NODENV, NODENV_ENV)
