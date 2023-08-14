# pyright: reportUnusedImport=false

from . import ops, types

def new(use_operators: bool = True) -> types.BMesh: ...
