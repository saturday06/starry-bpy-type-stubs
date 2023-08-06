def orphans_purge(
    num_deleted: int = 0,
    do_local_ids: bool = True,
    do_linked_ids: bool = True,
    do_recursive: bool = False,
) -> set[str]: ...
