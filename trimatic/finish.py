import pymatic
import trimatic.utils

from trimatic.data import TextAlignment

from enum import Enum


def fillet(entities, radius = 2.0000, tolerance = 0.0100):
    """ Rounds (fillets) the sharp edges between surfaces to a desired radius.
 
    :param entities: Borders or contours to be rounded.
    :type entities: trimatic.SurfaceBorder | trimatic.SurfaceContour |
                          [trimatic.SurfaceBorder | trimatic.SurfaceContour]
    :param radius: The radius of the fillet.
    :type radius: float, optional
    :param tolerance: This parameter allows you to set the accuracy of the fillet. A lower tolerance will lead to a higher accuracy and smaller triangles, whereas a higher tolerance will lead to a lower accuracy and larger triangles. A value equal to or smaller than the radius divided by a factor of 200 usually provides a good result without leading to an excessive number of triangles being generated. 
    :type tolerance: float, optional
    :return: The rounded surfaces that were created
    :rtype: trimatic.Surface | (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/finish/fillet.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.SurfaceBorder, trimatic.SurfaceContour))
    trimatic.utils.check_param_greater_or_equal("radius", radius, trimatic.utils.get_resolution())
    trimatic.utils.check_param_greater_or_equal("tolerance", tolerance, trimatic.utils.get_resolution())
    return pymatic.fillet(trimatic.utils.single_or_multiple_entities(entities), radius, tolerance)


def quick_label(
    *args,#'force named parameters'
    entity,
    text,
    point,
    direction,
    follow_surface = True,
    alignment = TextAlignment.Center,
    font = 'Arial',
    font_height = 4,
    label_height = 1,
    bold = False,
    italic = False
    ):
    """Places a label on a part based on text.

    :param entity: Entity to label.
    :type entity: trimatic.Part
    :param text: Text to use for label. Can be multiline. Use <backslash>n for new lines.
    :type text: string
    :param point: Point where the label will start.
    :type point: trimatic.Point
    :param direction: Direction of the label.
    :type direction: trimatic.Point
    :param follow_surface: When True, the label will be bent to follow the surface normal. When False, the label will be aligned with the normal at the starting point.
    :type follow_surface: bool, optional
    :param alignment: The text alignment.
    :type alignment: trimatic.TextAlignment, optional
    :param font: Font to use for the label.
    :type font: string, optional
    :param font_height: Font height
    :type font_height: float, optional
    :param label_height: Label height (embossed text). Use a negative value for labeling inwards (debossed text).
    :type label_height: float, optional
    :param bold: Set to True for bold font style.
    :type bold: bool, optional
    :param italic: Set to True for italic font style.
    :type italic: bool, optional
    :return: SurfaceSet containing surfaces that were created for the label.
    :rtype: trimatic.SurfaceSet
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/finish/quick_label.py
    """

    trimatic.utils.check_type("entity", entity, (trimatic.Part,))
    trimatic.utils.check_type("alignment", alignment, (TextAlignment,))

    trimatic.utils.check_param_greater("font_height", font_height, 0)

    return pymatic.quick_label(entity, text, trimatic.utils.point_argument(point), trimatic.utils.point_argument(direction), follow_surface, alignment.value, font, font_height, label_height, bold, italic )

def quick_label_dxf(
    *args,#'force named parameters'
    entity,
    filename,
    point,
    direction,
    follow_surface = True,
    scale = 1,
    label_height = 1
    ):
    """Places a label on a part based on a .dxf file.

    :param entity: Entity to label.
    :type entity: trimatic.Part
    :param filename: File to use for label.
    :type filename: string
    :param point: Point where the label will start.
    :type point: trimatic.Point
    :param direction: Direction of the label.
    :type direction: trimatic.Point
    :param follow_surface: When True, the label will be bent to follow the surface normal. When False, the label will be aligned with the normal at the starting point.
    :type follow_surface: bool, optional
    :param scale: Scale factor to be applied to the .dxf file.
    :type scale: float, optional
    :param label_height: Label height (embossed text). Use a negative value for labeling inwards (debossed text).
    :type label_height: float, optional
    :return: SurfaceSet containing surfaces that were created for the label.
    :rtype: trimatic.SurfaceSet
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/finish/quick_label_dxf.py
    """

    trimatic.utils.check_type("entity", entity, (trimatic.Part))


    return pymatic.quick_label_dxf(entity, filename, trimatic.utils.point_argument(point), trimatic.utils.point_argument(direction), follow_surface, scale, label_height)

def remove_undercut(
        undercut_entity,
        fitting_entity, 
        direction,
        draft_angle = 0.0,
        detail = 0.3
    ):
    """Removes excess undercuts from a part, such that it fits into another part according to a set direction.

    :param undercut_entity: Part that should have its undercuts removed.
    :type undercut_entity: trimatic.Part
    :param fitting_entity: Part that the undercut entity should fit into after the operation completes.
    :type fitting_entity: trimatic.Part
    :param direction: The direction to take out the undercut entity from the fitting entity.
    :type direction: trimatic.Point
    :param draft_angle: The draft angle by which you want to take out the undercut entity from the fitting entity.
    :type draft_angle: float, optional
    :param detail: Smaller input here gives a smoother cut surface at the cost of increased computation time.
    :type detail: float, optional
    :return: Part after removal of undercut.
    :rtype: trimatic.Part
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/finish/remove_undercut.py
    """


    trimatic.utils.check_type("undercut_entity", undercut_entity, (trimatic.Part))
    trimatic.utils.check_type("fitting_entity", fitting_entity, (trimatic.Part))
    trimatic.utils.check_param_in_range("draft_angle", draft_angle, 0, 80)
    trimatic.utils.check_param_greater_or_equal("detail", detail, 0.0001)

    return pymatic.remove_undercut(undercut_entity, fitting_entity, trimatic.utils.point_argument(direction), draft_angle, detail)

class SmoothDetail(Enum):
    """Smooth detail type."""

    Coarse = "Coarse"
    """Coarse level"""

    Medium = "Medium"
    """Medium level"""

    Fine = "Fine"
    """Fine level"""

def smooth_edge(entity, distance = 0.5, smooth_detail = SmoothDetail.Coarse):
    """Smoothes a sharp edge. The operation will smooth the edge of the input contour.

    :param entity: Surface contour.
    :type entity: trimatic.SurfaceContour
    :param distance: Distance from the selected contour to which the smoothing should be applied.
    :type distance: float, optional
    :param smooth_detail: Smooth detail type.
    :type smooth_detail: trimatic.SmoothDetail, optional
    :return: The smoothed surfaces.
    :rtype: (trimatic.Surface)
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/finish/smooth_edge.py
    """


    trimatic.utils.check_type("entity", entity, (trimatic.SurfaceContour))
    trimatic.utils.check_param_greater("distance", distance, 0)
    trimatic.utils.check_type("smooth_detail", smooth_detail, (SmoothDetail,))

    return pymatic.smooth_edge(entity, distance, smooth_detail.value)

def create_path_based_pattern(*args, path, pattern_entity, distance = 1.0, number_of_copies = 10, is_follow_curve = True,
                              is_follow_surface = False, is_transform_displacement = False):
    """ Patterns entities along the guiding path that is defined by the curve.

    :param path: The curve that is used as the guiding path.
    :type path: trimatic.Curve
    :param pattern_entity: The entity to be patterned along the guiding path.
    :type pattern_entity: trimatic.Part, trimatic.Sketch, trimatic.Plane
    :param distance: The distance between the pattern entities. If set to None, the distance will be computed automatically
        based on the number of copies. If number_of_copies is also None, then the pattern entities will be placed on the curve segment endpoints.
    :type distance: float | None, optional
    :param number_of_copies: The number of pattern entities to be added along the guiding path. If set to None, the number
        will be computed automatically based on the distance. If distance is also None, then the pattern entities will be
        placed on the curve segment endpoints.
    :type number_of_copies: int | None, optional
    :param is_follow_curve: If True, the direction of the pattern entity will follow the curve direction.
    :type is_follow_curve: bool, optional
    :param is_follow_surface: If True, and the path is an attached curve, the triangle normals are used to align the Z axis
        of the pattern entity.
    :type is_follow_surface: bool, optional
    :param is_transform_displacement: If True, the displacement between the pattern entity and the path curve will be
        transformed such that the pattern entity will be centered on top of the path.
    :type is_transform_displacement: bool, optional
    :return: One or multiple pattern results.
    :rtype: trimatic.Part | (trimatic.Plane) | (trimatic.Sketch)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/finish/create_path_based_pattern.py
    """


    trimatic.utils.check_type("path", path, trimatic.Curve)
    trimatic.utils.check_type("pattern_entity", pattern_entity, (trimatic.Part, trimatic.Sketch, trimatic.Plane))
    if distance is not None:
        trimatic.utils.check_resolution("distance", distance)
    if number_of_copies is not None:
        trimatic.utils.check_param_greater("number_of_copies", number_of_copies, 0)

    return pymatic.create_path_based_pattern(path, pattern_entity, distance, number_of_copies, is_follow_curve,
                                             is_follow_surface, is_transform_displacement)

def create_point_based_pattern(
    *args,
    entity,
    pattern_entity,
    specific_points_on_mesh,
    direction = None,
    rotation_angle = 0.0000,
    height_offset = 0.0000):
    """ Operation to place pattern entities on the desired points of a reference mesh.

    :param entity: A single part to be used as the marker for the points to place the pattern entities.
    :type entity: trimatic.Part
    :param pattern_entity: A single part to be used as the pattern entity.
    :type pattern_entity: trimatic.Part
    :param specific_points_on_mesh: One or a list of points to be used as the markers to place the pattern entities.
    :type specific_points_on_mesh: trimatic.Point | [trimatic.Point] | [(float, float, float)]
    :param direction: The direction vector for the X axis of the pattern entity to be aligned to. If set to None, all pattern entities are placed without a shared common direction.
    :type direction: (float, float, float), optional
    :param rotation_angle: The rotation of the pattern entities about the vertical axis of the pattern entity.
    :type rotation_angle: float, optional
    :param height_offset: Offset of the pattern position from the specified point along the vertical axis.
    :type height_offset: float, optional

    :return: One part with the patterned result.
    :rtype: trimatic.Part
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/finish/create_point_based_pattern.py
    """


    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    trimatic.utils.check_type("pattern_entity", pattern_entity, (trimatic.Part))
    trimatic.utils.check_param_in_range("rotation_angle", rotation_angle, -180.0, 180.0)

    if direction is not None:
        trimatic.utils.check_direction("direction", direction)
        return pymatic.create_point_based_pattern(entity, pattern_entity, trimatic.utils.point_sequence_argument(specific_points_on_mesh),
                                                  trimatic.utils.point_argument(direction), rotation_angle, height_offset)
    else:
        return pymatic.create_point_based_pattern(entity, pattern_entity, trimatic.utils.point_sequence_argument(specific_points_on_mesh),
                                                  direction, rotation_angle, height_offset)