import pymatic
import trimatic.utils

from enum import Enum

def get_view():
    """Returns the view direction from the 3D view. 

    :return: Tuple of 2 vectors. The view vector and view up vector.
    :rtype: ((float, float, float), (float, float, float))
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/view/get_view.py
    """



    return pymatic.get_view()

def view_custom(view_vector, up_vector):
    """Sets the 3D view to a custom view direction. View is zoomed such that all objects are visible ("Unzoom All").

    :param view_vector: view_vector is an eye vector, this vector is orthogonal to the screen and directed from the user. If passed vectors are not orthogonal, up_vector is set as orthogonal to view_vector in the plane determined by up and view vectors.
    :type view_vector: trimatic.Point
    :param up_vector: up_vector is aligned with Y-axis (bottom to top) of the window.
    :type up_vector: trimatic.Point
    :return: Operation successfull or not.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/view/view_custom.py
    """


    py_view_vector= trimatic.utils.point_argument(view_vector)
    trimatic.utils.check_direction("view_vector", py_view_vector)

    py_up_vector = trimatic.utils.point_argument(up_vector)
    trimatic.utils.check_direction("up_vector", py_up_vector)

    return pymatic.view_custom(py_view_vector,py_up_vector)

def zoom(entities):
    """ Zoom the view in such a way that the specified entities will be enclosed in the view. The resulting view will be the same as when using "Zoom Selection" in GUI for the specified entities.

    :param entities: Either a single object or list of trimatic.Objects
    :type  entities: trimatic.Object | [trimatic.Object]
    :return: Operation successful or not.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/view/zoom.py
    """


    return pymatic.zoom(trimatic.utils.single_or_multiple_entities(entities))

def show_only(entities):
    """ Zoom and show only the specified entities and hide the non-specified entities.

    Entities refer to all root level entities including groups and subgroups.

    :param entities: Either a single or list of trimatic.Object and/or trimatic.Group
    :type  entities: trimatic.Object | trimatic.Group | [trimatic.Object | trimatic.Group]
    :return: Operation successful or not.
    :rtype: bool
    :raises: ValueError, RuntimeError

    :example:

    .. literalinclude:: example/view/show_only.py
    """


    pymatic_entities = trimatic.utils.single_or_multiple_entities(entities)
    trimatic.utils.check_type("entities", pymatic_entities, (trimatic.Object, trimatic.Group)) 
    trimatic.utils.check_type_is_not("entities", pymatic_entities, (trimatic.Analysis)) 

    return pymatic.show_only(trimatic.utils.single_or_multiple_entities(pymatic_entities))

class DefaultViews(Enum):
    """Default views."""

    Top = "Top"
    Bottom = "Bottom"
    Left = "Left"
    Right = "Right"
    Front = "Front"
    Back = "Back"
    Isometric = "Isometric"

def view_default(view):
    """Sets the 3D view to a predefined view direction. View is zoomed such that all objects are visible ("Unzoom All").

    Top: Direction of visualization is perpendicular to the XY plane, in the Z-direction. 

    Bottom: Direction of visualization is perpendicular to the XY plane, against the Z- direction. 

    Left: Direction of visualization is perpendicular to the YZ plane, in the X-direction. 

    Right: Direction of visualization is perpendicular to the YZ plane, against the X-direction. 

    Front: Direction of visualization is perpendicular to the XZ plane, in the Y-direction. 

    Back: Direction of visualization is perpendicular to the XZ plane, against the Y-direction. 

    Isometric: Direction of visualization is (1,1, -1). 

    :param view: Which view to set.
    :type view: trimatic.DefaultView
    :return: Operation successfull or not.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/view/view_default.py
    """


    trimatic.utils.check_type("view", view, (DefaultViews,))

    return pymatic.view_default(view.value)