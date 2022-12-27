"""Common functions
"""
import builtins
from os.path import join, exists

from builtins import __xonsh__  # XonshSession (${...} is '__xonsh__.env')
from xonsh.lib import subprocess as subproc

def get_bin(base):
    bin = __xonsh__.commands_cache.lazy_locate_binary(base, ignore_alias=True)
    if not bin:
        envx = __xonsh__.env
        PATH = envx.get("PATH")
        print(f"Cannot find '{base}' in {PATH}")
        return None
    else:
        return bin

def create_alias(base, bin, output):
    commands = []
    for line in [l for l in output.split('\n') if 'shell' in l]:
        commands += line.strip()[:-1].split('|')

    def alias(args):
        if args and len(args):
            cmd = args[0]
            arguments = args[1:]
        else:
            cmd = None
            arguments = []

        if cmd in commands:
            source-bash --suppress-skip-message $(@(bin) sh-@(cmd) @(arguments))
        else:
            @(bin) @(args)

    builtins.aliases[base] = alias

