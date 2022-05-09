import os
import random
import sys
from os import makedirs, path
from os.path import abspath as ap
from os.path import dirname as dn

import inquirer

from . import globals
from .globals import CFLOP, POSIX, TW
from .settings import stg, wr_stg
from .style import S, ct, pp

title = S.p1(S.t1("whinee/tournament-cutter"))

tww = []

if TW < 40:
    tww = [
        S.t_error("Your terminal width is well below than"),
        S.t_error("the bare minimum"),
        S.t_error(f"({TW} instead of 40 and above)"),
        S.t_error(f"Consider resizing\n")
    ]
else:
    if TW < 55:
        tww = [
                S.t_warning("Your terminal width is below than"),
                S.t_warning(f"recommended ({TW} instead of 55 and above)\n")
            ]

pp(
    ct.group(
        title,
        S.t1("Tournament Cutter."),
        S.t1("\nConsider donating to the project: https://whinyaan.xyz/donate\n"),
        *tww,
    )
)

def init(idx: int) -> None:
    cm = stg(None, path.join(dn(ap(__file__)), "cf_tpl.mp"))

    if sys.platform == "win32":
        op_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'tc')
    else:
        op_dir = os.path.join(os.path.expanduser('~'), "tc")

    validate = False
    while not validate:
        if inquirer.list_input(
            message="Choose the path to download the chapter to",
            choices=[
                [op_dir, False],
                ["Input it myself", True],
            ]
        ):
            pd = input("Input the path to output the processed tournaments to: ")
            if not path.isdir(pd):
                if inquirer.confirm("The path does not exist. Do you want to make it?", default=False):
                    makedirs(pd)
                    validate = True
        else:
            validate = True
    cm["output_directory"] = op_dir
    globals.config_path = cfn = CFLOP[idx]
    wr_stg(None, cm, cfn)

for i in CFLOP:
    if os.path.exists(str(i)):
        globals.config_path = i
        break

if globals.config_path is None:
    if POSIX:
        from . import appimage
        if appimage:
            init(1)
        else:
            init(0)
    else:
        init(0)