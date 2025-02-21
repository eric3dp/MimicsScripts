import pymatic
import trimatic.utils
import math
import os

def collision_detection(entities, clearance_check = 0.0):
    """ Detect collision between parts by considering acceptable clearance between parts.

    :param entities: A list of parts to check whether the parts are colliding.
    :type entities: [trimatic.Part] | (trimatic.Part)
    :param clearance_check: The minimum distance between parts that can be considered collision. 
     If the distance between parts is less than or equal to this value, the parts are considered to be colliding.
    :type clearance_check: float

    :return: A tuple of tuples containing colliding parts as pairs.
    :rtype: ((trimatic.Part, trimatic.Part)) 
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/collision_detection.py
    """
    

    trimatic.utils.check_type("entities", entities, trimatic.Part)
    trimatic.utils.check_param_greater_or_equal("clearance_check", clearance_check, 0.0)
    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)

    if len(pymatic_entities) < 2:
        raise ValueError("Atleast two entities are required for collision stection")

    return pymatic.collision_detection(pymatic_entities, clearance_check)


def collision_detection_with_colliding_volume(entities):
    """ Detect collision between parts and calculate colliding volume. 

    :param entities: A list of parts to check whether colliding or not.
    :type entities: [trimatic.Part] | (trimatic.Part)

    :return: A tuple of tuples containing colliding parts as pairs along with colliding volume information.
    :rtype: ((trimatic.Part, trimatic.Part, float)) 
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/collision_detection_with_colliding_volume.py
    """
    

    trimatic.utils.check_type("entities", entities, trimatic.Part)
    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)

    if len(pymatic_entities) < 2:
        raise ValueError("Atleast two entities are required for collision stection")

    return pymatic.collision_detection_with_colliding_volume(pymatic_entities)

def create_arc_3_points(point_from, point_to, arc_side):
    """Creates an open arc based on 3 points method.

    :param point_from: Begin point of the arc.
    :type point_from: trimatic.Point
    :param point_to: End point of the arc.
    :type point_to: trimatic.Point
    :param arc_side: Indicates the side of the arc that will be visible, and determines the radius. 
                     The end result is an arc beginning in point_from, ending in point_to, and going through arc_side.
    :type arc_side: trimatic.Point
    :return: Created arc
    :rtype: trimatic.Arc
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_arc_3_points.py
    """
    

    pymatic_point_from = trimatic.utils.point_argument(point_from)
    pymatic_point_to = trimatic.utils.point_argument(point_to)
    pymatic_arc_side = trimatic.utils.point_argument(arc_side)
    trimatic.utils.check_points_not_collinear(pymatic_point_from, pymatic_point_to, pymatic_arc_side)
    trimatic.utils.check_3points_not_coincident('point_from', 'point_to', 'arc_side', pymatic_point_from, pymatic_point_to, pymatic_arc_side)

    return pymatic.create_arc_3_points(pymatic_point_from, pymatic_point_to, pymatic_arc_side)

def create_circle_arc_3_points(point1, point2, point3):
    """Creates a circle that passes through 3 points.

    :param point1: First point.
    :type point1: trimatic.Point
    :param point2: Second point.
    :type point2: trimatic.Point
    :param point3: Third point.
    :type point3: trimatic.Point
    :return: Created arc (circle).
    :rtype: trimatic.Arc
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_circle_arc_3_points.py
    """
    

    pymatic_point1 = trimatic.utils.point_argument(point1)
    pymatic_point2 = trimatic.utils.point_argument(point2)
    pymatic_point3 = trimatic.utils.point_argument(point3)
    trimatic.utils.check_points_not_collinear(pymatic_point1, pymatic_point2, pymatic_point3)
    trimatic.utils.check_3points_not_coincident('point1', 'point2', 'point3', pymatic_point1, pymatic_point2, pymatic_point3)
    
    return pymatic.create_circle_arc_3_points(pymatic_point1, pymatic_point2, pymatic_point3)

def create_circle_arc_normal_center_radius(normal, center_point, radius):
    """Creates a circle based on normal, center, and radius.

    :param normal: Direction of the normal of the arc or circle, that is the normal of the plane in which the arc or circle lies.
    :type normal: trimatic.Point
    :param center_point: Center point of circle.
    :type center_point: trimatic.Point
    :param radius: Radius of circle.
    :type radius: float
    :return: Created arc (circle).
    :rtype: trimatic.Arc
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_circle_arc_normal_center_radius.py
    """
    

    pymatic_center_point = trimatic.utils.point_argument(center_point)
    pymatic_normal = trimatic.utils.point_argument(normal)
    trimatic.utils.check_direction("normal", pymatic_normal)
    trimatic.utils.check_resolution("radius", radius)

    return pymatic.create_circle_arc_normal_center_radius(pymatic_normal, pymatic_center_point, radius)

def create_arc_normal_center_radius(normal, center_point, radius, start_point, end_point):
    """Creates an open arc based on normal, center, radius and two points.

    :param normal: Direction of the normal of the arc or circle, which is the normal of the plane in which the arc or circle lies.
    :type normal: trimatic.Point
    :param center_point: Center point of arc.
    :type center_point: trimatic.Point
    :param radius: Radius of arc.
    :type radius: float
    :param start_point: Start point of arc.
    :type start_point: trimatic.Point
    :param end_point: End point of arc.
    :type end_point: trimatic.Point
    :return: Created arc.
    :rtype: trimatic.Arc
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_arc_normal_center_radius.py
    """
    

    trimatic.utils.check_resolution("radius", radius)
    pymatic_normal = trimatic.utils.point_argument(normal)
    pymatic_center_point = trimatic.utils.point_argument(center_point)
    pymatic_start_point = trimatic.utils.point_argument(start_point)
    pymatic_end_point = trimatic.utils.point_argument(end_point)
    trimatic.utils.check_3points_not_coincident('center_point', 'start_point', 'end_point',
                                          pymatic_center_point, pymatic_start_point, pymatic_end_point)
    trimatic.utils.check_direction("normal", pymatic_normal)
    
    return pymatic.create_arc_normal_center_radius(pymatic_normal, pymatic_center_point, radius, pymatic_start_point, pymatic_end_point)

def create_circle_arc_fit(entity):
    """Creates a fit circle.

    :param entity: Contour or curve to fit arc.
    :type entity: trimatic.Curve | trimatic.SurfaceContour
    :return: Created arc.
    :rtype: trimatic.Arc
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_circle_arc_fit.py
    """
    

    trimatic.utils.check_type("entity", entity, (trimatic.Curve, trimatic.SurfaceContour))
    
    return pymatic.create_circle_arc_fit(entity)

def create_cone(bottom_point, top_point, bottom_radius, top_radius = 0):
    """Creates an analytical cone.

    :param bottom_point: Center point of bottom of the cone.
    :type bottom_point: trimatic.Point
    :param top_point: Center point of the top of the cone.
    :type top_point: trimatic.Point
    :param bottom_radius: Bottom radius of the cone.
    :type bottom_radius: float
    :param top_radius: Top radius of the cone.
    :type top_radius: float, optional
    :return: Created cone.
    :rtype: trimatic.Cone
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_cone.py
    """


    trimatic.utils.check_param_greater_or_equal("bottom_radius", bottom_radius, 0)
    trimatic.utils.check_param_greater_or_equal("top_radius", top_radius, 0)

    return pymatic.create_cone(trimatic.utils.point_argument(bottom_point), trimatic.utils.point_argument(top_point), bottom_radius, top_radius)

def create_cylinder_fit(entities):
    """Creates an analytical cylinder by fitting to entities.

    :param entities: Either single object or a heterogeneous list of parts, surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :return: Fitted cylinder.
    :rtype: trimatic.Cylinder
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_cylinder_fit.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles ))
    trimatic.utils.check_part_has_surface("entities", entities)

    return pymatic.create_cylinder_fit(trimatic.utils.single_or_multiple_entities(entities))
    
def create_cylinder_axis(origin_point, direction, radius, height):
    """Creates an analytical cylinder using axis method.

    :param origin_point: Origin of the cylinder.
    :type origin_point: trimatic.Point
    :param direction: Direction of the axis of the cylinder.
    :type direction: trimatic.Point
    :param radius: Radius of cylinder.
    :type radius: float
    :param height: Height of the cylinder.
    :type height: float
    :return: Created cylinder.
    :rtype: trimatic.Cylinder
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_cylinder_axis.py
    """


    trimatic.utils.check_param_greater_or_equal("radius", radius, 0.0001)
    trimatic.utils.check_param_greater_or_equal("height", height, 0.0001)

    return pymatic.create_cylinder_axis(trimatic.utils.point_argument(origin_point), trimatic.utils.point_argument(direction), radius, height)

def create_line(point1, point2):
    """Creates a line between 2 points.

    :param point1: First point of the line.
    :type point1: trimatic.Point
    :param point2: Second point of the line.
    :type point2: trimatic.Point
    :return: Created line.
    :rtype: trimatic.Line
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_line.py
    """


    pymatic_point1 = trimatic.utils.point_argument(point1) 
    pymatic_point2 = trimatic.utils.point_argument(point2) 
    trimatic.utils.check_2points_not_coincident("point1", "point2", pymatic_point1, pymatic_point2)
    
    return pymatic.create_line(pymatic_point1, pymatic_point2)

def create_line_direction_and_length(point, direction, length):
    """Creates a line starting from a point in given direction with specified length.

    :param point: First point of the line.
    :type point: trimatic.Point
    :param direction: Direction of the line.
    :type direction: trimatic.Point
    :param length: Length of the line.
    :type length: float
    :return: Created line.
    :rtype: trimatic.Line
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_line_direction_and_length.py
    """
    

    pymatic_direction = trimatic.utils.point_argument(direction)
    trimatic.utils.check_direction("direction", pymatic_direction)
    trimatic.utils.check_resolution("length", length)
    pymatic_point = trimatic.utils.point_argument(point)
    
    point1 = list(point)
    l2 = 0
    for i in range(3):
        l2 += direction[i] * direction[i]
    l = math.sqrt(l2)
    for i in range(3):
        point1[i] = point[i] + direction[i]/l * length
    return pymatic.create_line(pymatic_point, trimatic.utils.point_argument(point1))


def create_line_fit_ruled_surface(entities):
    """Creates a line by fitting a ruled surface and returning its axis.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :return: Axis of fitted ruled surface.
    :rtype: trimatic.Line
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_line_fit_ruled_surface.py
    """
    

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    return pymatic.create_line_fit_ruled_surface(trimatic.utils.single_or_multiple_entities(entities))


def create_line_plane_intersection(plane1, plane2):
    """Creates a line on intersection of two planes.

    :param plane1: First plane.
    :type plane1: trimatic.Plane
    :param plane2: Second plane.
    :type plane2: trimatic.Plane
    :return: Created line.
    :rtype: trimatic.Line
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_line_plane_intersection.py
    """
    

    trimatic.utils.check_type("plane1", plane1, (trimatic.Plane))
    trimatic.utils.check_type("plane2", plane2, (trimatic.Plane))
    return pymatic.create_line_plane_intersection(plane1, plane2)

def create_part_comparison_analysis(entity, target_entity, signed = True):
    """Creates part comparison analysis.

    :param entity: The part to analyze.
    :type entity: trimatic.Part
    :param target_entity: The part to compare with.
    :type target_entity: trimatic.Part | trimatic.Plane | trimatic.Sphere | trimatic.Cone | trimatic.Cylinder
    :param signed: When True, this means that negative and positive deviation are used to differentiate between areas where target entity is inside the selected entity (negative) and where target entity is outside the selected entity (positive). When False, all distances are positive.
    :type signed: bool, optional
    :return: Created analysis.
    :rtype: trimatic.Analysis
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_part_comparison_analysis.py
    """
    


    trimatic.utils.check_type("entity", entity, (trimatic.Part, ))
    trimatic.utils.check_type("target_entity", target_entity, (trimatic.Part, trimatic.Plane, trimatic.Sphere, trimatic.Cone, trimatic.Cylinder))

    return pymatic.create_part_comparison_analysis(entity, target_entity, signed)

def create_plane_fit(entities):
    """Creates a datum plane by fitting into entities.

    :param entities: Either single object or heterogeneous list of parts, surfaces, surface sets, curves, or curve sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve  | trimatic.CurveSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve  | trimatic.CurveSet | trimatic.MarkedTriangles] 
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_fit.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.Curve, trimatic.CurveSet, trimatic.MarkedTriangles))
    trimatic.utils.check_entities_does_not_have_part_and_one_of_its_surfaces('entities', entities)
    
    return pymatic.create_plane_fit(trimatic.utils.single_or_multiple_entities(entities))


def create_plane_3_points(point1, point2, point3):
    """Creates a datum plane through 3 points.

    The points should not be coincident (more than one point is of the same coordinate) or collinear (all 3 points form a line).

    :param point1: First point to define the plane.
    :type point1: trimatic.Point
    :param point2: Second point to define the plane.
    :type point2: trimatic.Point
    :param point3: Third point to define the plane.
    :type point3: trimatic.Point
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_3_points.py
    """


    pypoint1 = trimatic.utils.point_argument(point1)
    pypoint2 = trimatic.utils.point_argument(point2)
    pypoint3 = trimatic.utils.point_argument(point3)
    trimatic.utils.check_points_not_collinear(pypoint1, pypoint2, pypoint3)
    trimatic.utils.check_3points_not_coincident("point1", "point2", "point3", pypoint1, pypoint2, pypoint3)
    
    return pymatic.create_plane_3_points(pypoint1, pypoint2, pypoint3)


def create_plane_2_points_perpendicular_1_plane(point1, point2, perpendicular_plane):
    """Creates a datum plane through 2 points and perpendicular to a selected plane.

    The points should not be coincident (more than one point is of the same coordinate).

    :param point1: First point to define the plane.
    :type point1: trimatic.Point
    :param point2: Second point to define the plane.
    :type point2: trimatic.Point
    :param perpendicular_plane: The created datum plane will be perpendicular to this selected plane.
    :type perpendicular_plane: trimatic.Plane | trimatic.Surface
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_2_points_perpendicular_1_plane.py
    """


    pypoint1 = trimatic.utils.point_argument(point1)
    pypoint2 = trimatic.utils.point_argument(point2)
    trimatic.utils.check_2points_not_coincident("point1", "point2", pypoint1, pypoint2)
    trimatic.utils.check_type("perpendicular_plane", perpendicular_plane, (trimatic.Plane, trimatic.Surface))
    
    return pymatic.create_plane_2_points_perpendicular_1_plane(perpendicular_plane, pypoint1, pypoint2)


def create_plane_normal_origin(normal, origin):
    """Creates a datum plane with given normal vector and an origin.

    :param normal: Normal vector of the plane.
    :type normal: trimatic.Point
    :param origin: Origin of the plane.
    :type origin: trimatic.Point
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_normal_origin.py
    """

    trimatic.utils.check_direction("normal", normal)
    
    return pymatic.create_plane_normal_origin(trimatic.utils.point_argument(normal), trimatic.utils.point_argument(origin))


def create_plane_midplane(point1, point2):
    """Creates a datum plane between two points.

    :param point1: First point.
    :type point1: trimatic.Point
    :param point2: Second point.
    :type point2: trimatic.Point
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_midplane.py
    """


    
    return pymatic.create_plane_midplane(trimatic.utils.point_argument(point1), trimatic.utils.point_argument(point2))


def create_plane_1_point_perpendicular_2_planes(origin, perpendicular_plane1, perpendicular_plane2):
    """Creates a datum plane through one point and perpendicular to two selected planes.

    :param origin: Origin of the plane.
    :type origin: trimatic.Point
    :param perpendicular_plane1: First perpendicular plane.
    :type perpendicular_plane1: trimatic.Plane | trimatic.Surface
    :param perpendicular_plane2: Second perpendicular plane.
    :type perpendicular_plane2: trimatic.Plane | trimatic.Surface
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_1_point_perpendicular_2_planes.py
    """


    trimatic.utils.check_type("perpendicular_plane1", perpendicular_plane1, (trimatic.Plane, trimatic.Surface))
    trimatic.utils.check_type("perpendicular_plane2", perpendicular_plane2, (trimatic.Plane, trimatic.Surface))
    trimatic.utils.check_entity_sets_do_not_contain_equal_entities("perpendicular_plane1", "perpendicular_plane2",
                                                                   perpendicular_plane1, perpendicular_plane2)
    return pymatic.create_plane_1_point_perpendicular_2_planes(trimatic.utils.point_argument(origin),
                                                              perpendicular_plane1,
                                                              perpendicular_plane2)


def create_plane_1_point_parallel_plane(point, parallel_plane):
    """Creates a datum plane through one point and parallel to a selected plane.

    :param point: Origin of the plane.
    :type point: trimatic.Point
    :param parallel_plane: Parallel plane.
    :type parallel_plane: trimatic.Plane | trimatic.Surface
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_1_point_parallel_plane.py
    """


    trimatic.utils.check_type("parallel_plane", parallel_plane, (trimatic.Plane, trimatic.Surface))

    return pymatic.create_plane_1_point_parallel_plane(trimatic.utils.point_argument(point), parallel_plane)


def create_plane_average_existing(planes):
    """Creates a datum plane based on the average of selected planes.

    :param planes: Either single or heterogeneous list of planes.
    :type planes: trimatic.Plane | [trimatic.Plane]
    :return: Created plane.
    :rtype: trimatic.Plane
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_plane_average_existing.py
    """


    trimatic.utils.check_type("planes", planes, trimatic.Plane)
    
    return pymatic.create_plane_average_existing(trimatic.utils.single_or_multiple_entities(planes))

def create_point(coords):
    """Creates point in 3-matic based on xyz coordinates.

    :param coords: (x,y,z) of point to create.
    :type coords: trimatic.Point
    :return: Created point.
    :rtype: trimatic.Point
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_point.py
    """



    return pymatic.create_point(trimatic.utils.point_argument(coords))

def compute_center_of_gravity(part, method='Based on mesh'):
    """Computes center of gravity of a part.
   
    :param part: Part to compute center of gravity.
    :type part: trimatic.Part
    :param method: "Based on mesh" or "Based on points" or "Based on volume".
    :type method: string, optional
    :return: Computed center of gravity in tuple.
    :rtype: (float,float,float)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/compute_center_of_gravity.py
    """
    computation_methods = ["Based on mesh",
                           "Based on points",
                           "Based on volume"]

    trimatic.utils.check_type("part", part, trimatic.Part)
    trimatic.utils.check_valid_name("method", method, computation_methods)
    
    return pymatic.compute_center_of_gravity(part, method)

def project_point(point_to_project, direction, parts, project_through = False):
    """Projects a point on a part given in a direction.
    
    :param point_to_project: Select a point to project, it can also be a list or tuple of xyz coordinates.
    :type point_to_project: trimatic.Point
    :param direction: Direction to project
    :type direction: trimatic.Point
    :param parts: Either single entity or a heterogeneous list of parts.
    :type parts: trimatic.Part | [trimatic.Part]
    :param project_through: If True, the point will be projected through the selected entities.
    :type project_through: bool, optional
    :return: Tuple of points (will only contain 1 item when project_through = False).
    :rtype: ((float,float,float))
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/project_point.py
    """

    trimatic.utils.check_vector_not_equal("direction", direction, [0, 0, 0])
    trimatic.utils.check_type("parts", parts, trimatic.Part)
    
    return pymatic.project_point(trimatic.utils.point_argument(point_to_project), trimatic.utils.point_argument(direction),
                                 trimatic.utils.single_or_multiple_entities(parts), project_through)

def compute_closest_point(point, parts):
    """Computes the point on one or more parts that is closest to a query point.
   
    :param point: the query point. 
    :type point: (float,float,float) | trimatic.Point
    :param parts: target part(s).
    :type parts: trimatic.Part | [trimatic.Part]
    :return: closest point.
    :rtype: (float,float,float)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/compute_closest_point.py
    """

    trimatic.utils.check_type("parts", parts, trimatic.Part)
    
    return pymatic.compute_closest_point(trimatic.utils.point_argument(point), trimatic.utils.single_or_multiple_entities(parts))

def compute_normal_and_closest_point(point, parts):
    """Computes the normal vector in the point closest to one or more parts in a query point.

    This function does the same as compute_closest_point, but also return normal vector in the closest point.
   
    :param point: the query point. 
    :type point: (float,float,float) | trimatic.Point
    :param parts: target part.
    :type parts: trimatic.Part | [trimatic.Part]
    :return: Tuple with points: normal vector and closest point
    :rtype: ((float,float,float), (float,float,float))
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/compute_normal_and_closest_point.py
    """

    trimatic.utils.check_type("parts", parts, trimatic.Part)
    
    return pymatic.compute_normal_and_closest_point(trimatic.utils.point_argument(point), trimatic.utils.single_or_multiple_entities(parts))


def compute_extrema_analysis_points(entities, direction, minima = True, maxima = True, global_extrema_only = True):
    """Computes extremal points of multiple entities along a direction.
    
    :param entities: Either single object or a heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | (trimatic.Part | trimatic.Surface | trimatic.SurfaceSet)
    :param direction: Direction.
    :type direction: trimatic.Point
    :param minima: If True, computes minima.
    :type minima: bool, optional
    :param maxima: If True, computes maxima.
    :type maxima: bool, optional
    :param global_extrema_only: If True, only global extrema will be generated. If False, local extrema points will also be computed.
    :type global_extrema_only: bool, optional
    :return: 0, 1 or 2 tuples of points, depending on minima or maxima were queried.
    :rtype: (((float,float,float)),((float,float,float)))
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/compute_extrema_analysis_points.py
    """

    trimatic.utils.check_vector_not_equal("direction", direction, [0, 0, 0])
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    
    return pymatic.compute_extrema_analysis_points(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.point_argument(direction), minima, maxima, global_extrema_only)
   
def create_sphere_fit(entities):
    """Creates an analytical sphere by fitting to entities.

    :param entities: Either single object or heterogeneous list of parts, surfaces, or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :return: Created sphere.
    :rtype: trimatic.Sphere
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_sphere_fit.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_part_has_surface("entities", entities)

    return pymatic.create_sphere_fit(trimatic.utils.single_or_multiple_entities(entities))
    
def create_sphere_center_radius(center_point, radius):
    """Creates an analytical sphere by specifying its center point and radius.

    :param center_point: Center point of the sphere.
    :type center_point: trimatic.Point
    :param radius: Radius of the sphere.
    :type radius: float
    :return: Created sphere.
    :rtype: trimatic.Sphere
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_sphere_center_radius.py
    """


    trimatic.utils.check_resolution("radius", radius)

    return pymatic.create_sphere_center_radius(trimatic.utils.point_argument(center_point), radius)

def import_fea_results(filename_model, filename_report, recreate_surface_mesh = True):
    """Imports results from FEA packages like ABAQUS.

    :param filename_model: The filename of the file that contains the model.
    :type filename_model: string
    :param filename_report: The filename of the file that contains the report.
    :type filename_report: string
    :param recreate_surface_mesh: When True, new surface will be created for the volume element being imported.
    :type recreate_surface_mesh: bool, optional
    :return: Imported model containing the analysis.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/import_fea_results.py
    """



    if not os.path.isfile(filename_model):
        raise FileNotFoundError('Unable to open file ' + filename_model)
    if not os.path.isfile(filename_report):
        raise FileNotFoundError('Unable to open file ' + filename_report)
    
    return pymatic.import_fea_results(filename_model, filename_report, recreate_surface_mesh)

def compute_inertia_axes(part):
    """Calculates the inertia axes of a part. 

    :param part: The part.
    :type part: trimatic.Part
    :return: Returns center of gravity, the main, second and third inertia axis of the part (in that order).
    :rtype: ((float, float, float),(float, float, float),(float, float, float),(float, float, float))

    :example:

    .. literalinclude:: example/analyze/compute_inertia_axes.py
    """


    trimatic.utils.check_type("part", part, (trimatic.Part))
    
    return pymatic.compute_inertia_axes(part)
    
def create_wall_thickness_analysis(entity, max_wall_thickness = 10.0):
    """Create wall thickness analysis for given entity.

    :param entity: Entity for which analysis needs to be created.
    :type entity: trimatic.Part
    :param max_wall_thickness: Defines maximum allowed wall thickness for the analysis.
    :type max_wall_thickness: float
    :return: Created analysis object.
    :rtype: trimatic.Analysis 
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_wall_thickness_analysis.py

    """


    trimatic.utils.check_type('entity', entity, (trimatic.Part))
    trimatic.utils.check_param_greater_or_equal('max_wall_thickness', max_wall_thickness, 0.0)
    
    return pymatic.create_wall_thickness_analysis(entity, max_wall_thickness)

def create_maximum_curvature_analysis(entity, fitting_radius = None):
    """Create maximum curvature analysis for given part.
    
    :param entity: Part for which analysis needs to be created.
    :type entity: trimatic.Part
    :param fitting_radius: If specified the curvature in each point is based on the global curvature in that area around the point. This way you can avoid that local peaks influence the curvature analysis. Otherwise, curvature is calculated locally in each point.
    :type fitting_radius: float, optional
    :return: Created analysis object.
    :rtype: trimatic.Analysis 
    :raises: RuntimeError, ValueError
    
    :example:
    
    .. literalinclude:: example/analyze/create_maximum_curvature_analysis.py
    
    """
    

    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    
    if fitting_radius is not None:
      trimatic.utils.check_param_greater('fitting_radius', fitting_radius, 0.0)

    return pymatic.create_maximum_curvature_analysis(entity, fitting_radius)

def create_minimum_curvature_analysis(entity, fitting_radius = None):
    """Create minimum curvature analysis for given part.
    
    :param entity: Part for which analysis needs to be created.
    :type entity: trimatic.Part
    :param fitting_radius: If specified the curvature in each point is based on the global curvature in that area around the point. This way you can avoid that local peaks influence the curvature analysis. Otherwise, curvature is calculated locally in each point.
    :type fitting_radius:  float, optional
    :return: Created analysis object.
    :rtype: trimatic.Analysis 
    :raises: RuntimeError, ValueError
    
    :example:
    
    .. literalinclude:: example/analyze/create_minimum_curvature_analysis.py
    
    """
    

    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    
    if fitting_radius is not None:
      trimatic.utils.check_param_greater('fitting_radius', fitting_radius, 0.0)

    return pymatic.create_minimum_curvature_analysis(entity, fitting_radius)

def create_mean_curvature_analysis(entity, fitting_radius = None):
    """Create mean curvature analysis for given part.
    
    :param entity: Part for which analysis needs to be created.
    :type entity: trimatic.Part
    :param fitting_radius: If specified the curvature in each point is based on the global curvature in that area around the point. This way you can avoid that local peaks influence the curvature analysis. Otherwise, curvature is calculated locally in each point.
    :type fitting_radius: float, optional
    :return: Created analysis object.
    :rtype: trimatic.Analysis 
    :raises: RuntimeError, ValueError
    
    :example:
    
    .. literalinclude:: example/analyze/create_mean_curvature_analysis.py
    
    """
    

    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    
    if fitting_radius is not None:
       trimatic.utils.check_param_greater('fitting_radius', fitting_radius, 0.0)

    return pymatic.create_mean_curvature_analysis(entity, fitting_radius)

def create_gaussian_curvature_analysis(entity, fitting_radius = None):
    """Create gaussian curvature analysis for given part.
    
    :param entity: Part for which analysis needs to be created.
    :type entity: trimatic.Part
    :param fitting_radius: If specified the curvature in each point is based on the global curvature in that area around the point. This way you can avoid that local peaks influence the curvature analysis. Otherwise, curvature is calculated locally in each point.
    :type fitting_radius:  float, optional
    :return: Created analysis object.
    :rtype: trimatic.Analysis 
    :raises: RuntimeError, ValueError
    
    :example:
    
    .. literalinclude:: example/analyze/create_gaussian_curvature_analysis.py
    
    """
    

    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    
    if fitting_radius is not None:
      trimatic.utils.check_param_greater('fitting_radius', fitting_radius, 0.0)

    return pymatic.create_gaussian_curvature_analysis(entity, fitting_radius)
    
def create_segmentation(entity, 
                        band_thresholds,
                        band_colors):
    """This will generate a surface structure based on the given analysis.
    
    :param entity: Analysis object based on which the surface structure is created.
    :type entity: trimatic.Analysis
    :param band_thresholds: A list of adjacent values which represents minimum and maximum threshold for each band.
    :type band_thresholds:  [float]
    :param band_colors: A list of colors for the surfaces corresponding to the given bands.
    :type band_colors:  [(float, float, float)]

    :rtype: Generated surfaces.  
    :rtype: (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/analyze/create_segmentation.py
    
    """


    trimatic.utils.check_type("entity", entity, trimatic.Analysis)
    vertices, values = entity.get_values()
    sorted_analysis = sorted(values)
    # N values create (N-1) bands
    num_bands = len(band_thresholds) - 1

    sorted_bands = tuple(sorted(band_thresholds))       
    actual_min = sorted_analysis[0]
    actual_max = sorted_analysis[-1]
    
    for i in range(len(sorted_bands)):
        trimatic.utils.check_param_in_range("Band threshold value({})".format( i + 1), sorted_bands[i], actual_min, actual_max)
        
    if num_bands < 1:
       raise ValueError("There should be atleast one band to be spcified for the operation")

    if num_bands != len(band_colors):
        raise ValueError("No. of colors must be equal to number of bands")

    colors = []
    for color in band_colors:
        colors.append(tuple(color))

    return pymatic.create_segmentation(entity, sorted_bands , tuple(colors))
