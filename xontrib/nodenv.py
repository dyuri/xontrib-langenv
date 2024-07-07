"""Initialize nodenv at xonsh start
"""
import builtins
import os
from builtins import __xonsh__  # XonshSession (${...} is '__xonsh__.env')

from .langenv_common import create_alias, get_bin


__all__ = ()

base = "nodenv"
NODENV = get_bin("nodenv")

# check if nodenv installed
if NODENV:
    # Set environment
    envx = __xonsh__.env
    Home = envx.get("HOME")
    NODENV_ROOT = envx.get("NODENV_ROOT")
    if not NODENV_ROOT:
        NODENV_ROOT = f"{Home}/.{base}"
    envx.get("PATH").add(f"{NODENV_ROOT}/shims", front=True)  # prepend shims to PATH
    envx["NODENV_SHELL"] = "Python"

    create_alias(base, NODENV)
