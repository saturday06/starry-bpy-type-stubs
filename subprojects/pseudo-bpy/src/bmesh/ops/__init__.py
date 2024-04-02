from __future__ import annotations

from bmesh.types import BMesh, BMFaceSeq


def recalc_face_normals(
    bm: BMesh,
    /,
    *,
    faces: BMFaceSeq = ...,
) -> set[str]: ...
