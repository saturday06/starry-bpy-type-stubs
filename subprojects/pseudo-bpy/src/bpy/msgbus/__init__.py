from __future__ import annotations


# TODO: 正しい型
def subscribe_rna(
    key: object,
    owner: object,
    args: object,
    notify: object,
    options: set[str] = ...,
) -> None: ...
def publish_rna(key: object) -> None: ...
def clear_by_owner(owner: object) -> None: ...
