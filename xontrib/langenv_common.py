"""Common functions
"""
import builtins
import subprocess
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
            cmd_bash = ['source-bash','--suppress-skip-message',cmd_run_out]
            full_cmd = [bin] + ['sh-'+cmd] + arguments
            cmd_run = subprocess.run(full_cmd,capture_output=True,encoding="UTF-8")
            cmd_out = cmd_run.stdout
            cmd_err = cmd_run.stderr
            if cmd_err:
                print(cmd_err.rstrip('\n'))
            subproc.run(cmd_bash)
        else:
            cmd_full = [bin] + args
            subproc.run(cmd_full)

    builtins.aliases[base] = alias
