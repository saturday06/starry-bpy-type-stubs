# pylint: disable=unused-argument

def orphans_purge(
    execution_context: str = "EXEC_DEFAULT",
    /,
    *,
    num_deleted: int = 0,
    do_local_ids: bool = True,
    do_linked_ids: bool = True,
    do_recursive: bool = False,
) -> set[str]: ...
