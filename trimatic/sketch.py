import pymatic
import trimatic.utils

def create_sketch(planes):
    """Creates a sketch from one or more existing plane(s).

    :param planes: Planes that define the sketch. When multiple planes are specified, they are averaged.
    :type planes: trimatic.Plane | [trimatic.Plane]
    :raises: ValueError, RuntimeError
    :return: sketch 
    :rtype: trimatic.Sketch

    :example:

    .. literalinclude:: example/sketch/create_sketch.py
    """

    trimatic.utils.check_type("planes", planes, (trimatic.Plane))
    return pymatic.create_sketch(trimatic.utils.single_or_multiple_entities(planes))

def import_intersection(sketch, entities, construction = False):
    """Imports entities into a sketch by making intersections.

    :param entities: One or more entities to intersect with.
    :type entities: trimatic.Curve | trimatic.CurveSet | trimatic.Surface | trimatic.SurfaceSet | trimatic.Part | trimatic.Plane | trimatic.Arc | trimatic.Line | trimatic.Point | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.CurveSet | trimatic.Surface | trimatic.SurfaceSet | trimatic.Part | trimatic.Plane | trimatic.Arc | trimatic.Line | trimatic.Point | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param sketch: Target sketch for import.
    :type sketch: trimatic.Sketch
    :param construction: When True, geometry is imported as construction. 
    :type construction: bool, optional
    :raises: ValueError, RuntimeError
    :return: sketch 
    :rtype: trimatic.Sketch

    :example:

    .. literalinclude:: example/sketch/import_intersection.py
    """

    trimatic.utils.check_type("sketch", sketch, (trimatic.Sketch))
    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Surface, trimatic.SurfaceSet, trimatic.Plane, trimatic.Part, trimatic.Arc, trimatic.Line, trimatic.Point, trimatic.SurfaceBorder,  trimatic.SurfaceContour))
    return pymatic.import_intersection(sketch, trimatic.utils.single_or_multiple_entities(entities), construction )

def import_outline(sketch, entities, construction = False):
    """Imports outline of entities into a sketch.

    :param entities: One or more entities to compute outline.
    :type entities: trimatic.Surface | trimatic.SurfaceSet | trimatic.Part | [trimatic.Surface | trimatic.SurfaceSet | trimatic.Part]
    :param sketch: Target sketch for import.
    :type sketch: trimatic.Sketch
    :param construction: When True, geometry is imported as construction. 
    :type construction: bool, optional
    :raises: ValueError, RuntimeError
    :return: sketch 
    :rtype: trimatic.Sketch

    :example:

    .. literalinclude:: example/sketch/import_outline.py
    """

    trimatic.utils.check_type("sketch", sketch, (trimatic.Sketch))
    trimatic.utils.check_type("entities", entities, (trimatic.Surface, trimatic.SurfaceSet, trimatic.Part))
    return pymatic.import_outline(sketch, trimatic.utils.single_or_multiple_entities(entities), construction )

def import_projection(sketch, entities, construction = False):
    """Projects entities onto a sketch.

    :param entities: One or more entities to project.
    :type entities: trimatic.Curve | trimatic.CurveSet | trimatic.Arc | trimatic.Line | trimatic.Point | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.CurveSet | trimatic.Arc | trimatic.Line | trimatic.Point | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param sketch: Sketch to project onto.
    :type sketch: trimatic.Sketch
    :param construction: When True, geometry is imported as construction. 
    :type construction: bool, optional
    :raises: ValueError, RuntimeError
    :return: sketch 
    :rtype: trimatic.Sketch

    :example:

    .. literalinclude:: example/sketch/import_projection.py
    """

    trimatic.utils.check_type("sketch", sketch, (trimatic.Sketch))
    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Arc, trimatic.Line, trimatic.Point, trimatic.SurfaceBorder,  trimatic.SurfaceContour))
    return pymatic.import_projection(sketch, trimatic.utils.single_or_multiple_entities(entities), construction )

def sketch_to_curves(sketch, add_to = None):
    """Converts a sketch to curves.

    :param sketch: Sketch to export.
    :type sketch: trimatic.Sketch
    :param add_to: Target part to add the resulting curve to. If set to None, a new part is created.
    :type add_to: trimatic.Part, optional
    :raises: ValueError, RuntimeError
    :return: Part that contains the output curves.
    :rtype: trimatic.Part

    :example:

    .. literalinclude:: example/sketch/sketch_to_curves.py
    """

    trimatic.utils.check_type("sketch", sketch, (trimatic.Sketch))
    trimatic.utils.check_type("add_to", add_to,(trimatic.Part,), True)
    return pymatic.sketch_to_curves(sketch, add_to)
