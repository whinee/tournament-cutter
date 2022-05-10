import base64
from datetime import date
from functools import partial

import tc

from . import docs
from .settings import stg
from .utils import ddir

icons = ["issues", "forks", "stars", "contributors", "license", "code"]
langs = ["python", "html", "yaml"]

def b64(name: str):
    with open(f"./docs/assets/images/icons/{name}", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

YML = stg(None, "dev.yml")
R_GLOBAL = ddir(YML, "md_vars/global")
GLOBAL = partial(ddir, R_GLOBAL)
LICENSE = partial(ddir, ddir(YML, "license"))

PN = GLOBAL("project_name")
ORG = GLOBAL("organization")
USER = GLOBAL("user")

if (copyright := []) == []:
    for c, mp in LICENSE("cholder").items():
        user = mp['user']
        for org, projects in mp["projects"].items():
            for project, pm in projects.items():
                copyright.append(
                    f"by [{c}, Github account [{user}](https://github.com/{user}) owner, {pm['year']}] as part of project [{project}](https://github.com/{org}/{project})"
                )
    if len(copyright) > 1:
        copyright[-2] += f", and {copyright[-1]}"
        del copyright[-1]
    cholder = f"""Copyright for portions of project [{PN}](https://github.com/{ORG}/{PN}) are held {', '.join(copyright)}.\n
All other copyright for project [{PN}](https://github.com/{ORG}/{PN}) are held by [Github Account [{USER}](https://github.com/{USER}) Owner, {LICENSE('year')}]."""
else:
    cholder = f"Copyright (c) 2021 Github Account [{PN}](https://github.com/{USER}) Owner"

RULES_MDV = {
    "rules": {
        "del": {},
        "repl": {},
    },
    "md_vars": {
        "global": {
            "year": str(date.today().year),
            "cholder": cholder,
            "ver": tc.__version__,
            "prerel": not tc.vls[-2] == 3,
            **{f"{i}_b64": b64(f"{i}.png") for i in icons},
            **dict(
                zip([f'v_{i}' for i in ["d", "u", "m", "p", "pri", "prv"]], tc.vls)
            ),
            **R_GLOBAL
        },
        "local": {
            **ddir(YML, "md_vars/local"),
        },
    }
}

def main(hr: bool=False):
    docs.main(RULES_MDV, hr)