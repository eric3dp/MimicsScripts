import pymatic
import trimatic.utils
from enum import Enum

class CADLinkFormat(Enum):
    """CAD Formats."""

    step = "step"
    igs = "igs"

class CADLinkPatchDensityType(Enum):
    """Patch Decomposition Types."""

    none = 0
    adaptive = 1
    low = 2
    below_normal = 3
    normal = 4
    above_normal = 5
    high = 6
    
class CADLinkAnalyticalStructures(Enum):
    """Analytical Structures"""
    
    """Split closed analytical surfaces into two faces (no seam)."""
    split = 0
    
    """Single surface with a seam."""
    seam = 1
    
    """Single surface with slit contours."""
    slit = 2

def cadlink_quad_dominant(*args,#'force named parameters'
                          entity, format=CADLinkFormat.step, output_directory, nurbs_only=False, border_tolerance=None,
                          analytical_structures=CADLinkAnalyticalStructures.slit, preserve_surface_structure=True,
                          improve_mesh=True, patch_size=None, number_of_control_points=None, smoothing_strength=0.0):
    """The CAD link module makes it possible to convert a triangulated mesh to an Iges or Step file using Quad dominant method.
    
    :param entity: part to convert.
    :type entity: trimatic.Part
    :param format: CAD file format, igs or step.
    :type format: trimatic.CADLinkFormat, optional
    :param output_directory: Destination path to save the CAD file.
    :type output_directory: string
    :param nurbs_only: When True, all surfaces will be converted to NURBS surfaces. 
        When False, the opertion will first search for a match of the triangulated surfaces with an analytical primitive like a plane, cylinder etc.
    :type nurbs_only: bool, optional    
    :param border_tolerance: The border tolerance is the tolerance with which the file is read.     
        When two points are further apart than this tolerance, they are considered to be 2 different points.     
        When they are closer to each other as the defined tolerance, they are considered to fall together.     
        When None is specified, tolerance will be estimated automatically (Like "Estimate" button in GUI).
    :type border_tolerance: float, optional
    :param analytical_structures: Trimming loop representation for closed analytical surfaces.
    :type analytical_structures: trimatic.CADLinkAnalyticalStructures, optional
    :param preserve_surface_structure: Specifies whether the surface structure should be preserved or not.
    :type preserve_surface_structure: bool, optional
    :param improve_mesh: Specifies whether or not the mesh improving shall be performed before reverse (recommended).
    :type improve_mesh: bool, optional
    :param patch_size: Desired edge length for decomposition via quadrangulation algorithm.
    :type patch_size: float, optional
    :param number_of_control_points: Number of control points. If None, then estimate automatically.
    :type number_of_control_points: integer, optional
    :param smoothing_strength: Strength of NURBS surfaces smoothing. Value from 0 to 1.
    :type smoothing_strength: float, optional    
    :return: Names of written file.
    :rtype: string
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/cadlink/cadlink_quad_dominant.py
    """

    trimatic.utils.check_type("entity", entity, (trimatic.Part))
    trimatic.utils.check_folder_path_is_valid(output_directory)
    if patch_size is not None:
        trimatic.utils.check_param_greater("patch_size", patch_size, 0.0)
    if border_tolerance is not None:
        trimatic.utils.check_param_greater("tolerance", border_tolerance, 0.0)
    if number_of_control_points is not None:
        trimatic.utils.check_param_greater("number_of_control_points", number_of_control_points, 0)
    trimatic.utils.check_param_in_range("smoothing_strength", smoothing_strength, 0.0, 1.0)
    return pymatic.cadlink(entity, format.value, output_directory, nurbs_only, border_tolerance, analytical_structures.value, 
                           preserve_surface_structure, improve_mesh, patch_size, CADLinkPatchDensityType.adaptive.value,
                           number_of_control_points, smoothing_strength)

def cadlink_voronoi_based(*args,#'force named parameters'
                          entity, format=CADLinkFormat.step, output_directory, nurbs_only=False, border_tolerance=None,
                          analytical_structures=CADLinkAnalyticalStructures.slit, preserve_surface_structure=True,
                          improve_mesh=True, patch_density=CADLinkPatchDensityType.adaptive, number_of_control_points=None, smoothing_strength=0.0):
    """The CAD link module makes it possible to convert a triangulated mesh to an Iges or Step file using Voronoi based patching method.
    
    :param entity: part to convert.
    :type entity: trimatic.Part
    :param format: CAD file format, igs or step.
    :type format: trimatic.CADLinkFormat, optional
    :param output_directory: Destination path to save the CAD file.
    :type output_directory: string
    :param nurbs_only: When True, all surfaces will be converted to NURBS surfaces. 
        When False, the opertion will first search for a match of the triangulated surfaces with an analytical primitive like a plane, cylinder etc.
    :type nurbs_only: bool, optional    
    :param border_tolerance: The border tolerance is the tolerance with which the file is read.     
        When two points are further apart than this tolerance, they are considered to be 2 different points.     
        When they are closer to each other as the defined tolerance, they are considered to fall together.     
        When None is specified, tolerance will be estimated automatically (Like "Estimate" button in GUI).
    :type border_tolerance: float, optional
    :param analytical_structures: Trimming loop representation for closed analytical surfaces.
    :type analytical_structures: trimatic.CADLinkAnalyticalStructures, optional
    :param preserve_surface_structure: Specifies whether the surface structure should be preserved or not.
    :type preserve_surface_structure: bool, optional
    :param improve_mesh: Specifies whether or not the mesh improving shall be performed before reverse (recommended).
    :type improve_mesh: bool, optional
    :param patch_density: Recommended density of resulting parametric faces. Used with regular decomposition method only. 
        It is called 'recommended density' because it can contradict the reversing tolerance parameter that is considered as a superior one.
        The default 'adaptive' value is used to vary patch density depending on mesh curvature.
        Other possible value can be None, Low, Below normal, Normal, Above normal, or High.  
        If None, reverse must be performed as a single patch in this case.
    :type patch_density: trimatic.CADLinkPatchDecompositionType, optional
    :param number_of_control_points: Number of control points. If None, then estimate automatically.
    :type number_of_control_points: int, optional
    :param smoothing_strength: Strength of NURBS surfaces smoothing. Value from 0 to 1.
    :type smoothing_strength: float, optional    
    :return: Names of written file.
    :rtype: string
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/cadlink/cadlink_voronoi_based.py
    """


    trimatic.utils.check_folder_path_is_valid(output_directory)
    if border_tolerance is not None:
        trimatic.utils.check_param_greater("tolerance", border_tolerance, 0.0)
    if number_of_control_points is not None:
        trimatic.utils.check_param_greater("number_of_control_points", number_of_control_points, 0)
    trimatic.utils.check_param_in_range("smoothing_strength", smoothing_strength, 0.0, 1.0)
    return pymatic.cadlink(entity, format.value, output_directory, nurbs_only, border_tolerance, analytical_structures.value, 
                           preserve_surface_structure, improve_mesh, None, patch_density.value,
                           number_of_control_points, smoothing_strength)