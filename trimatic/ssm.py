import pymatic
import trimatic.utils
from enum import Enum

def convert_ssm_instance_to_part(entity, remesh=True, coefficients=()):
    """Converts an SSM instance to part.

    :param entity: SSM instance to convert to part.
    :type entity: trimatic.SSM
    :param remesh: Determines if the SSM instance is remeshed when converted to part.
       By using remesh=False, the node-to-node correspondence between different created instances is preserved.
    :type remesh: bool, optional
    :param coefficients: Coefficient values to define the SSM shape. The number of coefficients must be the same as SSM modes.
    :type coefficients: [float], optional
    :return: Created part from SSM instance.
    :rtype: trimatic.Part
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/adam/convert_ssm_instance_to_part.py
    """


    trimatic.utils.check_type('entity', entity, (trimatic.SSM))
    return pymatic.convert_ssm_instance_to_part(entity, remesh, coefficients)

class SSMAlignmentMethod(Enum):
    """Create SSM alignment method."""

    none = "None"
    """Create SSM without alignment."""

    procrustes = "Procrustes"
    """Create SSM with alignment with procrustes."""

    scaledProcrustes = "Scaled Procrustes"
    """Create SSM with alignment with scaling and procrustes."""

    """ If alignment method not speficied, create SSM will use no scaling and no procrustes option."""

def create_ssm(*args,  
               #'force named parameters'
               entities,              
               number_of_modes = None,
               alignment_method= SSMAlignmentMethod.procrustes):
    """Create a statistical shape model.

    :param entities: List of parts with point correspondence.
    :type entities: [trimatic.Part]
    :param number_of_modes: The number of principal modes retained in the model. If None, the number of modes is equal to the number of entities.
    :type number_of_modes: int, optional
    :param alignment_method: Initial alignment method.
    :type alignment_method: trimatic.SSMAlignmentMethod, optional

    :return: Created SSM
    :rtype: trimatic.SSM
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/adam/create_ssm.py
    """


    trimatic.utils.check_type("entities", entities, (trimatic.Part))
    trimatic.utils.check_entities_must_be_multiple("entities",entities)
    collection_entities = trimatic.utils.single_or_multiple_entities(entities)
    if number_of_modes is not None:
        trimatic.utils.check_param_between("number_of_modes", number_of_modes, 0, len(collection_entities) + 1)
    trimatic.utils.check_type("alignment_method", alignment_method, (SSMAlignmentMethod,), True)
    return pymatic.create_ssm(collection_entities, alignment_method.value, number_of_modes)

def create_ssm_subregion(*args,
                         #'force named parameters'
                         full_ssm,
                         subregion,
                         extend_ssm = False):
    """Create an SSM Subregion
    
    :param full_ssm: The full SSM from which the subregion SSM is created.
    :type full_ssm: trimatic.SSM
    :param subregion: Input part with marked subregion.
    :type subregion: trimatic.Part   
    :param extend_ssm: If True, the full SSM is forced to follow the same mode distribution as the subregion SSM.
    :type extend_ssm: bool, optional

    :return: Created Subregion SSM.
    :rtype: trimatic.SSM
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/adam/create_ssm_subregion.py
    """

    trimatic.utils.check_type("full_ssm", full_ssm, (trimatic.SSM))
    trimatic.utils.check_type("subregion", subregion, (trimatic.Part))
    return pymatic.create_ssm_subregion(full_ssm, subregion, extend_ssm)

def registration_with_scaling(*args, #'force named parameters'
                               fixed_entity,
                               moving_entity,
                               move_along_entities=(),
                               sample_points=15.0,
                               number_of_iterations=10):
    """An iterative closest point registration with isotropic scaling.

    :param fixed_entity: Reference entity to be aligned with.
    :type fixed_entity: trimatic.Part
    :param moving_entity: Entity to align/move.
    :type moving_entity: trimatic.Part
    :param move_along_entities: Either a single object or heterogeneous list of root level entities (parts, analytical primitives) that will be aligned along with the moving entity.
    :type move_along_entities: trimatic.Object | [trimatic.Object], optional
    :param sample_points: The size of the point sample in percentage. A higher value implies more points and thus a higher computation time.
    :type sample_points: float, optional
    :param number_of_iterations: The number of iterations. A higher value results in better quality but increases the computation time.
    :type number_of_iterations: int, optional

    :return: Root mean squared error of deviation between the moving entity and the fixed entity. None if operation failed.
    :rtype: float
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/adam/registration_with_scaling.py
    """

    trimatic.utils.check_type('fixed_entity', fixed_entity, (trimatic.Part,))
    trimatic.utils.check_type('moving_entity', moving_entity, (trimatic.Part,))
    trimatic.utils.check_type('move_along_entities', move_along_entities, trimatic.utils.transformable_types(), True)
    trimatic.utils.check_param_greater_or_equal('number_of_iterations', number_of_iterations, 1)
    trimatic.utils.check_param_in_range('sample_points', sample_points, 1.0, 100.0)

    return pymatic.registration_with_scaling(fixed_entity,
                                             moving_entity,
                                             trimatic.utils.single_or_multiple_entities(move_along_entities),
                                             sample_points,
                                             number_of_iterations)

def warp_part(*args, #'force named parameters'
        fixed_entity,
        moving_entity,
        fixed_landmarks=None,
        moving_landmarks=None,
        number_of_smooth_iteration=50,
        bidirectional_point_correspondence=True,
        bad_contour_correspondence =False,
        triangle_correspondence=True,
        max_stiffness=30.0,
        min_stiffness=5.0,
        max_geometrical_error=0.01,
        max_non_smooth_iterations=300,
        subsample_ratio=0.5,
        convergence_tolerance=0.001,
        normal_constraint_angle=30.0):
    """Adapts the mesh of the moving entity to create point correspondence with the fixed entity.

    :param fixed_entity: Fixed/target entity to be warped with.
    :type fixed_entity: trimatic.Part
    :param moving_entity: Moving/master entity to warp.
    :type moving_entity: trimatic.Part
    :param fixed_landmarks: Landmarks on fixed/target entity.
    :type fixed_landmarks: [(float,float,float)], optional
    :param moving_landmarks: Landmarks on moving/master entity.
    :type moving_landmarks: [(float,float,float)], optional
    :param number_of_smooth_iteration: Number of smooth warping iterations upfront.
    :type number_of_smooth_iteration: int, optional
    :param bidirectional_point_correspondence: When True, search for corresponding points from the moving entity to the fixed entity and from the fixed entity to the moving entity.
    :type bidirectional_point_correspondence: bool, optional
    :param triangle_correspondence: When True, the triangle centers are included in the corresponding point search.
    :type triangle_correspondence: bool, optional
    :param bad_contour_correspondence: When True, the bad contours of the moving and fixed entities will be matched.
    :type bad_contour_correspondence: bool, optional
    :param normal_constraint_angle: The angle [degrees] with which the normal of a corresponding point may deviate.
    :type normal_constraint_angle: float, optional
    :param subsample_ratio: The fraction of points on the moving surface which search for a corresponding point in each iteration.
    :type subsample_ratio: float, optional
    :param max_stiffness: The maximum stiffness determines the maximum strength of the connections between neighbouring points.
    :type max_stiffness: float, optional
    :param min_stiffness: The minimum stiffness determines the minimum strength of the connections between neighbouring points.
    :type min_stiffness: float, optional
    :param max_non_smooth_iterations: The maximum number of iterations after which the algorithm will stop.
    :type max_non_smooth_iterations: int, optional
    :param max_geometrical_error: The maximum geometrical error for the Housdorff distance between the moving surface and the fixed surface.
    :type max_geometrical_error: float, optional
    :param convergence_tolerance: The tolerance for the difference between the Housdorff distance in interation n and iteration n-1 of the warping algorithm.
    :type convergence_tolerance: float, optional

    :return: Created part from the warping operation.
    :rtype: trimatic.Part | (trimatic.Part)
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/adam/warp_part.py
    """

    trimatic.utils.check_type("moving_entity", moving_entity, (trimatic.Part))
    trimatic.utils.check_type("fixed_entity", fixed_entity, (trimatic.Part))
    trimatic.utils.trimatic.utils.check_entity_sets_do_not_contain_equal_entities("moving_entity", "fixed_entity", moving_entity, fixed_entity)
    return pymatic.warp_part(fixed_entity, moving_entity,
                                             trimatic.utils.point_sequence_argument(fixed_landmarks),
                                             trimatic.utils.point_sequence_argument(moving_landmarks),
                                             number_of_smooth_iteration,
                                             bidirectional_point_correspondence, triangle_correspondence,
                                             bad_contour_correspondence, normal_constraint_angle, subsample_ratio,
                                             max_stiffness, min_stiffness, max_non_smooth_iterations,
                                             max_geometrical_error, convergence_tolerance)

