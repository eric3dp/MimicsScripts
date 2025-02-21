import pymatic
import trimatic.utils

from trimatic.data import TriangulationAccuracy

from enum import Enum

def auto_adjust_normals(entities):
    """Adjust normals of the input parts.

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Fixed parts
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/auto_adjust_normals.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    return pymatic.auto_adjust_normals(trimatic.utils.single_or_multiple_entities(entities))

def auto_fix(entities):
    """Performs auto fix on selected parts using the Automatic method, which includes filtering and small shell removal.

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Fixed parts
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/auto_fix.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    return pymatic.auto_fix(trimatic.utils.single_or_multiple_entities(entities))

def fill_hole_freeform(entities, accuracy = trimatic.TriangulationAccuracy.Coarse, treat_as_one_hole = False, tangent = False):
    """The freeform hole filler will use a freeform surface. This functions corresponds to the GUI behavior with the Fill Algorithm "Advanced" and Method "Automatic".
    
    :param entities: Entities to fill.
    :type entities: trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles | [trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles]
    :param accuracy: Accuracy of the triangulation.
    :type accuracy: trimatic.TriangulationAccuracy, optional
    :param tangent: When True, the surface will be created tangentially to the surrounding surface(s).
    :type tangent: bool, optional
    :param treat_as_one_hole: If True, 3-matic will interpret the selection as being the contours of one surface and create only one.
    :type treat_as_one_hole: bool, optional
    :return: Surface(s) that were created to fill the hole(s).
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError
    :example:
    
    .. literalinclude:: example/fix/fill_hole_freeform.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceContour, trimatic.Curve, trimatic.CurveSet, trimatic.MarkedTriangles ))
    return pymatic.fill_hole_freeform(trimatic.utils.single_or_multiple_entities(entities), accuracy.value, treat_as_one_hole, tangent)

def fill_hole_freeform_expert(entities, grid_size = 3, treat_as_one_hole = False, tangent = False):
    """The freeform hole filler will use a freeform surface. This functions corresponds to the GUI behavior with Fill Algorithm "Normal".
    
    :param entities: Entities to fill.
    :type entities: trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles | [trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles]
    :param grid_size: The size of the triangles that will create the surface.
    :type grid_size: float, optional
    :param tangent: When True, the surface will be created tangentially to the surrounding surface(s).
    :type tangent: bool, optional
    :param treat_as_one_hole: If True, 3-matic will interpret the selection as being the contours of one surface and create only one.
    :type treat_as_one_hole: bool, optional
    :return: Surface(s) that were created to fill the hole(s).
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError
    :example:
    
    .. literalinclude:: example/fix/fill_hole_freeform_expert.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Curve, trimatic.CurveSet, trimatic.MarkedTriangles ))
    trimatic.utils.check_resolution("grid_size", grid_size)
    return pymatic.fill_hole_freeform_expert(trimatic.utils.single_or_multiple_entities(entities), grid_size, treat_as_one_hole, tangent)

def fill_hole_normal(entities, treat_as_one_hole = False):
    """Fills the hole with the fastest and easiest triangulation.
    
    :param entities: Entities to fill.
    :type entities: trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles | [trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles]
    :param treat_as_one_hole: If True, 3-matic will interpret the selection as being the contours of one surface and create only one.
    :type treat_as_one_hole: bool, optional
    :return: Surface(s) that were created to fill the hole(s).
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/fill_hole_normal.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Curve, trimatic.CurveSet, trimatic.MarkedTriangles ))
    return pymatic.fill_hole_normal(trimatic.utils.single_or_multiple_entities(entities), treat_as_one_hole)

def fill_hole_ruled(entities, direction):
    """The ruled hole filler directs the triangulation according to the specified direction. 
    
    :param entities: Entities to fill.
    :type entities: trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles | [trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles]
    :param direction: Direction along which the triangulation of the hole will be performed.
    :type direction: float, optional
    :return: Surface(s) that were created to fill the hole(s).
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError
    :example:
    
    .. literalinclude:: example/fix/fill_hole_ruled.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Curve, trimatic.CurveSet, trimatic.MarkedTriangles ))
    pymatic_direction = trimatic.utils.point_argument(direction)
    trimatic.utils.check_direction("direction", pymatic_direction)

    return pymatic.fill_hole_ruled(trimatic.utils.single_or_multiple_entities(entities), pymatic_direction)

class FilterSharpTriangleMode(Enum):
    """Mode for filter sharp triangle."""

    Collapse = "Collapse"
    Delete = "Delete"


def filter_sharp_triangles(entities, filter_distance=0.0100, threshold_angle=5.0000, filter_mode=FilterSharpTriangleMode.Collapse):
    """ Removes sharp, thin and long triangles of the selected parts.

    :param entities: Either a single object or heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param filter_distance: Triangles with an edge or height smaller than this distance will be filtered.
    :type filter_distance: float, optional
    :param threshold_angle: A triangle will be filtered when the angle it makes with its neighbors is larger than the threshold angle.
    :type threshold_angle: float, optional
    :param filter_mode: 2 Options - Collapse and Delete.
        With Collapse, the thin triangle will be removed and its neighbours will be connected to each other.
        With Delete, the thin triangle will be deleted, and bad edges will appear.
    :type filter_mode: FilterSharpTriangleMode, optional
    :return: Fixed input entities.
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/filter_sharp_triangles.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_param_in_range("threshold_angle", threshold_angle, 0, 180)
    trimatic.utils.check_resolution("filter_distance", filter_distance)
    trimatic.utils.check_type("filter_mode", filter_mode, (FilterSharpTriangleMode,))

    return pymatic.filter_sharp_triangles(trimatic.utils.single_or_multiple_entities(entities), filter_distance,
                                          threshold_angle, filter_mode.value)

def filter_small_edges(entities, filter_distance=0.0010, threshold_angle=30.0000, number_of_iterations=3,
                       surface_border_only=True):
    """ Removes small edges of the selected parts.
    
    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :param filter_distance: Triangles with an edge or height smaller than this distance are filtered.
    :type filter_distance: float, optional
    :param threshold_angle: A triangle will be filtered when the angle it makes with its neighbors is larger than the threshold angle.
    :type threshold_angle: float, optional
    :param number_of_iterations: The number of iterations to filter the small edges.
    :type number_of_iterations: int, optional
    :param surface_border_only: If True, only edges situated on a surface border of the selected part are filtered.
    :type surface_border_only: bool, optional
    :return: Fixed parts
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/filter_small_edges.py
    """


    trimatic.utils.check_type("entities", entities, trimatic.Part)
    trimatic.utils.check_resolution("filter_distance", filter_distance)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 0)

    return pymatic.filter_small_edges(trimatic.utils.single_or_multiple_entities(entities), filter_distance,
                                      threshold_angle, number_of_iterations, surface_border_only)

def filter_small_shells(
        entities,
        threshold_area=10.0,
        threshold_volume=10.0,
        threshold_relative=True
):
    """Removes small noisy shells from the parts.
    
    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :param threshold_area: Area threshold (in terms of percentage or absolute value depending on threshold_relative).
    :type threshold_area: float, optional
    :param threshold_volume: Volume threshold (in terms of percentage or absolute value depending on threshold_relative).
    :type threshold_volume: float, optional
    :param threshold_relative: If True, thresholds values are interpreted as percentage; if False, the absolute values are taken.
    :type threshold_relative: bool, optional
    :return: Fixed parts
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/filter_small_shells.py
    """


    trimatic.utils.check_type("entities", entities, trimatic.Part)
    if threshold_relative:
        trimatic.utils.check_param_between("threshold_area", threshold_area, 0, 100)
        trimatic.utils.check_param_between("threshold_volume", threshold_volume, 0, 100)
    else:
        trimatic.utils.check_param_greater_or_equal("threshold_area", threshold_area, 0)
        trimatic.utils.check_param_greater_or_equal("threshold_volume", threshold_volume, 0)
    return pymatic.filter_small_shells(trimatic.utils.single_or_multiple_entities(entities), threshold_area,
                                       threshold_volume, threshold_relative)

def get_number_of_intersecting_triangles(entity):
    """Returns the number of intersecting triangles.
    
    :param entity: The part from which a user wants the number of intersecting triangles.
    :type entity: trimatic.Part
    :return: Returns the number of intersecting triangles.
    :rtype: int
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/get_number_of_intersecting_triangles.py
    """

    trimatic.utils.check_type("entity", entity, trimatic.Part)


    return pymatic.get_number_of_intersecting_triangles(entity)

def get_number_of_overlapping_triangles(entity):
    """Returns the number of overlapping triangles.
    
    :param entity: The part from which a user wants the number of overlapping triangles.
    :type entity: trimatic.Part
    :return: Returns the number of overlapping triangles.
    :rtype: int
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/get_number_of_overlapping_triangles.py
    """

    trimatic.utils.check_type("entity", entity, trimatic.Part)


    return pymatic.get_number_of_overlapping_triangles(entity)

def improve_mesh(entities, shape_quality_high = False, maximum_geometrical_error = 0.05, maximum_edge_length = 20.0):
    """Improves the meshes of the selected entities.

    :param entities: Either single object or a heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param shape_quality_high: If True, the original mesh will be converted into high quality triangles.
    :type shape_quality_high: bool, optional
    :param maximum_geometrical_error: No geometrical error higher than this value will be introduced.
    :type maximum_geometrical_error: float, optional
    :param maximum_edge_length: The maximum triangle edge length in the output.
    :type maximum_edge_length: float, optional
    :return: Entities with improved meshes.
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/improve_mesh.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_resolution("maximum_edge_length", maximum_edge_length)
    return pymatic.improve_mesh(trimatic.utils.single_or_multiple_entities(entities), shape_quality_high, maximum_geometrical_error, maximum_edge_length)

def invert_normal(entities):
    """Inverts the normal of all triangles of part, surface, or surface sets.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :return: Entities with the normals inverted
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/invert_normal.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    return pymatic.invert_normal(trimatic.utils.single_or_multiple_entities(entities))

def reduce(entities, flip_threshold_angle = 15.0, geometrical_error = 0.0500, number_of_iterations = 5, preserve_surfaces = False):
    """This function reduces the number of triangles in a chosen entity. 
    The number of triangles will be as small as possible within given geometric error constraints.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets.
    :type  entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param flip_threshold_angle:
           This parameter avoids that triangles will flip during the reduce process. It determines the
           maximum allowed deviation between the normals of the triangles before and after the reduction.
    :type  flip_threshold_angle: float, optional
    :param geometrical_error: Maximum error that can be produced by the reduction.
    :type  geometrical_error: float, optional
    :param number_of_iterations: Higher number of iterations will further reduce the entity’s number of triangles.
    :type  number_of_iterations: int, optional
    :param preserve_surfaces: If True, the geometry of surface contours will be preserved during reduction.
           This is useful when there are surfaces defined that are not based on the part geometry.
    :type  preserve_surfaces: bool, optional

    :return: Reduced parts
    :rtype:  trimatic.Part | trimatic.Surface | trimatic.SurfaceSet |
             (trimatic.Part) | (trimatic.Surface) | (trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/reduce.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    trimatic.utils.check_param_in_range("flip_threshold_angle", flip_threshold_angle, 0, 180)

    return pymatic.reduce(trimatic.utils.single_or_multiple_entities(entities), flip_threshold_angle, geometrical_error,
                          number_of_iterations, preserve_surfaces)


def reduce_quality_preserving(entities, quality_threshold = 0.3, geometrical_error = 0.0500, number_of_iterations = 3, preserve_surfaces = False):
    """This function reduces the number of triangles in a chosen entity. 
    The number of triangles will be as small as possible within given geometric error constraints, and
    besides that, it does not create any triangle with quality worse than the specified quality threshold.

    :param entities: Either a single object or a heterogeneous list of parts, surfaces, or surface sets.
    :type  entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param quality_threshold:
           Choose a triangle quality between 1 (all sides of the triangle are equal) and 0 (collapsed triangle).
    :type  quality_threshold: float, optional
    :param geometrical_error: Maximum error that can be produced by the reduction.
    :type  geometrical_error: float, optional
    :param number_of_iterations: Higher number of iterations will further reduce the entity’s number of triangles.
    :type  number_of_iterations: int, optional
    :param preserve_surfaces: If True, the geometry of surface contours will be preserved during the reduction.
           This is useful when there are surfaces defined that are not based on the part geometry.
    :type  preserve_surfaces: bool, optional

    :return: Reduced parts
    :rtype:  trimatic.Part | trimatic.Surface | trimatic.SurfaceSet |
             (trimatic.Part) | (trimatic.Surface) | (trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/reduce_quality_preserving.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    trimatic.utils.check_param_in_range("quality_threshold", quality_threshold, 0.1, 1.0)

    return pymatic.reduce_quality_preserving(trimatic.utils.single_or_multiple_entities(entities), quality_threshold,
                                             geometrical_error, number_of_iterations, preserve_surfaces)

def remove_spikes(
    *args,#'force named parameters'
    entities,
    spike_size = 1,
    smallest_detail = 1,
    reduce = True,
    preserve_surface_structure = False):
    """Remove unwanted spike shaped noise on parts.

    :param entities: Either single object or a list of parts, surface or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param spike_size: The average size of spikes that will be removed. The value must be greater than or equal to the smallest detail.
    :type spike_size: float, optional
    :param smallest_detail: Targeted size of triangles of the part.
    :type smallest_detail: float, optional
    :param reduce: If True, triangle reduction will be applied to the parts.
    :type reduce: bool, optional
    :param preserve_surface_structure: If True, the original surface structure and the surface color will be preserved.
    :type preserve_surface_structure: bool, optional

    :return: Part after spikes are removed.
    :rtype: trimatic.Part
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/remove_spikes.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_resolution("smallest_detail", smallest_detail)
    trimatic.utils.check_resolution("spike_size", spike_size)
  
    return pymatic.remove_spikes(trimatic.utils.single_or_multiple_entities(entities), 
                                 spike_size, 
                                 smallest_detail, 
                                 reduce,
                                 preserve_surface_structure)

def shells_to_parts(entities):
    """This function creates one part from each shell in the specified part(s).

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Single part or a tuple of parts.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/shells_to_parts.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    return pymatic.shells_to_parts(trimatic.utils.single_or_multiple_entities(entities))

class SmoothMethod(Enum):
    """Smooth method for smooth."""

    first_order_laplacian = "First Order Laplacian"
    second_order_laplacian = "Second Order Laplacian"
    curvature = "Curvature"

def smooth(
    entities, 
    smooth_method = SmoothMethod.first_order_laplacian,
    smooth_factor = 0.7,
    perform_post_processing = True
    ):
    """Smooths entities with simplified parameters.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param smooth_method: Method used to smooth the selected entities.
    :type smooth_method: trimatic.SmoothMethod, optional
    :param smooth_factor: Strength of smoothing – higher values give better smoothing but may change geometry
    :type smooth_factor: float, optional
    :param perform_post_processing: When True, postprocessing will be performed after smoothing
    :type perform_post_processing: bool, optional
    :return: Smoothed entities
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/smooth.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_type("smooth_method", smooth_method, (SmoothMethod,))
    trimatic.utils.check_param_in_range("smooth_factor", smooth_factor, 0, 1)
    return pymatic.smooth(trimatic.utils.single_or_multiple_entities(entities), smooth_method.value, smooth_factor, perform_post_processing)

def split_surface(entities):
    """This function creates multiple surfaces if the given surface has unconnected triangles.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :return: Surface or tuple of surfaces.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/split_surface.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet ))
    return pymatic.split_surface(trimatic.utils.single_or_multiple_entities(entities))

def stitch(entities, tolerance=0.01, iteration=5):
    """Stitches small holes in the mesh by moving triangle nodes.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param tolerance: Maximum distance that a point will be moved to fill a gap.
    :type tolerance: float, optional
    :param iteration: Number of times the stitch algorithm will be applied.
    :type iteration: int, optional
    :return: Stitched entities
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/stitch.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_param_greater_or_equal("tolerance", tolerance, 0.0)
    trimatic.utils.check_param_greater("iteration", iteration, 0)

    return pymatic.stitch(trimatic.utils.single_or_multiple_entities(entities), tolerance, iteration)

def subdivide(entities, number_of_iterations = 1, maximum_edge_length = None):
    """This operation increases the number of triangles in the chosen entity by splitting triangles into smaller ones.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param number_of_iterations: Number of subdivide iterations.
    :type number_of_iterations: int, optional
    :param maximum_edge_length: When specified, only subdivide triangles with an edge longer than this length. When not specified, all triangles are subdivided.
    :type maximum_edge_length: float, optional
    :return: Subdivided entities
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/subdivide.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 0)
    if maximum_edge_length is not None:
        trimatic.utils.check_param_greater_or_equal("maximum_edge_length", maximum_edge_length, 0)
    return pymatic.subdivide(trimatic.utils.single_or_multiple_entities(entities), number_of_iterations, maximum_edge_length)

def surface_sets_to_parts(entities):
    """This operation creates one part from each surface set in the specified part(s).

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Single part or a tuple of parts.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/surface_sets_to_parts.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    return pymatic.surface_sets_to_parts(trimatic.utils.single_or_multiple_entities(entities))

def surfaces_to_parts(entities):
    """This operation creates one part from each surface in the specified part(s).

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Single part or a tuple of parts.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/surfaces_to_parts.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    return pymatic.surfaces_to_parts(trimatic.utils.single_or_multiple_entities(entities))

def unify(entities):
    """This operation preserves the outer triangles, and deletes all the inner triangles for each entity.

    :param entities: Either single part or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Single part or a tuple of parts.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/fix/unify.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    return pymatic.unify(trimatic.utils.single_or_multiple_entities(entities))
