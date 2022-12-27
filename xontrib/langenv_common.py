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


def create_alias(base,bin):
    def alias(args):
        if len(args) == 0:
            full_cmd    = [bin]
            subproc.run(full_cmd)

        elif args[0] in ['rehash','shell']:
            args[0] = 'sh-' + args[0]
            full_cmd = [bin] + args

            cmd_run = subprocess.run(full_cmd,capture_output=True,encoding="UTF-8")
            cmd_out = cmd_run.stdout.rstrip('\n')
            cmd_err = cmd_run.stderr.rstrip('\n')

            if cmd_err:
                print(cmd_err)
            else:
                cmd_bash = ['source-bash','--suppress-skip-message','-n',cmd_out]
                subproc.run(cmd_bash)

        else:
            full_cmd = [bin] + args
            subproc.run(full_cmd)

    builtins.aliases[base] = alias
