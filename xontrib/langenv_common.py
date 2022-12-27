"""Common functions
"""
import builtins
from os.path import join, exists


def get_bin(base):
    capped = base.upper() + "_ROOT"
    root = join($HOME, f".{base}") if not capped in ${...} else ${...}[capped]
    try:
        bin = $(which @(base) 2> /dev/null).strip()
    except:
        bin = None
    if not bin:
        new_path = join(root, "bin")
        if exists(join(new_path, base)):
            $PATH.add(new_path, front=True, replace=True)
            bin = $(which @(base)).strip()
            ${...}[capped] = root
            return bin
        else:
            print(f"Cannot find {base} in {new_path}")
        return None
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

