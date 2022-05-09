import ast
import itertools
import os
import re
import sys
import unicodedata
from os.path import dirname as dn
from os.path import realpath as rp
import shlex
from subprocess import Popen
from typing import Any
from os import path, makedirs

# https://stackoverflow.com/a/93029
ALL_CHARS = (chr(i) for i in range(sys.maxunicode))
CATEGORIES = {'Cn'}
CCHARS = ''.join(map(chr, itertools.chain(range(0x00,0x20), range(0x7f,0xa0))))
CCHARS_RE = re.compile('[%s]' % re.escape(CCHARS))

def run(s: str, cwd: str=os.getcwd()):
    p = Popen(shlex.split(s), cwd=cwd)
    p.wait()
    return

def sanitize_text(s: str):
    return unicodedata.normalize("NFKD", CCHARS_RE.sub('', s)).strip()

def dnrp(file: str, n: int=1) -> str:
    """
    Get the directory component of a pathname by n times recursively then return it.

    Args:
        file (str): File to get the directory of.
        n (int, optional): Number of times to get up the directory???? Defaults to 1.

    Returns:
        op (str): The directory component got recursively by n times from the given pathname
    """
    op = rp(file)
    for _ in range(n):
        op = dn(op)
    return op

def de(a: Any, d: Any) -> Any:
    """
    Defaults. Return a if a is True, else returns d.

    Args:
        a (Any): Object to be tested, will be returned if evaluates to True.
        d (Any): Default object to be returned if `a` evaluates to False.

    Returns:
        Any
    """
    if a:
        return a
    else:
        return d

def dd(default: dict[Any, Any], d: dict[Any, Any] | None) -> dict[Any, Any]:
    """
    Defaults dictionary. Overwrite the items in the default dict with the
    items in the d dict.

    Args:
        default (Dict[Any, Any]): The dict to rewrite the items to.
        d (Union[Dict[Any, Any], None]): The dict to rewrite the items from.

    Returns:
        dict[Any, Any]
    """
    op = default
    if d:
        for a, v in d.items():
            op[a] = v
    return op

def ddir(d: dict[Any, Any], dir: str, de: Any={}) -> Any:
    """
    Retrieve dictionary value using recursive indexing with a string.
    ex.:
        `ddir({"data": {"attr": {"ch": 1}}}, "data/attr/ch")`
        will return `1`


    Args:
        dict (dict): Dictionary to retrieve the value from.
        dir (str): Directory of the value to be retrieved.

    Returns:
        op (Any): Retrieved value.
    """
    op = d
    for a in dir.split("/"):
        op = op[a]
    return op or de

def dpop(
    d: dict[Any, Any],
    pop: list[int | tuple[str | int | tuple] | str],
    de: Any=None
) -> Any:
    """
    Iterate through the preferred order of precedence (`pop`) and see if
    the value exists in the dictionary. If it does, return it. If not, return
    `de`.

    Args:
        d (Dict[Any, Any]): Dictionary to retrieve the value from.
        pop (list[int | tuple[str | int | tuple]  |  str]): List of keys to
            iterate through.
        de (Any, optional): Default object to be returned. Defaults to None.

    Returns:
        Any: Retrieved value.
    """

    for i in pop:
        if op:= d.get(i):
            return op
    return de

def le(expr: str) -> Any:
    return ast.literal_eval(expr) if expr else expr

def dnrp(file: str, n: int=1) -> str:
    """
    Get the directory component of a pathname by n times recursively then return it.

    Args:
        file (str): File to get the directory of.
        n (int, optional): Number of times to get up the directory???? Defaults to 1.

    Returns:
        op (str): The directory component got recursively by n times from the given pathname
    """
    op = rp(file)
    for _ in range(n):
        op = dn(op)
    return op

def inmd(p: str, ls: list[str]=None):
    """
    "If Not `path.isdir`, Make Directories"

    Args:
        p (str): [description]
    """

    pd = path.dirname(p)
    if (pd) and (not path.isdir(pd)):
        makedirs(pd)
        if ls:
            ls.append(pd)
    return p