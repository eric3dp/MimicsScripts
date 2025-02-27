import pymatic
import trimatic
import math
import os
import sys
from numbers import Number
from enum import Enum


def get_resolution():
    return 0.0001

def get_zero_vector():
    return (0, 0, 0)

def check_param_not_equal(name, value, comparison_value):
    if (value == comparison_value):
        raise ValueError("Parameter " + name + " should not be equal to " + str(comparison_value) + ".")

def check_param_greater(name, value, minimum):
    if value <= minimum:
        raise ValueError("Parameter " + name + " should be greater than " + str(minimum) + ".")

def check_param_greater_or_equal(name, value, minimum):
    if value < minimum:
        raise ValueError("Parameter " + name + " should be greater than or equal to " + str(minimum) + ".")


def check_param_smaller_or_equal(name, value, maximum):
    if value > maximum:
        raise ValueError("Parameter " + name + " should be smaller than or equal to " + str(maximum) + ".")


def check_param_in_range(name, value, minimum, maximum):
    if not (minimum <= value <= maximum):
        raise ValueError("Parameter " + name + " should be in the range from " + str(minimum) + " to " + str(maximum) + ".")


def check_param_between(name, value, minimum, maximum):
    if not (minimum < value < maximum):
        raise ValueError("Parameter " + name + " should be between " + str(minimum) + " to " + str(maximum) + ".")


def check_valid_name(name, value, list):
    if not (value in list):
        raise ValueError("Invalid/misspelled " + name + " is used" + ".")


def check_parameters_dependency(condition_param_name, dependant_param_name, condition_value, param_value):
    if (param_value and not condition_value):
        raise ValueError("Parameter " + dependant_param_name + " cannot be true if " + condition_param_name + " is not true" + ".")


def check_resolution(name, value):
    check_param_greater_or_equal(name, value, get_resolution())


def check_vector_not_equal(name, value, forbidden_value):
    if value == forbidden_value:
        raise ValueError("Parameter " + name + " cannot take the value of " + str(forbidden_value) + ".")


def check_entity_sets_do_not_contain_equal_entities(name1, name2, entity_set1, entity_set2):
    pymatic_entities1 = single_or_multiple_entities(entity_set1)
    pymatic_entities2 = single_or_multiple_entities(entity_set2)
    for entity in pymatic_entities1:
        if entity in pymatic_entities2:
            raise ValueError("Parameter " + name2 + " contains an entity that is already in " + name1 + ".")


def check_entities_does_not_have_part_and_one_of_its_surfaces(name, entities):
    pymatic_entities = single_or_multiple_entities(entities)
    surface_entities = []
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Surface):
            surface_entities.append(entity)
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Part):
            part_surfaces = entity.find_surfaces(".*")
            for part_surface in part_surfaces:
                if part_surface in surface_entities:
                    raise ValueError("Parameter " + name + " cannot contain a part and its surface")

def check_entity_set_does_not_have_surface_or_surface_set_of_another_entity_set(name1, name2, entity_set1, entity_set2):
    pymatic_entities1 = single_or_multiple_entities(entity_set1)
    pymatic_entities2 = single_or_multiple_entities(entity_set2)
    for entity1 in pymatic_entities1:
        if isinstance(entity1, trimatic.Part) or isinstance(entity1, trimatic.SurfaceSet):
            surfaces = entity1.get_surfaces()
            surface_sets = entity1.get_surface_sets()
            for entity2 in pymatic_entities2:
                if isinstance(entity2, trimatic.Surface) and entity2 in surfaces:
                    raise ValueError("Parameter " + name1 + " contains an item from the entity that is already in " + name2 + ".")
                elif isinstance(entity2, trimatic.SurfaceSet) and entity2 in surface_sets:
                    raise ValueError("Parameter " + name1 + " contains an item from the entity that is already in " + name2 + ".")                

def check_entities_only_contain_fully_attached_curves(name, entities, allow_none_or_empty = False):
    if allow_none_or_empty:
        if entities is None:
            return True
    pymatic_entities = single_or_multiple_entities(entities)
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Curve) and not entity.fully_attached:
            raise ValueError("Parameter " + name + " cannot contain curves which are not fully attached")

def check_entities_only_contain_open_curves(name, entities):
    pymatic_entities = single_or_multiple_entities(entities)
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Curve) and entity.closed:
            raise ValueError("Parameter " + name + " cannot contain closed curves")

def check_entities_only_contain_closed_curves(name, entities):
    pymatic_entities = single_or_multiple_entities(entities)
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Curve) and not entity.closed:
            raise ValueError("Parameter " + name + " cannot contain open curves")


def check_part_has_surface(name, entities):
    pymatic_entities = single_or_multiple_entities(entities)
    for entity in pymatic_entities:
        if isinstance(entity, trimatic.Part):
            try:
                entity.find_surfaces(".*")
            except ValueError:
                raise ValueError("Parameter " + name + " contains part without surface")


def check_entities_must_be_multiple(name, entities):
    if len(single_or_multiple_entities(entities)) <= 1:
        raise ValueError("Parameter " + name + " requires two or more entities")


def check_points_not_collinear(point0, point1, point2):
    v1 = [point1[0] - point0[0], point1[1] - point0[1], point1[2] - point0[2]]
    v2 = [point2[0] - point0[0], point2[1] - point0[1], point2[2] - point0[2]]
    cross = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
    length = math.sqrt(cross[0] * cross[0] + cross[1] * cross[1] + cross[2] * cross[2])
    if (length <= get_resolution()):
        raise ValueError("Point0, point1 and point2 should not be collinear (form a line)")


def check_2points_not_coincident(name0, name1, point0, point1):
    if point0 == point1:
        raise ValueError("Parameter " + name0 + " and " + name1 + " should not be coincident")


def check_3points_not_coincident(name0, name1, name2, point0, point1, point2):
    check_2points_not_coincident(name0, name1, point0, point1)
    check_2points_not_coincident(name1, name2, point1, point2)
    check_2points_not_coincident(name0, name2, point0, point2)


def check_file_type(filename, extensions):
    allowed_extensions = single_or_multiple_entities(extensions)
    file_extension = os.path.splitext(filename)
    if file_extension[1] not in allowed_extensions:
        error_msg = "Not a valid file type " + " ,".join(extensions) + " files are supported only."
        raise ValueError(error_msg)

def check_direction(name, point):
    if point == get_zero_vector():
        raise ValueError("Parameter " + name + " is not a valid direction")

def check_type(name, entities, allowed_type_tuple, allow_none_or_empty = False ):
    if allow_none_or_empty:
        if entities is None:
            return True
    else:
        if entities is None:
            raise ValueError("Parameter " + name + " can not be None.")
        if not entities:
            raise ValueError("Parameter " + name + " can't be empty.")
    pymatic_entities = single_or_multiple_entities(entities)
    pymatic_allowed_type_tuple = single_or_multiple_entities(allowed_type_tuple)
    raise_error = False
    warning = ""
    num_of_entities = len(pymatic_entities)
    type_enumeration = make_type_enumeration_string(pymatic_allowed_type_tuple)
    if num_of_entities == 1:
        if not isinstance(pymatic_entities[0], pymatic_allowed_type_tuple):
            raise_error = True
            warning = "Parameter " + name + "(" + str(pymatic_entities[0]) + ") does not have the right type , use a " + type_enumeration
    else:
        for i in range(num_of_entities):
            if not isinstance(pymatic_entities[i], pymatic_allowed_type_tuple):
                raise_error = True
                warning = "Parameter " + name + "(" + str(pymatic_entities[i]) + ") does not have the right type at index " + str(i) + ", use a " + type_enumeration
    if raise_error:
        raise ValueError(warning)

def check_type_is_not(name, entities, type_not_allowed_tuple):
    pymatic_entities = single_or_multiple_entities(entities)
    pymatic_not_allowed_type_tuple = single_or_multiple_entities(type_not_allowed_tuple)
    raise_error = False
    warning = ""
    num_of_entities = len(pymatic_entities)
    type_enumeration = make_type_enumeration_string(pymatic_not_allowed_type_tuple)
    if num_of_entities == 1:
        if isinstance(pymatic_entities[0], pymatic_not_allowed_type_tuple):
            raise_error = True
            warning = "Parameter " + name + "(" + str(pymatic_entities[0]) + ") does not have the right type , " + type_enumeration + " is not allowed"
    else:
        for i in range(num_of_entities):
            if isinstance(pymatic_entities[i], pymatic_not_allowed_type_tuple):
                raise_error = True
                warning = "Parameter " + name + "(" + str(pymatic_entities[i]) + ") does not have the right type at index " + str(i) + ", " + type_enumeration +" is not allowed"
    if raise_error:
        raise ValueError(warning)

def analytical_primitive_types():
    return (trimatic.Point,
           trimatic.Line,
           trimatic.Arc,
           trimatic.Plane,
           trimatic.Cylinder,
           trimatic.Cone,
           trimatic.Sphere)

def root_level_types():
    return analytical_primitive_types() + (trimatic.Part,) + (trimatic.Sketch,) + (trimatic.SSM,)

def transformable_types():
    return analytical_primitive_types() + (trimatic.Part,) + (trimatic.Sketch,) + (trimatic.SSM,)

def single_or_multiple_entities(entities):
    if entities is None:
        return None
    if isinstance(entities, trimatic.Point):  # something special for point because it is iteratable
        return (entities,)
    try:
        return tuple(entities)
    except TypeError:
        # single item
        return (entities,)

def point_argument(point):
    ok = True
    try:
        point_as_tuple = tuple(point)
        if len(point_as_tuple) == 3:
            if 'numpy' in sys.modules:
                #convert numpy types to regular ones to avoid various issues (https://stackoverflow.com/questions/9452775/converting-numpy-dtypes-to-native-python-types)
                #something goes wrong when using numpy for numpy.int32
                #something goes wrong when using numpy via external IDE for numpy.float64
                import numpy
                point_as_list = list(point_as_tuple)
                for i in range(3):
                        if type(point_as_list[i]) is numpy.float64 or type(point_as_list[i]) is numpy.int32:
                            point_as_list[i] = point_as_list[i].item()
                point_as_tuple = tuple(point_as_list)
        else:
            ok = False
    except:
        ok = False
    if not ok:
        raise ValueError('point argument should be convertible to tuple of size 3')
    return point_as_tuple

def point_sequence_argument(points):
    if points is None:
        return None
    else:
        return tuple( point_argument(point) for point in points)

def check_file_saveable(filename):
    # empty filename or only whitespace not allowed
    # filename without extension (e.g. .mxp) not allowed
    # get filename only (no path)
    basename = os.path.basename(filename)
    # split filename & extension
    [filename_only, ext]= os.path.splitext(basename)
    filename_only = filename_only.strip()
    
    if len(filename_only) == 0:
        return False
    #for .mxp, splitext will return .mxp as filename and empty extension
    if filename_only.find('.') >= 0 and len(ext) == 0:
        return False
    if os.path.isfile(filename):
        # existing file
        try:
            fp = open(filename, mode='a')
            fp.close()
        except:
            return False
    else:
        # new file, can it be created (valid file name, writable location)?
        try:
            fp = open(filename, mode='w')
            fp.close()
            os.remove(filename)
        except:
            return False
    return True

def make_type_enumeration_string(type_tuple):
    type_enumeration = ""
    num_of_types = len(type_tuple)
    for i in range(num_of_types):
        if i == (num_of_types - 2):
            type_enumeration = type_enumeration + str(type_tuple[i]) + " or "
        elif i == (num_of_types - 1):
            type_enumeration = type_enumeration + str(type_tuple[i]) + "."
        else:
            type_enumeration = type_enumeration + str(type_tuple[i]) + ", "
    return type_enumeration

def check_folder_path_is_valid(directory):
    if not isinstance(directory, str) or not os.path.isdir(directory):
       raise ValueError("Invalid Directory")
       
def check_and_return_tuple_of_vertices_and_indices(vertices, indices):

    if not isinstance(vertices, tuple) and not isinstance(vertices, list):
        raise ValueError("Invalid Vertices: Expected list or tuple of vertices")
    if not isinstance(indices, tuple) and not isinstance(indices, list):
        raise ValueError("Invalid Indices: Expected list or tuple of indices")

    no_of_vertices = len(vertices)

    if no_of_vertices < 3:
        raise ValueError("Expected at least 3 vertices")

    if len(indices) <= 0:
        raise ValueError("Indices cannot be empty")

    if isinstance(vertices, list):
       vertices = tuple(vertices)
    if isinstance(indices, list):
       indices = tuple(indices)

    return vertices, indices

def check_and_return_tuple_of_create_part_surfaces(surfaces):

    if not isinstance(surfaces, list) and not isinstance(surfaces, tuple):
        raise ValueError("Invalid Surfaces: Expected list or tuple of surfaces")

    if len(surfaces) == 0:
        raise ValueError("Surfaces cannot be empty")

    if isinstance(surfaces, tuple):
        surfaces = list(surfaces)

    for surface_idx in range(len(surfaces)):
        if not isinstance(surfaces[surface_idx], list) and not isinstance(surfaces[surface_idx], tuple):
            raise ValueError("Invalid Vertices: Expected list or tuple containing surface data")
        if len(surfaces[surface_idx]) != 3:
            raise ValueError("Surface data: Expected 3 elements")

        if not isinstance(surfaces[surface_idx][2], str):
            raise ValueError("Expected surface name as string")

        surfaces[surface_idx] = list(surfaces[surface_idx])

        vertices, indices = check_and_return_tuple_of_vertices_and_indices(surfaces[surface_idx][0],
                                                                           surfaces[surface_idx][1])

        surfaces[surface_idx][0] = vertices
        surfaces[surface_idx][1] = indices
        surfaces[surface_idx] = tuple(surfaces[surface_idx])

    surfaces = tuple(surfaces)
    return surfaces


# Tuple of Tuples Constraints
class TOT_Constraint(Enum):
    """Constraint Type."""

    GT_ZERO = 'greater than zero'
    GT_EQ_ZERO = 'greater than or equal to zero'
    NT_EQ_ZERO = 'not equal to zero'
    LT_ZERO = 'less than zero'
    LT_EQ_ZERO = 'less than or equalt to zero'
    CHECK_RESOLUTION_GT_EQ = 'greater than or equal to '+ str(get_resolution())
    NOT_NONE = 'not None'

def ensure_constraint(i_value, i_constraint):
    if i_constraint == TOT_Constraint.GT_ZERO:
        return i_value > 0
    if i_constraint == TOT_Constraint.GT_EQ_ZERO:
        return i_value >= 0
    if i_constraint == TOT_Constraint.NT_EQ_ZERO:
        return i_value != 0
    if i_constraint == TOT_Constraint.LT_ZERO:
        return i_value < 0
    if i_constraint == TOT_Constraint.LT_EQ_ZERO:
        return i_value <= 0
    if i_constraint == TOT_Constraint.CHECK_RESOLUTION_GT_EQ:
        return i_value >= get_resolution()
    if i_constraint == TOT_Constraint.NOT_NONE:
        return not i_value is None
    return False

def are_constraints_and_types_for_same_object_type(i_type, i_constraints):
    if len(i_type) != len(i_constraints):
        return False
    return True

def check_at_least_one_of_type(name, i_entities, i_type):
    """Check and validate: there is at least one object of specified type"""

    for entity in i_entities:
        if isinstance(entity, i_type):
            return
    raise TypeError('Parameter ' +  name + ' ( ' + str(i_entities) + ' ) must contain at least one item that belongs to type ( ' + str(i_type) + ' ).')

def check_type_tuple_of_tuples(name, i_object, i_type, i_constraints=None):
    """Check and validate: the type of tuple. Use only second level of nesting Ex:((tuple,),)"""

    # passed object and type must be tuple
    if type(i_object)!=tuple or type(i_type)!= tuple:
        raise TypeError('Parameter ' +  name + ' ( ' + str(i_object) + ' ) and it\'s type ( ' + str(i_type) + ' ) need to be tuple.')

    if i_constraints and len(i_type)!=len(i_constraints):
        raise TypeError('Parameter ' +  name + ' type does not match with the constraints.')

    for obj in i_object:
        if len(obj)!=len(i_type):
            # number of items in every tuple should match with type passed.
            raise TypeError('Parameter ' + name + ' ( ' + str(obj) + ' ) is not of type ( '+ str(i_type) +' ).')
        # check every item individually for type matching
        for idx in range(len(i_type)):
            if not isinstance(obj[idx], i_type[idx]):
                raise TypeError('Parameter ' + name + ' ( ' + str(obj[idx]) + ' ) is not of type ( ' + str(i_type[idx]) + ' ).')
            if i_constraints and i_constraints[idx] and not ensure_constraint(obj[idx], i_constraints[idx]):
                raise ValueError('Parameter ' + name + ' ( ' + str(obj[idx]) + ' ) expected ' + i_constraints[idx].value + '.')
