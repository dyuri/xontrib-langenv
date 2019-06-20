"""Initialize pyenv at xonsh start
"""
import builtins

__all__ = ()

PYENV = $(which pyenv)
PYENV_VENV = None


def create_alias(output):
    commands = []
    for line in [l for l in output.split('\n') if 'shell' in l]:
        commands += line.strip()[:-1].split('|')

    def pyenv(args):
        if args and len(args):
            cmd = args[0]
            arguments = args[1:]
        else:
            cmd = None
            arguments = []

        if cmd in commands:
            source-bash --suppress-skip-message $(@(PYENV) sh-@(cmd) @(arguments))
        else:
            @(PYENV) @(args)

    builtins.aliases['pyenv'] = pyenv


# check if pyenv installed
if PYENV:
    PYENV_ENV = $(@(PYENV) init -)
    PYENV_VENV = $(@(PYENV) virtualenv-init -)
    
    # init pyenv
    source-bash --suppress-skip-message @(PYENV_ENV)

    if PYENV_VENV:
        # init pyenv-virtualenv
        source-bash --suppress-skip-message @(PYENV_VENV)

    create_alias(PYENV_ENV)
