from .proxy import _BaseProxy

class Object(metaclass=_BaseProxy):
    @property
    def name(self):
        """Name of the entity.

        :rtype: string
        """
        pass

    @property
    def valid(self):
        """Inspect if the entity is valid and not destroyed.

        :rtype: bool
        """
        pass

    @property
    def visible(self):
        """Visibility of the entity.

        :rtype: bool
        """
        pass

class Analysis(Object):
    """Analysis."""

    def get_values(self):
        """returns all analysis values and correspondence vertices.

        :rtype: ((trimatic.Point),float)
        """
        pass

    def get_parent(self):
        """Returns the part that contains the analysis. 

        :rtype: trimatic.Part
        """
        pass

class AngleMeasurement(Object):
    """Angle measurement entity."""

    @property
    def value(self):
        """Measurement value.

        :rtype: float
        """
        pass

    @property
    def center(self):
        """Center of rotation.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point1(self):
        """Start point of the angle measurement.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point2(self):
        """End point of the angle measurement.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get angle measurement's metadata.

        :return: The angle measurement's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Annotation(Object):
    """Annotation entity"""

    @property
    def text(self):
        """Label text of the annotation entity.

        :rtype: string
        """
        pass

    @property
    def point_anchor(self):
        """Coordinate of the point the annotation text is referencing.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point_text(self):
        """Coordinate of the label of the annotation.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get annotation's metadata.

        :return: The annotation's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Arc(Object):
    """Analytical Arc entity."""

    @property
    def angle(self):
        """Angle between the two points of the arc along the arc edge. Angle is fixed at 360 degrees for a closed arc.

        :rtype: float
        """
        pass

    @property
    def center(self):
        """Center of the arc.

        :rtype: (float, float, float)
        """
        pass

    @property
    def closed(self):
        """True if arc is closed.

        :rtype: bool
        """
        pass

    @property
    def color(self):
        """Color of the arc in (R, G, B). Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def direction(self):
        """Direction perpendicular to the place of the arc.

        :rtype: (float, float, float)
        """
        pass

    @property
    def length(self):
        """Length along the curved edge of the arc.

        :rtype: float
        """
        pass

    @property
    def point1(self):
        """Coordinates of the start point of the arc.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point2(self):
        """Coordinates of the end point of the arc.

        :rtype: (float, float, float)
        """
        pass

    @property
    def radius(self):
        """Radius of the arc.

        :rtype: float
        """
        pass

    def get_metadata(self):
        """Get arc's metadata.

        :return: The arc's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Cone(Object):
    """Analytical Cone entity."""

    @property
    def bottom_point(self):
        """Center of the bottom surface of the cone.

        :rtype: (float, float, float)
        """
        pass

    @property
    def bottom_radius(self):
        """Radius of the bottom surface of the cone.

        :rtype: float
        """
        pass

    @property
    def top_point(self):
        """Center of the top surface of the cone.

        :rtype: (float, float, float)
        """
        pass

    @property
    def top_radius(self):
        """Radius of the top surface of the cone.

        :rtype: float
        """
        pass
    @property
    def color(self):
        """Color of the line entity in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get cone's metadata.

        :return: The cone's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class CoordinateSystem(Object):
    """Coordinate System entity."""

    @property
    def origin(self):
        """Origin of the coordinate system.

        :rtype: (float, float, float)
        """
        pass

    @property
    def x_axis(self):
        """X-axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def y_axis(self):
        """Y-axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def z_axis(self):
        """Z-axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def xy_plane(self):
        """XY-plane direction of the coordinate system.

        :rtype: trimatic.CoordinateSystemPlane
        """
        pass

    @property
    def yz_plane(self):
        """YZ-plane direction of the coordinate system.

        :rtype: trimatic.CoordinateSystemPlane
        """
        pass

    @property
    def zx_plane(self):
        """ZX-plane direction of the coordinate system.

        :rtype: trimatic.CoordinateSystemPlane
        """
        pass

class CoordinateSystemPlane(Object):
    """Coordinate System Plane entity."""

    @property
    def normal(self):
        """Normal of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def origin(self):
        """Origin of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def x_axis(self):
        """X-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def y_axis(self):
        """Y-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def z_axis(self):
        """Z-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    def convert_to_plane(self):
        """Converts the coordinate system plane to trimatic.plane.

        :return: The trimatic.Plane object
        :rtype: trimatic.Plane
        """
        pass

class Curve(Object):
    """Curve entity."""

    @property
    def fully_attached(self):
        """True if the curve is fully attached to the surfaces of the parent part entity.

        :rtype: bool
        """
        pass

    @property
    def length(self):
        """Length of the curve.

        :rtype: float
        """
        pass

    @property
    def number_of_segments(self):
        """Number of line segments in the curve.

        :rtype: int
        """
        pass

    @property
    def closed(self):
        """True if the curve is closed.

        :rtype: bool
        """
        pass

    @property
    def points(self):
        """Tuple of points in the curve.

        :rtype: ((float, float, float))
        """
        pass

    def get_parent(self):
        """Returns the parent of the curve. 
        When the curve is inside a curve set, that curve set is returned. 
        If the curve is not inside a curve set, the containing part will be returned.

        :rtype: trimatic.CurveSet|trimatic.Part
        """
        pass

class CurveSet(Object):
    """Curve Set entity."""

    @property
    def fully_attached(self):
        """True if all child curves are fully attached to the surfaces of the parent part entity.

        :rtype: bool
        """
        pass

    @property
    def number_of_curves(self):
        """Number of curves in the curve set.

        :rtype: int
        """
        pass


    def clear(self):
        """Delete all curves in the curve set."""
        pass

    def find_curve(self, name):
        """Finds a Curve object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Curve object found. None if no match is found.
        :rtype: trimatic.Curve
        """
        pass

    def find_curves(self, regex):
        """Finds Curve objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of Curve objects that match the specified expression. Empty list if no match is found.
        :rtype: (trimatic.Curve)
        """
        pass

    def get_curves(self):
        """Get all Curve objects within the CurveSet.

        :return: Tuple of Curve objects. Empty list if none are found.
        :rtype: (trimatic.Curve)
        """
        pass

    def get_parent(self):
        """Returns the part that the curve set belongs to.

        :rtype: trimatic.Part
        """
        pass


class Cylinder(Object):
    """Analytical Cylinder entity."""

    @property
    def color(self):
        """Color of the line entity in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def direction(self):
        """Direction of the cylinder.

        :rtype: (float, float, float)
        """
        pass

    @property
    def height(self):
        """Height of the cylinder.

        :rtype: float
        """
        pass

    @property
    def point1(self):
        """Center of the bottom surface of the cylinder.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point2(self):
        """Center of the top surface of the cylinder.

        :rtype: (float, float, float)
        """
        pass

    @property
    def radius(self):
        """Radius of the cylinder.

        :rtype: float
        """
        pass

    def get_metadata(self):
        """Get cylinder's metadata.

        :return: The cylinder's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class DiameterMeasurement(Object):
    """Diameter measurement entity."""

    @property
    def value(self):
        """Measurement value

        :rtype: float
        """
        pass

    @property
    def center_point(self):
        """Center of the measurement.

        :rtype: (float, float, float)
        """
        pass

    @property
    def normal(self):
        """Normal of the plane of measurement.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get diameter measure's metadata.

        :return: The diameter measure's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class DistanceMeasurement(Object):
    """Distance measurement entity."""

    @property
    def value(self):
        """Measurement value

        :rtype: float
        """
        pass

    @property
    def point1(self):
        """Start point of the distance calculation.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point2(self):
        """End point of the distance calculation.

        :rtype: (float, float, float)
        """
        pass
 
    def get_metadata(self):
        """Get distance measure's metadata.

        :return: The distance measure's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Graph(Object):
    """Graph entity."""

    @property
    def color(self):
        """Color of the graph. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def number_of_beams(self):
        """Number of beams.

        :rtype: int
        """
        pass

    @property
    def accuracy(self):
        """accuracy.

        :rtype: float
        """
        pass

    @property
    def minimum_thickness(self):
        """Minimum thickness of all beams in the graph.

        :rtype: float
        """
        pass

    def maximum_thickness(self):
        """Maximum thickness of all beams in the graph.

        :rtype: float
        """
        pass

    def get_beams(self):
        """Get all beams from the graph.

        :return: A tuple containing a tuple of points and a tuple of beams. Tuple of beams defined as indices in the point list.
        :rtype: ((trimatic.Point),((int,int)))
        """
        pass

    def get_parent(self):
        """Returns the parent of the graph. 
        When the graph is inside a graph set, that graph set is returned. 
        If the graph is not inside a graph set, the containing part will be returned.

        :rtype: trimatic.GraphSet|trimatic.Part
        """
        pass


class GraphSet(Object):
    """GraphSet entity."""

    @property
    def number_of_graphs(self):
        """Number of graphs in a set.

        :rtype: int
        """
        pass

    def get_graphs(self):
        """Get all Graph objects.

        :return: Tuple of Graphs
        :rtype: (trimatic.Graph)
        """
        pass

    def find_graph(self, name):
        """Finds a Graph object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Graph object found. None if no match is found.
        :rtype: trimatic.Graph
        """
        pass

    def find_graphs(self, regex):
        """Finds Graph objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of Graph objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Graph)
        """
        pass

    def get_parent(self):
        """Returns the part that the graph set belongs to.

        :rtype: trimatic.Part
        """
        pass

    def minimum_thickness(self):
        """Minimum thickness of all beams in the graph set.

        :rtype: float
        """
        pass

    def maximum_thickness(self):
        """Maximum thickness of all beams in the graph set.

        :rtype: float
        """
        pass



class Line(Object):
    """Analytical Line entity."""

    @property
    def color(self):
        """Color of the line entity in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def direction(self):
        """Direction of the line.

        :rtype: (float, float, float)
        """
        pass

    @property
    def length(self):
        """Length of the line.

        :rtype: float
        """
        pass

    @property
    def point1(self):
        """Start point of the line.

        :rtype: (float, float, float)
        """
        pass

    @property
    def point2(self):
        """End point of the line.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get line's metadata.

        :return: The line's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class MarkedTriangles(Object):
    """Marked triangles entity."""

    @property
    def surface_area(self):
        """Total surface area of the marked triangles.

        :rtype: float
        """
        pass

    @property
    def number_of_triangles(self):
        """Number of triangles.

        :rtype: int
        """
        pass

    def get_parent(self):
        """Returns the part that the marked triangles belong to.

        :rtype: trimatic.Part
        """
        pass

    def get_triangles(self):
        """Get marked triangles coordinates.

        :return: A tuple containing a tuple of points and a tuple of triangles. Tuple of triangles defined as indices in the point list.
        :rtype: ((trimatic.Point),((int,int,int)))
        """
        pass

class Metadata(Object):
    """3-matic Metadata."""

    def create(self, name, value):
        """Adds a metadata item.

        :param name: the name of the item to add.
        :type name: string
        :param value: the value of the item to add.
        :type value: string
        :return: The added metadata item.
        :rtype: trimatic.MetadataItem
        """
        pass

    def create_multi(self, items):
        """Adds multiple metadata items. The items must be given as a tuple of tuples with string pairs.
        To add multiple metadata items from a list, you can easily convert the list to a tuple in the function call.
        For example: ret = md.create_multi(tuple(thedata)), in which thedata can be a list of tuples.

        :param items: the items to add.
        :type items: ((string,string))
        :return: The added metadata items.
        :rtype: (trimatic.MetadataItem)
        """
        pass

    def find(self, name, value):
        """Finds a metadata item.

        :param name: the name of the item to search. When None is specified, name is ignored.
        :type name: string
        :param value: the value of the item to search. When None is specified, value is ignored.
        :type value: string
        :return: The metadata item(s) matching the search criteria.
        :rtype: (trimatic.MetadataItem)
        """
        pass

    def get_parent(self):
        """Returns the object that contains the metadata. Returns None for project level metadata.

        :rtype: trimatic.Object
        """
        pass

class MetadataItem(Object):
    """3-matic Metadata item."""

    @property
    def name(self):
        """Name of the metadata item.

        :rtype: string
        """
        pass

    @property
    def value(self):
        """Value of the metadata item.

        :rtype: string
        """
        pass

    def get_parent(self):
        """Returns the object that contains the metadata item.

        :rtype: trimatic.MetaData
        """
        pass

class Part(Object):
    """3-matic Part entity."""

    @property
    def color(self):
        """Color of the part in (R, G, B). Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def dimension_delta(self):
        """Absolute dimensions of the part along each axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def dimension_max(self):
        """Maximum dimension of the part along each axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def dimension_min(self):
        """Minimum dimension of the part along each axis.

        :rtype: (float, float, float)
        """
        pass

    @property
    def guid(self):
        """Unique identifier for every part.

        :rtype: string
        """
        pass

    @property
    def number_of_bad_contours(self):
        """Number of bad contours.

        :rtype: int
        """
        pass

    @property
    def number_of_bad_edges(self):
        """Number of bad edges.

        :rtype: int
        """
        pass

    @property
    def number_of_invisible_triangles(self):
        """Number of invisible triangles.

        :rtype: int
        """
        pass

    @property
    def number_of_marked_triangles(self):
        """Number of marked triangles.

        :rtype: int
        """
        pass

    @property
    def number_of_points(self):
        """Number of points/vertices in the part.

        :rtype: int
        """
        pass

    @property
    def number_of_surfaces(self):
        """Number of surfaces.

        :rtype: int
        """
        pass

    @property
    def number_of_triangles(self):
        """Number of triangles.

        :rtype: int
        """
        pass

    @property
    def object_coordinate_system(self):
        """Object coordinate system details of the part.

        :rtype: trimatic.CoordinateSystem
        """
        pass

    @property
    def surface_area(self):
        """Total surface area of the part.

        :rtype: float
        """
        pass

    @property
    def transparency(self):
        """Transparency value of the part specified in floating point between 0.0 to 1.0.

        :rtype: float
        """
        pass

    @property
    def vertex_color(self):
        """Visibility of the vertex color scheme of the part.

        :rtype: bool
        """
        pass

    @property
    def volume(self):
        """Total volume of the part.

        :rtype: float
        """
        pass

    def delete_all_curves(self):
        """Delete all curves in the part."""
        pass

    def find_analysis(self, name):
        """Finds an Analysis with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Analysis object found. None if no match is found.
        :rtype: trimatic.Analysis
        """
        pass

    def find_analyses(self, regex):
        """Finds Analysis objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return:  Tuple of Analysis objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Analysis)
        """
        pass

    def find_curve(self, name):
        """Finds a Curve object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Curve object found. None if no match is found.
        :rtype: trimatic.Curve
        """
        pass

    def find_curves(self, regex):
        """Finds Curve objects with names that match a specified regular expression.

        :param regex: Regular expression to match
        :type regex: string
        :return:  Tuple of Curve objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Curve)
        """
        pass

    def find_curve_set(self, name):
        """Finds a CurveSet object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first CurveSet object found. None if no match is found.
        :rtype: trimatic.CurveSet
        """
        pass

    def find_curve_sets(self, regex):
        """Finds CurveSet objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of CurveSet objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.CurveSet)
        """
        pass

    def find_surface(self, name):
        """Finds a Surface object with a specific name.

        :param name: Name to find
        :type name: string
        :return: The first Surface object found. None if no match is found.
        :rtype: trimatic.Surface
        """
        pass

    def find_surfaces(self, regex):
        """Finds Surface objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of Surface objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Surface)
        """
        pass

    def find_surface_set(self, name):
        """Finds a SurfaceSet object with a specific name.

        :param name: Name to find
        :type name: string
        :return: The first SurfaceSet object found. None if no match is found.
        :rtype: trimatic.SurfaceSet
        """
        pass

    def find_surface_sets(self, regex):
        """Finds SurfaceSet objects with names that match a specified regular expression.

        :param regex: Regular expression to match
        :type regex: string
        :return: Tuple of SurfaceSet objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.SurfaceSet)
        """
        pass

    def find_volume_mesh(self, name):
        """Finds a VolumeMesh object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first VolumeMesh object found. None if no match is found.
        :rtype: trimatic.VolumeMesh
        """
        pass

    def find_volume_meshes(self, regex):
        """Finds VolumeMesh objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of VolumeMesh objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.VolumeMesh)
        """
        pass

    def get_bad_contours(self):
        """Returns a tuple of bad contours. Contours that contain bad edges only.

        :rtype: (trimatic.SurfaceContour)
        """
        pass

    def get_analyses(self):
        """Get all Analysis objects within the Part.

        :return:  Tuple of Analysis objects. Empty tuple if none are found.
        :rtype: (trimatic.Analysis)
        """
        pass

    def get_curves(self):
        """Get all Curve objects within the Part.

        :return: Tuple of Curve objects. Empty tuple if none are found.
        :rtype: (trimatic.Curve)
        """
        pass

    def get_curve_sets(self):
        """Get all CurveSet objects within the Part.

        :return: Tuple of CurveSet objects. Empty tuple if none are found.
        :rtype: (trimatic.CurveSet)
        """
        pass

    def get_marked_triangles(self):
        """Get all marked triangles within the Part.

        :return: The part's marked triangles.
        :rtype: trimatic.MarkedTriangles
        """
        pass

    def get_metadata(self):
        """Get part's metadata.

        :return: The part's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

    def get_surfaces(self):
        """Get all Surface objects within the Part.

        :return: Tuple of Surface objects. Empty tuple if none are found.
        :rtype: (trimatic.Surface)
        """
        pass

    def get_surface_sets(self):
        """Get all SurfaceSet objects within the Part.

        :return: Tuple of SurfaceSet objects. Empty tuple if none are found.
        :rtype: (trimatic.SurfaceSet)
        """
        pass

    def get_volume_meshes(self):
        """Get all VolumeMesh objects within the Part.

        :return: Tuple of VolumeMesh objects. Empty tuple if none are found.
        :rtype: (trimatic.VolumeMesh)
        """
        pass

    def merge_all_surfaces(self):
        """Merge all Surface and SurfaceSet objects in the Part into one Surface."""
        pass

    def get_triangles(self):
        """Get points and triangles in the part.

        :return: A tuple containing a tuple of points and a tuple of triangles. Tuple of triangles defined as indices in the point list.
        :rtype: ((trimatic.Point),((int,int,int)))
        """
        pass

    def get_graphs(self):
        """Get all Graph objects within the Part.

        :return: Tuple of Graph objects. Empty tuple if none are found.
        :rtype: (trimatic.Graph)
        """
        pass

    def get_graph_sets(self):
        """Get all GraphSet objects within the Part.

        :return: Tuple of GraphSet objects. Empty tuple if none are found.
        :rtype: (trimatic.GraphSet)
        """
        pass

    def find_graph(self, name):
        """Finds a Graph object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Graph object found. None if no match is found.
        :rtype: trimatic.Graph
        """
        pass

    def find_graphs(self, regex):
        """Finds Graph objects with names that match a specified regular expression.

        :param regex: Regular expression to match
        :type regex: string
        :return: Tuple of Graph objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Graph)
        """
        pass

    def find_graph_set(self, name):
        """Finds a GraphSet object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first GraphSet object found. None if no match is found.
        :rtype: trimatic.GraphSet
        """
        pass

    def find_graph_sets(self, regex):
        """Finds GraphSet objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of GraphSet objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.GraphSet)
        """
        pass

    def get_uv_maps(self):
        """ Get all UV Map objects within the Part entity.

        :return: Tuple of UV Map objects. Empty tuple if none are found.
        :rtype: (trimatic.UVMap)
        """
        pass

    def get_textures(self):
        """ Get all Texture objects within the Part entity.

        :return: Tuple of Texture objects. Empty tuple if none are found.
        :rtype: (trimatic.Texture)
        """
        pass

    def get_uv_regions(self):
        """ Get all UV Region objects within the Part entity.

        :return: Tuple of UV Region objects. Empty tuple if none are found.
        :rtype: (trimatic.UVRegion)
        """
        pass

    def find_uv_map(self, name):
        """ Get the UV Map that matches the specified name.

        :param name: Name to find.
        :type name: string
        :return: The first UV Map object found to match the specified name. None if no match is found.
        :rtype: trimatic.UVMap
        """
        pass

    def find_texture(self, name):
        """ Get the texture object that matches the specified name.

        :param name: Name to find.
        :type name: string
        :return: The first Texture object found to match the specified name. None if no match is found.
        :rtype: trimatic.Texture
        """
        pass

    def find_uv_region(self, name):
        """ Get the UV Region object that matches the specified name.

        :param name: Name to find.
        :type name: string
        :return: The first UV Region object found to match the specified name. None if no match is found.
        :rtype: trimatic.UVRegion
        """
        pass

    def find_uv_maps(self, regex):
        """ Finds UV Map objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of UV Map objects that match the specified regular expression. Empty tuple if no match is found.
        :rtype: (trimatic.UVMap)
        """
        pass

    def find_textures(self, regex):
        """ Finds Texture objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of Texture objects that match the specified regular expression. Empty tuple if no match is found.
        :rtype: (trimatic.Texture)
        """
        pass

    def find_uv_regions(self, regex):
        """ Finds UV Region objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of UV Region objects that match the specified regular expression. Empty tuple if no match is found.
        :rtype: (trimatic.UVRegion)
        """
        pass


class Plane(Object):
    """Plane entity"""

    @property
    def color(self):
        """Color of the plane in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def delta_x(self):
        """Extension length of the plane along the X-axis in either direction from the plane origin.

        :rtype: float
        """
        pass

    @property
    def delta_y(self):
        """Extension length of the plane along the Y-axis in either direction from the plane origin.

        :rtype: float
        """
        pass

    @property
    def normal(self):
        """Normal of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def object_coordinate_system(self):
        """Object coordinate system details of the plane.

        :rtype: trimatic.CoordinateSystem
        """
        pass

    @property
    def origin(self):
        """Origin of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def x_axis(self):
        """X-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def y_axis(self):
        """Y-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    @property
    def z_axis(self):
        """Z-axis direction of the plane.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get plane's metadata.

        :return: The plane's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Point(Object):
    """Analytical Point entity."""

    @property
    def x(self):
        """X-coordinate of the point.

        :rtype: float
        """
        pass

    @property
    def y(self):
        """Y-coordinate of the point.

        :rtype: float
        """
        pass

    @property
    def z(self):
        """Z-coordinate of the point.

        :rtype: float
        """
        pass

    @property
    def color(self):
        """Color of the line entity in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def coordinates(self):
        """Coordinates of the Point.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get point's metadata.

        :return: The point's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Sketch(Object):
    """Sketch entity.

    For scripting, sketching functionality is limited. Sketch entity is mainly intended as a carrier for planar curves.
    Some operations take 2D curves as input, and therefore only accept trimatic.Sketch entity. For example, profile curve for sweep operation must be planar.

    """

    @property
    def object_coordinate_system(self):
        """Object coordinate system details of the sketch.

        :rtype: trimatic.CoordinateSystem
        """
        pass

    @property
    def cell_size_x(self):
        """Cell size in x-direction.

        :rtype: float
        """
        pass

    @property
    def cell_size_y(self):
        """Cell size in y-direction.

        :rtype: float
        """
        pass

    @property
    def cell_count_x(self):
        """Cell count in x-direction.

        :rtype: int
        """
        pass

    @property
    def cell_count_y(self):
        """Cell count in y-direction.

        :rtype: int
        """
        pass

    def get_metadata(self):
        """Get sketch's metadata.

        :return: The sketch's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Sphere(Object):
    """Analytical sphere entity."""

    @property
    def color(self):
        """Color of the sphere in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def radius(self):
        """Radius of the sphere.

        :rtype: float
        """
        pass

    @property
    def center(self):
        """Center of the sphere.

        :rtype: (float, float, float)
        """
        pass

    def get_metadata(self):
        """Get sphere's metadata.

        :return: The sphere's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

class Surface(Object):
    """Surface entity."""

    @property
    def area(self):
        """Total area of the surface.

        :rtype: float
        """
        pass

    @property
    def color(self):
        """Color of the surface in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def number_of_contours(self):
        """Number of contours.

        :rtype: int
        """
        pass

    @property
    def number_of_points(self):
        """Number of points/vertices.

        :rtype: int
        """
        pass

    @property
    def number_of_triangles(self):
        """Number of triangles.

        :rtype: int
        """
        pass

    def get_border(self):
        """Get surface border

        :rtype: trimatic.SurfaceBorder
        """
        pass

    def get_parent(self):
        """Returns the parent of the surface. 
        When the surface is inside a surface set, that surface set is returned. 
        If the surface is not inside a surface set, the containing part will be returned.

        :rtype: trimatic.SurfaceSet|trimatic.Part
        """
        pass


class SurfaceBorder(Object):
    """Surface border entity."""

    @property
    def number_of_contours(self):
        """Number of contours.

        :rtype: int
        """
        pass

    def get_contours(self):
        """Returns a tuple of contours.

        :rtype: (trimatic.SurfaceContour)
        """
        pass

    def get_parent(self):
        """Returns the parent of the border. 

        :rtype: trimatic.Surface
        """
        pass


class SurfaceContour(Object):
    """Surface contour entity."""

    @property
    def has_bad_edges(self):
        """Returns True if contour has bad edges.

        :rtype: bool
        """
        pass

    @property
    def number_of_edges(self):
        """Number of edges.

        :rtype: int
        """
        pass

    @property
    def points(self):
        """Tuple of points in the contour.

        :rtype: ((float, float, float))
        """
        pass

    @property
    def length(self):
        """Length of the contour.

        :rtype: float
        """
        pass

    def get_parent(self):
        """Returns the parent of the contour. For the bad contours of a part, the part is returned.

        :rtype: trimatic.SurfaceBorder|trimatic.Part
        """
        pass


class SurfaceSet(Object):
    """Surface Set entity."""

    @property
    def area(self):
        """Total area of all surfaces in the surface set.

        :rtype: float
        """
        pass

    @property
    def number_of_surfaces(self):
        """Number of surfaces in the surface set.

        :rtype: int
        """
        pass

    def clear(self):
        """Delete all surfaces in the surface set."""
        pass

    def find_surface(self, name):
        """Finds a Surface object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first Surface object found. None if no match is found.
        :rtype: trimatic.Surface
        """
        pass

    def find_surfaces(self, regex):
        """Finds Surface objects with names that match a specified regular expression.

        :param regex: Regular expression to match
        :type regex: string
        :return: Tuple of Surface objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.Surface)
        """
        pass

    def find_surface_set(self, name):
        """Finds a SurfaceSet object with a specific name.

        :param name: Name to find.
        :type name: string
        :return: The first SurfaceSet object found. None if no match is found.
        :rtype: SurfaceSet
        """
        pass

    def find_surface_sets(self, regex):
        """Finds SurfaceSet objects with names that match a specified regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of SurfaceSet objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.SurfaceSet)
        """
        pass

    def get_surfaces(self):
        """Get all Surface objects within the SurfaceSet.

        :return: Tuple of Surface objects. Empty tuple if none are found.
        :rtype: (trimatic.Surface)
        """
        pass

    def get_surface_sets(self):
        """Get all SurfaceSet objects within the SurfaceSet.

        :return: Tuple of SurfaceSet objects. Empty tuple if none are found.
        :rtype: (trimatic.SurfaceSet)
        """
        pass

    
    def get_parent(self):
        """Returns the parent of the surface set. 
        When the surface is inside a surface set, that surface set is returned. 
        If the surface set is not inside a SurfaceSet, the containing part will be returned.

        :rtype: trimatic.SurfaceSet|trimatic.Part
        """
        pass

class VolumeMesh(Object):
    """Volume Mesh entity."""

    @property
    def color(self):
        """Color of the volume mesh in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def number_of_elements(self):
        """Number of volume elements.

        :rtype: int
        """
        pass

    @property
    def number_of_nodes(self):
        """Number of nodes.

        :rtype: int
        """
        pass

    @property
    def volume(self):
        """Total volume of the entity.

        :rtype: float
        """
        pass

    def get_parent(self):
        """Returns the parent of the volume mesh. 

        :rtype: trimatic.Part
        """
        pass
        
class SSM(Object):
    """Statistical Shape Model entity."""

    @property
    def color(self):
        """Color of the SSM in (R, G, B) tuple. Colors are specified with floating point number between 0 and 1. In 3-matic GUI, RGB colors are specified with values between 0 and 255. To convert, divide by 255.

        :rtype: (float, float, float)
        """
        pass

    @property
    def transparency(self):
        """Transparency value of the SSM specified in floating point between 0.0 to 1.0.

        :rtype: float
        """
        pass

    @property
    def distance_to_average(self):
        """Distance to average of the SSM instance. Value recalculated when the coefficients are changed.

        :rtype: float
        """
        pass

    @property
    def instance_probability (self):
        """Probability of the SSM instance. Value recalculated when the coefficients are changed.

        :rtype: float
        """
        pass

    @property
    def coefficients (self):
        """Coefficients of the SSM instance specified by a list of floating numbers between -3.0 and 3.0.

        :rtype: (float)
        """
        pass

    def get_metadata(self):
        """Get SSM's metadata.

        :return: The SSM's metadata object.
        :rtype: trimatic.Metadata
        """
        pass

    def get_triangles(self):
        """Get the points and triangles of the ssm. These points will keep their correspondence when coefficients change.

        :return: A tuple containing a tuple of points and a tuple of triangles. Tuple of triangles defined as indices in the point list.
        :rtype: ((trimatic.Point),((int,int,int)))
        """
        pass
    
    @property
    def patient_data(self):
        """Get the patient data of the SSM. It consists of a list of SSMPatientData objects containing patient information.

        :return: Tuple with list of SSMPatientData objects.
        :rtype: (trimatic.SSMPatientData)
        """
        pass


class SSMPatientData(metaclass=_BaseProxy):
    """ SSMPatientData entity """
    
    @property
    def name(self):
        """ Name of the patient.

        :rtype: string
        """
        pass

    @property
    def part_name(self):
        """ Name of the patient part.

        :rtype: string
        """
        pass

    @property
    def pathology(self):
        """ Patient pathology.

        :rtype: string
        """
        pass

    @property
    def anatomy(self):
        """ Patient anatomy.

        :rtype: string
        """
        pass

    @property
    def region(self):
        """ Patient region.

        :rtype: string
        """
        pass

    @property
    def sex(self):
        """ Patient sex.

        :rtype: string
        """
        pass

    @property
    def age(self):
        """ Patient age.

        :rtype: int
        """
        pass

    @property
    def coefficients(self):
        """ Coefficients used to reconstruct the patient.

        :rtype: (float)
        """
        pass

class Texture(Object):
    """ Image Texture entity """

    @property
    def tile_image(self):
        """ To tile the texture image or not.

        :rtype: bool
        """
        pass

    @property
    def white_offset(self):
        """ White offset value of the image texture

        :rtype: float
        """
        pass

    @property
    def black_offset(self):
        """ Black offset value of the image texture.

        :rtype: float
        """
        pass

    @property
    def accuracy(self):
        """ Slice accuracy of the texture image in the build processor.

        :rtype: float
        """
        pass

    def get_parent(self):
        """ Gets the parent UV Map of the texture entity.

        :rtype: trimatic.UVMap
        """
        pass

    def export_bitmap(self):
        """ Exports Texture image to a file. Format is determined by file name extension.
        Supported formats/extensions are: .bmp, .jpeg, .gif, .png, .tiff

        :rtype: string
        """
        pass

class UVMap(Object):
    """ UV Map entity. """

    @property
    def number_of_uv_regions(self):
        """ Number of UV regions in this UV Map.

        :rtype: int
        """
        pass

    @property
    def xyz_to_u_factor(self):
        """ XYZ to U factor of the UV Map.

        :rtype: float
        """
        pass

    @property
    def xyz_to_v_factor(self):
        """ XYZ to V factor of the UV Map.

        :rtype: float
        """
        pass

    def get_texture(self):
        """ Returns the texture object assigned to the UV Map, but returns None if there are no texture images assigned.

        :rtype: trimatic.Texture
        """
        pass

    def get_uv_regions(self):
        """ Get all UV Regions in the UV Map.

        :rtype: (trimatic.UVRegion)
        """
        pass

    def find_uv_region(self, name):
        """ Find a UV Region object with a specific name.

        :param name: Name to find. 
        :type name: string
        :return: The first UV Region object found. None if no match is found.
        :rtype: trimatic.UVRegion
        """
        pass

    def find_uv_regions(self, regex):
        """ Find a UV Region objects that matches the specific regular expression.

        :param regex: Regular expression to match.
        :type regex: string
        :return: Tuple of UV Region objects that match the specified expression. Empty tuple if no match is found.
        :rtype: (trimatic.UVRegion)
        """
        pass

    def get_parent(self):
        """ Gets the parent object the UV Map belongs to.

        :rtype: trimatic.Part
        """
        pass

    def merge_all_regions(self):
        """ Merge all regions in the UV Map to a single UV Region.

        :rtype: trimatic.UVRegion
        """
        pass

class UVRegion(Object):
    """ UV Region entity. """

    @property
    def size_u(self):
        """ Size U of the UV Region.

        :rtype: float
        """
        pass

    @property
    def size_v(self):
        """ Size V of the UV Region.

        :rtype: float
        """
        pass

    @property
    def position_u(self):
        """ Position U of the center of the UV Region.

        :rtype: float
        """
        pass

    @property
    def position_v(self):
        """ Position V of the center of the UV Region.

        :rtype: float
        """
        pass

    @property
    def normalized_uv_area(self):
        """ Returns if the UV regions have a normalized UV area relative to the XYZ to UV factors of the UV Map.

        :rtype: bool
        """
        pass

    def get_parent(self):
        """ Returns the parent UV Map of the UV Region.

        :rtype: trimatic.UVMap
        """
        pass

    def get_texture(self):
        """ Returns the texture object assigned to the parent UV Map, but returns None if there are no texture images assigned.

        :rtype: trimatic.Texture
        """
        pass

class Group(Object):
    """Group of trimatic objects."""

    @property
    def  items(self):
        """Tuple of items in group. It's a read only property.

        :rtype: (trimatic.Object)
        """
        pass

    def add_items(self, entities):
        """Add items to group.

        :param entities: A tuple of objects to add in the group.
        :type entities: (trimatic.Object)
        :raises: RuntimeError
        
        :example:

        .. literalinclude:: example/group/add_items.py
        """
        pass
    
    def get_parent(self):
        """Returns the parent group. Returns None if the group doesn't have a parent group.

        :rtype: trimatic.Group
        """
        pass

