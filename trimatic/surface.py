import pymatic
import trimatic.utils

def automatic_rectangular_patching(entities, perform_preprocessing = True, low_curvature = True, part_complexity = None, allow_t_junctions = True):
    """The patching operation allows preparing a part before applying the export_iges or export_step operation. 

    :param entities: Part or list of parts to export.
    :type entities: trimatic.Part | [trimatic.Part]
    :param perform_preprocessing: Destination path to save the file(s).
    :type perform_preprocessing: bool, optional
    :param low_curvature: Set to True when the part contains a low curvature. Set to False when the part contains a high curvature.
    :type low_curvature: bool, optional
    :param part_complexity: Value between 1 and 10 to indicate the complexity of a part. The complexity of a part determines the patch density.
                            Higher density will result in a more accurate representation, but more data. 
                            When specifiying None, 3-matic will automatically estimate the complexity of the selected part(s) and use the average complexity.
    :type part_complexity: int, optional

    :param allow_t_junctions: When True, the edge of one patch can be built out of 2 edges of other patches.
    :type allow_t_junctions: bool, optional

    :return: For every input part: 
                            The resulting surfaces grouped into surface sets. 
                            When no patching problems have occurred, only one surface set is returned. 
                            When patching problems have occured, more than one surface set will be returned. The first will contain the successful surfaces, the other ones contain problem surfaces.
    :rtype: ((trimatic.SurfaceSet))
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/surface/automatic_rectangular_patching.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    if part_complexity is not None:
        trimatic.utils.check_param_greater_or_equal("part_complexity", part_complexity, 1)
        trimatic.utils.check_param_smaller_or_equal("part_complexity", part_complexity, 10)

    return pymatic.automatic_rectangular_patching(trimatic.utils.single_or_multiple_entities(entities),  perform_preprocessing, low_curvature, part_complexity, allow_t_junctions )

def estimate_part_complexity(entity):
    """Estimates the part complexity.

    :param entity: Part to estimate.
    :type entity: trimatic.Part

    :return: Value between 1 and 10 to indicate the complexity of a part.
    :rtype: int
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/surface/estimate_part_complexity.py
    """


    trimatic.utils.check_type("entity", entity, (trimatic.Part))

    return pymatic.estimate_part_complexity(entity)

def unfold_surface(entities, seams = None, preserve_surface_connections = False):
    """Performs unfold surface on selected entitites.

    :param entities: Surface(s) to unfold.
    :type entities: trimatic.Surface | trimatic.SurfaceSet | [trimatic.Surface | trimatic.SurfaceSet]
    :param seams: One or multiple attached curve(s) to be used as relaxer cuts in the unfolding.
    :type seams: trimatic.Curve | [trimatic.Curve], optional
    :param preserve_surface_connections: When True, all the existing connections between the selected entities will be preserved.
    :type preserve_surface_connections: bool, optional
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/surface/unfold_surface.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Surface, trimatic.SurfaceSet))
    trimatic.utils.check_type("seams", seams, trimatic.Curve, True)

    return pymatic.unfold_surface(trimatic.utils.single_or_multiple_entities(entities), trimatic.utils.single_or_multiple_entities(seams), preserve_surface_connections)
