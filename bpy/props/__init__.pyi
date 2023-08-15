from typing import Callable, Optional, Sequence, TypeVar, Union

import bpy
import mathutils

__PointerPropertyTarget = TypeVar("__PointerPropertyTarget")
__CollectionPropertyElement = TypeVar("__CollectionPropertyElement")
__CallbackSelf = TypeVar("__CallbackSelf", bound=bpy.types.PropertyGroup)

def BoolProperty(
    name: str = "",
    description: str = "",
    default: bool = False,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    subtype: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], bool]] = None,
    set: Optional[Callable[[__CallbackSelf, bool], None]] = None,
) -> bool: ...
def CollectionProperty(
    type: type[__CollectionPropertyElement],
    name: str = "",
    description: str = "",
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
) -> __CollectionPropertyElement: ...
def EnumProperty(
    items: Sequence[tuple[int]],
    name: str = "",
    description: str = "",
    default: Optional[Union[str, int]] = None,  # setも受け取れるらしいが仕様が読み取れなかった
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], int]] = None,
    set: Optional[Callable[[__CallbackSelf, int], None]] = None,
) -> str: ...
def FloatProperty(
    name: str = "",
    description: str = "",
    default: float = 0.0,
    min: float = ...,
    max: float = ...,
    soft_min: float = ...,
    soft_max: float = ...,
    step: int = 3,
    precision: int = 2,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
    subtype: str = "NONE",
    unit: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], float]] = None,
    set: Optional[Callable[[__CallbackSelf, float], None]] = None,
) -> float: ...
def FloatVectorProperty(
    name: str = "",
    description: str = "",
    default: tuple[float, ...] = (0.0, 0.0, 0.0),
    min: float = ...,
    max: float = ...,
    soft_min: float = ...,
    soft_max: float = ...,
    step: int = 3,
    precision: int = 2,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
    subtype: str = "NONE",
    unit: str = "NONE",
    size: int = 3,
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], mathutils.Vector]] = None,
    set: Optional[
        Callable[[__CallbackSelf, mathutils.Vector], None]
    ] = None,  # TODO: たしかVectorが来たけど自信がない
) -> mathutils.Vector: ...  # TODO: たしかVectorが返ったけど自信がない
def IntProperty(
    name: str = "",
    description: str = "",
    default: int = 0,
    min: int = ...,
    max: int = ...,
    soft_min: int = ...,
    soft_max: int = ...,
    step: int = 1,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
    subtype: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], int]] = None,
    set: Optional[Callable[[__CallbackSelf, int], None]] = None,
) -> int: ...
def PointerProperty(
    type: type[__PointerPropertyTarget],
    name: str = "",
    description: str = "",
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    poll: Optional[Callable[[__CallbackSelf, object], bool]] = None,
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
) -> __PointerPropertyTarget: ...
def StringProperty(
    name: str = "",
    description: str = "",
    default: str = "",
    maxlen: int = 0,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    subtype: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, bpy.types.Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], str]] = None,
    set: Optional[Callable[[__CallbackSelf, str], None]] = None,
) -> str: ...
