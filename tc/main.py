from os import path
from os.path import dirname, realpath
from string import Template
from typing import Any

from scripts.utils import inmd

from . import globals
from .settings import stg
from .utils import run

coords_keys = "whxy"
tsd = {
    "tss": "start",
    "tse": "end"
}

op_tpl = Template("$evt_name - $p1 VS $p2 - $name")
op_ff_tpl = Template('ffmpeg -ss $tss -i $ip -to $tse -c copy -copyts "$op"')
board_ff_tpl = Template(
    'ffmpeg -ss $ts -i $ip -vf "crop=$w:$h:$x:$y" -frames:v 1 "$op"'
)

def main(config: str, directory: str, **kwargs: dict[str, Any]):
    config = realpath(config or globals.config_path)
    cwd = dirname(config)
    v_stg = stg(None, realpath(config))
    op_pdir = directory or v_stg["output_directory"]
    for event in v_stg["events"]:
        op_en_tpl = Template(op_tpl.safe_substitute(evt_name=event["event"]))
        for tnm in event["tournaments"]:
            vid_ip = tnm["input"]
            op_ff_ip_tpl = Template(op_ff_tpl.safe_substitute(ip=vid_ip))
            board_ff_ip_tpl = Template(board_ff_tpl.safe_substitute(ip=vid_ip))
            for op in tnm["outputs"]:
                pls = []
                for plr in op["players"]:
                    pls.append(plr["name"])
                tnm_name = op_en_tpl.safe_substitute(
                    **{f'p{str(idx)}': i for idx, i in enumerate(pls, start=1)},
                    name=op["name"],
                )
                op_dir = path.join(op_pdir, tnm_name, "op.mp4")
                inmd(op_dir)
                op_name = op_ff_ip_tpl.safe_substitute(
                    op=op_dir,
                    **{k: op["timestamp"][v] for k, v in tsd.items()}
                )
                run(op_name, cwd)
                for idx_plr, plr in enumerate(op["players"], start=1):
                    pb = plr["board"]
                    coords = {}
                    for i in coords_keys:
                        coords[i] = pb["coords"][i]
                    board_op_dir = path.join(op_pdir, tnm_name, f"board {idx_plr}.png")
                    inmd(board_op_dir)
                    ff_board = board_ff_ip_tpl.safe_substitute(
                        ts=pb["timestamp"],
                        **coords,
                        op=board_op_dir
                    )
                    run(ff_board, cwd)