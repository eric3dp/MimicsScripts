import pymatic
import trimatic.utils

from enum import Enum

def get_angle_measurements():
    """Get all AngleMeasurement objects.

    :return: Tuple of AngleMeasurement objects. Empty tuple if none are found. 
    :rtype: (trimatic.AngleMeasurement)
    """
    return pymatic.get_angle_measurements()


def get_annotations():
    """Get all Annotation objects.

    :return: Tuple of Annotation objects. Empty tuple if none are found. 
    :rtype: (trimatic.Annotation)
    """
    return pymatic.get_annotations()


def get_arcs():
    """Get all Arc objects.

    :return: Tuple of Arc objects. Empty tuple if none are found. 
    :rtype: (trimatic.Arc)
    """
    return pymatic.get_arcs()


def get_cones():
    """Get all Cone objects.

    :return: Tuple of Cone objects. Empty tuple if none are found. 
    :rtype: (trimatic.Cone)
    """
    return pymatic.get_cones()


def get_cylinders():
    """Get all Cylinder objects.

    :return: Tuple of Cylinder objects. Empty tuple if none are found. 
    :rtype: (trimatic.Cylinder)
    """
    return pymatic.get_cylinders()


def get_diameter_measurements():
    """Get all DiameterMeasurement objects.

    :return: Tuple of DiameterMeasurement objects. Empty tuple if none are found. 
    :rtype: (trimatic.DiameterMeasurement)
    """
    return pymatic.get_diameter_measurements()


def get_distance_measurements():
    """Get all DistanceMeasurement objects.

    :return: Tuple of DistanceMeasurement objects. Empty tuple if none are found. 
    :rtype: (trimatic.DistanceMeasurement)
    """
    return pymatic.get_distance_measurements()
    
def get_groups():
    """Get all groups present.

    :return: Tuple of Group objects. Empty tuple if none are found.
    :rtype: (trimatic.Group)
    """
    return pymatic.get_groups()

def get_lines():
    """Get all Line objects.

    :return: Tuple of Line objects. Empty tuple if none are found. 
    :rtype: (trimatic.Line)
    """
    return pymatic.get_lines()


def get_objects():
    """Get all Objects.

    :return: Tuple of all Objects. Empty tuple if none are found. 
    :rtype: (trimatic.Object)
    """
    return pymatic.get_objects()


def get_parts():
    """Get all Part objects.

    :return: Tuple of Part objects. Empty tuple if none are found. 
    :rtype: (trimatic.Part)
    """
    return pymatic.get_parts()


def get_planes():
    """Get all Plane objects.

    :return: Tuple of Plane objects. Empty tuple if none are found. 
    :rtype: (trimatic.Plane)
    """
    return pymatic.get_planes()


def get_points():
    """Get all Point objects.

    :return: Tuple of Point objects. Empty tuple if none are found. 
    :rtype: (trimatic.Point)
    """
    return pymatic.get_points()


def get_spheres():
    """Get all Sphere objects.

    :return: Tuple of Sphere objects. Empty tuple if none are found. 
    :rtype: (trimatic.Sphere)
    """
    return pymatic.get_spheres()

def get_sketches():
    """Get all Sketches.

    :return: Tuple of Sketches. Empty tuple if none are found. 
    :rtype: (trimatic.Sketch)
    """
    return pymatic.get_sketches()

def get_ssms():
    """Get all SSM objects.

    :return: Tuple of SSM objects. Empty tuple if none are found. 
    :rtype: (trimatic.SSM)
    """
    return pymatic.get_ssms()

def copy_to_part(entities, destination = None):
    """Copies surfaces, curves, and surface or curve sets from one part to another.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities: [ trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles ]
    :param destination: The part where the data has to be copied to. When None is specified, a new one will be created.
    :type destination: trimatic.Part
    :return: copied entities or newly created part when a new part was created.
    :rtype: ( trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve | trimatic.CurveSet ) | trimatic.Part

    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/data/copy_to_part.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles) )
    if destination is not None:
        trimatic.utils.check_type("destination", destination, (trimatic.Part, ) )

    return pymatic.copy_to_part(trimatic.utils.single_or_multiple_entities(entities), destination)

def delete(entities):
    """Deletes the specified objects.

    Deleting an object multiple times or attempting to access a deleted object will raise an AttributeError.

    :param entities: Either single object or heterogeneous list of parts, surfaces, surface sets, etc.
    :type entities: trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :return: True if delete is successful.
    :rtype: bool
    :raises: RuntimeError, AttributeError
    :example:

    .. literalinclude:: example/data/delete.py
    """


    return pymatic.delete(trimatic.utils.single_or_multiple_entities(entities))

def duplicate(entities):
    """Duplicates the specified entities.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :return: Duplicated entity or tuple of duplicated entities.
    :rtype: trimatic.Object | (trimatic.Object)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/data/duplicate.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Curve,) +  (trimatic.CurveSet,) + trimatic.utils.root_level_types())

    return pymatic.duplicate(trimatic.utils.single_or_multiple_entities(entities))

class TextAlignment(Enum):
    """Text alignment methods."""

    Left = "Left"
    Right = "Right"
    Center = "Center"

class TriangulationAccuracy(Enum):
    """Accuracy of triangulation."""

    Very_Coarse = "Very coarse"
    """Very coarse level."""

    Coarse = "Coarse"
    """Coarse level."""

    Medium = "Medium"
    """Medium level."""

    Fine = "Fine"
    """Fine level."""

    Very_Fine = "Very fine"
    """Very fine level."""
    
class HollowType(Enum):
      """Hollow type."""
      
      Inside = "Inside"
      """Creates an extra shell to give the part a thickness on the outside."""
      
      Outside = "Outside"
      """Creates an extra shell to give the part a thickness on the inside."""
      
      Both = "Both"
      """Creates an extra shell that gives the part a thickness in both directions."""
    
def find_angle_measurement(name):
    """Finds an AngleMeasurement object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first AngleMeasurement object found. None if no match is found.
    :rtype: trimatic.AngleMeasurement
    """
    return pymatic.find_angle_measurement(name)


def find_angle_measurements(regex):
    """Finds AngleMeasurement objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of AngleMeasurement objects that match the specified expression. Empty tuple if no match is found. 
    :rtype: (trimatic.AngleMeasurement)
    """
    return pymatic.find_angle_measurements(regex)


def find_annotation(name):
    """Finds an Annotation object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Annotation object found. None if no match is found.
    :rtype: trimatic.Annotation
    """
    return pymatic.find_annotation(name)


def find_annotations(regex):
    """Finds Annotation objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Annotation objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Annotation)
    """
    return pymatic.find_annotations(regex)


def find_arc(name):
    """Finds an Arc object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Arc object found. None if no match is found.
    :rtype: trimatic.Arc
    """
    return pymatic.find_arc(name)


def find_arcs(regex):
    """finds Arc objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Arc objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Arc)
    """
    return pymatic.find_arcs(regex)


def find_cone(name):
    """Finds a Cone object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Cone object found. None if no match is found.
    :rtype: trimatic.Cone
    """
    return pymatic.find_cone(name)


def find_cones(regex):
    """Finds Cone objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Cone objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Cone)
    """
    return pymatic.find_cones(regex)


def find_cylinder(name):
    """Finds a Cylinder object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Cylinder object found. None if no match is found.
    :rtype: trimatic.Cylinder
    """
    return pymatic.find_cylinder(name)


def find_cylinders(regex):
    """Finds Cylinder objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Cylinder objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Cylinder)
    """
    return pymatic.find_cylinders(regex)


def find_distance_measurement(name):
    """Finds a DistanceMeasurement object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first DistanceMeasure object found. None if no match is found.
    :rtype: trimatic.DistanceMeasurement
    """
    return pymatic.find_distance_measurement(name)


def find_distance_measurements(regex):
    """Find DistanceMeasurement objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of DistanceMeasurement objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.DistanceMeasurement)
    """
    return pymatic.find_distance_measurements(regex)


def find_diameter_measurement(name):
    """Finds a DiameterMeasurement object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first DiameterMeasurement object found. None if no match is found.
    :rtype: trimatic.DiameterMeasurement
    """
    return pymatic.find_diameter_measurement(name)


def find_diameter_measurements(regex):
    """Find DiameterMeasurement objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of DiameterMeasurement objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.DiameterMeasurement)
    """
    return pymatic.find_diameter_measurements(regex)

def find_group(name):
    """Finds a group with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first group object found. None if no match is found.
    :rtype: trimatic.Group
    """
    return pymatic.find_group(name)

def find_groups(regex):
    """Finds groups with names that match a specified regular expression.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of group objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Group)
    """
    return pymatic.find_groups(regex)


def find_line(name):
    """Finds a Line object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Line object found. None if no match is found.
    :rtype: trimatic.Line
    """
    return pymatic.find_line(name)


def find_lines(regex):
    """Find Line objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Line objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Line)
    """
    return pymatic.find_lines(regex)


def find_object(name):
    """Finds an object with a specific name. 

    :param name: Name to find.
    :type name: string
    :return: The first Object found. None if no match is found.
    :rtype: trimatic.Object
    """
    return pymatic.find_object(name)

def find_objects_with_metadata(name, value):
    """Finds objects whose metadata matches specified criteria. Objects without metadata will be ignored.

    :param name: Name to find. When None is specified, name can be anything.
    :type name: string
    :param value: Value to find. When None is specified, value can be anything.
    :type value: string
    :return: The object(s) matching the search criteria.
    :rtype: (trimatic.Object)

    :example:

    .. literalinclude:: example/data/find_objects_with_metadata.py
    
    """
    return pymatic.find_objects_with_metadata(name, value)


def find_objects(regex):
    """Finds objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.\n
    :type regex: string
    :return: Tuple of Objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Object)
    """
    return pymatic.find_objects(regex)


def find_part(name):
    """Finds a Part object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Part object found. None if no match is found.
    :rtype: trimatic.Part
    """
    return pymatic.find_part(name)


def find_parts(regex):
    """Finds Part objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Part objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Part)
    """
    return pymatic.find_parts(regex)


def find_part_byguid(guid):
    """Finds a Part object with a specific Globally Unique Identifier (GUID).
    
    This is the recommended method to search for Parts reliably. Names are not guaranteed to be unique, but every Part
    with the same name will have a different GUID. This is especially useful when exchanging data between 3-matic and
    Mimics.

    :param guid: GUID to find.
    :type guid: string
    :return: The Part with a matching GUID. None if no match is found.
    :rtype: trimatic.Part
    """
    return pymatic.find_part_byguid(guid)


def find_plane(name):
    """Finds a Plane object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Plane object found. None if no match is found.
    :rtype: trimatic.Plane
    """
    return pymatic.find_plane(name)


def find_planes(regex):
    """finds planes whose name match a regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.
    Find Plane objects with names that match a specified regular expression.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Plane objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Plane)
    """
    return pymatic.find_planes(regex)


def find_point(name):
    """Finds a Point object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Point object found. None if no match is found.
    :rtype: trimatic.Point
    """
    return pymatic.find_point(name)


def find_points(regex):
    """Find Point objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Point objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Point)
    """
    return pymatic.find_points(regex)


def find_sketch(name):
    """Finds a Sketch with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Sketch found. None if no match is found.
    :rtype: trimatic.Sketch
    """
    return pymatic.find_sketch(name)


def find_sketches(regex):
    """Find Sketches with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Sketches that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Sketch)
    """
    return pymatic.find_sketches(regex)

def find_sphere(name):
    """Finds a Sphere object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first Sphere object found. None if no match is found.
    :rtype: trimatic.Sphere
    """
    return pymatic.find_sphere(name)


def find_spheres(regex):
    """Find Sphere objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of Sphere objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.Sphere)
    """
    return pymatic.find_spheres(regex)

def find_ssm(name):
    """Finds a SSM object with a specific name.

    :param name: Name to find.
    :type name: string
    :return: The first SSM object found. None if no match is found.
    :rtype: trimatic.SSM
    """
    return pymatic.find_ssm(name)

def find_ssms(regex):
    """Find SSM objects with names that match a specified regular expression. For more information on regular expressions we refer to section :ref:`finding_objects`.

    :param regex: Regular expression to match.
    :type regex: string
    :return: Tuple of SSM objects that match the specified expression. Empty tuple if no match is found.
    :rtype: (trimatic.SSM)
    """
    return pymatic.find_ssms(regex)

def merge(entities):
    """Merges the specified entities. You can only merge entities of the same type: surfaces with surfaces, parts with parts or graphs with graphs. You can pass either a single entity or multiple entities to merge. For 
    example, you can (i) merge a single SurfaceSet which merges all surfaces in the SurfaceSet, or (ii) merge multiple SurfaceSets, which merges the SurfaceSets into one.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Graph | trimatic.GraphSet | trimatic.UVRegion | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Graph | trimatic.GraphSet | trimatic.UVRegion]
    :return: merged entities.
    :rtype: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.Graph | trimatic.GraphSet | trimatic.UVRegion
    :raises: RuntimeError

    :example: 

    .. literalinclude:: example/data/merge.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.Graph, trimatic.GraphSet, trimatic.UVRegion))

    return pymatic.merge(trimatic.utils.single_or_multiple_entities(entities))

def get_metadata():
    """Gets project level metadata.

    :return: The project level metadata object.
    :rtype: trimatic.Metadata
    """
    return pymatic.get_metadata()


def move_to_part(entities, destination = None):
    """Moves surfaces, curves, and surface or curve sets from one part to another.

    :param entities: Either single object or heterogeneous list of objects.
    :type entities: [ trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve | trimatic.CurveSet | trimatic.MarkedTriangles]
    :param destination: The part where the data has to be moved to. When None is specified, a new one will be created.
    :type destination: trimatic.Part
    :return: moved entities or newly created part when a new part was created.
    :rtype: ( trimatic.Surface | trimatic.SurfaceSet | trimatic.Curve | trimatic.CurveSet ) | trimatic.Part

    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/data/move_to_part.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.CurveSet, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles) )
    if destination is not None:
        trimatic.utils.check_type("destination", destination, (trimatic.Part, ) )

    return pymatic.move_to_part(trimatic.utils.single_or_multiple_entities(entities), destination)

