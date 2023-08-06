from typing import Optional

import bpy

def save_as_mainfile(
    filepath: str, copy: bool = False, check_existing: bool = False
) -> set[str]: ...
def quit_blender() -> None: ...
def open_mainfile(
    filepath: str = "",
    hide_props_region: bool = True,
    filter_blender: bool = True,
    filter_backup: bool = False,
    filter_image: bool = False,
    filter_movie: bool = False,
    filter_python: bool = False,
    filter_font: bool = False,
    filter_sound: bool = False,
    filter_text: bool = False,
    filter_archive: bool = False,
    filter_btx: bool = False,
    filter_collada: bool = False,
    filter_alembic: bool = False,
    filter_usd: bool = False,
    filter_volume: bool = False,
    filter_folder: bool = True,
    filter_blenlib: bool = False,
    filemode: int = 8,
    display_type: str = "DEFAULT",
    sort_method: str = "",
    load_ui: bool = True,
    use_scripts: bool = True,
    display_file_selector: bool = True,
    state: int = 0,
) -> set[str]: ...
def append(
    filepath: str = "",
    directory: str = "",
    filename: str = "",
    files: Optional[
        bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    ] = None,
    filter_blender: bool = True,
    filter_backup: bool = False,
    filter_image: bool = False,
    filter_movie: bool = False,
    filter_python: bool = False,
    filter_font: bool = False,
    filter_sound: bool = False,
    filter_text: bool = False,
    filter_archive: bool = False,
    filter_btx: bool = False,
    filter_collada: bool = False,
    filter_alembic: bool = False,
    filter_usd: bool = False,
    filter_volume: bool = False,
    filter_folder: bool = True,
    filter_blenlib: bool = True,
    filemode: int = 1,
    display_type: str = "DEFAULT",
    sort_method: str = "",
    link: bool = False,
    autoselect: bool = True,
    active_collection: bool = True,
    instance_collections: bool = False,
    instance_object_data: bool = True,
    set_fake: bool = False,
    use_recursive: bool = True,
) -> set[str]: ...
