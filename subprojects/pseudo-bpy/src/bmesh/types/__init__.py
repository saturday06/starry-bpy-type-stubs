from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Generic, Optional, TypeVar

import mathutils
from bpy.types import Mesh

__BMElemSeqElement = TypeVar("__BMElemSeqElement")


class BMElemSeq(Generic[__BMElemSeqElement]):
    def __len__(self) -> int: ...
    def __getitem__(self, key: int) -> __BMElemSeqElement: ...
    def __iter__(self) -> Iterator[__BMElemSeqElement]: ...


class BMLoopUV:
    uv: mathutils.Vector


class BMVert:
    index: int
    co: mathutils.Vector

    def __getitem__(
        self,
        value: BMLoopUV,
    ) -> mathutils.Vector: ...  # ドキュメントには存在しない


class BMLayerCollection:
    def __getitem__(self, key: str) -> BMLoopUV: ...  # ドキュメントに記載はない?


class BMLayerAccessLoop:
    uv: BMLayerCollection


class BMLayerAccessVert:
    shape: BMLayerCollection


class BMVertSeq:
    def new(
        self,
        co: Sequence[float] = (0.0, 0.0, 0.0),
        example: Optional[BMVert] = None,
    ) -> BMVert: ...
    @property
    def layers(self) -> BMLayerAccessVert: ...


class BMEdge: ...


class BMEdgeSeq:
    def new(
        self,
        verts: tuple[
            BMVert,
            BMVert,
        ],  # 実際にはSequenceだと思うが、2要素チェックをしたいのでtuple
        example: Optional[BMEdge] = None,
    ) -> BMEdge: ...


class BMLoop:
    index: int

    @property
    def face(self) -> BMFace: ...
    @property
    def vert(self) -> BMVert: ...
    def __getitem__(
        self,
        uv: BMLoopUV,
    ) -> BMLoopUV: ...  # TODO: ドキュメントに存在しない


class BMLoopSeq:
    @property
    def layers(self) -> BMLayerAccessLoop: ...


class BMFace:
    material_index: int

    @property
    def loops(self) -> BMElemSeq[BMLoop]: ...


class BMFaceSeq:
    def new(
        self,
        verts: Sequence[BMVert],
        example: Optional[BMFace] = None,
    ) -> BMFace: ...
    def __iter__(self) -> Iterator[BMFace]: ...


class BMesh:
    @property
    def faces(self) -> BMFaceSeq: ...
    @property
    def edges(self) -> BMEdgeSeq: ...
    @property
    def verts(self) -> BMVertSeq: ...
    @property
    def loops(self) -> BMLoopSeq: ...
    def free(self) -> None: ...
    def to_mesh(self, mesh: Mesh) -> None: ...
    def from_mesh(
        self,
        mesh: Mesh,
        face_normals: bool = True,
        use_shape_key: bool = False,
        shape_key_index: int = 0,
    ) -> None: ...
    def calc_loop_triangles(self) -> list[tuple[BMLoop, ...]]: ...  # TODO: 正しい型
