import contextlib
from collections.abc import Iterable, KeysView, MutableSequence, Sequence
from typing import Callable, Generic, Iterator, Optional, TypeVar, Union, overload

# pyright: reportMissingImports=false, reportUnknownVariableType=false
from io_scene_vrm.editor.extension import (
    VrmAddonArmatureExtensionPropertyGroup,
    VrmAddonBoneExtensionPropertyGroup,
    VrmAddonMaterialExtensionPropertyGroup,
    VrmAddonObjectExtensionPropertyGroup,
    VrmAddonSceneExtensionPropertyGroup,
)

import mathutils

class bpy_struct:
    id_data: Optional["ID"]
    def __contains__(self, key: str) -> bool: ...

__BpyPropCollectionElement = TypeVar("__BpyPropCollectionElement")

class bpy_prop_collection(Generic[__BpyPropCollectionElement]):
    def get(
        self, key: str, default: Optional[__BpyPropCollectionElement] = None
    ) -> Optional[__BpyPropCollectionElement]: ...
    def __contains__(self, key: str) -> bool: ...
    def __iter__(self) -> Iterator[__BpyPropCollectionElement]: ...
    def __getitem__(self, key: Union[int, str]) -> __BpyPropCollectionElement: ...
    def __len__(self) -> int: ...
    def remove(self, element: __BpyPropCollectionElement) -> None: ...
    def keys(self) -> KeysView[str]: ...

# ドキュメントには存在しない
__BpyPropArrayElement = TypeVar("__BpyPropArrayElement")

class bpy_prop_array(Generic[__BpyPropArrayElement]):
    def __iter__(self) -> Iterator[__BpyPropArrayElement]: ...
    @overload
    def __getitem__(self, index: int) -> __BpyPropArrayElement: ...
    @overload
    def __getitem__(self, index: slice) -> tuple[__BpyPropArrayElement, ...]: ...

# カスタムプロパティ対応クラス。2.93ではID,Bone,PoseBoneのみ
# https://docs.blender.org/api/2.93/bpy.types.bpy_struct.html#bpy.types.bpy_struct.values
class __CustomProperty:
    def __getitem__(self, key: str) -> object: ...
    def __setitem__(self, key: str, value: object) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def get(self, key: str, default: object = None) -> object: ...

class ID(bpy_struct, __CustomProperty):
    name: str
    is_evaluated: bool
    users: int
    use_fake_user: bool

class AnyType(bpy_struct): ...

class ColorManagedInputColorspaceSettings(bpy_struct):
    name: str

class Event(bpy_struct): ...
class ImageUser(bpy_struct): ...

class Image(ID):
    colorspace_settings: ColorManagedInputColorspaceSettings
    size: bpy_prop_array[float]
    alpha_mode: str
    generated_color: tuple[float, float, float, float]  # Vectorかもしれない
    depth: int
    file_format: str
    filepath: str
    filepath_raw: str
    generated_height: int
    generated_width: int
    is_dirty: bool
    def filepath_from_user(self, image_user: Optional[ImageUser] = None) -> str: ...
    def update(self) -> None: ...
    def gl_load(self, frame: int = 0) -> None: ...
    def unpack(self, method: str = "USE_LOCAL") -> None: ...

class Texture(ID): ...

class LayerObjects(bpy_prop_collection["Object"]):
    active: Optional["Object"]

class Space(bpy_struct): ...
class SpaceView3D(Space): ...

class Depsgraph(bpy_struct):
    def update(self) -> None: ...

class ViewLayer(bpy_struct):
    objects: LayerObjects
    depsgraph: Depsgraph
    def update(self) -> None: ...

class Bone(bpy_struct, __CustomProperty):
    name: str
    parent: Optional["Bone"]
    tail: mathutils.Vector  # ドキュメントには3要素のfloat配列と書いてあるが、実際にはVector
    vrm_addon_extension: VrmAddonBoneExtensionPropertyGroup

class EditBone(bpy_struct):
    @property
    def head(self) -> mathutils.Vector: ...  # ドキュメントには3要素のfloat配列と書いてあるが、実際にはVector
    @head.setter
    def head(self, value: Iterable[float]) -> None: ...
    @property
    def tail(self) -> mathutils.Vector: ...  # ドキュメントには3要素のfloat配列と書いてあるが、実際にはVector
    @tail.setter
    def tail(self, value: Iterable[float]) -> None: ...

    parent: Optional["EditBone"]
    roll: float
    use_local_location: bool
    use_connect: bool

class PoseBoneConstraints(bpy_prop_collection["Constraint"]):
    def new(self, type: str) -> "Constraint": ...

class PoseBone(bpy_struct, __CustomProperty):
    name: str
    constraints: PoseBoneConstraints
    head: mathutils.Vector  # ドキュメントには3要素のfloat配列と書いてあるが、実際にはVector
    rotation_mode: str
    rotation_quaternion: mathutils.Quaternion
    bone: Bone

class ArmatureBones(bpy_prop_collection[Bone]): ...
class OperatorProperties(bpy_struct): ...

class UILayout(bpy_struct):
    def box(self) -> "UILayout": ...
    def column(
        self,
        align: bool = False,
        heading: str = "",
        heading_ctxt: str = "",
        translate: bool = True,
    ) -> "UILayout": ...
    def row(
        self,
        align: bool = False,
        heading: str = "",
        heading_ctxt: str = "",
        translate: bool = True,
    ) -> "UILayout": ...
    def prop(
        self,
        data: bpy_struct,  # TODO: AnyType
        property: str,
        text: str = "",
        text_ctxt: str = "",
        translate: bool = True,
        icon: str = "NONE",
        expand: bool = False,
        slider: bool = False,
        toggle: int = -1,
        icon_only: bool = False,
        event: bool = False,
        full_event: bool = False,
        emboss: bool = True,
        index: int = -1,
        icon_value: int = 0,
        invert_checkbox: bool = False,
    ) -> "UILayout": ...
    def label(
        self,
        text: str = "",
        text_ctxt: str = "",
        translate: bool = True,
        icon: str = "NONE",
        icon_value: int = 0,
    ) -> "UILayout": ...
    def split(self, factor: float = 0.0, align: bool = False) -> "UILayout": ...
    def operator(
        self,
        operator: str,
        text: str = "",
        text_ctxt: str = "",
        translate: bool = True,
        icon: str = "NONE",
        emboss: bool = True,
        depress: bool = False,
        icon_value: int = 0,
    ) -> OperatorProperties: ...
    def separator(self, factor: float = 1.0) -> None: ...
    alignment: str
    scale_x: float

class AddonPreferences(bpy_struct):
    layout: UILayout  # TODO: No documentation

class Addon(bpy_struct):
    preferences: AddonPreferences

class Addons(bpy_prop_collection[Addon]): ...
class IDMaterials(
    bpy_prop_collection[Optional["Material"]]
): ...  # ドキュメントにはMaterialと書いてあるが実際にはOptional[Material]

class Curve(ID):
    materials: IDMaterials

class MeshUVLoop(bpy_struct): ...

class MeshUVLoopLayer(bpy_struct):
    data: bpy_prop_collection[MeshUVLoop]

class UVLoopLayers(bpy_prop_collection[MeshUVLoopLayer]): ...

class MeshLoopTriangle(bpy_struct):
    vertices: tuple[int, int, int]
    material_index: int

class MeshLoopTriangles(bpy_prop_collection[MeshLoopTriangle]): ...

class MeshVertex(bpy_struct):
    co: tuple[float, float, float]  # Vectorかも?

class MeshVertices(bpy_prop_collection[MeshVertex]): ...

class Mesh(ID):
    use_auto_smooth: bool
    materials: IDMaterials
    uv_layers: UVLoopLayers
    loop_triangles: MeshLoopTriangles
    vertices: MeshVertices
    has_custom_normals: bool
    def calc_tangents(self, uvmap: str = "") -> None: ...
    def calc_loop_triangles(self) -> None: ...

class ArmatureEditBones(bpy_prop_collection[EditBone]):
    def new(self, name: str) -> EditBone: ...

class Armature(ID):
    bones: ArmatureBones
    edit_bones: ArmatureEditBones
    vrm_addon_extension: VrmAddonArmatureExtensionPropertyGroup

class Text(ID):
    def write(self, text: str) -> None: ...

class NodeSocketInterface(bpy_struct):
    description: str
    name: str
    bl_socket_idname: str
    type: str  # ドキュメントには存在しない

    # bpy.app.version >= (3, 0, 0)
    attribute_domain: str
    bl_label: str

class NodeSocket(bpy_struct):
    display_shape: str
    enabled: bool
    hide: bool
    hide_value: bool
    link_limit: int
    name: str
    show_expanded: bool
    type: str
    links: list["NodeLink"]

class NodeSocketStandard(NodeSocket): ...

class NodeSocketBool(NodeSocketStandard):
    default_value: bool

class NodeSocketFloat(NodeSocketStandard):
    default_value: float

class NodeSocketFloatAngle(NodeSocketStandard):
    default_value: float

class NodeSocketFloatDistance(NodeSocketStandard):
    default_value: float

class NodeSocketFloatFactor(NodeSocketStandard):
    default_value: float

class NodeSocketFloatPercentage(NodeSocketStandard):
    default_value: float

class NodeSocketFloatTime(NodeSocketStandard):
    default_value: float

class NodeSocketFloatUnsigned(NodeSocketStandard):
    default_value: float

class NodeSocketInt(NodeSocketStandard):
    default_value: int

class NodeSocketIntFactor(NodeSocketStandard):
    default_value: int

class NodeSocketIntPercentage(NodeSocketStandard):
    default_value: int

class NodeSocketIntUnsigned(NodeSocketStandard):
    default_value: int

class NodeSocketString(NodeSocketStandard):
    default_value: str

class NodeSocketVector(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorAcceleration(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorDirection(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorEuler(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorTranslation(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorVelocity(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketVectorXYZ(NodeSocketStandard):
    default_value: tuple[float, float, float]  # TODO: Vector?

class NodeSocketColor(NodeSocketStandard):
    default_value: tuple[float, float, float, float]  # TODO: Color?

class NodeOutputs(bpy_prop_collection[NodeSocket]): ...
class NodeInputs(bpy_prop_collection[NodeSocket]): ...

class Node(bpy_struct):
    bl_idname: str
    outputs: NodeOutputs
    inputs: NodeInputs
    color: tuple[float, float, float]  # TODO: Color?
    height: float
    hide: bool
    label: str
    location: tuple[float, float]
    mute: bool
    name: str
    parent: Optional["Node"]
    select: bool
    show_options: bool
    show_preview: bool
    show_texture: bool
    use_custom_color: bool
    width: float
    type: str

    # bpy.app.version < (4, 0):
    width_hidden: bool

class NodeInternal(Node): ...
class ShaderNode(NodeInternal): ...
class NodeReroute(NodeInternal): ...

class NodeFrame(NodeInternal):
    shrink: bool
    label_size: int
    text: Text

class NodeGroup(NodeInternal): ...

class NodeGroupOutput(NodeInternal):
    is_active_output: bool

class ShaderNodeWireframe(ShaderNode):
    use_pixel_size: bool

class ShaderNodeVertexColor(ShaderNode):
    layer_name: str

class ShaderNodeVectorTransform(ShaderNode):
    convert_from: str
    convert_to: str
    vector_type: str

class ShaderNodeVectorRotate(ShaderNode):
    invert: bool
    rotation_type: str

class ShaderNodeVectorMath(ShaderNode):
    operation: str

class ShaderNodeVectorDisplacement(ShaderNode):
    space: str

class ShaderNodeUVMap(ShaderNode):
    from_instancer: bool
    uv_map: str

class ShaderNodeUVAlongStroke(ShaderNode):
    use_tips: bool

class ShaderNodeTexWhiteNoise(ShaderNode):
    noise_dimensions: str

class ColorRamp(bpy_struct):
    color_mode: str
    elements: object  # TODO: object

class ColorMapping(bpy_struct):
    blend_color: tuple[float, float, float]  # TODO: Color?
    blend_factor: float
    blend_type: str
    brightness: float
    color_ramp: ColorRamp
    contrast: float
    saturation: float
    use_color_ramp: bool

class TexMapping(bpy_struct):
    # incomplete
    mapping: str
    mapping_x: str
    mapping_y: str
    mapping_z: str

class ShaderNodeTexWave(ShaderNode):
    bands_direction: str
    color_mapping: ColorMapping
    rings_direction: str
    texture_mapping: object  # TODO
    wave_profile: str
    wave_type: str

class ShaderNodeTexVoronoi(ShaderNode):
    color_mapping: ColorMapping
    distance: str
    feature: str
    texture_mapping: object  # TODO:
    voronoi_dimensions: str

class ShaderNodeTexSky(ShaderNode):
    air_density: float
    altitude: float
    color_mapping: ColorMapping
    dust_density: float
    ground_albedo: float
    ozone_density: float
    sky_type: str
    sun_direction: tuple[float, float, float]  # TODO: Vector?
    turbidity: float

class ShaderNodeTexPointDensity(ShaderNode):
    interpolation: str
    object: Optional["Object"]
    particle_color_source: str
    point_source: str
    radius: float
    resolution: int
    space: str
    vertex_attribute_name: str
    vertex_color_source: str

class ShaderNodeTexNoise(ShaderNode):
    noise_dimensions: str

class ShaderNodeTexMusgrave(ShaderNode):
    musgrave_dimensions: str
    musgrave_type: str

class ShaderNodeTexMagic(ShaderNode):
    turbulence_depth: int

class ShaderNodeTexImage(ShaderNode):
    extension: str
    image: Optional[Image]
    interpolation: str
    projection: str
    projection_blend: float

class ShaderNodeTexIES(ShaderNode):
    filepath: str
    ies: Text
    mode: str

class ShaderNodeTexGradient(ShaderNode):
    gradient_type: str

class ShaderNodeTexEnvironment(ShaderNode):
    image: Optional[Image]
    interpolation: str
    projection: str

class ShaderNodeTexCoord(ShaderNode):
    from_instancer: bool
    object: Optional["Object"]

class ShaderNodeTexBrick(ShaderNode):
    offset: float
    offset_frequency: int
    squash: float
    squash_frequency: int

class ShaderNodeTangent(ShaderNode):
    axis: str
    direction_type: str
    uv_map: str

class ShaderNodeSubsurfaceScattering(ShaderNode):
    falloff: str

class ShaderNodeScript(ShaderNode):
    bytecode: str
    bytecode_hash: str
    filepath: str
    mode: str
    script: Text
    use_auto_update: bool

class ShaderNodeOutputWorld(ShaderNode):
    is_active_output: bool
    target: str

class ShaderNodeOutputMaterial(ShaderNode):
    is_active_output: bool
    target: str

class ShaderNodeOutputLineStyle(ShaderNode):
    blend_type: str
    is_active_output: bool
    target: str
    use_alpha: bool
    use_clamp: bool

class ShaderNodeOutputLight(ShaderNode):
    is_active_output: str
    target: str

class ShaderNodeOutputAOV(ShaderNode):
    name: str

class ShaderNodeNormalMap(ShaderNode):
    space: str
    uv_map: str

class ShaderNodeMixRGB(ShaderNode):
    blend_type: str
    use_alpha: bool
    use_clamp: bool

class ShaderNodeMath(ShaderNode):
    operation: str
    use_clamp: bool

class ShaderNodeMapping(ShaderNode):
    vector_type: str

class ShaderNodeMapRange(ShaderNode):
    clamp: bool
    interpolation_type: str

class ShaderNodeDisplacement(ShaderNode):
    space: str

class ShaderNodeCustomGroup(ShaderNode): ...

class ShaderNodeClamp(ShaderNode):
    clamp_type: str

class ShaderNodeBump(ShaderNode):
    invert: bool

class ShaderNodeBsdfToon(ShaderNode):
    component: str

class ShaderNodeBsdfRefraction(ShaderNode):
    distribution: str

class ShaderNodeBsdfPrincipled(ShaderNode):
    distribution: str
    subsurface_method: str

class ShaderNodeBsdfHairPrincipled(ShaderNode):
    parametrization: str

class ShaderNodeBsdfHair(ShaderNode):
    component: str

class ShaderNodeBsdfGlass(ShaderNode):
    distribution: str

class ShaderNodeBsdfAnisotropic(ShaderNode):
    distribution: str

class ShaderNodeBevel(ShaderNode):
    samples: int

class ShaderNodeAttribute(ShaderNode):
    attribute_name: str
    attribute_type: str

class ShaderNodeAmbientOcclusion(ShaderNode):
    inside: bool
    only_local: bool
    samples: int

# bpy.app.version < (4, 0):
class ShaderNodeBsdfGlossy(ShaderNode):
    distribution: str

# bpy.app.version >= (3, 3):
class ShaderNodeCombineColor(ShaderNode):
    mode: str

# bpy.app.version >= (3, 3):
class ShaderNodeSeparateColor(ShaderNode):
    mode: str

# bpy.app.version >= (3, 4):
class ShaderNodeMix(ShaderNode):
    blend_type: str
    clamp_factor: bool
    clamp_result: bool
    data_type: str
    factor_mode: str

class GeometryNode(NodeInternal): ...

class GeometryNodeExtrudeMesh(GeometryNode):
    mode: str

class GeometryNodeDeleteGeometry(GeometryNode):
    domain: str
    mode: str

class GeometryNodeSeparateGeometry(GeometryNode):
    domain: str

# bpy.app.version >= (3, 3):
class GeometryNodeSwitch(GeometryNode):
    input_type: str

class ShaderNodeRGB(ShaderNode): ...
class ShaderNodeValue(ShaderNode): ...

class ShaderNodeGroup(ShaderNode):
    node_tree: "NodeTree"

class Pose(bpy_struct):
    bones: bpy_prop_collection[PoseBone]

class MaterialSlot(bpy_struct):
    material: Optional["Material"]  # マテリアル一覧の+を押したまま何も選ばないとNoneになる

class Object(ID):
    name: str
    type: str
    data: Union[None, Armature, Mesh]
    mode: str
    pose: Pose
    def select_set(
        self, state: bool, view_layer: Optional[ViewLayer] = None
    ) -> None: ...

    hide_render: bool
    hide_select: bool
    hide_viewport: bool
    material_slots: bpy_prop_collection[MaterialSlot]
    vrm_addon_extension: VrmAddonObjectExtensionPropertyGroup
    users_collection: bpy_prop_collection["Collection"]
    parent: Optional["Object"]
    def visible_get(
        self,
        view_layer: Optional[ViewLayer] = None,
        viewport: Optional[SpaceView3D] = None,
    ) -> bool: ...
    constraints: "ObjectConstraints"
    parent_type: str
    parent_bone: str
    empty_display_size: float
    empty_display_type: str
    display_type: str
    show_in_front: bool

    rotation_mode: str
    rotation_quaternion: mathutils.Quaternion  # TODO: 型あってる?

    bound_box: bpy_prop_array[bpy_prop_array[float]]

    matrix_world: mathutils.Matrix  # ドキュメントには4x4の2次元配列って書いてあるけど実際にはMatrix
    matrix_local: mathutils.Matrix  # ドキュメントには4x4の2次元配列って書いてあるけど実際にはMatrix
    scale: mathutils.Vector  # ドキュメントには3要素のfloat配列って書いてあるけど実際にはVector

    @property
    def location(self) -> mathutils.Vector: ...  # ドキュメントには3要素のfloat配列と書いてあるが、実際にはVector
    @location.setter
    def location(self, value: Iterable[float]) -> None: ...
    def evaluated_get(self, depsgraph: "Depsgraph") -> "Object": ...  # 本当はIDのメソッド
    def to_mesh(
        self,
        preserve_all_data_layers: bool = False,
        depsgraph: Optional[Depsgraph] = None,
    ) -> Mesh: ...

class PreferencesView:
    use_translate_interface: bool

class Preferences:
    view: PreferencesView
    addons: Addons

class NodeLink(bpy_struct):
    is_valid: bool
    to_socket: NodeSocket
    from_socket: NodeSocket
    from_node: Node
    to_node: Node

class NodeLinks(bpy_prop_collection[NodeLink]):
    def new(
        self, input: NodeSocket, output: NodeSocket, verify_limits: bool = True
    ) -> NodeLink: ...

class Nodes(bpy_prop_collection[Node]):
    def new(self, type: str) -> Node: ...

class NodeTreeInputs(bpy_prop_collection[NodeSocketInterface]):
    def new(self, type: str, name: str) -> NodeSocketInterface: ...

class NodeTreeOutputs(bpy_prop_collection[NodeSocketInterface]):
    def new(self, type: str, name: str) -> NodeSocketInterface: ...

class NodeTree(ID):
    links: NodeLinks
    nodes: Nodes
    inputs: NodeTreeInputs
    outputs: NodeTreeOutputs

class Material(ID):
    name: str
    blend_method: str
    node_tree: NodeTree  # TODO: 無いことがある?
    use_nodes: bool
    alpha_threshold: float
    shadow_method: str
    use_backface_culling: bool
    show_transparent_back: bool
    alpha_method: str

    vrm_addon_extension: VrmAddonMaterialExtensionPropertyGroup

class Modifier(bpy_struct): ...
class PropertyGroup(bpy_struct): ...
class ObjectConstraints(bpy_prop_collection["Constraint"]): ...
class OperatorFileListElement(PropertyGroup): ...

class Constraint(bpy_struct):
    name: str
    is_valid: bool
    mute: bool

class DampedTrackConstraint(Constraint):
    target: Optional[Object]
    subtarget: str
    head_tail: float

class CopyRotationConstraint(Constraint):
    target: Optional[Object]
    mix_mode: str
    use_x: bool
    use_y: bool
    use_z: bool
    invert_x: bool
    invert_y: bool
    invert_z: bool
    owner_space: str
    target_space: str
    subtarget: str

class ViewLayers(bpy_prop_collection[ViewLayer]):
    def update(self) -> None: ...  # TODO: ドキュメントに記載されていない

class ColorManagedViewSettings(bpy_struct):
    view_transform: str

class Scene(ID):
    collection: "Collection"
    view_layers: ViewLayers
    view_settings: ColorManagedViewSettings
    vrm_addon_extension: VrmAddonSceneExtensionPropertyGroup

class WindowManager(ID):
    @classmethod
    def invoke_props_dialog(
        cls, operator: "Operator", width: int = 300
    ) -> set[str]: ...

class SpaceFileBrowser(Space):
    active_operator: "Operator"

class Context(bpy_struct):
    # https://docs.blender.org/api/2.93/bpy.context.html
    # https://docs.blender.org/api/2.93/bpy.types.Context.html

    # Global Context
    blend_data: "BlendData"
    mode: str
    preferences: Preferences
    scene: Scene
    space_data: Space
    view_layer: ViewLayer
    window_manager: WindowManager

    # Screen Context
    object: Optional[Object]
    active_object: Optional[Object]
    selectable_objects: Sequence[Object]

class CollectionObjects(bpy_prop_collection[Object]):
    def link(self, obj: Object) -> None: ...
    def unlink(self, obj: Object) -> None: ...

class CollectionChildren(bpy_prop_collection["Collection"]):
    def link(self, child: "Collection") -> None: ...

class Collection(ID):
    objects: CollectionObjects
    children: CollectionChildren

class BlendDataCollections(bpy_prop_collection[Collection]):
    def new(self, name: str) -> Collection: ...
    active: Optional[Object]

class BlendDataObjects(bpy_prop_collection[Object]):
    def new(self, name: str, object_data: Optional[ID]) -> Object: ...
    def remove(
        self,
        element: Object,
        do_unlink: bool = True,
        do_id_user: bool = True,
        do_ui_user: bool = True,
    ) -> None: ...

class Library(ID): ...
class BlendDataMaterials(bpy_prop_collection[Material]): ...

class BlendDataImages(bpy_prop_collection[Image]):
    def new(
        self,
        name: str,
        width: int,
        height: int,
        alpha: bool = False,
        float_buffer: bool = False,
        stereo3d: bool = False,
        is_data: bool = False,
        tiled: bool = False,
    ) -> Image: ...
    def load(self, filepath: str, check_existing: bool = False) -> Image: ...

class BlendDataArmatures(bpy_prop_collection[Armature]): ...

class BlendDataTexts(bpy_prop_collection[Text]):
    def new(self, name: str) -> Text: ...

class BlendDataMeshes(bpy_prop_collection[Mesh]):
    def new(self, name: str) -> Mesh: ...

class BlendDataLibraries(bpy_prop_collection[Library]):
    @contextlib.contextmanager
    def load(
        self, filepath: str, link: bool
    ) -> Iterator[tuple["BlendData", "BlendData"]]: ...  # ドキュメントに存在しない

class BlendDataNodeTrees(bpy_prop_collection[NodeTree]):
    def new(self, name: str, type: str) -> NodeTree: ...
    def append(self, node_group: NodeTree) -> None: ...  # ドキュメントに存在しない

class BlendData:
    filepath: str
    collections: BlendDataCollections
    objects: BlendDataObjects
    materials: BlendDataMaterials
    images: BlendDataImages
    armatures: BlendDataArmatures
    texts: BlendDataTexts
    meshes: BlendDataMeshes
    libraries: BlendDataLibraries
    node_groups: BlendDataNodeTrees

class Operator(bpy_struct):
    bl_idname: str
    layout: UILayout

TOPBAR_MT_file_import: MutableSequence[Callable[[Operator, Context], None]]
TOPBAR_MT_file_export: MutableSequence[Callable[[Operator, Context], None]]
VIEW3D_MT_armature_add: MutableSequence[Callable[[Operator, Context], None]]
