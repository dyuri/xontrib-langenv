"""Initialize goenv at xonsh start
"""
import builtins
import os
from .langenv_common import get_bin, create_alias
from builtins        import __xonsh__    # XonshSession (${...} is '__xonsh__.env')
from xonsh.lib       import subprocess as subproc

__all__ = ()

base  = 'goenv'
GOENV = get_bin(base)

# check if goenv installed
if GOENV:
    # Set environment
    envx = __xonsh__.env
    Home = envx.get("HOME")
    GOENV_ROOT = envx.get("GOENV_ROOT")
    if not GOENV_ROOT:
        GOENV_ROOT = f"{Home}/.{base}"
    envx.get("PATH").add(f'{GOENV_ROOT}/shims', front=True) # prepend shims to PATH
    envx["GOENV_SHELL"] = "Python"

    create_alias(base, GOENV)

    full_cmd = [base] + ['rehash','--only-manage-paths']
    subproc.run(full_cmd)
