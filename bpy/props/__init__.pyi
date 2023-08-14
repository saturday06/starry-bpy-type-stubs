from typing import Callable, TypeVar

import bpy

__PointerPropertyTarget = TypeVar("__PointerPropertyTarget")

def PointerProperty(
    type: type[__PointerPropertyTarget],
    name: str = "",
    description: str = "",
    update: Callable[
        [bpy.types.PropertyGroup, bpy.types.Context], None
    ] = lambda _self, _context: None,
) -> __PointerPropertyTarget: ...
