import pymatic
import trimatic.utils

def create_group(name, entities=None, parent_group=None):
    """Create a group with a given name and entities.

    :param name: Name of the group.
    :type name: string
    :param entities: Objects to be included in the group. 
    :type entities: trimatic.Object | [trimatic.Object], optional
    :param parent_group: The created group is added as a subgroup of the indicated parent group. 
    :type parent_group: trimatic.Group, optional
    :return: Created group
    :rtype: trimatic.Group
    :raises: ValueError, RuntimeError
    
    :example:

    .. literalinclude:: example/group/create_group.py
    """

    if parent_group:
        trimatic.utils.check_type("parent_group", parent_group, (trimatic.Group))
        return pymatic.create_sub_group(name, trimatic.utils.single_or_multiple_entities(entities), parent_group)
    return pymatic.create_group(name, trimatic.utils.single_or_multiple_entities(entities))
