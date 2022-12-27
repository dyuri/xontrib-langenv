"""Initialize pyenv at xonsh start
"""
import builtins
import os
import subprocess
from .langenv_common import get_bin, create_alias
from xonsh.lib      import subprocess as subproc
from builtins        import __xonsh__    # XonshSession (${...} is '__xonsh__.env')

__all__ = ()

base  = 'pyenv'
PYENV = get_bin(base)
if PYENV:
    # Set environment
    envx = __xonsh__.env
    Home = envx.get("HOME")
    PYENV_ROOT = envx.get("PYENV_ROOT")
    if not PYENV_ROOT:
        PYENV_ROOT = f"{Home}/.{base}"
    envx.get("PATH").add(f'{PYENV_ROOT}/shims', front=True) # prepend shims to PATH
    envx["PYENV_SHELL"] = "Python"

    PYENV_VENV = None

    cmd_venv   = [PYENV,'virtualenv-init','-']
    PYENV_VENV = subprocess.run(cmd_venv,capture_output=True,encoding="UTF-8").stdout
    if PYENV_VENV:
        # init pyenv-virtualenv
        cmd_venv = ['source-bash','-n','--suppress-skip-message',PYENV_VENV]
        subproc.run(cmd_venv)

    create_alias(base, PYENV)
