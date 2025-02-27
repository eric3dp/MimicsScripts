import pymatic
import trimatic.utils

from enum import Enum

def attach_curve(entities, target_entities = None, distance_threshold = 5.0000):
    """Attaches curve(s) to the specified part(s)/surface(s). The curve is first attracted and then attached.

    :param entities: Either single object or list of curves, curve sets or sketches.
    :type entities: trimatic.Curve | trimatic.CurveSet | trimatic.Sketch | [trimatic.Curve | trimatic.CurveSet | trimatic.Sketch] | (trimatic.Curve | trimatic.CurveSet | trimatic.Sketch)
    :param target_entities: The target entities that the curves will be attached to. If set to None, the
      curves will be attached to the part they currently belong to.
    :type target_entities: trimatic.Part | trimatic.Surface | [trimatic.Part | trimatic.Surface], optional
    :param distance_threshold: Curve segments that are within the distance threshold will be attached.
    :type distance_threshold: float, optional
    :return: Attached curve(s).
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/attach_curve.py
    """
    return attract_curve(entities,target_entities,distance_threshold,True)

def attract_curve(entities, target_entities = None, distance_threshold = 5.0000, attach_curve = True):
    """Attracts curve(s) to the specified part(s)/surface(s).

    If multiple curves are specified as input, operation will succeed if at least one of the curves is successfully
    attracted.

    :param entities: Either single object or list of curves, curve sets or sketches.
    :type entities: trimatic.Curve | trimatic.CurveSet | trimatic.Sketch | [trimatic.Curve | trimatic.CurveSet | trimatic.Sketch] | (trimatic.Curve | trimatic.CurveSet | trimatic.Sketch)
    :param target_entities: The target entities that the curves will be attracted to. If set to None, the
        curves will be attracted to the part they currently belong to.
    :type target_entities: trimatic.Part | trimatic.Surface | [trimatic.Part | trimatic.Surface], optional
    :param distance_threshold: Curve segments that are within the distance threshold will be attracted.
    :type distance_threshold: float, optional
    :param attach_curve: If True, the target_entities will be retriangulated and the curve will be attached
        to the part.
    :type attach_curve: bool, optional
    :return: Attracted curve(s).
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/attract_curve.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Sketch)) 
    pymatic_target_entities = trimatic.utils.single_or_multiple_entities(target_entities)
    trimatic.utils.check_type("target_entities", pymatic_target_entities, ( trimatic.Part, trimatic.Surface, trimatic.SurfaceSet), allow_none_or_empty = True)
    trimatic.utils.check_param_greater_or_equal("distance_threshold", distance_threshold, 0)

    return pymatic.attract_curve(pymatic_entities, pymatic_target_entities, distance_threshold, attach_curve)

def connect_curves(entities, distance_threshold = 0.1):
    """Connects curves together.If there is a small overlap, this will be removed.

    If there is a small gap between the endings of two selected curves, they will be connected with a free curve, 
    if the gap is smaller than a specified distance.

    :param entities: List of curves to connect.
    :type entities: [trimatic.Curve]
    :param distance_threshold: Curve endings that are within the distance threshold will be connected and merged.
    :type distance_threshold: float, optional
    :return: Connected curve.
    :rtype: trimatic.Curve
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/connect_curves.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Curve,)) 
    trimatic.utils.check_entities_only_contain_open_curves("entities", entities)
    trimatic.utils.check_param_greater_or_equal("distance_threshold", distance_threshold, 0)
    trimatic.utils.check_entities_must_be_multiple("entities",entities)

    return pymatic.connect_curves(pymatic_entities, distance_threshold)

def convert_to_curve(entities, accuracy = 0.05, add_to = None):
    """The analytical line and arc, but also all contours can be converted with this operation.

    :param entities: Entities you like to convert.
    :type entities: trimatic.Arc | trimatic.Line | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Arc | trimatic.Line | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param accuracy: The maximum deviation between the input entity and the output curve.
    :type accuracy: float, optional
    :param add_to: Target part to add the resulting curve to. If set to None, a new part is created.
    :type add_to: trimatic.Part, optional
    :return: If add_to is None, a part is created. Otherwise, a curve is created.
    :rtype: trimatic.Part | trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/convert_to_curve.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Arc, trimatic.Line, trimatic.SurfaceBorder, trimatic.SurfaceContour)) 
    trimatic.utils.check_param_greater("accuracy", accuracy, 0)
    trimatic.utils.check_type("add_to", add_to,(trimatic.Part,), True)

    return pymatic.convert_to_curve(pymatic_entities, accuracy, add_to)

def fit_centerline_curve(entity, segment_length = 1.0, detail = 1.0):
    """Creates center line(s) for the given part. The center line is kept as a curve inside a curve set.

    :param entity: Part for which center line is created.
    :type entity: trimatic.Part
    :param segment_length: Value defines the length of the different segments of the center line.
    :type segment_length: float
    :param detail: Value defines the accuracy of the center line definition.
    :type detail: float
    :return: If successful, a center line is returned. Otherwise, a runtime error is raised.
    :rtype: trimatic.CurveSet
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/fit_centerline_curve.py
    """

    trimatic.utils.check_type('entity', entity, (trimatic.Part))
    trimatic.utils.check_param_greater_or_equal('segment_length', segment_length, trimatic.utils.get_resolution())
    trimatic.utils.check_param_greater_or_equal('detail', detail, trimatic.utils.get_resolution())

    return pymatic.fit_centerline_curve(entity, segment_length, detail)

def create_curve(points, part = None):
    """Creates a free curve from a list of points.

    :param points: List of points representing the curve nodes. Points are specified with tuples of (x,y,z) coordinates. 
    :type points: [trimatic.Point]
    :param part: Target part to add the resulting curve to. If set to None, a new part is created.
    :type part: trimatic.Part, optional
    :return: The curve.
    :rtype: trimatic.Curve
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_curve.py
    """


    trimatic.utils.check_type("part", part,(trimatic.Part,), True)
    return pymatic.create_curve(trimatic.utils.point_sequence_argument(points),part)

def create_geometry_curve_angle_based(entities, angle = 30.0000):
    """Creates curves on the common edge of two triangles that make an angle larger than the specified angle.

    :param entities: Either single object or list of parts, surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param angle: If the angle between the normal of two triangles is bigger than the defined threshold, a curve is 
        created on the common edge.
    :type angle: float, optional
    :return: The created geometry curves.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_geometry_curve_angle_based.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part,trimatic.Surface,trimatic.SurfaceSet)) 

    return pymatic.create_geometry_curve_angle_based(pymatic_entities, angle)

class CurvatureType(Enum):
    """Curvature type for curvature based geometry curve."""

    gaussian = "Gaussian"
    mean = "Mean"
    minimal = "Minimal"
    maximal = "Maximal"

def create_geometry_curve_curvature_based(entities, curvature_type = CurvatureType.maximal, radius_threshold = 16.0000, sharp_edge_threshold = 30.0000):
    """Creates curves where the surface has a curvature specified by the input parameters.

    :param entities: Either single object or list of parts, surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param curvature_type: Method used to calculate curvature information.
    :type curvature_type: trimatic.CurvatureType, optional
    :param radius_threshold: Threshold of the average triangle curvature. A curve is created on the common edge of two 
        triangles when one triangle has a curvature smaller than the threshold and the other triangle has a curvature 
        bigger than the threshold.
    :type radius_threshold: float, optional
    :param sharp_edge_threshold: If the angle between two triangles is smaller than the defined threshold, the common 
        edge is considered sharp. Whether a curve is created on the comon triangle edge depends on the radius threshold.
    :type sharp_edge_threshold: float, optional
    :return: The created geometry curves.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_geometry_curve_curvature_based.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part,trimatic.Surface,trimatic.SurfaceSet)) 
    trimatic.utils.check_type("curvature_type", curvature_type, (CurvatureType,))
    trimatic.utils.check_param_greater("radius_threshold", radius_threshold, 0)
    trimatic.utils.check_param_greater("sharp_edge_threshold", sharp_edge_threshold, 0)

    return pymatic.create_geometry_curve_curvature_based(pymatic_entities, curvature_type.value, radius_threshold, sharp_edge_threshold)

def create_geometry_curve_draft_based(entities, direction, draft_angle = 0.0000):
    """Creates curves where the surface changes direction specified by the draft direction.

    :param entities: Either single object or list of parts, surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param direction: Direction vector, specified as a tuple of (x,y,z). The direction towards which the draft is defined.
    :type direction: (float, float, float)
    :param draft_angle: If the angle w.r.t. the draft direction is bigger than the defined threshold, the triangle is 
        considered drafted.
    :type draft_angle: float, optional
    :return: The created geometry curves.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_geometry_curve_draft_based.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part,trimatic.Surface,trimatic.SurfaceSet)) 
    trimatic.utils.check_vector_not_equal("direction", direction, [0, 0, 0])
    trimatic.utils.check_param_between("draft_angle", draft_angle, -90.0000, 90.0000)

    return pymatic.create_geometry_curve_draft_based(pymatic_entities, trimatic.utils.point_argument(direction), draft_angle)

def create_intersection_curve(entity_set1, entity_set2, intersection_curve_in = 2):
    """Creates curves representing the intersection lines of two sets of entities.

    :param entity_set1: First set of entities. Either single object or heterogeneous list of parts, surfaces, or surface
        sets.
    :type entity_set1: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param entity_set2: Second set of entities. Either single object or heterogeneous list of parts, surfaces, surface
        sets, or planes.
    :type entity_set2: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Plane | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Plane]
    :param intersection_curve_in: Flag to determine which entity set will contain the output curves. 0 for
        entity from first set, 1 for entity from second set and 2 for both entities.
    :type intersection_curve_in: int, optional
    :return: Intersection curves. Empty tuple if no intersection exists.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_intersection_curve.py
    """


    trimatic.utils.check_entity_sets_do_not_contain_equal_entities("entity_set1", "entity_set2", entity_set1, entity_set2)
    trimatic.utils.check_entity_set_does_not_have_surface_or_surface_set_of_another_entity_set("entity_set1", "entity_set2", entity_set1, entity_set2)
    trimatic.utils.check_entity_set_does_not_have_surface_or_surface_set_of_another_entity_set("entity_set2", "entity_set1", entity_set2, entity_set1)
    trimatic.utils.check_type("entity_set1", entity_set1,
                              (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_type("entity_set2", entity_set2,
                              (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.Plane))
    return pymatic.create_intersection_curve(trimatic.utils.single_or_multiple_entities(entity_set1),
                                             trimatic.utils.single_or_multiple_entities(entity_set2),
                                             intersection_curve_in)

class DirectionMethod(Enum):
    """Method for direction of isocurves."""

    inside = "Inside"
    outside = "Outside"
    both = "Both"

def create_iso_curves(entities, interval_distance = 1.0, number_of_copies = 1, direction = DirectionMethod.outside):
    """Creates isocurves from the specified attached curves.

    :param entities: One or more reference curves.
    :type entities: trimatic.Curve | trimatic.SurfaceContour | [trimatic.Curve | trimatic.SurfaceContour]
    :param interval_distance: Distance at which the isocurve will be created from the reference.
    :type interval_distance: float, optional
    :param number_of_copies: Number of isocurves that should be created in the defined direction.
    :type number_of_copies: int, optional
    :param direction: Direction at which the isocurve will be created.
    :type direction: trimatic.DirectionMethod, optional
    :return: The created isocurves.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/create_iso_curves.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Curve, trimatic.SurfaceContour)) 
    trimatic.utils.check_param_greater_or_equal("interval_distance", interval_distance, 0)
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 1)
    trimatic.utils.check_type("direction", direction, (DirectionMethod,))

    return pymatic.create_iso_curves(pymatic_entities, interval_distance, number_of_copies, direction.value)

def filter_curve(entities, sharp_angle_threshold = 20.0, small_edge_threshold = 0.1, treat_as_free_curve = True):
    """Filters curves.

    :param entities: Entities to filter.
    :type entities: trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param sharp_angle_threshold: Curve segments with angles smaller than the threshold will be removed.
    :type sharp_angle_threshold: float, optional
    :param small_edge_threshold: Curve segments with edges smaller than the threshold will be removed.
    :type small_edge_threshold: float, optional
    :param treat_as_free_curve: If True, changes to the curve do not alter the underlying triangles of the part containing
        the curve. 
    :type treat_as_free_curve: bool, optional
    :return: Filtered entities.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/filter_curve.py
    """
 

    trimatic.utils.check_type("entities", entities, (trimatic.Curve,  trimatic.SurfaceBorder, trimatic.SurfaceContour))
    trimatic.utils.check_param_greater_or_equal("sharp_angle_threshold", sharp_angle_threshold, 0)
    trimatic.utils.check_param_greater_or_equal("small_edge_threshold", small_edge_threshold, 0)
    return pymatic.filter_curve(trimatic.utils.single_or_multiple_entities(entities), sharp_angle_threshold, small_edge_threshold, treat_as_free_curve)

def project_curve(entities, direction, target_entities, visibility_threshold = 10.0):
    """Projects curve(s) to the specified part(s)/surface(s).

    :param entities: Either single object or list of curves or sketches.
    :type entities: trimatic.Curve | trimatic.Sketch |  [trimatic.Curve | trimatic.Sketch]
    :param direction: Direction vector for the projection, specified as a tuple of (x,y,z).
    :type direction: (float, float, float)
    :param target_entities: The target entities that the curves will be projected to.
    :type target_entities: trimatic.Part | trimatic.Surface | [trimatic.Part | trimatic.Surface]
    :param visibility_threshold: If None, projected curve segments are connected along the part of the mesh in the
        projection direction even if the region of the mesh is not visible from the original curve. The threshold value
        determines the maximum distance between curve segments across non-visible regions that will be connected. 
    :type visibility_threshold: float | None, optional
    :return: Projected curve(s).
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/project_curve.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Curve, trimatic.Sketch)) 
    pymatic_target_entities = trimatic.utils.single_or_multiple_entities(target_entities)
    trimatic.utils.check_type("target_entities", pymatic_target_entities, ( trimatic.Part, trimatic.Surface, trimatic.SurfaceSet), allow_none_or_empty = True)
    if visibility_threshold is not None:
        trimatic.utils.check_param_greater_or_equal("visibility_threshold", visibility_threshold, 0)
    trimatic.utils.check_vector_not_equal("direction", direction, [0, 0, 0])

    return pymatic.project_curve(pymatic_entities, trimatic.utils.point_argument(direction), pymatic_target_entities, visibility_threshold)

def reduce_curve(entities, geometrical_error = 0.1000, treat_as_free_curve = True):
    """Reduce the number of segments in a curve.

        :param entities: Entities to be reduced.
        :type entities: trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | [trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve]
        :param geometrical_error: Maximum error that can be produced by the reduction.
        :type geometrical_error: float, optional
        :param treat_as_free_curve: If True, changes to the curve do not alter the underlying triangles of the part containing the curve.
        :type treat_as_free_curve: bool, optional
        :return: Reduced entities.
        :rtype: trimatic.Curve | (trimatic.Curve)
        :raises: RuntimeError, ValueError

        :example:

        .. literalinclude:: example/curve/reduce_curve.py
        """

    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Curve))
    trimatic.utils.check_param_greater_or_equal("geometrical_error", geometrical_error, 0)
    return pymatic.reduce_curve(trimatic.utils.single_or_multiple_entities(entities), geometrical_error, treat_as_free_curve)

def smooth_curve(entities, smooth_factor = 0.7, use_compensation = True, number_of_iterations = 10, treat_as_free_curve = True):
    """Smooths curves.

    :param entities: Entities to smooth.
    :type entities: trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param smooth_factor: Strength of the smoothing. 1.0 indicates maximum smoothing.
    :type smooth_factor: float, optional
    :param number_of_iterations: Increases the number of times smooth is repeated.
    :type number_of_iterations: int, optional
    :param use_compensation: If True, prevents reduction of a circular curve into a point.
    :type use_compensation: bool, optional
    :param treat_as_free_curve: If True, changes to the curve do not alter the underlying triangles of the part containing
        the curve.
    :type treat_as_free_curve: bool, optional
    :return: Smoothed entities.
    :rtype: trimatic.Curve | (trimatic.Curve)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/smooth_curve.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Curve,trimatic.SurfaceBorder, trimatic.SurfaceContour))
    trimatic.utils.check_param_in_range("smooth_factor", smooth_factor, 0, 1)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    return pymatic.smooth_curve(trimatic.utils.single_or_multiple_entities(entities),smooth_factor,use_compensation, number_of_iterations, treat_as_free_curve)

def split_surfaces_by_curves(entities = None, curves = None):
    """Splits surfaces by curves.

    :param entities: Entities to split. If set to None, the part(s) containing the curves will be split.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet] | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet) | None, optional
    :param curves: Curves to use for the split. If set to None, all closed and attached curves are used to
        split surfaces of the entities.
    :type curves: trimatic.Curve | trimatic.CurveSet | [trimatic.Curve | trimatic.CurveSet] | (trimatic.Curve | trimatic.CurveSet), optional
    :return: Split surfaces.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/curve/split_surfaces_by_curves.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part,trimatic.Surface,trimatic.SurfaceSet,), True) 
    pymatic_curves = trimatic.utils.single_or_multiple_entities(curves)
    trimatic.utils.check_type("curves", pymatic_curves, (trimatic.Curve,trimatic.CurveSet,), True) 
    if entities is None and curves is None:
        raise ValueError("entities and curves can't both be None")

    return pymatic.split_surfaces_by_curves(pymatic_entities, pymatic_curves)
