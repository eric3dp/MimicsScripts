import pymatic
import trimatic.utils

from enum import Enum

class ShapeMeasuresAll(Enum):
    """Measures for remesh, analyze mesh etc."""

    rin_rout = "R-in/R-out (N)"
    height_base_n = "Height/Base (N)"
    height_base_a = "Height/Base (A)"
    skewness_n = "Skewness (N)"
    minimum_face_angle_n = "Minimum face angle (N)"
    maximum_face_angle_n = "Maximum face angle (N)"
    minimum_face_angle_a = "Minimum face angle (A)"
    angle_ratio_n = "Angle ratio (N)"
    edge_ratio_n = "Edge ratio (min/max) (N)"
    equi_angle_skewness_n = "Equi-angle skewness (N)"
    stretch_n = "Stretch (N)"
    #analysis
    minimum_edge_length_a = "Minimum edge length (A)"
    maximum_edge_length_a = "Maximum edge length (A)"
    edge_ratio_a = "Edge ratio (max/min) (A)"
    abaqus_shape_factor_n = "Abaqus shape factor (N)"
    ansys_element_quality_n = "Ansys element quality (N)"
    fluent_orthogonal_quality_n = "Fluent orthogonal quality (N)"
    maximum_face_angle_a = "Maximum face angle (A)"
    #volume specific

    r_in_edge_n = "R-in/Edge (N)"
    r_out_edge_a = "R-out/Edge (A)"
    mean_ratio_n = "Mean ratio (N)"
    aspect_ratio_a = "Aspect ratio (A)"
    jacobian_a = "Jacobian (A)"
    jacobian_n = "Jacobian (N)"
    jacobian_ratio_a = "Jacobian Ratio (A)"
    minimum_volume_a = "Minimum volume (A)"
    maximum_volume_a = "Maximum volume (A)"
    minimum_dihedral_angle_a = "Minimum dihedral angle (A)"
    maximum_dihedral_angle_a = "Maximum dihedral angle (A)"

class ShapeMeasures(Enum):
    """Measures for adaptive_remesh_expert."""

    rin_rout = ShapeMeasuresAll.rin_rout.value
    height_base_n = ShapeMeasuresAll.height_base_n.value
    height_base_a = ShapeMeasuresAll.height_base_a.value
    skewness_n = ShapeMeasuresAll.skewness_n.value
    minimum_face_angle_n = ShapeMeasuresAll.minimum_face_angle_n.value
    maximum_face_angle_n = ShapeMeasuresAll.maximum_face_angle_n.value
    minimum_face_angle_a = ShapeMeasuresAll.minimum_face_angle_a.value
    angle_ratio_n = ShapeMeasuresAll.angle_ratio_n.value
    edge_ratio_n = ShapeMeasuresAll.edge_ratio_n.value
    equi_angle_skewness_n = ShapeMeasuresAll.equi_angle_skewness_n.value
    stretch_n = ShapeMeasuresAll.stretch_n.value

class ShapeMeasuresAnalyzeMeshQualitySurface(Enum):
    """Measures for analyze_mesh_quality_surface."""

    rin_rout = ShapeMeasuresAll.rin_rout.value
    height_base_n = ShapeMeasuresAll.height_base_n.value
    minimum_face_angle_n = ShapeMeasuresAll.minimum_face_angle_n.value
    maximum_face_angle_n = ShapeMeasuresAll.maximum_face_angle_n.value
    minimum_face_angle_a = ShapeMeasuresAll.minimum_face_angle_a.value
    edge_ratio_n = ShapeMeasuresAll.edge_ratio_n.value
    equi_angle_skewness_n = ShapeMeasuresAll.equi_angle_skewness_n.value
    minimum_edge_length_a = ShapeMeasuresAll.minimum_edge_length_a.value 
    maximum_edge_length_a = ShapeMeasuresAll.maximum_edge_length_a.value 
    edge_ratio_a = ShapeMeasuresAll.edge_ratio_a.value 
    abaqus_shape_factor_n = ShapeMeasuresAll.abaqus_shape_factor_n.value 
    ansys_element_quality_n = ShapeMeasuresAll.ansys_element_quality_n.value 
    fluent_orthogonal_quality_n = ShapeMeasuresAll.fluent_orthogonal_quality_n.value 
    maximum_face_angle_a = ShapeMeasuresAll.maximum_face_angle_a.value 
    #surface specific
    angle_ratio_n = ShapeMeasuresAll.angle_ratio_n.value
    stretch_n = ShapeMeasuresAll.stretch_n.value
    height_base_a = ShapeMeasuresAll.height_base_a.value
    skewness_n = ShapeMeasuresAll.skewness_n.value

class ShapeMeasuresAnalyzeMeshQualityVolume(Enum):
    """Measures for analyze_mesh_quality_volume."""

    rin_rout = ShapeMeasuresAll.rin_rout.value
    height_base_n = ShapeMeasuresAll.height_base_n.value
    minimum_face_angle_n = ShapeMeasuresAll.minimum_face_angle_n.value
    maximum_face_angle_n = ShapeMeasuresAll.maximum_face_angle_n.value
    minimum_face_angle_a = ShapeMeasuresAll.minimum_face_angle_a.value
    edge_ratio_n = ShapeMeasuresAll.edge_ratio_n.value
    equi_angle_skewness_n = ShapeMeasuresAll.equi_angle_skewness_n.value
    minimum_edge_length_a = ShapeMeasuresAll.minimum_edge_length_a.value 
    maximum_edge_length_a = ShapeMeasuresAll.maximum_edge_length_a.value 
    edge_ratio_a = ShapeMeasuresAll.edge_ratio_a.value 
    abaqus_shape_factor_n = ShapeMeasuresAll.abaqus_shape_factor_n.value 
    ansys_element_quality_n = ShapeMeasuresAll.ansys_element_quality_n.value 
    fluent_orthogonal_quality_n = ShapeMeasuresAll.fluent_orthogonal_quality_n.value 
    maximum_face_angle_a = ShapeMeasuresAll.maximum_face_angle_a.value 
    #volume specific
    r_in_edge_n = ShapeMeasuresAll.r_in_edge_n.value
    r_out_edge_a = ShapeMeasuresAll.r_out_edge_a.value
    mean_ratio_n = ShapeMeasuresAll.mean_ratio_n.value
    aspect_ratio_a = ShapeMeasuresAll.aspect_ratio_a.value
    jacobian_a = ShapeMeasuresAll.jacobian_a.value
    jacobian_n = ShapeMeasuresAll.jacobian_n.value
    jacobian_ratio_a = ShapeMeasuresAll.jacobian_ratio_a.value
    minimum_volume_a = ShapeMeasuresAll.minimum_volume_a.value
    maximum_volume_a = ShapeMeasuresAll.maximum_volume_a.value
    minimum_dihedral_angle_a = ShapeMeasuresAll.minimum_dihedral_angle_a.value
    maximum_dihedral_angle_a = ShapeMeasuresAll.maximum_dihedral_angle_a.value

def adaptive_remesh(
    *args,#'force named parameters'
    entities, 
    target_triangle_edge_length = 1.0,
    preserve_surface_contours = False, 
    local_remesh_parameters = (()), 
    local_growth_rate : float = 25 
    ):
    """Applies adaptive remesh on the specified entities.

    :param entities: Either single object or heterogeneous list of parts, surfaces, surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param target_triangle_edge_length: The approximate triangle edge length in the output.
    :type target_triangle_edge_length: float, optional
    :param preserve_surface_contours: If True, the geometry along surface contours will be unchanged.
    :type preserve_surface_contours: bool, optional
    :param local_remesh_parameters: Tuple of tuples containing the info 
        (entity, maximum triangle edge length, influence area).
    :type local_remesh_parameters: ((trimatic.Object, float, float),), optional
    :param local_growth_rate: Controls the rate of triangle edge length growth (in percentage) as the
        distance from the selected entities increases. Ignored if local_remesh_parameters is empty.
    :type local_growth_rate: float, optional
    :raises: ValueError, RuntimeError
    :return: Remeshed entities
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles)

    :example:

    .. literalinclude:: example/remesh/adaptive_remesh.py
    """

    trimatic.utils.check_resolution("target_triangle_edge_length", target_triangle_edge_length)
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    return pymatic.adaptive_remesh(trimatic.utils.single_or_multiple_entities(entities), target_triangle_edge_length, preserve_surface_contours, local_remesh_parameters, local_growth_rate)

def adaptive_remesh_expert(
    *args,#'force named parameters'
    entities,
    shape_measure = ShapeMeasures.skewness_n, 
    shape_quality_threshold = 0.3,
    maximum_geometrical_error = 0.1732,
    minimum_triangle_edge_length = 0,
    maximum_triangle_edge_length = 1.7321, 
    number_of_iterations = 3, 
    skip_bad_edges = False, 
    preserve_surface_contours = False, 
    preserve_sharp_edges = False,
    local_remesh_parameters = (()), 
    local_growth_rate = 25
    ):
    """Applies adaptive remesh on the specified entities with advanced control parameters.

    :param entities: Either single object or heterogeneous list of parts, surfaces, surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param shape_measure: Method of determining the quality of the triangles in the resulting mesh.
    :type shape_measure: trimatic.ShapeMeasures, optional
    :param shape_quality_threshold: The minimum value that triangles need to meet for the selected shape measure.
    :type shape_quality_threshold: float, optional
    :param maximum_geometrical_error: The maximum distance deviation between the original entity and the output.
    :type maximum_geometrical_error: float, optional
    :param minimum_triangle_edge_length: The minimum triangle edge length in the output. Set to None to disable.  
    :type minimum_triangle_edge_length: float | None, optional
    :param maximum_triangle_edge_length: The maximum triangle edge length in the output. Set to None to disable.
    :type maximum_triangle_edge_length: float | None, optional
    :param number_of_iterations: Increases the number of passes for higher quality but increases computation time.
    :type number_of_iterations: int, optional
    :param skip_bad_edges: If True, bad edges will not be moved.
    :type skip_bad_edges: bool, optional
    :param preserve_surface_contours: If True, the geometry along surface contours will be unchanged.
    :type preserve_surface_contours: bool, optional
    :param preserve_sharp_edges: If True, sharp edges will be preserved.
    :type preserve_sharp_edges: bool, optional
    :param local_remesh_parameters: Tuple of tuples containing the info
        (entity, maximum triangle edge length, influence area).
    :type local_remesh_parameters: ((trimatic.Object, float, float),), optional
    :param local_growth_rate: Controls the rate of triangle edge length growth (in percentage) as the
        distance from the selected entities increases. Ignored if local_remesh_parameters is empty.
    :type local_growth_rate: float, optional
    :return: Remeshed entities
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/remesh/adaptive_remesh_expert.py
    """

    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    if minimum_triangle_edge_length is not None:
        trimatic.utils.check_param_greater_or_equal("minimum_triangle_edge_length", minimum_triangle_edge_length, 0)
    if maximum_triangle_edge_length is not None:
        trimatic.utils.check_resolution("maximum_triangle_edge_length", maximum_triangle_edge_length)
        if ( minimum_triangle_edge_length is not None and minimum_triangle_edge_length > maximum_triangle_edge_length/2. ):
            raise ValueError("Minimum triangle edge length should be smaller than half the maximum triangle edge length")

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasures,))
    trimatic.utils.check_param_in_range("shape_quality_threshold",shape_quality_threshold,0,1)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    if (len(local_remesh_parameters) > 0):  # parameters are non-empty
        if len(pymatic_entities) > 1 :
            raise ValueError("Local remesh parameters should be empty when multiple entities are passed")
        if isinstance(local_remesh_parameters[0], tuple or list): #Tuple of tuples, check max edge length of all
            for parameters in local_remesh_parameters:
                trimatic.utils.check_resolution("maximum_triangle_edge_length", parameters[1])
        else: #only one tuple
            trimatic.utils.check_resolution("maximum_triangle_edge_length", local_remesh_parameters[1])
    return pymatic.adaptive_remesh_expert(pymatic_entities, shape_measure.value, shape_quality_threshold, maximum_geometrical_error, minimum_triangle_edge_length, maximum_triangle_edge_length, number_of_iterations, skip_bad_edges, preserve_surface_contours, preserve_sharp_edges, local_remesh_parameters, local_growth_rate)

def analyze_mesh_quality_surface(
    part,
    shape_measure = ShapeMeasuresAnalyzeMeshQualitySurface.skewness_n, 
    shape_quality_threshold = 0.3
    ):
    """Analyzes (surface) mesh quality and returns simple analysis (% below quality threshold).

    :param part: Part to analyze.
    :type part: trimatic.Part
    :param shape_measure: Method of determining the quality value in the analysis.
    :type shape_measure: trimatic.ShapeMeasuresAnalyzeMeshQualitySurface, optional
    :param shape_quality_threshold: The threshold value that triangles need to meet for the selected shape measure.
    :type shape_quality_threshold: float, optional
    :return: Tuple of analysis results containing (shape measure, shape quality threshold, number of elements not
        meeting threshold, value of element with lowest quality, True/False to indicate if the mesh passed the quality check).
    :rtype: (string, float, int, float, bool)

    :example:

    .. literalinclude:: example/remesh/analyze_mesh_quality_surface.py
    """

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasuresAnalyzeMeshQualitySurface,))
    trimatic.utils.check_param_greater_or_equal("shape_quality_threshold", shape_quality_threshold, 0.0)

    return pymatic.analyze_mesh_quality_surface(part, shape_measure.value, shape_quality_threshold)

def analyze_mesh_quality_volume(
    part,
    shape_measure = ShapeMeasuresAnalyzeMeshQualityVolume.aspect_ratio_a, 
    shape_quality_threshold = 100
    ):
    """Analyzes (volume) mesh quality and returns simple analysis (% below quality threshold).

    :param part: Part to analyze.
    :type part: trimatic.Part
    :param shape_measure: Method of determining the quality value in the analysis.
    :type shape_measure: trimatic.ShapeMeasuresAnalyzeMeshQualityVolume, optional
    :param shape_quality_threshold: The threshold value that triangles need to meet for the selected shape
        measure.
    :type shape_quality_threshold: float, optional
    :return: Tuple of analysis results containing (shape measure, shape quality threshold, number of elements not
        meeting threshold, value of element with lowest quality, True/False to indicate if the mesh passed the quality check).
    :rtype: (string, float, int, float, bool)

    :example:

    .. literalinclude:: example/remesh/analyze_mesh_quality_volume.py
    """

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasuresAnalyzeMeshQualityVolume,))
    trimatic.utils.check_param_greater_or_equal("shape_quality_threshold", shape_quality_threshold, 0.0)

    return pymatic.analyze_mesh_quality_volume(part, shape_measure.value, shape_quality_threshold)

def compute_quality_histogram_surface(
    part,
    shape_measure = ShapeMeasuresAnalyzeMeshQualitySurface.skewness_n,
    bin_size = 0.1,
    upper_limit = None
    ):
    """Analyzes (surface) mesh quality and returns the histogram data.

    :param part: Part to analyze.
    :type part: trimatic.Part
    :param shape_measure: Method of determining the quality value in the analysis.
    :type shape_measure: trimatic.ShapeMeasuresAnalyzeMeshQualitySurface, optional
    :param bin_size: Width of each interval of the histogram.
    :type bin_size: float, optional
    :param upper_limit: The upper limit of the histogram. Values beyond this are excluded from the analysis.
    :type upper_limit: float, optional
    :return: Tuple of histogram bins. Each bin is a tuple containing (minimum bin value, maximum bin value, number of
        elements in bin).
    :rtype: ((float, float, int))

    :example:

    .. literalinclude:: example/remesh/compute_quality_histogram_surface.py
    """

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasuresAnalyzeMeshQualitySurface,))
    trimatic.utils.check_param_greater("bin_size", bin_size, 0.0)

    if upper_limit != None:
        trimatic.utils.check_param_greater_or_equal("upper_limit", upper_limit, 0.0)

    return pymatic.compute_quality_histogram_surface(part, shape_measure.value, bin_size, upper_limit)

def compute_quality_histogram_volume(
    part,
    shape_measure = ShapeMeasuresAnalyzeMeshQualityVolume.aspect_ratio_a,
    bin_size = 0.1,
    upper_limit = None
    ):
    """Analyzes (volume) mesh quality and returns the histogram data.

    :param part: Part to analyze.
    :type part: trimatic.Part
    :param shape_measure: Method of determining the quality value in the analysis.
    :type shape_measure: trimatic.ShapeMeasuresAnalyzeMeshQualitySurface, optional
    :param bin_size: Width of each interval of the histogram.
    :type bin_size: float, optional
    :param upper_limit: The upper limit of the histogram. Values beyond this are excluded from the analysis.
    :type upper_limit: float, optional
    :return: Tuple of histogram bins. Each bin is a tuple containing (minimum bin value, maximum bin value, number of
        elements in bin).
    :rtype: ((float, float, int))

    :example:

    .. literalinclude:: example/remesh/compute_quality_histogram_volume.py
    """

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasuresAnalyzeMeshQualityVolume,))
    trimatic.utils.check_param_greater("bin_size", bin_size, 0.0)

    if upper_limit != None:
        trimatic.utils.check_param_greater_or_equal("upper_limit", upper_limit, 0.0)

    return pymatic.compute_quality_histogram_volume(part, shape_measure.value, bin_size, upper_limit)

def create_non_manifold_assembly_intersection(main_entity, intersecting_entities):
    """Creates an assembly based on the intersection of the parts.

    The result contains non-manifold connections at the intersecting areas. The link with the original entities is also 
    preserved via the names of the surface sets. If the name of these surface sets remain unchanged, the original parts
    structure can be restored using Split Non-manifold Assembly.

    :param main_entity: Main entity
    :type main_entity: trimatic.Part
    :param intersecting_entities: One or more intersecting entities. If more than one entity is specified, the assembly 
        will be created according to the order in the list.
    :type intersecting_entities: trimatic.Part | [trimatic.Part]
    :return: Resulting non-manifold assembly part.
    :rtype: trimatic.Part

    :example:

    .. literalinclude:: example/remesh/create_non_manifold_assembly_intersection.py
    """


    trimatic.utils.check_type("main_entity", main_entity, trimatic.Part)
    trimatic.utils.check_type("intersecting_entities", intersecting_entities, trimatic.Part)
    return pymatic.create_non_manifold_assembly_intersection(main_entity, trimatic.utils.single_or_multiple_entities(intersecting_entities))

def create_non_manifold_assembly_grid(
        main_entity,
        intersecting_entities,
        grid_resolution = 0.1,
        grid_presmoothing_iterations = 2,
        point_smoothing = 0.5,
        smooth_contours = True,
        post_smoothing_compensation = False,
        reduce_triangles = False,
        ):
    """Creates an assembly using a grid conversion method.

    :param main_entity: Main entity.
    :type main_entity: trimatic.Part
    :param intersecting_entities: One or more intersecting entities. If more than one entity is specified, the assembly 
        will be created according to the order in the list.
    :type intersecting_entities: trimatic.Part | [trimatic.Part]
    :param grid_resolution: Size of the grid used for conversion.
    :type grid_resolution: float, optional
    :param grid_presmoothing_iterations: Number of times the grid will be smoothed before converting the
        parts to a grid structure.
    :type grid_presmoothing_iterations: int, optional
    :param point_smoothing: Strength of the grid smoothing.
    :type point_smoothing: float, optional
    :param smooth_contours: If True, bad contours in the resulting assembly will be smoothed.
    :type smooth_contours: bool, optional
    :param post_smoothing_compensation: If True, the smoothing performed after the assembly creation uses a
        shrinkage compensation. This is useful for thin regions.
    :type post_smoothing_compensation: bool, optional
    :param reduce_triangles: If True, the number of triangles of the output assembly will be reduced while
        preserving overall quality.
    :type reduce_triangles: bool, optional
    :return: Resulting non-manifold assembly part.
    :rtype: trimatic.Part

    :example:

    .. literalinclude:: example/remesh/create_non_manifold_assembly_grid.py
    """


    trimatic.utils.check_type("main_entity", main_entity, trimatic.Part)
    trimatic.utils.check_type("intersecting_entities", intersecting_entities, trimatic.Part)
    trimatic.utils.check_resolution("grid_resolution", 0.0001)
    trimatic.utils.check_param_in_range("grid_presmoothing_iterations", grid_presmoothing_iterations, 0, 10)
    trimatic.utils.check_param_in_range("point_smoothing", point_smoothing, 0, 1)
    return pymatic.create_non_manifold_assembly_grid(
        main_entity, 
        trimatic.utils.single_or_multiple_entities(intersecting_entities),
        grid_resolution,
        grid_presmoothing_iterations,
        point_smoothing,
        smooth_contours,
        post_smoothing_compensation,
        reduce_triangles)

class ElementType(Enum):
    """Volume mesh element type."""

    Tet4 = "Tet 4"
    """Tet 4 volume mesh element type."""

    Tet10 = "Tet 10"
    """Tet 10 volume mesh element type."""

def create_volume_mesh(
    part,
    element_type = ElementType.Tet4,
    project_midpoint_entity = None,
    maximum_edge_length = None,
    solid_volume_only = False,
    group_by_materials = False,
    local_remesh_parameters = (()),
    local_growth_rate = 25
    ):
    """Creates a volume mesh from a triangulated surface.

    :param part: Single part.
    :type part: trimatic.Part
    :param element_type: Element type of the volume mesh.
    :type element_type: trimatic.ElementType, optional
    :param project_midpoint_entity: Target entity to project midpoints of Tet10 elements. Set to None to disable.
    :type project_midpoint_entity: trimatic.Part | None, optional
    :param maximum_edge_length: The maximum triangle edge length in the output. Set to None to disable.
    :type maximum_edge_length: float | None, optional
    :param solid_volume_only: If True, will create a volume based on solid part only.
    :type solid_volume_only: bool, optional
    :param group_by_materials: If True, volumes will be grouped based on the surface name information.
    :type group_by_materials: bool, optional
    :param local_remesh_parameters: Tuple of tuples containing the info
        (entity, maximum triangle edge length, influence area).
    :type local_remesh_parameters: ((trimatic.Object, float, float),), optional
    :param local_growth_rate: Controls the rate of tetrahedra growth (in percentage) as the
        distance from the selected entities increases. Ignored if local_remesh_parameters is empty.
    :type local_growth_rate: float, optional
    :return: Volume mesh.
    :rtype: trimatic.VolumeMesh
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/remesh/create_volume_mesh.py
    """


    if element_type is ElementType.Tet10:
        trimatic.utils.check_type("project_midpoint_entity", project_midpoint_entity, (trimatic.Part, None), True)
    else:
        trimatic.utils.check_type("project_midpoint_entity", project_midpoint_entity, (None,), True)

    if maximum_edge_length is not None:
        trimatic.utils.check_resolution("maximum_edge_length", maximum_edge_length)
    
    trimatic.utils.check_type("part", part, trimatic.Part)
    trimatic.utils.check_type("element_type", element_type, (ElementType,))
    trimatic.utils.check_param_in_range("local_growth_rate", local_growth_rate, 0, 100)

    return pymatic.create_volume_mesh(part, element_type.value, project_midpoint_entity, maximum_edge_length, solid_volume_only, group_by_materials, local_remesh_parameters, local_growth_rate)

def quality_preserving_reduce_triangles(
    *args,#'force named parameters'
    entities,
    shape_measure = ShapeMeasures.skewness_n,
    shape_quality_threshold = 0.3,
    maximum_geometrical_error = 0.1732,
    maximum_triangle_edge_length = None,
    number_of_iterations = 3,
    skip_bad_edges = False,
    preserve_surface_contours = False):
    """Reduces number of triangles in a high-quality mesh while preserving its quality.

    :param entities: Either single object or heterogeneous list of parts, surfaces, surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet] | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :param shape_measure: Method of determining the quality of the triangles in the resulting mesh.
    :type shape_measure: trimatic.ShapeMeasures, optional
    :param shape_quality_threshold: The minimum value that triangles need to meet for the selected shape measure.
    :type shape_quality_threshold: float, optional
    :param maximum_geometrical_error: The maximum distance deviation between the original entity and the output.
    :type maximum_geometrical_error: float, optional
    :param maximum_triangle_edge_length: The maximum triangle edge length in the output. Set to None to disable.
    :type maximum_triangle_edge_length: float, optional
    :param number_of_iterations: Increases the number of passes for higher quality but increases computation time.
    :type number_of_iterations: int, optional
    :param skip_bad_edges: If True, bad edges will not be moved.
    :type skip_bad_edges: bool, optional
    :param preserve_surface_contours: If True, the geometry along surface contours will be unchanged.
    :type preserve_surface_contours: bool, optional
    :return: Remeshed entities.
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)

    :example:

    .. literalinclude:: example/remesh/quality_preserving_reduce_triangles.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    if maximum_triangle_edge_length is not None:
        trimatic.utils.check_resolution("maximum_triangle_edge_length", maximum_triangle_edge_length)

    trimatic.utils.check_type("shape_measure", shape_measure, (ShapeMeasures,))
    trimatic.utils.check_param_in_range("shape_quality_threshold",shape_quality_threshold,0,1)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    return pymatic.quality_preserving_reduce_triangles(pymatic_entities, shape_measure.value, shape_quality_threshold, maximum_geometrical_error,  maximum_triangle_edge_length, number_of_iterations, skip_bad_edges, preserve_surface_contours)

def split_non_manifold_assembly_surface(entity, interface_entity = None):
    """Splits a non-manifold assembly into it's surface parts.

    :param entity: Entity to split.
    :type entity: trimatic.Part
    :param interface_entity: When interface_entity is None, the assembly will be split based on surface set names
        created by the Create Non-manifold Assembly operation. When  interface_entity is not None, this is the surface set
        that contains the interface surfaces between the two different parts of the assembly.
    :type interface_entity: trimatic.SurfaceSet, optional
    :return: Split parts.
    :rtype: (trimatic.Part)

    :example:

    .. literalinclude:: example/remesh/split_non_manifold_assembly_surface.py
    """

    trimatic.utils.check_type("entity", entity, trimatic.Part)
    if interface_entity is not None:
      trimatic.utils.check_type("interface_entity", interface_entity, trimatic.SurfaceSet)

    return pymatic.split_non_manifold_assembly_surface(entity, interface_entity)

def split_non_manifold_assembly_volume(entity):
    """Splits a non-manifold assembly into its volume parts.

    The assembly will be split based on its volume meshes; for this method, the input entity must contain at least 2 volume meshes.

    :param entity: Entity to split
    :type entity: trimatic.Part
    :return: Split parts.
    :rtype: (trimatic.Part)

    :example:

    .. literalinclude:: example/remesh/split_non_manifold_assembly_volume.py
    """


    trimatic.utils.check_type("entity", entity, trimatic.Part)
    return pymatic.split_non_manifold_assembly_volume(entity)

def uniform_remesh(
    *args,#'force named parameters'
    entities,
    target_triangle_edge_length = 1.0,
    preserve_sharp_edge_angle = None,
    preserve_surface_contours = False,
    split_edge_factor = 0.2,
    skip_bad_edges = False
    ):
    """Applies uniform remesh on the specified entities.
 
    :param entities: Either single object or heterogeneous list of parts, surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param target_triangle_edge_length: The approximate triangle edge length in the output.
    :type target_triangle_edge_length: float, optional 
    :param preserve_sharp_edge_angle: Edges with angles greater than this value will be preserved. Set to None to disable.
    :type preserve_sharp_edge_angle: float, optional
    :param preserve_surface_contours: If True, the geometry along surface contours will be unchanged.
    :type preserve_surface_contours: bool, optional
    :param split_edge_factor: Controls the size of the minimum edge length during the subdivision of large triangles.
    :type split_edge_factor: float | None, optional
    :param skip_bad_edges: If True, the bad edges will not be modified during the operation.
    :type skip_bad_edges: bool, optional
    :return: Remeshed entities.
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/remesh/uniform_remesh.py
    """

    trimatic.utils.check_resolution("target_triangle_edge_length", target_triangle_edge_length)
    if preserve_sharp_edge_angle is not None:
        trimatic.utils.check_param_in_range("preserve_sharp_edge_angle", preserve_sharp_edge_angle, 0, 180)
    trimatic.utils.check_param_in_range("split_edge_factor", split_edge_factor, trimatic.utils.get_resolution(), 1)
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    return pymatic.uniform_remesh(trimatic.utils.single_or_multiple_entities(entities), target_triangle_edge_length, preserve_sharp_edge_angle, preserve_surface_contours, split_edge_factor, skip_bad_edges)
