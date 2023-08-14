from collections.abc import Sequence

from bmesh.types import BMesh, BMFace

def recalc_face_normals(bm: BMesh, faces: Sequence[BMFace] = ()) -> set[str]: ...
