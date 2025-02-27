import pymatic
import trimatic.utils

def mark_overlapping_triangles(entities, tolerance = 0.1, angle = 5, face_to_face = True, face_to_back = True):
    """Marks overlapping triangles in the specified entities.
    
    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param tolerance: The distance between the 2 triangles that are considered as ‘double’ is smaller than the given tolerance.
    :type tolerance: float, optional
    :param angle: The angle (in degrees) between the 2 normals of the triangles that are considered to be ‘double’ is smaller than the given angle
    :type angle: float, optional
    :param face_to_face: The normals of the triangles that are considered as ‘double’ must be pointing in opposite direction.
    :type face_to_face: bool, optional
    :param face_to_back: The normals of the triangles that are considered as ‘double’ must be pointing in the same direction.
    :type face_to_back: bool, optional
    :return: Marked triangles for every part that was processed (complete or entity in it).
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/mark_overlapping_triangles.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_param_in_range("angle", angle, 0, 180)
    trimatic.utils.check_param_greater_or_equal("tolerance", tolerance, 0)


    return pymatic.mark_overlapping_triangles(trimatic.utils.single_or_multiple_entities(entities), tolerance, angle, face_to_face, face_to_back)

def mark_identical_triangles(entities, face_to_face = True, face_to_back = True):
    """Marks identical triangles in the specified entities.
    
    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param face_to_face: The normals of the triangles that are considered as ‘double’ must be pointing in opposite direction.
    :type face_to_face: bool, optional
    :param face_to_back: The normals of the triangles that are considered as ‘double’ must be pointing in the same direction.
    :type face_to_back: bool, optional
    :return: Marked triangles for every part that was processed (complete or entity in it).
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/mark_identical_triangles.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))


    return pymatic.mark_identical_triangles(trimatic.utils.single_or_multiple_entities(entities), face_to_face, face_to_back)

def mark_entities(entities, mark = True):
    """The entities to mark or unmark.
    
    :param entities: Either a single object or a heterogeneous list of objects.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.Curve]
    :param mark: The entities will be marked (True) or unmarked (False).
    :type mark: bool, optional
    :return: Marked triangles for every part that was processed (complete or entity in it).
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/mark_entities.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Curve))


    return pymatic.mark_entities(trimatic.utils.single_or_multiple_entities(entities), mark)

def mark_expand(entities, number_of_iterations = 1, mark_across_surfaces = True):
    """Expand marking.
    
    :param entities: One or more objects of type trimatic.MarkedTriangles.
    :type entities: trimatic.MarkedTriangles | [trimatic.MarkedTriangles]
    :param number_of_iterations: The number of expansions.
    :type number_of_iterations: int, optional
    :param mark_across_surfaces: When True, the marking is not limited to one surface.
    :type mark_across_surfaces: bool, optional
    :return: Resulting marked triangles objects.
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/mark_expand.py
    """

    trimatic.utils.check_type("entities", entities, trimatic.MarkedTriangles)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)


    return pymatic.mark_expand(trimatic.utils.single_or_multiple_entities(entities), number_of_iterations, mark_across_surfaces)

def mark_intersecting_triangles(entities):
    """Marks overlapping triangles in the specified parts.
    
    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.Part | [trimatic.Part]
    :return: Marked triangles for every part that was processed.
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/mark_intersecting_triangles.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, ))


    return pymatic.mark_intersecting_triangles(trimatic.utils.single_or_multiple_entities(entities))

def mark_shrink(entities, number_of_iterations = 1):
    """Shrinks marking.
    
    :param entities: One or more objects of type trimatic.MarkedTriangles.
    :type entities: trimatic.MarkedTriangles | [trimatic.MarkedTriangles]
    :param number_of_iterations: The number of shrinking steps.
    :type number_of_iterations: int, optional
    :return: Resulting marked triangles objects.
    :rtype: trimatic.MarkedTriangles | (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/mark/mark_shrink.py
    """

    trimatic.utils.check_type("entities", entities, trimatic.MarkedTriangles)
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1)


    return pymatic.mark_shrink(trimatic.utils.single_or_multiple_entities(entities), number_of_iterations)

def move_to_surface(entities):
    """Moves marked triangles to a new surface.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.MarkedTriangles | [trimatic.MarkedTriangles]
    :return: Newly created surface.
    :rtype: trimatic.Surface | (trimatic.Surface)

    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/mark/move_to_surface.py
    """

    trimatic.utils.check_type("entities", entities, trimatic.MarkedTriangles )

    return pymatic.move_to_surface(trimatic.utils.single_or_multiple_entities(entities))
