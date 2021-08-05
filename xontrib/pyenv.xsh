"""Initialize pyenv at xonsh start
"""
import builtins

__all__ = ()

PYENV = $(which pyenv).strip()
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
    PYENV_PATH = $(@(PYENV) init --path)
    PYENV_ENV = $(@(PYENV) init -)
    PYENV_VENV = $(@(PYENV) virtualenv-init - 2> /dev/null)
    
    # add shims to path
    source-bash --login=false --interactive=false --suppress-skip-message @(PYENV_PATH) e>/dev/null

    # init pyenv
    source-bash --login=false --interactive=false --suppress-skip-message @(PYENV_ENV) e>/dev/null

    if PYENV_VENV:
        # init pyenv-virtualenv
        source-bash --login=false --interactive=false --suppress-skip-message @(PYENV_VENV) e>/dev/null

    create_alias(PYENV_ENV)
