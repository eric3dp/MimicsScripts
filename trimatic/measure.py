import pymatic
import trimatic.utils

from trimatic.data import TextAlignment

from enum import Enum

class MeasurementCoordinates(Enum):
    """Measure coordinates method."""

    XYZ = "XYZ"
    """Measure coordinates XYZ method."""

    XY = "XY"
    """Measure coordinates XY method."""

    XZ = "XZ"
    """Measure coordinates XZ method."""

    YZ = "YZ"
    """Measure coordinates YZ method."""

def create_angle_measurement_line_to_line(line_from, line_to, measurement_coordinates = MeasurementCoordinates.XYZ, user_defined_cs = None, leader_line_length = None):
    """Creates an angle measurement from one line to another line.

    :param line_from: The first line.
    :type line_from: trimatic.Line
    :param line_to: The second line.
    :type line_to: trimatic.Line
    :param measurement_coordinates: Choose to measure the angle in all 3 axes or only one plane.
    :type measurement_coordinates: trimatic.MeasurementCoordinates, optional
    :param user_defined_cs:  Single entity of trimatic.CoordinateSystem. If this parameter is not valid, then the world coordinate system will be applied. The measurement will be taken based on the coordinate system of the selected entity.
    :type user_defined_cs: trimatic.CoordinateSystem, optional
    :param leader_line_length: The length of the leader lines. When None, the length is computed automatically.
    :type leader_line_length: float, optional
    :return: Created measurement.
    :rtype: trimatic.AngleMeasurement
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/measure/create_angle_measurement_line_to_line.py
    """


    trimatic.utils.check_type("line_from", line_from, trimatic.Line)
    trimatic.utils.check_type("line_to", line_to, trimatic.Line)
    trimatic.utils.check_type("measurement_coordinates", measurement_coordinates, (MeasurementCoordinates,))
    if leader_line_length is not None:
        trimatic.utils.check_param_greater_or_equal("leader_line_length", leader_line_length, 0)

    if not user_defined_cs is None:
        trimatic.utils.check_type("user_defined_cs", user_defined_cs, trimatic.CoordinateSystem)

    return pymatic.create_angle_measurement_line_to_line(line_from, line_to, measurement_coordinates.value, user_defined_cs, leader_line_length)

def create_angle_measurement_3points(center, point1, point2, measurement_coordinates = MeasurementCoordinates.XYZ, user_defined_cs = None):
    """Creates an angle measurement between 3 points. The position of the angle measurement is defined by the sum of the center-point1 vector and the center-point2 vector.

    :param center: Center point of the measurement.
    :type center: [float] | (float) | trimatic.Point
    :param point1: Point1 of the measurement.
    :type point1: [float] | (float) | trimatic.Point
    :param point2: Point2 of the measurement.
    :type point2: [float] | (float) | trimatic.Point
    :param measurement_coordinates: Choose to measure the angle in all 3 axes or only one plane.
    :type measurement_coordinates: trimatic.MeasurementCoordinates, optional
    :param user_defined_cs:  Single entity of trimatic.CoordinateSystem. If this parameter is not valid, then the world coordinate system will be applied. The measurement will be taken based on the coordinate system of the selected entity.
    :type user_defined_cs: trimatic.CoordinateSystem, optional
    :return: Created measurement.
    :rtype: trimatic.AngleMeasurement
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/measure/create_angle_measurement_3points.py
    """


    trimatic.utils.check_type("measurement_coordinates", measurement_coordinates, (MeasurementCoordinates,))

    if not user_defined_cs is None:
        trimatic.utils.check_type("user_defined_cs", user_defined_cs, trimatic.CoordinateSystem)

    return pymatic.create_angle_measurement_3points(trimatic.utils.point_argument(center), trimatic.utils.point_argument(point1), trimatic.utils.point_argument(point2), measurement_coordinates.value, user_defined_cs)

def create_annotation(point_anchor, point_text, text, alignment = TextAlignment.Left):
    """Creates an annotation.

    :param point_anchor: The point to annotate.
    :type point_anchor: trimatic.Point
    :param point_text: The anchor point of the text.
    :type point_text: trimatic.Point
    :param text: The text of the annotation.
    :type text: string
    :param alignment: The text alignment of the annotation.
    :type alignment: trimatic.TextAlignment, optional
    :return: Created annotation.
    :rtype: trimatic.Annotation 
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/measure/create_annotation.py
    """



    return pymatic.create_annotation(trimatic.utils.point_argument(point_anchor), trimatic.utils.point_argument(point_text), text, alignment.value)

def create_diameter_measurement(point1, point2, point3):
    """Measures diameter using 3 points method.

    :param point1: First point.
    :type point1: trimatic.Point
    :param point2: Second point.
    :type point2: trimatic.Point
    :param point3: Third point.
    :type point3: trimatic.Point
    :return: Created diameter measurement.
    :rtype: trimatic.DiameterMeasurement
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/measure/create_diameter_measurement.py
    """


    return pymatic.create_diameter_measurement(trimatic.utils.point_argument(point1), trimatic.utils.point_argument(point2), trimatic.utils.point_argument(point3))

def create_distance_measurement(point1, point2, measurement_coordinates = MeasurementCoordinates.XYZ, user_defined_cs = None):
    """ Measures the distance between 2 points.

    :param point1: Creates first point.
    :type point1: [float] | (float) | trimatic.Point
    :param point2: Creates second point.
    :type point2: [float] | (float) | trimatic.Point
    :param measurement_coordinates: Specify coordinates to measure the angle in all 3 axes or only one plane.
    :type measurement_coordinates: trimatic.MeasurementCoordinates, optional
    :param user_defined_cs:  Single entity of trimatic.CoordinateSystem. When this parameter is None, the world coordinate system will be applied. The measurement will be taken based on the coordinate system of the selected entity.
    :type user_defined_cs: trimatic.CoordinateSystem, optional
    :return: Created measurement.
    :rtype: trimatic.DistanceMeasurement
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/measure/create_distance_measurement.py
    """


    trimatic.utils.check_type("measurement_coordinates", measurement_coordinates, (MeasurementCoordinates,))

    if not user_defined_cs is None:
        trimatic.utils.check_type("user_defined_cs", user_defined_cs, trimatic.CoordinateSystem)

    return pymatic.create_distance_measurement(trimatic.utils.point_argument(point1), trimatic.utils.point_argument(point2),
                                               measurement_coordinates.value, user_defined_cs)
