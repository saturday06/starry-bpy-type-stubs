from __future__ import annotations

GL_BACK: int
GL_BLEND: int
GL_CLAMP_TO_EDGE: int
GL_COLOR_BUFFER_BIT: int
GL_CULL_FACE: int
GL_DEPTH_BUFFER_BIT: int
GL_DEPTH_TEST: int
GL_ONE: int
GL_ONE_MINUS_SRC_ALPHA: int
GL_SRC_ALPHA: int
GL_TEXTURE0: int
GL_TEXTURE1: int
GL_TEXTURE_2D: int
GL_TEXTURE_WRAP_S: int
GL_TEXTURE_WRAP_T: int
GL_TRUE: int
GL_ZERO: int


def glClearColor(red: float, green: float, blue: float, alpha: float) -> None: ...
def glClear(mask: int) -> None: ...
def glEnable(cap: int) -> None: ...
def glDisable(cap: int) -> None: ...
def glBlendFunc(sfactor: int, dfactor: int) -> None: ...
def glDepthMask(flag: int) -> None: ...
def glCullFace(mode: int) -> None: ...
def glActiveTexture(texture: int) -> None: ...
def glBindTexture(target: int, texture: int) -> None: ...
def glTexParameteri(target: int, pname: int, param: int) -> None: ...