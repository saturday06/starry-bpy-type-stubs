import bpy

class ImportHelper:
    filepath: str  # ドキュメントには記載がない

    def invoke(
        self,
        context: bpy.types.Context,
        event: bpy.types.Event,
    ) -> set[str]: ...

class ExportHelper:
    filepath: str  # ドキュメントには記載がない

    def invoke(
        self,
        context: bpy.types.Context,
        event: bpy.types.Event,
    ) -> set[str]: ...
