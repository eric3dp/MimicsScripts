import pymatic
import trimatic.utils
from enum import Enum

def analyze_lattice_porosity(
    entities,
    sample_region,
    sample_size = 100000
    ):
    """Analyzes the porosity of a lattice.

    :param entities: Graph(s) to analyze.
    :type entities: trimatic.Graph | trimatic.GraphSet | [trimatic.Graph | trimatic.GraphSet]
    :param sample_region: Region in 3D space where graph needs to be analyzed.
    :type sample_region: trimatic.Part | [trimatic.Part]
    :param sample_size: The number of points that will be sampled to calculate the density. 
        With larger sample size, a more accurate estimate will be obtained. 
        GUI Precision 'Medium' corresponds to sample size 100000, 'High' with 1000000.
    :type sample_size: int, optional
    :return: A tuple that contains for every sample region, a tuple of analysis results containing (porosity value in region (in %), confidence interval start, confidence end)
    :rtype: ((float, float, float))
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/analyze_lattice_porosity.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_type("sample_region", sample_region, (trimatic.Part, ))
    trimatic.utils.check_param_greater_or_equal("sample_size", sample_size, 1)

    return pymatic.analyze_lattice_porosity(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.single_or_multiple_entities(sample_region), sample_size)

def analyze_lattice_pore_size(entities, step_size, maximum_pore_size):
    """Analyzes the pore size of the lattice structure.

    :param entities: Graph(s) to analyze.
    :type entities: trimatic.Graph | trimatic.GraphSet | [trimatic.Graph | trimatic.GraphSet]
    :param step_size: The analysis step size (equivalent to the step size as well) 
        from the minimum pore size to the the maximum pore size.
    :type step_size: float
    :param maximum_pore_size: The maximum pore size to analyze to. The operation 
        will terminate when this value is reached.
    :type maximum_pore_size: float

    :return: A tuple of analysis that consists of input graph corresponding to the result, 
        maximum pore radius, minimum pore radius, mode pore radius, average pore radius, 
        and for every sample pore, a tuple of coordinates and radius(X coordinate, 
        Y coordinate, Z coordinate, Radius) for every graph entity that exists in the input 
        entities. The ordering of a graph entity within the input entities serves as its 
        index into the top-level tuple of the returned value.
    :rtype: ((trimatic.Graph, float, float, float, float, ((float, float, float, float),)),)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/analyze_lattice_pore_size.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_param_greater_or_equal("step_size", step_size, trimatic.utils.get_resolution())
    trimatic.utils.check_param_greater_or_equal("maximum_pore_size", maximum_pore_size, step_size)
    return pymatic.analyze_lattice_pore_size(trimatic.utils.single_or_multiple_entities(entities),
                                             step_size, maximum_pore_size)

def attach_graph_to_mesh(graphs, entity, margin = 0.5):
    """Attaches graphs to a mesh.

    :param graphs: The graph(s) to attach.
    :type graphs: trimatic.Graph | trimatic.GraphSet | [trimatic.Graph | trimatic.GraphSet]
    :param entity: Part on which to attach.
    :type entity: trimatic.Part
    :param margin: When specified, nodes on the surface closer than this value will be merged. When None, no nodes will be merged.
    :type margin: float, optional
    :return: A newly created part containing the retriangulated surface of the target part and the attached graph.
    :rtype: trimatic.Part
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/attach_graph_to_mesh.py
    """
    

    trimatic.utils.check_type("graphs", graphs, (trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    if margin:
        trimatic.utils.check_param_greater_or_equal("margin", margin, 0)
    
    return pymatic.attach_graph_to_mesh(trimatic.utils.single_or_multiple_entities(graphs), entity, margin)

def connect_graphs(*args, 
                   source, 
                   target, 
                   number_of_connections = 3, 
                   min_connection_radius = 0,
                   max_connection_radius = 1):
    """Creates connections between two graph structures.

    :param source: Either single object or heterogenous list of parts or graph or graph sets.
    :type source: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param target: Either single object or heterogenous list of parts or graph or graph sets.
    :type target: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param number_of_connections: If number of connections is 1 then a single connection between the inner points (source graph) and outer points (target graph) is laid. If number of connections is ‘n’ and the graph connections are chosen from inside to outside, then each inner point is connected to the ‘n’ nearest neighboring outer points.
    :type number_of_connections: int, optional
    :param min_connection_radius: Within this specified radius, the operation will look for the number of nearest neighboring points. Set None to disable.
    :type min_connection_radius: float | None, optional
    :param max_connection_radius: Within this specified radius, the operation will look for the number of nearest neighboring points. Set None to disable. This parameter together with 'min_connection_radius' specifies the range of connection radius.
    :type max_connection_radius: float | None, optional

    :return: newly created graphs.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/connect_graphs.py
    """


    trimatic.utils.check_type("source", source, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_type("target", target, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_entity_sets_do_not_contain_equal_entities("source","target", source, target)
    trimatic.utils.check_param_greater_or_equal("number_of_connections", number_of_connections, 1)

    if min_connection_radius is not None:
      trimatic.utils.check_param_greater_or_equal("min_connection_radius", min_connection_radius, 0.0)

    if max_connection_radius is not None:
       trimatic.utils.check_param_greater_or_equal("max_connection_radius", max_connection_radius, trimatic.utils.get_resolution())
       if min_connection_radius is not None:
           trimatic.utils.check_param_greater("max_connection_radius", max_connection_radius, min_connection_radius)

    return pymatic.connect_graphs(trimatic.utils.single_or_multiple_entities(source),
                                  trimatic.utils.single_or_multiple_entities(target),
                                  number_of_connections,
                                  min_connection_radius,
                                  max_connection_radius)

def connect_graphs_self_supporting(*args, 
                   source, 
                   target, 
                   normal,
                   minimum_angle,
                   number_of_connections = 3, 
                   min_connection_radius = 0,
                   max_connection_radius = 1
                   ):
    """Creates connections between two graph structures that are self supported based on the normal vector of the plane selected.

    :param source: Either single object or heterogenous list of parts or graph or graph sets.
    :type source: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param target: Either single object or heterogenous list of parts or graph or graph sets.
    :type target: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param normal: Normal vector of the reference plane to be used. 
    :type normal: trimatic.Point
    :param minimum_angle: Minimum required angle between created graph beams and reference plane. 
    :type minimum_angle: float
    :param number_of_connections: If number of connections is 1 then a single connection between the inner points (source graph) and outer points (target graph) is laid. If number of connections is ‘n’ and the graph connections are chosen from inside to outside, then each inner point is connected to the ‘n’ nearest neighboring outer points.
    :type number_of_connections: int, optional
    :param min_connection_radius: Within this specified radius, the operation will look for the number of nearest neighboring points. Set None to disable.
    :type min_connection_radius: float | None, optional
    :param max_connection_radius: Within this specified radius, the operation will look for the number of nearest neighboring points. Set None to disable. This parameter together with 'min_connection_radius' specifies the range of connection radius.
    :type max_connection_radius: float | None, optional
 
    :return: newly created graphs.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/connect_graphs_self_supporting.py
    """


    trimatic.utils.check_type("source", source, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_type("target", target, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_entity_sets_do_not_contain_equal_entities("source","target", source, target)
    trimatic.utils.check_param_greater_or_equal("number_of_connections", number_of_connections, 1)

    if min_connection_radius is not None:
      trimatic.utils.check_param_greater_or_equal("min_connection_radius", min_connection_radius, 0.0)

    if max_connection_radius is not None:
       trimatic.utils.check_param_greater_or_equal("max_connection_radius", max_connection_radius, trimatic.utils.get_resolution())
       if min_connection_radius is not None:
           trimatic.utils.check_param_greater("max_connection_radius", max_connection_radius, min_connection_radius)

    pymatic_normal = trimatic.utils.point_argument(normal)
    trimatic.utils.check_direction("normal", pymatic_normal)

    trimatic.utils.check_param_greater_or_equal("minimum_angle", minimum_angle, 0.0)
    trimatic.utils.check_param_smaller_or_equal("minimum_angle", minimum_angle, 90.0)

    return pymatic.connect_graphs_self_supporting(
        trimatic.utils.single_or_multiple_entities(source),
        trimatic.utils.single_or_multiple_entities(target),
        pymatic_normal,
        minimum_angle,
        number_of_connections,
        min_connection_radius,
        max_connection_radius)
 
def convert_lattice_to_regular_mesh(entities, connection_thickness = 0):
    """Converts graph(s) to part(s) where the beams are converted to cylindrical entities with spherical endings. 

    Input entities are grouped according to the part they belong to. For every group, a new part will be created. 
    To control beam thickness and/or accuracy, use trimatic.set_graph_properties. 
    When the input has graphs with thickness 0, the operation will fail.
    When the input has graphs with accuracy 0, the operation will use accuracy of 40% of the minimal thickness value.
    When the group does not have graphs with accuracy 0, the operation will use minimal accuracy value.
    
    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param connection_thickness: The diameters of the spheres at beam connections. This parameter only has effect when the connection_thickness is larger than beam thickness (e.g. when it is 0). 
    :type connection_thickness: float, optional

    :return: Newly created part(s).
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/convert_lattice_to_regular_mesh.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))

    if connection_thickness:
        trimatic.utils.check_resolution("connection_thickness", connection_thickness)

    return pymatic.convert_lattice_to_regular_mesh(trimatic.utils.single_or_multiple_entities(entities), connection_thickness)

def convert_lattice_to_organic_mesh(entities, organic_factor = 1.200) :
    """Converts graph(s) to part(s) where the beams are converted to organic (cancellous bone-like) mesh structure. 

    Input entities are grouped according to the part they belong to. For every group, a new part will be created. 
    To control beam thickness and/or accuracy, use trimatic.set_graph_properties. 
    When the input has graphs with thickness 0, the operation will fail.
    When the input has graphs with accuracy 0, the operation will use accuracy of 40% of the minimal thickness value.
    When the group does not have graphs with accuracy 0, the operation will use minimal accuracy value.
    
    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param organic_factor: The intensity of the organic effect on the output mesh. 
    :type organic_factor: float, optional

    :return: Newly created part(s).
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError | RuntimeError
    
    :example:

    .. literalinclude:: example/lattice/convert_lattice_to_organic_mesh.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))

    if organic_factor:
        trimatic.utils.check_param_greater_or_equal("organic_factor", organic_factor, 1.0001)

    return pymatic.convert_lattice_to_organic_mesh(trimatic.utils.single_or_multiple_entities(entities), organic_factor)

def convert_to_graph(entities):
    """Converts curve like entities to graphs.

    :param entities: Either single object or heterogenous list of curve, curve sets , surface borders or surface contours.
    :type entities: trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour |  trimatic.CurveSet | [trimatic.Curve | trimatic.SurfaceBorder | trimatic.SurfaceContour | trimatic.CurveSet ]

    :return: newly created graphs.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/convert_to_graph.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Curve, trimatic.CurveSet, trimatic.SurfaceBorder, trimatic.SurfaceContour))

    return pymatic.convert_to_graph(trimatic.utils.single_or_multiple_entities(entities))   

def create_beam(graph, point1, point2, thickness1 = 0, thickness2 = 0):
    """Creates a beam in a graph.

    :param graph: The graph in which to create a beam. When specifying None, a new part is created that contains a graph with the new beam.
    :type graph: trimatic.Graph
    :param point1: First point of the beam
    :type point1: trimatic.Point
    :param point2: Second point of the beam
    :type point2: trimatic.Point
    :param thickness1: Thickness (diameter) of the new beam at point1.
    :type thickness1: float, optional
    :param thickness2: Thickness (diameter) of the new beam at point2.
    :type thickness2: float, optional
    :return: Graph containing the new beam
    :rtype: trimatic.Graph
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/create_beam.py
    """
    

    trimatic.utils.check_type("graph", graph, (trimatic.Graph, ), True)
    trimatic.utils.check_param_greater_or_equal("thickness1", thickness1, 0)
    trimatic.utils.check_param_greater_or_equal("thickness2", thickness2, 0)
    pymatic_point1 = trimatic.utils.point_argument(point1) 
    pymatic_point2 = trimatic.utils.point_argument(point2) 
    trimatic.utils.check_2points_not_coincident("point1", "point2", pymatic_point1, pymatic_point2)
    
    return pymatic.create_beam(graph, pymatic_point1, pymatic_point2, thickness1, thickness2)

def fea_based_thickness(entity, analysis, minimum_thickness, maximum_thickness):
    """Uses FEA analysis to apply thickness on a graph.

    :param entity: The graph to apply thickness.
    :type entity: trimatic.Graph
    :param analysis: Analysis to use.
    :type analysis: trimatic.Analysis
    :param minimum_thickness: Minimum thickness to use for minimum analysis value.
    :type minimum_thickness: float
    :param maximum_thickness: Maximum thickness to use for maximum analysis value.
    :type maximum_thickness: float
    :return: Graph to which thickness was applied.
    :rtype: trimatic.Graph
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/lattice/fea_based_thickness.py
    """



    trimatic.utils.check_type("entity", entity, (trimatic.Graph))
    trimatic.utils.check_type("analysis", analysis, (trimatic.Analysis))

    trimatic.utils.check_param_greater_or_equal("minimum_thickness", minimum_thickness, 0.0)
    trimatic.utils.check_param_greater("maximum_thickness", maximum_thickness, minimum_thickness)
    
    return pymatic.fea_based_thickness(entity, analysis, minimum_thickness, maximum_thickness)

def filter_beams_by_length(entities, length_threshold):
    """Filters beams based on length.

    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param length_threshold: Beams with length > length_threshold will be filtered.
    :type length_threshold: float 

    :return: GraphSet that contains the graph with the filtered beams.
    :rtype: trimatic.GraphSet
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/filter_beams_by_length.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_param_greater_or_equal("length_threshold", length_threshold, trimatic.utils.get_resolution())

    return pymatic.filter_beams_by_length(trimatic.utils.single_or_multiple_entities(entities),length_threshold)

def filter_loose_beams(entities, connection_threshold = 0):
    """Filters beams based on connectivity.

    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param connection_threshold: Beams with that have <= connection_threshold connections will be filtered. 
                                For example, when connection_threshold = 0, graphs without connections will be filtered. 
                                when connection_threshold = 1, graphs with 0 or 1 connections will be filtered. 
    :type connection_threshold: int, optional 

    :return: GraphSet that contains the graph with the filtered beams.
    :rtype: trimatic.GraphSet
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/filter_loose_beams.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_param_greater_or_equal("connection_threshold", connection_threshold, 0)
    trimatic.utils.check_param_smaller_or_equal("connection_threshold", connection_threshold, 1)

    return pymatic.filter_loose_beams(trimatic.utils.single_or_multiple_entities(entities),connection_threshold)

def filter_overlapping_beams(entities, offset_margin = None):
    """Filters overlapping beams.

    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param offset_margin: When None, only fully overlapping beams are filtered. When specifying offset_margin, also beams that don't exactly overlap are filtered out.

    :type offset_margin: float, optional 

    :return: GraphSet that contains the graph with the filtered beams.
    :rtype: trimatic.GraphSet
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/filter_overlapping_beams.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    if offset_margin:
        trimatic.utils.check_param_greater_or_equal("offset_margin", offset_margin, 0)

    return pymatic.filter_overlapping_beams(trimatic.utils.single_or_multiple_entities(entities), offset_margin)

def mesh_based_lattice(entities, maximum_beam_length = None):
    """Creates graph on the selected part or surface.

    :param entities: Either single object or a heterogenous list of parts or surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet]
    :param maximum_beam_length: The maximum triangle edge length in the output. Set to None to disable.
    :type maximum_beam_length: (float | None, optional)

    :return: newly created graphs after converting mesh to lattice.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/mesh_based_lattice.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet ))

    if maximum_beam_length is not None:
       trimatic.utils.check_resolution("maximum_beam_length", maximum_beam_length)

    return pymatic.mesh_based_lattice(trimatic.utils.single_or_multiple_entities(entities), maximum_beam_length)

def mesh_based_lattice_with_volume(entities,  maximum_beam_length = None):
    """Creates graph on the selected part.

    :param entities: Either single object or a list of parts.
    :type entities: trimatic.Part | [trimatic.Part]
    :param maximum_beam_length: The maximum triangle edge length in the output. Set to None to disable.
    :type maximum_beam_length: (float | None, optional)

    :return: newly created graphs after converting mesh to lattice.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/mesh_based_lattice_with_volume.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))

    if maximum_beam_length is not None:
       trimatic.utils.check_resolution("maximum_beam_length", maximum_beam_length)

    return pymatic.mesh_based_lattice_with_volume(trimatic.utils.single_or_multiple_entities(entities), maximum_beam_length)
    
def move_graphs_to_graphset(graphs):
    """Moves graph(s) into a newly created graph set. The graphset is created in the part that contains the first graph in the list.

    :param entities: One or more graph(s) to move.
    :type entities: trimatic.Graph | [trimatic.Graph]
    :return: Newly created graphset.
    :rtype: trimatic.GraphSet
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/lattice/move_graphs_to_graphset.py
    """

    trimatic.utils.check_type("graphs", graphs, (trimatic.Graph))

    return pymatic.move_graphs_to_graphset(trimatic.utils.single_or_multiple_entities(graphs))

def porosity_based_thickness(entity, sample_region, target_porosity = 20, sample_size = 100000, affect_whole_entity = True, scaled = False):
    """Assigns porosity based thickness.

    :param entity: The graph to apply thickness.
    :type entity: trimatic.Graph | trimatic.GraphSet
    :param sample_region: The porosity will be calculated based on this region. 
    :type sample_region: trimatic.Part 
    :param target_porosity: The desired porosity to be achieved.
    :type target_porosity: float, optional
    :param sample_size: The number of points that will be sampled to calculate the density. 
        With larger sample size, a more accurate estimate will be obtained. 
        GUI Precision 'Medium' corresponds to sample size 100000, 'High' with 1000000.
    :type sample_size: int, optional
    :param affect_whole_entity: When True, The thickness will be applied to the whole graph set. When False, the operation will trim and apply thickness to graphs within the sample region only.
    :type affect_whole_entity: bool, optional
    :param scaled: When True, the operation will scale the thickness of the selection (zero thickness will remain zero). When False, the operation will apply absolute thickness to the selection.
    :type scaled: bool, optional

    :return: Tuple of acheived results containing (pososity value in region (in %), confidence interval start, confidence end)
    :rtype: (float, float, float)
    :raises: RuntimeError, ValueError
    
    :example:

    .. literalinclude:: example/lattice/porosity_based_thickness.py
    """
    

    trimatic.utils.check_type("entity", entity,(trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_type("sample_region", sample_region, (trimatic.Part, ))
    trimatic.utils.check_param_greater_or_equal("sample_size", sample_size, 1)
    trimatic.utils.check_param_in_range("target_porosity", target_porosity, 0, 100)

    return pymatic.porosity_based_thickness(entity, sample_region, target_porosity, sample_size, affect_whole_entity, scaled)

def quad_based_lattice(entities, edge_length = 2.0):
    """Creates graphs with quad based design.
    
    :param entities: Either single object or heterogenous list of parts or surfaces or surface sets.
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet ]
    :param edge_length: Target edge length of the quad mesh.
    :type edge_length: float, optional

    :return: newly created graphs.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/quad_based_lattice.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet ))
    trimatic.utils.check_param_greater_or_equal("edge_length", edge_length, trimatic.utils.get_resolution())

    return pymatic.quad_based_lattice(trimatic.utils.single_or_multiple_entities(entities), edge_length)
    
def set_graph_properties(entities, thickness, accuracy = None):
    """Sets properties (thickness and/or accuracy) of graph beams. 

    :param entities: Either single object or heterogenous list of parts or graph or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param thickness: The thickness that the beams should get. When specifying None, thickness will not be modified.
    :type thickness: float
    :param accuracy: The accuracy that the beams should get. When specifying None, accuracy will not be modified.
    :type accuracy: float, optional

    :return: The modified graphs.
    :rtype: trimatic.Part | trimatic.Graph | trimatic.GraphSet | (trimatic.Part | trimatic.Graph | trimatic.GraphSet)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/set_graph_properties.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))

    if thickness is not None:
        trimatic.utils.check_param_greater_or_equal("thickness", thickness, 0)
    if accuracy is not None:
        trimatic.utils.check_resolution("accuracy", accuracy)

    return pymatic.set_graph_properties(trimatic.utils.single_or_multiple_entities(entities),thickness, accuracy)

def unit_cell_based_lattice(
        *args,#'force named parameters'
        entity, 
        unit_cell, 
        fill_solid = True, 
        keep_beams_on_border = True, 
        randomization_min = None, 
        randomization_max = None, 
        trim_randomized = True, 
        randomization_seed = None):
    """Fills up the selected part with the provided unit cell. 

    :param entity: The part to fill.
    :type entity: trimatic.Part 
    :param unit_cell: The unit cell to use for filling.
    :type unit_cell: trimatic.GraphSet
    :param fill_solid: When True (solid fill), the operation will fill all the solid regions in the part with unit cells. When False (hollow fill), all hollow regions in the part are filled with unit cells.  
    :type fill_solid: bool, optional
    :param keep_beams_on_border: When False, beams on the surface of the input entity will be removed.  
    :type keep_beams_on_border: bool, optional
    :param randomization_min: The minimal (x,y,z) deviation of the endpoints.
    :type randomization_min: (float, float, float), optional
    :param randomization_max: The maximal (x,y,z) deviation of the endpoints.
    :type randomization_max: (float, float, float), optional
    :param trim_randomized: Any graph lines going out of the bounding box of the part to fill will be trimmed and deleted.  
    :type trim_randomized: bool, optional
    :param randomization_seed: Randomization can be controlled by specifying a seed value.
    :type randomization_seed: int, optional

    :return: Newly created graph. Note that a part was created as well to contain the graph.
    :rtype: trimatic.Graph 
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/unit_cell_based_lattice.py
    """


    trimatic.utils.check_type("entity", entity, (trimatic.Part, ))
    trimatic.utils.check_type("unit_cell", unit_cell, (trimatic.GraphSet))

    if randomization_min and randomization_max:
        if randomization_max[0] < randomization_min[0] or randomization_max[1] < randomization_min[1] or randomization_max[2] < randomization_min[2]:
            raise ValueError("Maximum deviation must be larger than Minimum deviation")

    pymatic_randomization_min = randomization_min
    if pymatic_randomization_min:
        pymatic_randomization_min = trimatic.utils.point_argument(randomization_min)

    pymatic_randomization_max = randomization_max
    if pymatic_randomization_max:
        pymatic_randomization_max = trimatic.utils.point_argument(randomization_max)

    return pymatic.unit_cell_based_lattice(entity, unit_cell, keep_beams_on_border, fill_solid, pymatic_randomization_min , pymatic_randomization_max, trim_randomized, randomization_seed)

def create_uv_based_conformal_lattice(
        *args,
        uv_map,
        unit_cell,
        margin_u = 0.0000,
        margin_v = 0.0000,
        preserve_unit_cell_height = False,
        height_offset = 0.0000,
        is_outside = True,
        number_of_layers = 1,
        preserve_boundary_unit_cells = True):
    """ Creates conformal lattice structure from an array of unit cells based on UV Map on the outside.

    :param uv_map: Parameterization to be used to guide the conformal lattice.
    :type uv_map: trimatic.UVMap
    :param unit_cell: The unit cell to be used as cells in the conformal lattice.
    :type unit_cell: trimatic.GraphSet
    :param margin_u: The distance between the unit cells in the U direction in UV units.
    :type margin_u: float, optional 
    :param margin_v: The distance between the unit cells in the V direction in UV units.
    :type margin_v: float, optional
    :param preserve_unit_cell_height: If True, preserve the original unit cell height in the output.
    :type preserve_unit_cell_height: bool, optional
    :param height_offset: The distance of the first layer of the unit cell from the UV mapped surface.
    :type height_offset: float, optional
    :param is_outside: IF True, the lattice structure will be generated in the outer side of the parameterized surface, else inner side.
    :type is_outside: bool, optional
    :param number_of_layers: Number of layers in the vertical direction for the unit cells.
    :type number_of_layers: int, optional 
    :param preserve_boundary_unit_cells: If True, the partial unit cells will be preserved as is in the final output.
    :type preserve_boundary_unit_cells: bool, optional

    :return: Graph entity that is the conformal lattice structure. A new part is created to contain the graph entity.
    :rtype: trimatic.Graph
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/uv_based_conformal_lattice.py
    """


    trimatic.utils.check_type("uv_map", uv_map, (trimatic.UVMap))
    trimatic.utils.check_type("unit_cell", unit_cell, (trimatic.GraphSet))
    trimatic.utils.check_param_in_range("margin_u", margin_u, 0.0000, 0.9999)
    trimatic.utils.check_param_in_range("margin_v", margin_v, 0.0000, 0.9999)
    trimatic.utils.check_param_greater_or_equal("number_of_layers", number_of_layers, 1)

    return pymatic.create_uv_based_conformal_lattice(uv_map, unit_cell, margin_u, margin_v, preserve_unit_cell_height,
                                                     height_offset, is_outside, number_of_layers, preserve_boundary_unit_cells)

class DesiredResultDualConformalLattice(Enum):
    """Desired Result Dual Conformal Lattice."""
    RefitBoundaryEntity = "RefitBoundaryEntity"
    Trimmed = "Trimmed"
    Untrimmed = "Untrimmed"

def create_uv_based_dual_conformal_lattice(
        *args,
        source_uv_map,
        target_uv_map,
        unit_cell,
        margin_u = 0.0000,
        margin_v = 0.0000,
        height_offset = 0.0000,
        number_of_layers = None,
        desired_result = DesiredResultDualConformalLattice.RefitBoundaryEntity,
        multi_cell_parameters = None):
    """ Creates conformal lattice structure from an array of unit cells in between 2 UV Maps.

    :param source_uv_map: First parameterization to be used to guide the conformal lattice.
    :type source_uv_map: trimatic.UVMap
    :param target_uv_map: Second parameterization to be used to guide the conformal lattice.
    :type target_uv_map: trimatic.UVMap
    :param unit_cell: The unit cell to be used as cells in the conformal lattice.
    :type unit_cell: trimatic.GraphSet
    :param margin_u: The distance between the unit cells in the U direction in UV units.
    :type margin_u: float, optional
    :param margin_v: The distance between the unit cells in the V direction in UV units.
    :type margin_v: float, optional
    :param height_offset: The distance of the first layer of the unit cell from the UV mapped surface.
    :type height_offset: float, optional
    :param number_of_layers: If set to None, then number_of_layers will be auto calculated else, the specified number of layers will fitted between the UV maps.
    :type number_of_layers: int/None, optional
    :param desired_result: Method to determine whether the partially boundary cells will be trimmed, refitted or not modified.
    :type desired_result: trimatic.DesiredResultDualConformalLattice, optional
    :param multi_cell_parameters: Tuple of tuple with the unit cell entity, start layer and end layer for the multi cells. If set to None, then only the main unit cell input will be applied for all layers.
    :type multi_cell_parameters: ((trimatic.GraphSet, int, int),), optional

    :return: Graph entity that is the dual conformal lattice structure. A new part is created to contain the graph entity.
    :rtype: trimatic.Graph
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/create_uv_based_dual_conformal_lattice.py
    """


    trimatic.utils.check_type("source_uv_map", source_uv_map, (trimatic.UVMap))
    trimatic.utils.check_type("target_uv_map", target_uv_map, (trimatic.UVMap))
    trimatic.utils.check_type("unit_cell", unit_cell, (trimatic.GraphSet))
    trimatic.utils.check_param_in_range("margin_u", margin_u, 0.0000, 0.9999)
    trimatic.utils.check_param_in_range("margin_v", margin_v, 0.0000, 0.9999)
    if number_of_layers is not None:
        trimatic.utils.check_param_greater_or_equal("number_of_layers", number_of_layers, 1)
    if desired_result is not None:
        trimatic.utils.check_type('desired_result', desired_result, (DesiredResultDualConformalLattice,))
    if multi_cell_parameters is not None:
        trimatic.utils.check_type_tuple_of_tuples("multi_cell_parameters",
                                                  multi_cell_parameters,
                                                  (trimatic.GraphSet, int, int),
                                                  (trimatic.utils.TOT_Constraint.NOT_NONE, trimatic.utils.TOT_Constraint.GT_ZERO, trimatic.utils.TOT_Constraint.GT_ZERO))

    return pymatic.create_uv_based_dual_conformal_lattice(source_uv_map, 
                                                          target_uv_map, 
                                                          unit_cell,
                                                          margin_u,
                                                          margin_v,
                                                          height_offset,
                                                          number_of_layers,
                                                          desired_result.value,
                                                          multi_cell_parameters)

def attract_graph_to_mesh(graphs, entity, distance_threshold = 1.0, clearance = 0.0):
    """ Attracts the beam nodes to the target mesh.

    :param graphs: Graphs and graph sets with beam nodes to be attracted to the target mesh.
    :type  graphs: trimatic.Graph | trimatic.GraphSet | [trimatic.Graph | trimatic.GraphSet]
    :param entity: A mesh to attract the beam nodes to. It should be within the same part as graphs.
    :type  entity: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet
    :param distance_threshold: The distance of beam nodes from the target mesh to be attracted.
    :type distance_threshold: float, optional
    :param clearance: The tolerance distance of the attracted nodes position from the target mesh.
    :type clearance: float, optional

    :return: Attracted graphs and graph sets.
    :rtype: trimatic.Graph | trimatic.GraphSet | (trimatic.Graph | trimatic.GraphSet)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/attract_graph_to_mesh.py
    """


    trimatic.utils.check_type("graphs", graphs, (trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_type("entity", entity, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_resolution("distance_threshold", distance_threshold)
    trimatic.utils.check_param_greater_or_equal("clearance", clearance, 0.0)

    return pymatic.attract_graph_to_mesh(trimatic.utils.single_or_multiple_entities(graphs), entity, distance_threshold, clearance)

def connect_nodes(entities,
                  number_of_connections = 3,
                  min_connection_distance = 0,
                  max_connection_distance = 1):
    """Creates connections between two or more beam nodes.

    :param entities: Single object or heterogeneous list of graphs for the nodes to be connected.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param number_of_connections: If a beam node already has equal or more than the specified number of connections, then that node will not be connected to any nodes, else enough connections will be added to satisfy this input.
    :type number_of_connections: int, optional
    :param min_connection_distance: Within this specified distance, the operation will look for the number of nearest neighboring points. Set None to disable.
    :type min_connection_distance: float | None, optional
    :param max_connection_distance: Within this specified distance, the operation will look for the number of nearest neighboring points. Set None to disable. This parameter together with 'min_connection_radius' specifies the range of connection radius.
    :type max_connection_distance: float | None, optional

    :return: Graph entities with the connected nodes.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/connect_nodes.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet ))
    trimatic.utils.check_param_greater_or_equal("number_of_connections", number_of_connections, 1)

    if min_connection_distance is not None:
      trimatic.utils.check_param_greater_or_equal("min_connection_distance", min_connection_distance, 0.0)

    if max_connection_distance is not None:
       trimatic.utils.check_resolution("max_connection_distance", max_connection_distance)
       if min_connection_distance is not None:
           trimatic.utils.check_param_greater("max_connection_distance", max_connection_distance, min_connection_distance)

    return pymatic.connect_nodes(trimatic.utils.single_or_multiple_entities(entities), number_of_connections, min_connection_distance, max_connection_distance)

def connect_nodes_self_supporting(*args,
                                  entities,
                                  number_of_connections = 3,
                                  normal,
                                  minimum_angle,
                                  min_connection_distance = 0,
                                  max_connection_distance = 1):
    """Creates connections between two or more beam nodes which are self supporting.

    :param entities: Single object or heterogeneous list of graphs for the nodes to be connected with self supporting beams.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param number_of_connections: If a beam node already has equal or more than the specified number of connections, then that node will not be connected to any nodes, else enough connections will be added to satisfy this input.
    :type number_of_connections: int, optional
    :param normal: Normal direction of the desired build platform of the selected entity.
    :type normal: trimatic.Point
    :param minimum_angle: Minimum required angle between created graph beams and reference plane.
    :type minimum_angle: float
    :param min_connection_distance: Within this specified distance, the operation will look for the number of nearest neighboring points. Set None to disable.
    :type min_connection_distance: float | None, optional
    :param max_connection_distance: Within this specified distance, the operation will look for the number of nearest neighboring points. Set None to disable. This parameter together with 'min_connection_radius' specifies the range of connection radius.
    :type max_connection_distance: float | None, optional
 
    :return: Graph entities with the connected nodes.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/connect_nodes_self_supporting.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_param_greater_or_equal("number_of_connections", number_of_connections, 1)

    if min_connection_distance is not None:
      trimatic.utils.check_param_greater_or_equal("min_connection_distance", min_connection_distance, 0.0)

    if max_connection_distance is not None:
       trimatic.utils.check_resolution("max_connection_distance", max_connection_distance)
       if min_connection_distance is not None:
           trimatic.utils.check_param_greater("max_connection_distance", max_connection_distance, min_connection_distance)

    pymatic_normal = trimatic.utils.point_argument(normal)
    trimatic.utils.check_direction("normal", pymatic_normal)

    trimatic.utils.check_param_greater_or_equal("minimum_angle", minimum_angle, 0.0)
    trimatic.utils.check_param_smaller_or_equal("minimum_angle", minimum_angle, 90.0)

    return pymatic.connect_nodes_self_supporting(trimatic.utils.single_or_multiple_entities(entities), number_of_connections, pymatic_normal, minimum_angle, min_connection_distance, max_connection_distance)

class LatticeType(Enum):
    """Lattice Type."""
    SurfaceAndVolume = "SurfaceAndVolume"
    Surface = "Surface"
    Volume = "Volume"

def create_voronoi_based_lattice(*args,#'force named parameters'
                                 entities,
                                 lattice_type = LatticeType.SurfaceAndVolume,
                                 target_pore_radius = 5.0000,
                                 thickness = 1.0000,
                                 push_nodes_under_surface = False,
                                 local_lattice_parameters = ()):
    """Create voronoi based lattices structure from an input mesh entity.

    :param entities: The mesh entity that needs to be used to generate the voronoi lattice structure. 
    :type entities: trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles | [trimatic.Part | trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles]
    :param lattice_type: Type of lattice to be generated, surface or volume or both.
    :type lattice_type: trimatic.LatticeType, optional
    :param target_pore_radius: The target radius of the pore sizes to be achieved for the voronoi cells. 
    :type target_pore_radius: float, optional
    :param thickness: The thickness of the beams of the voronoi based lattice structures. 
    :type thickness: float, optional
    :param push_nodes_under_surface: When true, all the beams nodes that is on or outside the mesh border will be pushed to be under the mesh entity with the thickness accounted for. 
    :type push_nodes_under_surface: bool, optional
    :param local_lattice_parameters: Tuple of tuples containing the info (entity, target pore radius, thickness)
    :type local_lattice_parameters: ((trimatic.Surface | trimatic.SurfaceSet | trimatic.MarkedTriangles, float, float),), optional
    :return: Graph structures from the voronoi edges. 
    :rtype: (trimatic.Graph)
    :raises: ValueError, RuntimeError

    Error shall be thrown in the following cases

    * When the local entities selected do not belong to the global entities o Error message: "Local entities does not match global entities",
    * When the local lattice thickness is non-zero and global thickness is zero o Error message: "The local lattice thickness shall be set to zero if the global thickness is zero" 
    * When the local lattice thickness is zero and global thickness is non-zero o Error message: "The local lattice thickness shall be set to a non-zero value if the global thickness is not zero"
    * When the global entity is not of type trimatic.Part but local lattice parameters are still passed. 

    Local parameters shall only be allowed with entities that are part of global entities that are of type trimatic.Part. No local parameters shall be allowed in case there is no global entity of type trimatic.Part.  

    :example:

    .. literalinclude:: example/lattice/create_voronoi_based_lattice.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles))
    if lattice_type is not None:
        trimatic.utils.check_type('lattice_type', lattice_type, (LatticeType,))
    if target_pore_radius is not None:
        trimatic.utils.check_resolution("target_pore_radius", target_pore_radius)
    if thickness is not None:
        trimatic.utils.check_param_greater_or_equal("thickness", thickness, 0.0)
    if local_lattice_parameters is not None:
        if len(local_lattice_parameters)>0:
            trimatic.utils.check_at_least_one_of_type("entities", entities, trimatic.Part)
        trimatic.utils.check_type_tuple_of_tuples("local_lattice_parameters", local_lattice_parameters,
            ((trimatic.Surface, trimatic.SurfaceSet, trimatic.MarkedTriangles), float, float),
            (trimatic.utils.TOT_Constraint.NOT_NONE, trimatic.utils.TOT_Constraint.CHECK_RESOLUTION_GT_EQ, trimatic.utils.TOT_Constraint.GT_EQ_ZERO)
            )
        is_global_thickness_zero = (thickness==0)
        for local_parameter in local_lattice_parameters:
            if (is_global_thickness_zero and local_parameter[2]!=0):
                raise ValueError("The local lattice thickness shall be set to zero if the global thickness is zero")
            elif(not is_global_thickness_zero and local_parameter[2]==0):
                raise ValueError("The local lattice thickness shall be set to a non-zero value if the global thickness is not zero")
    return pymatic.create_voronoi_based_lattice(trimatic.utils.single_or_multiple_entities(entities), 
                                                lattice_type.value,
                                                target_pore_radius,
                                                thickness,
                                                push_nodes_under_surface,
                                                local_lattice_parameters)

def stitch_graphs(entities, number_of_iterations=1, tolerance=1.0000, loose_beams_only = False):
    """Stitches beam nodes within the specified tolerance distance.

    :param entities: Either single object or a heterogenous list of parts or graphs or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param number_of_iterations: The maximum number of iterations to repeat the operation before terminating.
    :type number_of_iterations: (integer, optional) 
    :param tolerance: The tolerance distance between the nodes to be stitched together. 
    :type tolerance: (float, optional) 
    :param loose_beams_only: If set to True, then only the loose beams will be stitched.
    :type loose_beams_only: (bool, optional) 

    :return: Graphs with nodes stitched together.
    :rtype: trimatic.Graph | (trimatic.Graph)  
    :raises: ValueError | RuntimeError
    
    :example:

    .. literalinclude:: example/lattice/stitch_graphs.py
    """
    
    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))
    trimatic.utils.check_param_greater_or_equal("number_of_iterations", number_of_iterations, 1.0)
    trimatic.utils.check_param_greater_or_equal("tolerance", tolerance, 0.0001)
    return pymatic.stitch_graphs(trimatic.utils.single_or_multiple_entities(entities), number_of_iterations, tolerance, loose_beams_only)

def split_beams_at_intersection(entities, thickness_based_intersection = True):
    """Creates node at all positions where beams are crossing each other.

    :param entities: Either single object or a heterogenous list of parts or graphs or graph sets.
    :type entities: trimatic.Part | trimatic.Graph | trimatic.GraphSet | [trimatic.Part | trimatic.Graph | trimatic.GraphSet]
    :param thickness_based_intersection: If set to True, the intersecting thickness will be accounted to generate the nodes.
    :type thickness_based_intersection: (bool, optional) 

    :return: Graphs that has been modified by the operations.
    :rtype: trimatic.Graph | (trimatic.Graph)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/lattice/split_beams_at_intersection.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.Graph, trimatic.GraphSet))
    return pymatic.split_beams_at_intersection(trimatic.utils.single_or_multiple_entities(entities), thickness_based_intersection)
