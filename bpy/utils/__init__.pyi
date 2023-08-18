from typing import Union

import bpy

def register_class(
    t: Union[
        type[bpy.types.Operator],
        type[bpy.types.PropertyGroup],
        type[bpy.types.Panel],
        type[bpy.types.UIList],
        type[bpy.types.Preferences],
        type[bpy.types.AddonPreferences],
    ]
) -> None: ...
def unregister_class(
    t: Union[
        type[bpy.types.Operator],
        type[bpy.types.PropertyGroup],
        type[bpy.types.Panel],
        type[bpy.types.UIList],
        type[bpy.types.Preferences],
        type[bpy.types.AddonPreferences],
    ]
) -> None: ...
