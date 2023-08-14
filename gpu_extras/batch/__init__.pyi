import gpu

def batch_for_shader(
    shader: gpu.types.GPUShader, type: str, content: object, indices: object = None
) -> gpu.types.GPUBatch: ...
