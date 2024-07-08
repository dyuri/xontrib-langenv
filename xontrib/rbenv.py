"""Initialize rbenv at xonsh start
"""
import builtins
import os
from builtins import __xonsh__  # XonshSession (${...} is '__xonsh__.env')

from .langenv_common import create_alias, get_bin


__all__ = ()

base = "rbenv"
RBENV = get_bin(base)

# check if rbenv installed
if RBENV:
    # Set environment
    envx = __xonsh__.env
    Home = envx.get("HOME")
    RBENV_ROOT = envx.get("RBENV_ROOT")
    if not RBENV_ROOT:
        RBENV_ROOT = f"{Home}/.{base}"
    envx.get("PATH").add(f"{RBENV_ROOT}/shims", front=True)  # prepend shims to PATH
    envx["RBENV_SHELL"] = "Python"

    create_alias(base, RBENV)
