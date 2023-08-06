def delete(use_global: bool = False, confirm: bool = True) -> set[str]: ...
def mode_set(mode: str = "OBJECT", toggle: bool = False) -> set[str]: ...
def select_all(action: str = "TOGGLE") -> set[str]: ...
def shade_smooth() -> set[str]: ...
def modifier_add(type: str = "SUBSURF") -> set[str]: ...
def transform_apply(
    location: bool = True,
    rotation: bool = True,
    scale: bool = True,
    properties: bool = True,
) -> set[str]: ...
def add(
    radius: float = 1.0,
    type: str = "EMPTY",
    enter_editmode: bool = False,
    align: str = "WORLD",
    location: tuple[float, float, float] = (0.0, 0.0, 0.0),
    rotation: tuple[float, float, float] = (0.0, 0.0, 0.0),
    scale: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> set[str]: ...
def convert(
    target: str = "MESH",
    keep_original: bool = False,
    angle: float = 1.22173,
    thickness: int = 5,
    seams: bool = False,
    faces: bool = True,
    offset: float = 0.01,
) -> set[str]: ...
