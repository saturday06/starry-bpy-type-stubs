from typing import Optional

import bpy

__all__ = ("PrincipledBSDFWrapper",)

class ShaderWrapper:
    __slots__ = (
        "is_readonly",
        "material",
        "_textures",
        "_grid_locations",
        "node_out",
        "_node_texcoords",
    )

    @property
    def is_readonly(self) -> bool: ...
    @property
    def material(self) -> bpy.types.Material: ...
    @property
    def use_nodes(self) -> bool: ...
    @property
    def nodes_out(self) -> Optional[bpy.types.ShaderNodeOutputMaterial]: ...
    def __init__(
        self,
        material: bpy.types.Material,
        is_readonly: bool = True,
        use_nodes: bool = True,
    ) -> None: ...

class PrincipledBSDFWrapper(ShaderWrapper):
    @property
    def node_principled_bsdf(self) -> Optional[bpy.types.ShaderNodeBsdfPrincipled]: ...
    def __init__(
        self,
        material: bpy.types.Material,
        is_readonly: bool = True,
        use_nodes: bool = True,
    ) -> None: ...
