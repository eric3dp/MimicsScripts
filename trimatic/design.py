import pymatic
import trimatic.utils

from trimatic.data import TriangulationAccuracy
from trimatic.data import HollowType

def boolean_intersection(entities):
    """Creates a part representing an intersection of two or more parts or graphs.

    New part will be created and the original parts will be removed.

    :param entities: The parts or graphs used in the intersection operation.
    :type entities: [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :return: Intersected part.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/boolean_intersection.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))

    trimatic.utils.check_entities_must_be_multiple("entities",entities)

    return pymatic.boolean_intersection(trimatic.utils.single_or_multiple_entities(entities))

def boolean_subtraction(entities, subtracting_entities):
    """Subtracts single part or list of parts or graphs from another part or list of parts.

    New parts will be created and the original parts will be removed.

    :param entities: Boolean subtraction is performed on these parts or graphs.
    :type entities: [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param subtracting_entities: The subtraction is performed with these parts.
    :type subtracting_entities: trimatic.Part | [trimatic.Part]
    :return: Resulting part after subtraction.
    :rtype:  trimatic.Part | (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/boolean_subtraction.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_type("subtracting_entities", subtracting_entities, (trimatic.Part))
    trimatic.utils.trimatic.utils.check_entity_sets_do_not_contain_equal_entities("entities", "subtracting_entities", entities, subtracting_entities)

    return pymatic.boolean_subtraction(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.single_or_multiple_entities(subtracting_entities))

def boolean_union(entities):
    """Creates a part representing an union of two or more parts or graphs.

    New part will be created and the original parts will be removed.

    :param entities: Boolean union is performed on these parts or graphs.
    :type entities: [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :return: United part.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/boolean_union.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_entities_must_be_multiple('entities',entities)

    return pymatic.boolean_union(trimatic.utils.single_or_multiple_entities(entities))

def circular_sweep(
        sweep_paths,
        sweep_diameter=1.0,
        accuracy=0.01,
        round_begin=False,
        round_end=False
):
    """Creates a tubular structure along a path, with options to add round endpoints.

    :param sweep_paths: Paths to create circular sweeps.
    :type sweep_paths: trimatic.Curve | trimatic.CurveSet | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.CurveSet | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param sweep_diameter: Defines the diameter of the tubular shape of the sweep.
    :type sweep_diameter: float, optional
    :param accuracy: Defines the accuracy of the tubular shape in a polygon mesh.
    :type accuracy: float, optional
    :param round_begin: When True, the beginning part of the runner will be rounded.
    :type round_begin: bool, optional
    :param round_end: When True, the ending part of the runner will be rounded.
    :type round_end: bool, optional
    :returns: The resulting runner part.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/circular_sweep.py
    """


    trimatic.utils.check_type("sweep_paths", sweep_paths, (trimatic.Curve, trimatic.CurveSet, trimatic.SurfaceBorder, trimatic.SurfaceContour, trimatic.Sketch))
    trimatic.utils.check_param_greater("sweep_diameter", sweep_diameter, 0)
    trimatic.utils.check_param_greater("sweep_diameter", sweep_diameter, 2*accuracy)
    pymatic_entities = trimatic.utils.single_or_multiple_entities(sweep_paths)
    if len(pymatic_entities) > 99:
        raise ValueError("Parameter 'sweep_paths' The maximum number of path should only be 99")

    return pymatic.circular_sweep(pymatic_entities, sweep_diameter, accuracy, round_begin, round_end)


def convert_analytical_to_mesh(entities, tolerance = 0.01):
    """This operation allows you to convert existing analytical primitives to a triangulated part.

    :param entities: The analytical primitives to convert.
    :type entities: trimatic.Cone | trimatic.Cylinder | trimatic.Plane | trimatic.Sphere | [trimatic.Cone | trimatic.Cylinder | trimatic.Plane | trimatic.Sphere]
    :return: Triangulated parts.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/convert_analytical_to_mesh.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Cone, trimatic.Cylinder, trimatic.Plane, trimatic.Sphere))
    trimatic.utils.check_resolution("tolerance", tolerance)

    return pymatic.convert_analytical_to_mesh(trimatic.utils.single_or_multiple_entities(entities),tolerance)

def create_box_around_part(part):
    """Creates a box corresponding to the bounding box of a part.

    :param part: Part to create box around.
    :type part: trimatic.Part
    :return: Created box.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_box_around_part.py
    """

    trimatic.utils.check_type("part", part, (trimatic.Part, ))
    return pymatic.create_box_around_part(part)

def create_box_part(corner_point, x_extent, y_extent, z_extent):
    """Creates a box with the corner point method.

    :param corner_point: Corner point that is shared by the Back, Left and Bottom surface of the box.
    :type corner_point: trimatic.Point
    :param x_extent: Length of the box along positive x axis.
    :type x_extent: float
    :param y_extent: Length of the box along positive y axis.
    :type y_extent: float
    :param z_extent: Length of the box along positive z axis.
    :type z_extent: float
    :return: Created box.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_box_part.py
    """

    trimatic.utils.check_resolution("x_extend", x_extent)
    trimatic.utils.check_resolution("y_extend", y_extent)
    trimatic.utils.check_resolution("z_extend", z_extent)
    return pymatic.create_box_part(trimatic.utils.point_argument(corner_point), x_extent, y_extent, z_extent)

def create_cone_part(
    *args,#'force named parameters'
    origin,
    direction,
    height,
    bottom_radius,
    top_radius = 0,
    tolerance = 0.01,
    target_edge_length = 0
    ):
    """Creates a cone by specifying its axis.

    :param origin: Origin of the axis of the cone (center of bottom of the cone).
    :type origin: trimatic.Point
    :param direction: Up axis direction of the cone.
    :type direction: trimatic.Point
    :param height: Height of the cone.
    :type height: float
    :param bottom_radius: Bottom radius of the cone.
    :type bottom_radius: float
    :param top_radius: Top radius of the cone.
    :type top_radius: float, optional
    :param tolerance: The maximum error allowed between the mathematical cone and its triangulated representation.
    :type tolerance: float, optional
    :param target_edge_length: Targeted triangle edge length of the cone. If 0, no target edge length will be defined.
    :type target_edge_length: float, optional
    :return: Created cone.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_cone_part.py
    """


    trimatic.utils.check_vector_not_equal("direction", direction, [0, 0, 0])
    trimatic.utils.check_resolution("height", height)
    trimatic.utils.check_resolution("bottom_radius", bottom_radius)
    trimatic.utils.check_param_greater_or_equal("top_radius", top_radius, 0)
    trimatic.utils.check_param_greater_or_equal("tolerance", tolerance, trimatic.utils.get_resolution())
    trimatic.utils.check_param_greater_or_equal("target_edge_length", target_edge_length, 0)

    return pymatic.create_cone_part(trimatic.utils.point_argument(origin), trimatic.utils.point_argument(direction), height, bottom_radius, top_radius, tolerance, target_edge_length)

def create_cylinder_part(point_1, point_2, radius, tolerance = 0.01):
    """Creates a cylinder using 2 points method.

    :param point_1: The center point of the bottom surface of the cylinder.
    :type point_1: trimatic.Point
    :param point_2: The center point of the top surface of the cylinder.
    :type point_2: trimatic.Point
    :param radius: Radius of the cylinder.
    :type radius: float
    :param tolerance: The maximum error allowed between the mathematical cylinder and its triangulated representation.
    :type tolerance: float, optional
    :return: Created cylinder.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_cylinder_part.py
    """


    trimatic.utils.check_2points_not_coincident("point_1", "point_2", point_1, point_2)
    trimatic.utils.check_resolution("radius", radius)
    trimatic.utils.check_resolution("tolerance", tolerance)

    return pymatic.create_cylinder_part(trimatic.utils.point_argument(point_1), trimatic.utils.point_argument(point_2), radius, tolerance)

def create_pyramid(
    *args,#'force named parameters'
    bottom_point,
    top_point,
    bottom_radius,
    top_radius = 0,
    number_of_faces = 3,
    target_edge_length = 0
    ):
    """Creates a pyramid by specifying its bottom point and top point.

    :param bottom_point: Center of the bottom face of the pyramid.
    :type bottom_point: trimatic.Point
    :param top_point: Center of the top face of the pyramid.
    :type top_point: trimatic.Point
    :param bottom_radius: Bottom radius of the pyramid.
    :type bottom_radius: float
    :param top_radius: Top radius of the pyramid.
    :type top_radius: float, optional
    :param number_of_faces: The number of faces in the mantle of the pyramid.
    :type number_of_faces: int, optional
    :param target_edge_length: Targeted triangle edge length of the pyramid. If 0, no target edge length will be defined.
    :type target_edge_length: float, optional
    :return: Created pyramid.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_pyramid.py
    """


    trimatic.utils.check_2points_not_coincident("bottom_point", "top_point", bottom_point, top_point)
    trimatic.utils.check_resolution("bottom_radius", bottom_radius)
    trimatic.utils.check_param_greater_or_equal("top_radius", top_radius, 0)
    trimatic.utils.check_param_in_range("number_of_faces", number_of_faces, 3, 500)
    trimatic.utils.check_param_greater_or_equal("target_edge_length", target_edge_length, 0)

    return pymatic.create_pyramid(trimatic.utils.point_argument(bottom_point), trimatic.utils.point_argument(top_point), bottom_radius, top_radius, number_of_faces, target_edge_length)

def create_pyramid_part(
    *args,#'force named parameters'
    origin,
    direction,
    height,
    bottom_radius,
    top_radius = 0,
    number_of_faces = 3,
    target_edge_length = 0
    ):
    """Creates a pyramid by specifying its axis.

    :param origin: Origin of the axis of the pyramid (center of bottom of the pyramid).
    :type origin: trimatic.Point
    :param direction: Up axis direction of the pyramid.
    :type direction: trimatic.Point
    :param height: Height of the pyramid.
    :type height: float
    :param bottom_radius: Bottom radius of the pyramid.
    :type bottom_radius: float
    :param top_radius: Top radius of the pyramid.
    :type top_radius: float, optional
    :param number_of_faces: The number of faces in the mantle of the pyramid.
    :type number_of_faces: int, optional
    :param target_edge_length: Targeted triangle edge length of the pyramid. If 0, no target edge length will be defined.
    :type target_edge_length: float, optional
    :return: Created pyramid.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_pyramid_part.py
    """


    pymatic_direction = trimatic.utils.point_argument(direction)
    trimatic.utils.check_direction("direction", pymatic_direction)

    trimatic.utils.check_resolution("height", height)
    trimatic.utils.check_resolution("bottom_radius", bottom_radius)
    trimatic.utils.check_param_greater_or_equal("top_radius", top_radius, 0)
    trimatic.utils.check_param_in_range("number_of_faces", number_of_faces, 3, 500)
    trimatic.utils.check_param_greater_or_equal("target_edge_length", target_edge_length, 0)

    return pymatic.create_pyramid_part(trimatic.utils.point_argument(origin), pymatic_direction, height, bottom_radius, top_radius, number_of_faces, target_edge_length)

def create_sphere_part(point_center, radius, tolerance = 0.01):
    """Creates a sphere using center and radius method.

    :param point_center: The center point of sphere.
    :type point_center: trimatic.Point
    :param radius: The radius of the sphere.
    :type radius: float
    :param tolerance: The maximum error allowed between the mathematical sphere and its triangulated representation.
    :type tolerance: float, optional
    :return: Created sphere.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/create_sphere_part.py
    """


    trimatic.utils.check_resolution("radius", radius)
    trimatic.utils.check_resolution("tolerance", tolerance)
    return pymatic.create_sphere_part(trimatic.utils.point_argument(point_center), radius, tolerance)

def cut(entities, cutting_entity, clearance=0):
    """Cuts one or more parts with another part or a plane.

    New parts will be created and the original entities will be removed.

    :param entities: Entities to cut.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet ]
    :param cutting_entity: Single part or single plane.
    :type cutting_entity: trimatic.Part | trimatic.Plane
    :param clearance: The gap length between the split entities. Set to 0 for no clearance.
    :type clearance: float, optional
    :return: Resulting parts after cut.
    :rtype: (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/cut.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_type("cutting_entity", cutting_entity, (trimatic.Plane,trimatic.Part))
    trimatic.utils.check_param_greater_or_equal("clearance", clearance, 0)

    return pymatic.cut(pymatic_entities, cutting_entity, clearance)

def extend_surface_linear(entities, distance = 1.0, solid = False, segments = 1, smoothing_distance = 1.0):
    """Extends a surface.

    Extends a surface using linear tangential method. The extension is tangential to the surface and straight.

    :param entities: Either single object or a heterogeneous list of objects.
    :type entities: trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder | [trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder] | (trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder)
    :param distance: Length of extension.
    :type distance: float, optional
    :param solid: If True, the triangles on the neighboring surfaces will remain connected.
    :type solid: bool, optional
    :param segments: Number of segments in an extension part.
    :type segments: int, optional
    :param smoothing_distance: The smoothing distance will avoid wrinkles and overlays at the corners. It is advised to keep this parameter identical to the distance parameter.
    :type smoothing_distance: float, optional

    :return: Extended surfaces.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/extend_surface_linear.py
    """

    if smoothing_distance is None:
        smoothing_distance = 0.0


    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.Surface, trimatic.SurfaceContour, trimatic.SurfaceBorder))
    trimatic.utils.check_param_greater("distance", distance, 0.0)
    trimatic.utils.check_param_greater_or_equal("segments", segments, 1)
    trimatic.utils.check_param_greater_or_equal("smoothing_distance", smoothing_distance, 0.0)

    return pymatic.extend_surface_linear(trimatic.utils.single_or_multiple_entities(entities), distance, True, solid, segments, smoothing_distance)

def extend_surface_curved(entities, distance = 1.0, solid = False, accuracy = trimatic.TriangulationAccuracy.Coarse):
    """Extends a surface.

    Extends a surface using curved tangential method. The extension is tangential to the surface and tries to follow the curvature of the surface.

    :param entities: Either single object or a heterogeneous list of objects.
    :type entities: trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder | [trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder] | (trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour | trimatic.SurfaceBorder)
    :param distance: Distance of extension.
    :type distance: float, optional
    :param solid: If True, then neighbour triangles will be moved too.
    :type solid: bool, optional
    :param accuracy: Accuracy of triangulation.
    :type accuracy: trimatic.TriangulationAccuracy, optional

    :return: Extended surfaces.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/extend_surface_curved.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.Surface, trimatic.SurfaceContour, trimatic.SurfaceBorder))
    trimatic.utils.check_type("accuracy", accuracy, (trimatic.TriangulationAccuracy,))
    trimatic.utils.check_param_greater("distance", distance, 0.0)

    return pymatic.extend_surface_curved(trimatic.utils.single_or_multiple_entities(entities), distance, True, solid, accuracy.value)

def extrude(
    *args, #'force named parameters'
    entities,
    direction,
    depth1 = 1,
    upto_entities1 = None,
    draft_angle1 = 0,
    draft_outwards1 = False,
    depth2 = None,
    upto_entities2 = None,
    draft_angle2 = 0,
    draft_outwards2 = False,
    solid = True,
    part_to_cut = None,
    flip_side_to_cut = False
    ):
    """Extrudes curves, curve sets or sketch to create a part.

    :param entities: Either single object or a heterogeneous list of curve like entities.
    :type entities: trimatic.Curve | trimatic.CurveSet | trimatic.Sketch | trimatic.SurfaceBorder | trimatic.SurfaceContour | [trimatic.Curve | trimatic.CurveSet | trimatic.Sketch | trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param direction: Direction to extrude the curves.
    :type direction: trimatic.Point
    :param depth1: Depth for extrude along selected direction. Note that this value is ignored when upto_entities1 is not None.
    :type depth1: float, optional
    :param upto_entities1: When specified, the extrude will be done up to the entities specified.
    :type upto_entities1: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet], optional
    :param draft_angle1: Draft or taper applied to the extrusion. For example, draft applied during extrusion of a circle results in a cone.
    :type draft_angle1: float, optional
    :param draft_outwards1: If True, the draft angle will be oriented outwards.
    :type draft_outwards1: bool, optional
    :param depth2: Depth for extrude along opposite of the selected direction. Note that this value is ignored when upto_entities2 is not None.
    :type depth2: float, optional
    :param upto_entities2: When specified, the extrude will be done up to the entities spcified for the opposite direction.
    :type upto_entities2: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet], optional
    :param draft_angle2: Draft or taper applied to the opposite extrusion.
    :type draft_angle2: float, optional
    :param draft_outwards2: If True, the draft angle will be oriented outwards.
    :type draft_outwards2: bool, optional
    :param solid: If True, a bottom and top surface will be created when performed on a closed curve. When curves are not closed, RuntimeError will be raised.
    :type solid: bool, optional
    :param part_to_cut: When specified, the extrude will cut material from this part. This corresponds to method "Cut Extrude" in GUI.
    :type part_to_cut: trimatic.Part, optional
    :param flip_side_to_cut: When True, the cut will preserve outside, whereas when False the cut will preserve the inside. This paramter only has effect when part_to_cut is specified.
    :type flip_side_to_cut: trimatic.Part, optional
    :return: Resulting part after extrude.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/extrude.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Sketch, trimatic.SurfaceBorder, trimatic.SurfaceContour))
    trimatic.utils.check_param_greater_or_equal("draft_angle1", draft_angle1, 0)
    trimatic.utils.check_param_greater_or_equal("draft_angle2", draft_angle2, 0)

    pymatic_upto1 = trimatic.utils.single_or_multiple_entities(upto_entities1)
    trimatic.utils.check_type("upto_entities1", pymatic_upto1, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet), True)
    pymatic_upto2 = trimatic.utils.single_or_multiple_entities(upto_entities2)
    trimatic.utils.check_type("upto_entities2", pymatic_upto1, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet), True)
    trimatic.utils.check_type("part_to_cut", part_to_cut, (trimatic.Part, ), True)

    pydirection = trimatic.utils.point_argument(direction)
    trimatic.utils.check_direction("direction", pydirection)

    return pymatic.extrude(pymatic_entities, pydirection, depth1, pymatic_upto1, draft_angle1, draft_outwards1, depth2, pymatic_upto2, draft_angle2, draft_outwards2, solid, part_to_cut, flip_side_to_cut )



def hollow(
        *args,
        entities,
        hollow_type = HollowType.Inside,
        distance = 1.00,
        smallest_detail = 0.30,
        smooth_factor =0.5,
        reduce = True
    ):
    """Creates an extra shell that gives the part a thickness.
    New shells will be created and the original entities will be removed.

    :param entities: Either single object or a heterogeneous list of parts or surfaces.
    :type entities: trimatic.Part | trimatic.Surface | [trimatic.Part | trimatic.Surface]
    :param hollow_type: Define whether a new surface is created on the inside, outside or both side of the input entity. Hollowing an open entity on both sides will result in an enveloping surface. 
    :type hollow_type: trimatic.HollowType, optional
    :param distance: The overall thickness of the part after the operation.
    :type distance: float, optional
    :param smallest_detail: Targeted size of triangles of the newly created surface.
    :type smallest_detail: float, optional
    :param smooth_factor: Strength of smoothing of the created surfaces
    :type smooth_factor: float, optional
    :param reduce: If True, triangle reduction will be applied on the newly created surface.
    :type reduce: bool, optional
    :return: Newly created surface(s).
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/hollow.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface))
    trimatic.utils.check_entities_does_not_have_part_and_one_of_its_surfaces("entities", entities)
    trimatic.utils.check_param_greater_or_equal("distance", distance, 0)
    trimatic.utils.check_resolution("smallest_detail", smallest_detail)
    trimatic.utils.check_type("hollow_type", hollow_type, (trimatic.HollowType,))
    trimatic.utils.check_param_in_range("smooth_factor", smooth_factor, 0.0, 1.0)

    return pymatic.hollow(pymatic_entities, hollow_type.value, distance, smallest_detail, smooth_factor, reduce)

def local_offset(surface_entities, offset_distance = 1.0, diminishing_distance = 5.0):
    """Performs offset on a local area (surfaces).

    The offset will be zero at the surface border and increase over a given distance (diminishing distance) to the set maximum offset distance.

    :param surface_entities: Either single entity or a heterogeneous list of surface or surface sets.
    :type surface_entities: trimatic.Surface | trimatic.SurfaceSet | trimatic.SurfaceContour | trimatic.MarkedTriangles| [trimatic.Surface | trimatic.SurfaceSet | trimatic.SurfaceContour | trimatic.MarkedTriangles]
    :param offset_distance: The maximum distance for local offset, which is applied a given distance from surface border.
                            For external offset, specify positive distance. For internal offset, specify negative distance.
    :type offset_distance: float, optional
    :param diminishing_distance: The transitioning distance between surface border and the maximum offset distance. The offset will be zero at
        the surface border and increases over this distance to the given distance.
    :type diminishing_distance: float, optional
    :return: Surface after operation.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/local_offset.py
    """


    trimatic.utils.check_type("surface_entities", surface_entities, (trimatic.Surface, trimatic.SurfaceSet,  trimatic.SurfaceContour, trimatic.MarkedTriangles))

    trimatic.utils.check_param_greater("diminishing_distance",diminishing_distance, 0.0)

    return pymatic.local_offset(trimatic.utils.single_or_multiple_entities(surface_entities), offset_distance, diminishing_distance)

def loft(entity1, entity2, merge = True):
    """Surface loft operation.

    :param entity1: Bad Contour, Curve or Surface to start the loft. For surfaces, only surfaces with one contour are allowed. Surfaces with only bad contour(s) are not allowed.
                                    For curves, only closed curves are allowed.
    :type entity1: trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour
    :param entity2: Bad Contour, Curve or Surface to end the loft. Same restrictions as for entity1 apply.
    :type entity2: trimatic.Curve | trimatic.Surface | trimatic.SurfaceContour
    :param merge: When False, a new part is created and it contains the loft surface with two side surfaces.
                  When True, only loft surface is created and it will be merged with the original parts to which the seleted entities belong to. These original parts will be removed.
                  If surface is selected as input, the selected surface will be removed from the original part to create a solid result.
                  Remark: If curve is selected, this parameter has no effect. The result will be as with merge = False.
    :type merge: bool, optional

    :return: Resulting surface(s) after loft
    :rtype: (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/loft.py
    """


    trimatic.utils.check_type("entity1", entity1, (trimatic.Curve, trimatic.Surface, trimatic.SurfaceContour))
    trimatic.utils.check_type("entity2", entity2, (trimatic.Curve, trimatic.Surface, trimatic.SurfaceContour))

    return pymatic.loft(entity1, entity2, merge)

def move_surface(entities, direction = None, distance = 1.0, solid = True):
    """This operation will move selected surface in a defined direction and over a defined distance.

    :param entities: One or more surfaces or surface sets.
    :type entities: trimatic.Surface | trimatic.SurfaceSet | [trimatic.Surface | trimatic.SurfaceSet]
    :param direction: The direction vector according to which the selected surfaces will be moved. When None is specified, automatic directions per surface are chosen.
    :type direction: trimatic.Point, optional
    :param distance: The distance over which the selected surfaces will be moved. Positive distance corresponds to outside movement when direction is None.
    :type distance: float, optional
    :param solid: If True, the triangles on the neighboring surfaces will remain connected.
    :type solid: bool, optional

    :return: Newly created surfaces.
    :rtype: (trimatic.SurfaceSet)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/move_surface.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Surface, trimatic.SurfaceSet))
    py_direction = direction
    if direction is not None:
        trimatic.utils.check_param_greater("distance", distance, 0.0)
        py_direction = trimatic.utils.point_argument(direction)

    return pymatic.move_surface(trimatic.utils.single_or_multiple_entities(entities), py_direction, distance, solid)

def surface_construction(entities, guiding_lines = None, grid_size = 3):
    """The surface construction allows you to construct new surfaces.

    :param entities: Possible entities: Bad contour, curve (attached along a bad contour or partially attached along a bad contour).
                     Remark: the entity should be closed and the entity may not lie in a flat plane.
    :type entities: trimatic.Curve | trimatic.SurfaceContour | [trimatic.Curve | trimatic.SurfaceContour]
    :param guiding_lines: The guiding lines are optional. They only guide the newly constructed surface, which means that the newly constructed surface is not per definition going through the guides.
    :type guiding_lines: trimatic.Curve | trimatic.CurveSet | trimatic.Sketch | [trimatic.Curve | trimatic.CurveSet | trimatic.Sketch], optional
    :param grid_size: The size of the triangles that will create the surface.
    :type grid_size: float, optional
    :return: Resulting surfaces.
    :rtype: (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/surface_construction.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.SurfaceContour))
    trimatic.utils.check_entities_only_contain_closed_curves("entities", entities)
    pymatic_guiding_lines= trimatic.utils.single_or_multiple_entities(guiding_lines)
    trimatic.utils.check_resolution("grid_size", grid_size)
    trimatic.utils.check_type("pymatic_guiding_lines", pymatic_guiding_lines, ( trimatic.Curve, trimatic.CurveSet, trimatic.Sketch), allow_none_or_empty = True)
    return pymatic.surface_construction(trimatic.utils.single_or_multiple_entities(entities), pymatic_guiding_lines, grid_size)

def sweep_loft(start_profile, path, end_profile, intermediate_profiles = None, detail = 0.5):
    """With the Sweep-loft function, you can sweep multiple profiles along a path. Please take the following conditions into account to get a good result:

    i.  Profiles must be closed (both planar and non-planar profiles are allowed).

    ii.  Preferably the path is coincident with the center of the profile . The profile and the path are perpendicular to each other.

    iii.  Selected profiles must not intersect with each other.

    :param start_profile: The starting profile.
    :type start_profile: trimatic.Sketch | trimatic.Curve | trimatic.SurfaceContour
    :param end_profile: The ending profile.
    :type end_profile: trimatic.Sketch | trimatic.Curve | trimatic.SurfaceContour
    :param intermediate_profiles: The intermediate profile(s).
    :type intermediate_profiles: trimatic.Sketch | trimatic.Curve | trimatic.SurfaceContour | [trimatic.Sketch | trimatic.Curve | trimatic.SurfaceContour]
    :param path: The path to follow.
    :type path: trimatic.Curve
    :return: Resulting part.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/sweep_loft.py
    """


    trimatic.utils.check_type("start_profile", start_profile, (trimatic.Sketch, trimatic.Curve, trimatic.SurfaceContour ))
    trimatic.utils.check_type("end_profile", end_profile, (trimatic.Sketch, trimatic.Curve, trimatic.SurfaceContour ))
    trimatic.utils.check_type("intermediate_profiles", intermediate_profiles, (trimatic.Sketch, trimatic.Curve, trimatic.SurfaceContour ), True)
    trimatic.utils.check_type("path", path, (trimatic.Curve, ))
    trimatic.utils.check_resolution("detail", detail)
    return pymatic.sweep_loft(start_profile, path, end_profile, trimatic.utils.single_or_multiple_entities(intermediate_profiles), detail )

def sweep(
        *args,#'force named parameters',
        profile, path,
        follow_surface_left = False,
        follow_surface_right = False,
        segment_angle = 10,
        surface_segmentation_profile_based = False,
        surface_segmentation_path_based_direction_angle = None):
    """Sweeps a profile along a path to create a part.

    :param profile: The profile to be swept.
    :type profile: trimatic.Sketch
    :param path: The path to follow.
    :type path: trimatic.Curve
    :param follow_surface_left: When True, the orientation of the sweep profile during the sweep will follow the surface, so the orientation is preserved with respect to the surface left from the path. This is only possible for attached curves.
    :type follow_surface_left: bool, optional
    :param follow_surface_right: When True, the orientation of the sweep profile during the sweep will follow the surface, so the orientation is preserved with respect to the surface right from the path. This is only possible for attached curves.
    :type follow_surface_right: bool, optional
    :param segment_angle: When the path makes curves, the triangulated surface that originates from the sweep can never make a perfect round. Defining this parameter, you determine the deviation between the triangulated surface and a ‘perfect’ round. The bigger the angle, the fewer segments, the rougher the approximation.
    :type segment_angle: float, optional
    :param surface_segmentation_profile_based: When True, an additional ‘longitudinal’ segmentation is done: each segment of the profile becomes a surface when it is swept around.
    :type surface_segmentation_profile_based: bool, optional
    :param surface_segmentation_path_based_direction_angle: When specified, an additional ‘transversal’ segmentation is done: the surface is segmented when the direction of the path changes. You can set the value of an angle. When the direction changes more than this angle, the surface is split.
    :type surface_segmentation_path_based_direction_angle: float, optional
    :return: Resulting part.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/sweep.py
    """


    trimatic.utils.check_type("profile", profile, (trimatic.Sketch, ))
    trimatic.utils.check_type("path", path, (trimatic.Curve, trimatic.SurfaceContour))
    trimatic.utils.check_param_in_range("segment_angle", segment_angle, 0, 180)
    if surface_segmentation_path_based_direction_angle:
        trimatic.utils.check_param_in_range("surface_segmentation_path_based_direction_angle", surface_segmentation_path_based_direction_angle, 0, 180)
    return pymatic.sweep(profile, path, follow_surface_left, follow_surface_right, segment_angle, surface_segmentation_profile_based, surface_segmentation_path_based_direction_angle )

def uniform_offset(entities, distance, maximum_edge_length = 0.6, solid = False):
    """Performs uniform offset on selected entities.

    Preserve sharp features is assumed checked OFF. New parts will be created and the original entities will be removed.

    :param entities: Either single object or a heterogeneous list of parts, surface, or surface set.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param distance: Offset distance. For external offset, specify positive distance and for internal offset, specify negative distance.
    :type distance: float
    :param maximum_edge_length: Targeted maximum edge length of created triangles.
    :type maximum_edge_length: float, optional
    :param solid: If True, a solid is created. Useful when performing offset on an open part so that the result will be a closed part.
    :type solid: bool, optional
    :return: Resulting parts after uniform offset.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/uniform_offset.py
    """


    trimatic.utils.check_entities_does_not_have_part_and_one_of_its_surfaces("entities", entities)
    trimatic.utils.check_param_in_range("maximum_edge_length", maximum_edge_length, 0.001, 200000.0)
    return pymatic.uniform_offset(trimatic.utils.single_or_multiple_entities(entities), distance, maximum_edge_length, solid)

def uniform_offset_preserve_sharp_features(entities, distance, solid = False):
    """Performs uniform offset on selected entities.

    Preserve sharp features is assumed checked ON. New parts will be created and the original entities will be removed.

    :param entities: Either single object or a heterogeneous list of parts, surface, or surface set.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param distance: Offset distance. For external offset, specify positive distance and for internal offset, specify negative distance.
    :type distance: float
    :param solid: If True, a solid is created. Useful when performing offset on an open part where the result will be a closed part.
    :type solid: bool, optional
    :return: Resulting parts after uniform offset.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/design/uniform_offset_preserve_sharp_features.py
    """


    trimatic.utils.check_entities_does_not_have_part_and_one_of_its_surfaces("entities", entities)
    return pymatic.uniform_offset_preserve_sharp_features(trimatic.utils.single_or_multiple_entities(entities), distance, solid)

def wrap(
    *args,#'force named parameters'
    entities,
    gap_closing_distance = 0,
    smallest_detail = 1,
    protect_thin_walls = False,
    resulting_offset = 0,
    reduce = True,
    preserve_sharp_features = False,
    preserve_surface_structure = False):
    """Wraps part or surface to fix, smooth & offset in one operation.

    :param entities: Either single object or a list of parts, surface or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param gap_closing_distance: The size of gaps that will be closed
    :type gap_closing_distance: float, optional
    :param smallest_detail: Targeted size of triangles after the operation.
    :type smallest_detail: float, optional
    :param protect_thin_walls: If False, there is no protection of thin walls. Depending on the smallest detail, it is possible that walls with a thickness within the same range are collapsed.
        If True, these thin walls will be preserved. This will however mean that the resulting model will be slightly thicker than the original, entirely depending on the smallest detail parameter that is chosen
    :type protect_thin_walls: bool, optional
    :param resulting_offset: Offset that is applied to the parts or surfaces.
    :type resulting_offset: float, optional
    :param reduce: If True, triangle reduction will be applied after wrapping.
    :type reduce: bool, optional
    :param preserve_sharp_features: If True, sharp features will be preserved and not smoothed.
    :type preserve_sharp_features: bool, optional
    :param preserve_surface_structure: If True, the original surface structure and the surface color will be preserved. When input contains surfaces, we recommend using preserve_surface_structure = True.
    :type preserve_surface_structure: bool, optional
    :return: Either single part or a list of parts after wrapping. If the input surfaces/surface sets belong to same part, new single part will be created.
        Otherwise new parts will be created based on the number of parts to which the input surfaces/ surface sets belong.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/design/wrap.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    trimatic.utils.check_param_greater_or_equal("gap_closing_distance", gap_closing_distance, 0)
    trimatic.utils.check_resolution("smallest_detail", smallest_detail)

    return pymatic.wrap(pymatic_entities, gap_closing_distance,smallest_detail, protect_thin_walls, resulting_offset, reduce, preserve_sharp_features, preserve_surface_structure)

def wrap_get_additional_offset_to_protect_thin_walls(smallest_detail = 1):
    """Gets additional offset to protect thin walls.

    :param smallest_detail: Size of triangles on the newly created surface.
    :type smallest_detail: float, optional
    :return: Minimum offset value.
    :rtype: float
    :raises: ValueError

    :example:

    .. literalinclude:: example/design/wrap_get_additional_offset_to_protect_thin_walls.py
    """


    trimatic.utils.check_resolution("smallest_detail", smallest_detail)

    return pymatic.wrap_get_additional_offset_to_protect_thin_walls(smallest_detail)

def create_part(vertices, triangles):
    """Creates Part from given vertices and triangles indices.

    :param vertices: List or tuple of vertices to create part.
    :type vertices: [trimatic.Point] | (trimatic.Point)
    :param triangles: List or tuple of tuples of 3 indices that form triangles to create a part.
    :type triangles: [(int, int, int)] | ((int, int, int))

    :return: Created Part.
    :rtype: trimatic.Part
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/design/create_part.py
    """


    vertices, triangles = trimatic.utils.check_and_return_tuple_of_vertices_and_indices(vertices, triangles)

    return pymatic.create_part(vertices, triangles)

def create_part_by_surfaces(surfaces):
    """Create a part with list or tuple, of lists or tuples containing the information of vertices, triangles, and name for a surface.

    :param surfaces: **vertices** (*[trimatic.Point]|(trimatic.Point)*) is a list or tuple of vertices to form a surface of a part;
        **triangles** (*[(int, int, int)]|(int, int, int)*) is a list or tuple of 3 indices that form triangles to create a surface of a part; and,
        **surface name** (*string*) is a string that gives name to a surface of a part.

    :type surfaces: [[vertices, triangles, surface name],] | ((vertices, triangles, surface name),) | [(vertices, triangles, surface name),] | ([vertices, triangles, surface name],))

    :return: Created part with surfaces.
    :rtype: trimatic.Part
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/design/create_part_by_surfaces.py
    """


    surfaces = trimatic.utils.check_and_return_tuple_of_create_part_surfaces(surfaces)

    return pymatic.create_part_by_surfaces(surfaces)

def create_connections_automatic(
    *args,#'force named parameters'
    entities,
    target_entity = None,
    min_radius = 1,
    max_radius = 5,
    max_length = 50,
    distance = 50):
    """Creates cylindrical connections among parts. Connections are represented by analytical cylinders.

    :param entities: Parts to be connected.
    :type entities: trimatic.Part | [trimatic.Part]
    :param target_entity: A Part to connect entities with. If None, connections will be created among entities, else, between each entity and target_entity.
    :type target_entity: trimatic.Part, optional
    :param min_radius: Minimum radius that will be assigned to a connection.
    :type min_radius: float, optional
    :param max_radius: Maximum radius that will be assigned to a connection.
    :type max_radius: float, optional
    :param max_length: Maximum allowed length for connections.
    :type max_length: float, optional
    :param target_distance: Approximate distance between connections.
    :type target_distance: float, optional

    :return: Created connections.
    :rtype: trimatic.Cylinder | (trimatic.Cylinder)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/design/create_connections.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_type("target_entity", target_entity, (trimatic.Part), True)
    trimatic.utils.check_param_greater("min_radius", min_radius, 0)
    trimatic.utils.check_param_greater_or_equal("max_radius", max_radius, min_radius)
    trimatic.utils.check_param_greater("max_length", max_length, 0)
    trimatic.utils.check_param_greater("distance", distance, 0)
    if target_entity:
        trimatic.utils.check_entity_sets_do_not_contain_equal_entities("entities", "target_entities", entities, target_entity)

    return pymatic.create_connections_automatic(trimatic.utils.single_or_multiple_entities(entities), target_entity, min_radius, max_radius, max_length, distance)

def variable_offset(
    entity,
    base_thickness = -1.0,
    maximum_edge_length = 0.6,
    influence_region = 1.0,
    solid = False,
    local_thickness_parameters = ()):
    """Performs variable offset on selected surface.

    New surface(s) will be created and the original surface will be removed.

    :param entity: Surface with a single contour.
    :type entity: trimatic.Surface
    :param base_thickness: The thickness or distance between the original and offset surfaces on the area which is not influenced by the Influence region. For external offset, specify positive value. For internal offset, specify negative value. Only accepts non-zero value.
    :type base_thickness: float, optional
    :param maximum_edge_length: Targeted maximum edge length of created triangles.
    :type maximum_edge_length: float, optional 
    :param influence_region: The distance of influence from the surface contour outline, inwards to the center of the surface.
    :type influence_region: float, optional
    :param solid: if True, a solid is created. Useful when performing offset on an open part where the result will be a closed part.
    :type solid: bool, optional
    :param local_thickness_parameters: Tuple of tuples containing the info (point, local thickness). The selected points must lie on the contour of the selected surface. 
    :type local_thickness_parameters: ((trimatic.Point, float),), optional

    :return: Surface(s) after variable offset.
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/design/variable_offset.py
    """

    trimatic.utils.check_type("entity", entity, trimatic.Surface)
    trimatic.utils.check_param_not_equal("base_thickness", base_thickness, 0)
    trimatic.utils.check_param_greater("maximum_edge_length", maximum_edge_length, 0)
    trimatic.utils.check_param_greater("influence_region", influence_region, 0)
    if local_thickness_parameters is not None:
        if len(local_thickness_parameters)>0:
            local_thickness_parameters_tuple = []
            for parameter in local_thickness_parameters:
                tuple_point = trimatic.utils.point_argument(parameter[0])
                trimatic.utils.check_param_greater_or_equal("local_thickness_parameters", parameter[1], 0)
                local_thickness_parameters_tuple.append((tuple_point, parameter[1]),)
            local_thickness_parameters_tuple = tuple(local_thickness_parameters_tuple)
            trimatic.utils.check_type_tuple_of_tuples("local_thickness_parameters", local_thickness_parameters_tuple, ((tuple), float),)
            local_thickness_parameters = local_thickness_parameters_tuple

    return pymatic.variable_offset(entity, base_thickness, maximum_edge_length, influence_region, solid, local_thickness_parameters)
