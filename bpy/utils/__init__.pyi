from typing import Union

import bpy

def register_class(
    t: Union[type[bpy.types.Operator], type[bpy.types.PropertyGroup]]
) -> None: ...
def unregister_class(
    t: Union[type[bpy.types.Operator], type[bpy.types.PropertyGroup]]
) -> None: ...
