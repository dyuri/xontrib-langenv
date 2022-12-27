"""Initialize pyenv at xonsh start
"""
import builtins
import os
import subprocess
from .langenv_common import get_bin, create_alias
from xonsh.lib      import subprocess as subproc

__all__ = ()

PYENV = get_bin('pyenv')
if PYENV:
    PYENV_VENV = None

    cmd_env    = [PYENV,           'init','-','--no-rehash']
    cmd_venv   = [PYENV,'virtualenv-init','-']
    PYENV_ENV  = subprocess.run(cmd_env ,capture_output=True,encoding="UTF-8").stdout
    PYENV_VENV = subprocess.run(cmd_venv,capture_output=True,encoding="UTF-8").stdout

    # init pyenv
    cmd_pyenv = ['source-bash','-n','--suppress-skip-message',PYENV_ENV]
    subproc.run(cmd_pyenv)

    if PYENV_VENV:
        # init pyenv-virtualenv
        cmd_venv = ['source-bash','-n','--suppress-skip-message',PYENV_VENV]
        subproc.run(cmd_venv)

    create_alias("pyenv", PYENV, PYENV_ENV)
