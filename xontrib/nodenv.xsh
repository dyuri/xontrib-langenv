"""Initialize nodenv at xonsh start
"""
import builtins
import os

__all__ = ()

p = os.path.join($HOME, ".nodenv") if not $NODENV_ROOT else $NODENV_ROOT
if os.path.exists(p):
    $PATH.add(f"{p}/bin", front=True, replace=True)

    NODENV = $(which nodenv).strip()


    def create_alias(output):
        commands = []
        for line in [l for l in output.split('\n') if 'shell' in l]:
            commands += line.strip()[:-1].split('|')

        def nodenv(args):
            if args and len(args):
                cmd = args[0]
                arguments = args[1:]
            else:
                cmd = None
                arguments = []

            if cmd in commands:
                source-bash --suppress-skip-message $(@(NODENV) sh-@(cmd) @(arguments))
            else:
                @(NODENV) @(args)

        builtins.aliases['nodenv'] = nodenv


    # check if nodenv installed
    if NODENV:
        lines = $(@(NODENV) init -).split('\n')
        NODENV_PATH = lines[0]
        NODENV_ENV = $(@(NODENV) init -)

        # add shims to path
        source-bash --login=false --interactive=false --suppress-skip-message @(NODENV_PATH) e>/dev/null

        # init nodenv
        source-bash --login=false --interactive=false --suppress-skip-message @(NODENV_ENV) e>/dev/null

        create_alias(NODENV_ENV)
