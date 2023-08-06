# pyright: reportUnusedImport=false

from typing import TypeVar

__PointerPropertyTarget = TypeVar("__PointerPropertyTarget")

def PointerProperty(type: type[__PointerPropertyTarget]) -> __PointerPropertyTarget: ...
