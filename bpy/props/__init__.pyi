from typing import Callable, Optional, Sequence, TypeVar, Union

import mathutils
from bpy.types import Context, Operator, PropertyGroup

__PointerPropertyTarget = TypeVar("__PointerPropertyTarget", bound=type)
__CollectionPropertyElement = TypeVar("__CollectionPropertyElement", bound=type)
__CallbackSelf = TypeVar("__CallbackSelf", bound=Union[PropertyGroup, Operator])

def BoolProperty(
    *,
    name: str = "",
    description: str = "",
    default: bool = False,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    subtype: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], bool]] = None,
    set: Optional[Callable[[__CallbackSelf, bool], None]] = None,
) -> bool: ...
def CollectionProperty(
    *,
    type: __CollectionPropertyElement,
    name: str = "",
    description: str = "",
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
) -> __CollectionPropertyElement: ...
def EnumProperty(
    *,
    items: Union[
        Sequence[tuple[str, str, str, int]], Sequence[tuple[str, str, str, str, int]]
    ],
    name: str = "",
    description: str = "",
    default: Optional[Union[str, int]] = None,  # setも受け取れるらしいが仕様が読み取れなかった
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], int]] = None,
    set: Optional[Callable[[__CallbackSelf, int], None]] = None,
) -> str: ...
def FloatProperty(
    *,
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
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], float]] = None,
    set: Optional[Callable[[__CallbackSelf, float], None]] = None,
) -> float: ...
def FloatVectorProperty(
    *,
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
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], tuple[float, ...]]] = None,
    set: Optional[Callable[[__CallbackSelf, Sequence[float]], None]] = None,
) -> mathutils.Vector: ...  # TODO: たしかVectorが返ったけど自信がない
def IntProperty(
    *,
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
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], int]] = None,
    set: Optional[Callable[[__CallbackSelf, int], None]] = None,
) -> int: ...
def PointerProperty(
    *,
    type: __PointerPropertyTarget,
    name: str = "",
    description: str = "",
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    poll: Optional[Callable[[__CallbackSelf, object], bool]] = None,
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
) -> __PointerPropertyTarget: ...
def StringProperty(
    *,
    name: str = "",
    description: str = "",
    default: str = "",
    maxlen: int = 0,
    options: set[str] = ...,
    override: set[str] = ...,
    tags: set[str] = ...,  # TODO: 型がわからない
    subtype: str = "NONE",
    update: Optional[Callable[[__CallbackSelf, Context], None]] = None,
    get: Optional[Callable[[__CallbackSelf], str]] = None,
    set: Optional[Callable[[__CallbackSelf, str], None]] = None,
) -> str: ...
