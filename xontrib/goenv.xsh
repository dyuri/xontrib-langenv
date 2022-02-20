"""Initialize goenv at xonsh start
"""
import builtins
import os
from .pygonerb_common import get_bin, create_alias

__all__ = ()

GOENV = get_bin("goenv")

# check if goenv installed
if GOENV:
    GOENV_ENV = $(@(GOENV) init -)

    # init goenv
    source-bash --login=false --interactive=false --suppress-skip-message @(GOENV_ENV) e>/dev/null

    create_alias("goenv", GOENV, GOENV_ENV)
