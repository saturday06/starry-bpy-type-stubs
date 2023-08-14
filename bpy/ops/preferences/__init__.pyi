def addon_install(
    overwrite: bool = True,
    target: str = "DEFAULT",
    filepath: str = "",
    filter_folder: bool = True,
    filter_python: bool = True,
    filter_glob: str = "*.py;*.zip",
) -> set[str]: ...
def addon_enable(module: str = "") -> set[str]: ...
