from typing import Optional

import bpy

def vrm(
    filepath: str,
    extract_textures_into_folder: bool = True,
    make_new_texture_folder: bool = True,
) -> set[str]: ...
def vrma(filepath: str) -> set[str]: ...
def vrma_debug(filepath: str) -> set[str]: ...
def gltf(
    filepath: str = "",
    filter_glob: str = "*.glb;*.gltf",
    files: Optional[
        bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    ] = None,
    loglevel: int = 0,
    import_pack_images: bool = True,
    merge_vertices: bool = False,
    import_shading: str = "NORMALS",
    bone_heuristic: str = "TEMPERANCE",
    guess_original_bind_pose: bool = True,
) -> set[str]: ...
