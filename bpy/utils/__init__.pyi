# pylint: disable=unused-argument

from typing import Union

from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    Preferences,
    PropertyGroup,
    UIList,
)

def register_class(
    t: Union[
        type[Operator],
        type[PropertyGroup],
        type[Panel],
        type[UIList],
        type[Preferences],
        type[AddonPreferences],
    ]
) -> None: ...
def unregister_class(
    t: Union[
        type[Operator],
        type[PropertyGroup],
        type[Panel],
        type[UIList],
        type[Preferences],
        type[AddonPreferences],
    ]
) -> None: ...
