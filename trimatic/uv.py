import pymatic
import trimatic.utils
from enum import Enum

def create_uv_maps(
    *args, #'force named parameters'
    entities,
    seams = None,
    single_uv_map = True,
    preserve_surface_connections = False,
    xyz_to_u_factor = 10.0000,
    xyz_to_v_factor = 10.0000
    ) :
    """ Operation to create UV maps with surfaces/surface sets input.

    :param entities: Entities to be parameterized. Heterogeneous list of entities are allowed.
    :type entities: trimatic.Surface | trimatic.SurfaceSet | [trimatic.Surface | trimatic.SurfaceSet]
    :param seams: One or multiple attached curve(s) to be used as relaxer cuts in the parameterization.
    :type seams: trimatic.Curve | [trimatic.Curve], optional
    :param single_uv_map: When True, only one UV Map will be generated in a single parent part.
    :type single_uv_map: bool, optional
    :param preserve_surface_connections: When True, all the existing connections between the selected entities will be preserved in the output map.
    :type preserve_surface_connections: bool, optional
    :param xyz_to_u_factor: The XYZ to U factor of the initial parameterization.
    :type xyz_to_u_factor: float, optional
    :param xyz_to_v_factor: The XYZ to V factor of the initial parameterization.
    :type xyz_to_v_factor: float, optional
    :return: Newly created UV Maps.
    :rtype: trimatic.UVMap | (trimatic.UVMap)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/uv/create_uv_maps.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Surface, trimatic.SurfaceSet))
    if seams:
        trimatic.utils.check_type("seams", seams, (trimatic.Curve, ))
    trimatic.utils.check_resolution("xyz_to_u_factor", xyz_to_u_factor)
    trimatic.utils.check_resolution("xyz_to_v_factor", xyz_to_v_factor)

    return pymatic.create_uv_maps(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.single_or_multiple_entities(seams),
                                  single_uv_map, preserve_surface_connections, xyz_to_u_factor, xyz_to_v_factor)

class OptimizeMethod(Enum):
    """Methods to be used to optimize the UV parameterization."""

    Angles = "Angles"
    """Angles method."""

    AnglesAndArea = "Angles and Area"
    """Angles and Area method."""

    Area = "Area"
    """Area method."""

def optimize_uv(
    entities,
    iterations = 100,
    method = OptimizeMethod.AnglesAndArea,
    preserve_uv_border = True):
    """ Optimizes the UV Parameterization based on the selected method for the number of iterations set by the user.

    :param entities: Parameterized entities to be optimized. Heterogeneous list of entities are allowed.
    :type entities: trimatic.Part | trimatic.UVRegion | trimatic.UVMap | [trimatic.Part | trimatic.UVRegion | trimatic.UVMap]
    :param iterations: Number of iterations to perform the operation before termination.
    :type iterations: int, optional
    :param method: The method to be used to optimize the UV parameterizations.
    :type method: trimatic.OptimizeMethod, optional
    :param preserve_uv_border: If set to True, the UV border will not be changed after the optimization.  
    :type preserve_uv_border: bool, optional 

    :return: One or more optimized UV Maps. 
    :rtype: trimatic.UVMap | (trimatic.UVMap)
    :raises: ValueError | RuntimeError

    :example:

    .. literalinclude:: example/uv/optimize_uv.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part, trimatic.UVRegion, trimatic.UVMap))
    trimatic.utils.check_param_greater("iterations", iterations, 0.0)

    return pymatic.optimize_uv(trimatic.utils.single_or_multiple_entities(entities), iterations, method.value, preserve_uv_border)

def align_uv_automatic(uv_map, size_u = None, size_v = None):
    """ Align the UV region by four contour points automatically.

    :param uv_map: A UV Map with UV Regions to be aligned.
    :type uv_map: trimatic.UVMap
    :param size_u: The length of the U axis of the aligned region in UV units. If both size_u and size_v are set to None,
        the aligned region will result in a square region.
    :type size_u: (float, optional)
    :param size_v: The length of the V axis of the aligned region in UV units. If both size_u and size_v are set to None,
        the aligned region will result in a square region.
    :type size_v: (float, optional)
    :return: UV Map
    :rtype: trimatic.UVMap
    :raises: ValueError | Runtime Error (When only one of the two parameters size_u and size_v is None)

    :example:

    .. literalinclude:: example/uv/align_uv_automatic.py
    """

    trimatic.utils.check_type("uv_map", uv_map, trimatic.UVMap)
    if not ((size_u is not None and size_v is not None) or (size_u is None and size_v is None)):
        raise RuntimeError("Parameters size_u and size_v must both be None or not None.")
    if size_u is not None:
        trimatic.utils.check_resolution("size_u", size_u)
    if size_v is not None:
        trimatic.utils.check_resolution("size_v", size_v)

    return pymatic.align_uv_automatic(uv_map, size_u, size_v)
