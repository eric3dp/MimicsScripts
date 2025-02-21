import pymatic
import trimatic.utils

from enum import Enum

def arc_to_arc_align(fixed_entity, moving_entity, move_along_entities=(), coincident=True):
    """Aligns two (or more) entities, through arc-fitting method, based on the center and normal orientation of the selected arcs.

    :param fixed_entity: Reference entity to be aligned with.
    :type fixed_entity: trimatic.Curve | trimatic.Surface | trimatic.Arc
    :param moving_entity: Entity to align/move. For curves or surfaces, the part they belong to will be moved.
    :type moving_entity: trimatic.Curve | trimatic.Surface | trimatic.Arc
    :param move_along_entities: Either single object, empty or heterogeneous list/tuple of root level entities
        (parts, analytical primitives) that will be aligned along with the moving_entity.
    :type move_along_entities: trimatic.Object | [trimatic.Object] | (trimatic.Object), optional
    :param coincident: If True, centre points of the input arcs will be made coincident and their normals will be parallel.
    :type coincident: bool, optional
    :return: Aligned entities. This will be a combination of moving_entity and move_along_entities.
    :rtype: trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/arc_to_arc_align.py

    .. testcode::
        :hide:

        print(run_test('/example/align/arc_to_arc_align.py', ['result'], '/expected_results/align/arc_to_arc_align.json'))

    .. testoutput::
        :hide:

        [(<trimatic.Arc(Arc)>, <trimatic.Part(Cylinder-012-2)>)]
    """


    trimatic.utils.check_type("fixed_entity", fixed_entity, (trimatic.Arc, trimatic.Surface, trimatic.Curve))
    trimatic.utils.check_type("moving_entity", moving_entity, (trimatic.Arc, trimatic.Surface, trimatic.Curve))
    trimatic.utils.check_type("move_along_entities", move_along_entities, trimatic.utils.transformable_types(),True)

    return pymatic.arc_to_arc_align(fixed_entity,moving_entity,trimatic.utils.single_or_multiple_entities(move_along_entities),coincident)

def global_registration(
    *args,#'force named parameters'
    fixed_entity,
    moving_entity,
    move_along_entities=(),
    distance_threshold=None,
    number_of_iterations=10,
    subsample_percentage=15
    ):
    """Performs final registration of entities based on a heuristic algorithm.

    :param fixed_entity: Reference entity to be aligned with.
    :type fixed_entity: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles
    :param moving_entity: Entity to align/move.
    :type moving_entity: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles
    :param move_along_entities: Either single object or heterogeneous list of root level entities
     (parts, analytical primitives) that will be aligned along with the moving_entity.
    :type move_along_entities: trimatic.Object | [trimatic.Object] , optional
    :param distance_threshold: If distance between a point on fixed and moving entity is less than the
        threshold value, the point will be used for registration. Set to None for automatic calculation.
    :type distance_threshold: float, optional
    :param number_of_iterations: Increases the number of passes for higher quality but increases computation time.
    :type number_of_iterations: int, optional
    :param subsample_percentage: Defines how many points (in percentage) will be used for registration.
    :type subsample_percentage: int, optional
    :return: Average distance deviation after registration or None if operation failed.
    :rtype: float
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/global_registration.py
    """


    trimatic.utils.check_type("fixed_entity", fixed_entity, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_type("moving_entity", moving_entity, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_type("move_along_entities", move_along_entities, trimatic.utils.transformable_types(),True)
    if distance_threshold is not None:
        trimatic.utils.check_resolution("distance_threshold", distance_threshold)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)
    trimatic.utils.check_param_in_range("subsample_percentage", subsample_percentage, 1, 100)
    return pymatic.global_registration(
        fixed_entity,
        moving_entity,
        trimatic.utils.single_or_multiple_entities(move_along_entities),
        distance_threshold,
        number_of_iterations,
        subsample_percentage)

def mirror(entities, origin, normal):
    """This function mirrors the selected part around a mirror plane defined by the user.

    :param entities: Entities that need to be mirrored.
    :type entities:  trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :param origin: origin of the mirror plane.
    :type origin: trimatic.Point
    :param normal: normal of the mirror plane.
    :type normal: trimatic.Point
    :return: mirrored entities
    :rtype: (trimatic.Object)
    :raises: RuntimeError, ValueError, AttributeException

    :example:

    .. literalinclude:: example/align/mirror.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,) + trimatic.utils.analytical_primitive_types(), True)
    pymatic_normal = trimatic.utils.point_argument(normal)
    trimatic.utils.check_direction("normal", pymatic_normal)
    return pymatic.mirror(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.point_argument(origin), pymatic_normal)

def n_points_registration( fixed_points, moving_points, moving_entities ):
    """Performs registration based on 2 sets of points, e.g. landmarks

    :param fixed_points: Reference points to be aligned with.
    :type fixed_points: [(float,float,float)]
    :param moving_points: For every fixed point, a corresponding "moving point". The points won't actually move, but indicate points on the moving entities.
    :type moving_points: [(float,float,float)]
    :param moving_entities: Either single object or heterogeneous list of root level entities.
     (parts, analytical primitives) that will be aligned along with the moving_entity.
    :type moving_entities: trimatic.Object | [trimatic.Object]
    :return: moved entities
    :rtype: (trimatic.Object)
    :raises: RuntimeError, ValueError, AttributeException

    :example:

    .. literalinclude:: example/align/n_points_registration.py
    """


    trimatic.utils.check_type("moving_entities", moving_entities, trimatic.utils.transformable_types(), True)
    return pymatic.n_points_registration(trimatic.utils.point_sequence_argument(fixed_points), trimatic.utils.point_sequence_argument(moving_points), trimatic.utils.single_or_multiple_entities(moving_entities))

def plane_to_plane_align(plane_on_fixed_entity, plane_on_moving_entity, move_along_entities = (), coincident = True):
    """Aligns a moving plane against a fixed plane and repositioning specified entities along with the moving plane.

    :param plane_on_fixed_entity: Cartesian plane representing the reference plane to be aligned with.
    :type plane_on_fixed_entity: trimatic.Plane
    :param plane_on_moving_entity: Cartesian plane representing the plane to align/move.
    :type plane_on_moving_entity: trimatic.Plane
    :param move_along_entities: Either single object or heterogeneous list of root level entities
        (parts, analytical primitives) that will be aligned along with the plane_on_moving_entity.
    :type move_along_entities: trimatic.Object | [trimatic.Object] | (trimatic.Object) , optional
    :param coincident: If True, centre points of the input planes will be made coincident and the directions
        will be the same.
    :type coincident: bool, optional
    :return: Aligned entities. This will be a combination of plane_on_moving_entity and move_along_entities.
    :rtype: trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/plane_to_plane_align.py
    """


    trimatic.utils.check_type("plane_on_fixed_entity", plane_on_fixed_entity, (trimatic.Plane, trimatic.CoordinateSystemPlane))
    trimatic.utils.check_type("plane_on_moving_entity", plane_on_moving_entity, (trimatic.Plane, trimatic.CoordinateSystemPlane))

    return pymatic.plane_to_plane_align(plane_on_fixed_entity, plane_on_moving_entity, trimatic.utils.single_or_multiple_entities(move_along_entities), coincident)

def rotate(entities, angle_deg, axis_origin, axis_direction, number_of_copies = 0):
    """Rotates entities around a single axis.

    :param entities: Either single object or heterogeneous list of root level entities (parts, analytical primitives).
    :type entities:  trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :param angle_deg: Angle of rotation, in degrees.
    :type angle_deg: float
    :param axis_origin: Origin of axis of rotation.
    :type axis_origin: (float, float, float)
    :param axis_direction: Direction of axis of rotation.
    :type axis_direction: (float, float, float)
    :param number_of_copies: Number of additional copies of the input entities to create. Each copy is rotated
        by angle_deg relative to the last copy made.
    :type number_of_copies: int, optional
    :return: Rotated entities (including any copies).
    :rtype: trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/rotate.py
    """


    trimatic.utils.check_type("entities", entities, trimatic.utils.transformable_types())
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 0)

    return pymatic.rotate(trimatic.utils.single_or_multiple_entities(entities), angle_deg, trimatic.utils.point_argument(axis_origin), trimatic.utils.point_argument(axis_direction), number_of_copies)

def rotate_around_axes(entities, angle_axes, rotation_origin, number_of_copies = 0):
    """Rotates entities around an origin and angles along each major axis.

    :param entities: Either single object or heterogeneous list of root level entities (parts, analytical primitives).
    :type entities: trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :param angle_axes: An (x,y,z) tuple with values representing the angles, in degrees, along each major axis.
    :type angle_axes: (float, float, float)
    :param rotation_origin: Origin/center of rotation.
    :type rotation_origin: (float, float, float)
    :param number_of_copies: Number of additional copies of the input entities to create. Each copy is rotated
        by angle_axes relative to the last copy made.
    :type number_of_copies: int, optional
    :return: Rotated entities (including any copies).
    :rtype: trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/rotate_around_axes.py
    """


    trimatic.utils.check_type("entities", entities, trimatic.utils.transformable_types())
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 0)

    return pymatic.rotate_around_axes(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.point_argument(angle_axes), trimatic.utils.point_argument(rotation_origin), number_of_copies)

def scale_factor(entities, factor, center_object = True, number_of_copies = 0):
    """Scales entities by the specified factor along each major axis

    :param entities: Either single object or heterogeneous list of objects.
    :type entities:  trimatic.Object | [trimatic.Object]
    :param factor: An (x,y,z) tuple with values representing the scale factor along each major axis.
    :type factor: (float, float, float)
    :param center_object: If True, scaling is done relative to the center of each input entity independently.
        Otherwise, scaling is done against the average center of all the input entities.
    :type center_object: bool, optional
    :param number_of_copies: Number of additional copies of the input entities to create. Each copy is scaled
        by factor relative to the last copy made.
    :type number_of_copies: int, optional
    :return: Scaled entities (including any copies).
    :rtype:   trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/scale_factor.py
    """



    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    trimatic.utils.check_param_greater("factor[0]", factor[0], 0)
    trimatic.utils.check_param_greater("factor[1]", factor[1], 0)
    trimatic.utils.check_param_greater("factor[2]", factor[2], 0)
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 0)
    return pymatic.scale(trimatic.utils.single_or_multiple_entities(entities), True,
                         trimatic.utils.point_argument(factor), center_object, number_of_copies)


def scale_delta(entities, delta, center_object = True, number_of_copies = 0):
    """Scales entities by the specified distance along each major axis.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities:  trimatic.Part | [trimatic.Part] | (trimatic.Part)
    :param delta: An (x,y,z) tuple with values representing the scale distance along each major axis.
    :type delta: (float, float, float)
    :param center_object: position of scale, by default center around object.
     If False, center at midpoint of all objects.
    :type center_object: bool
    :param center_object: If True, scaling is done relative to the center of each input entity independently.
        Otherwise, scaling is done against the average center of all the input entities.
    :type center_object: bool, optional
    :param number_of_copies: Number of additional copies of the input entities to create. Each copy is scaled
        by factor relative to the last copy made.
    :type number_of_copies: int, optional
    :return: Scaled entities (including any copies).
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/scale_delta.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 0)

    return pymatic.scale(trimatic.utils.single_or_multiple_entities(entities), False,
                         trimatic.utils.point_argument(delta), center_object, number_of_copies)

def translate(entities,translation_vector, number_of_copies = 0):
    """Translates entities along the specified translation vector

    :param entities: Either single object or heterogeneous list of root level entities
        (parts, analytical primitives, datum planes).
    :type entities: trimatic.Object | [trimatic.Object]
    :param translation_vector: An (x,y,z) tuple representing the vector of translation.
    :type translation_vector: (float, float, float)
    :param number_of_copies: Number of additional copies of the input entities to create. Each copy is
        translated by translation_vector relative to the last copy made.
    :type number_of_copies: int, optional
    :return: Translated entities (including any copies).
    :rtype:  trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/translate.py
    """


    trimatic.utils.check_type("entities", entities, trimatic.utils.transformable_types())
    trimatic.utils.check_param_greater_or_equal("number_of_copies", number_of_copies, 0)

    return pymatic.translate(trimatic.utils.single_or_multiple_entities(entities),trimatic.utils.point_argument(translation_vector),number_of_copies)

class UpdateOCSMethod(Enum):
    """Updates object coordinate system method."""

    Inertia_axes = "Inertia axes"
    """Part inertia axes update OCS method."""

    WCS = "WCS"
    """World coordinate system update OCS method."""

    User_defined_CS = "User defined coordinate system"
    """User-defined entity coordinate system update OCS method."""


def update_ocs_to_cs(entity, method=UpdateOCSMethod.WCS, user_defined_cs=None):
    """Updates the object coordinate system to a defined coordinate system.

    :param entity: Part that needs the OCS to be updated
    :type entity: trimatic.Part
    :param method: Updates the OCS based on one of the methods
    :type method: trimatic.UpdateOCSMethod, optional
    :param user_defined_cs: The OCS of the part will be made the same as the OCS of selection here.
     This parameter is valid only when method = User_defined_CS
    :type user_defined_cs: trimatic.CoordinateSystem, optional

    :return: Part with updated OCS, which will be the same as the entity
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/align/update_ocs_to_cs.py
    """



    trimatic.utils.check_type("entity", entity, (trimatic.Part,))
    trimatic.utils.check_type("method", method, (UpdateOCSMethod,))

    if method == UpdateOCSMethod.User_defined_CS:
        trimatic.utils.check_type("user_defined_cs", user_defined_cs, (trimatic.Part,) + trimatic.utils.analytical_primitive_types())

    return pymatic.update_ocs_to_cs(trimatic.utils.single_or_multiple_entities(entity), method.value, user_defined_cs)

