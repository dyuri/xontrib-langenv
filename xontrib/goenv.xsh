"""Initialize goenv at xonsh start
"""
import builtins
import os

__all__ = ()

p = os.path.join($HOME, ".goenv") if not $GOENV_ROOT else $GOENV_ROOT
if os.path.exists(p):
    $PATH.add(f"{p}/bin", front=True, replace=True)

    GOENV = $(which goenv).strip()


    def create_alias(output):
        commands = []
        for line in [l for l in output.split('\n') if 'shell' in l]:
            commands += line.strip()[:-1].split('|')

        def goenv(args):
            if args and len(args):
                cmd = args[0]
                arguments = args[1:]
            else:
                cmd = None
                arguments = []

            if cmd in commands:
                source-bash --suppress-skip-message $(@(GOENV) sh-@(cmd) @(arguments))
            else:
                @(GOENV) @(args)

        builtins.aliases['goenv'] = goenv


    # check if goenv installed
    if GOENV:
        lines = $(@(GOENV) init -).split('\n')
        GOENV_PATH = lines[0]
        GOENV_ENV = $(@(GOENV) init -)

        # add shims to path
        source-bash --login=false --interactive=false --suppress-skip-message @(GOENV_PATH) e>/dev/null

        # init goenv
        source-bash --login=false --interactive=false --suppress-skip-message @(GOENV_ENV) e>/dev/null

        create_alias(GOENV_ENV)
