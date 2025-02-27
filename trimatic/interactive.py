import pymatic
import trimatic.utils

from enum import Enum

def activate_translate_rotate(main_entity = None, 
                              move_along_entities = None,
                              translation_step = None,
                              rotation_step = None):
    """Translate and (or) rotate objects.

    :param main_entity: Entity to be transformed. 
    :type main_entity: trimatic.Object
    :param move_along_entities: List of entities to move along.
    :type move_along_entities: trimatic.Object | [trimatic.Object] | (trimatic.Object)
    :param translation_step: The translation will be done in steps of this distance.
    :type translation_step: float, optional
    :param rotation_step: The rotation will be done in steps of this angle.
    :type rotation_step: float, optional
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_translate_rotate.py
    """
    if main_entity is not None:
       trimatic.utils.check_type("main_entity", main_entity, trimatic.utils.transformable_types())
       
    if move_along_entities is not None:
       trimatic.utils.check_type("move_along_entities", move_along_entities, trimatic.utils.transformable_types())
    
    if translation_step is not None:
        trimatic.utils.check_param_greater("translation_step", translation_step, 0.0)
        
    if rotation_step is not None:
        trimatic.utils.check_param_greater("rotation_step", rotation_step, 0.0)
        

    
    return pymatic.activate_translate_rotate(main_entity,
                                             trimatic.utils.single_or_multiple_entities(move_along_entities),
                                             translation_step, 
                                             rotation_step)

def activate_mark_freeform_area(mark_flipped_triangles = True, target_surfaces = None):
    """Mark triangles within a freely drawn area.
    
    :param mark_flipped_triangles: When False, triangles with an inverted normal will not be marked.
    :type mark_flipped_triangles: bool, optional
    :param target_surfaces: Surface(s) which contain the triangles that you want to be marked.
    :type target_surfaces: trimatic.Surface | [trimatic.Surface], optional
    :return: Marked triangles.
    :rtype: (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_mark_freeform_area.py
    """
    if target_surfaces is not None:
        trimatic.utils.check_type("target_surfaces", target_surfaces, (trimatic.Surface))

    
    return pymatic.activate_mark_freeform_area(mark_flipped_triangles, trimatic.utils.single_or_multiple_entities(target_surfaces))

def activate_mark_smooth_region(angle_deviation = 5.0, mark_across_surfaces = True):
    """Mark triangles within a smooth region.
    
    :param angle_deviation: This angle defines which triangles next to the already marked triangle(s) also become marked, based on their angle with respect to the already marked triangle.
    :type angle_deviation: float, optional
    :param mark_across_surfaces: When True, the marking is not limited to one surface.
    :type mark_across_surfaces: bool, optional
    :return: Marked triangles.
    :rtype: (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_mark_smooth_region.py
    """

    
    return pymatic.activate_mark_smooth_region(angle_deviation, mark_across_surfaces)

def activate_mark_shell():
    """All triangles belonging to the same shell are marked.
    
    :return: Marked triangles.
    :rtype: (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_mark_shell.py
    """

    
    return pymatic.activate_mark_shell()

def activate_mark_wave_brush(diameter = 10.0, mark_flipped_triangles = True, target_surfaces = None):
    """Mark triangles with a wave brush.
    
    :param diameter: Diameter of the brush.
    :type diameter: float, optional
    :param mark_flipped_triangles: If True, it is possible to mark from the backface of triangles.
    :type mark_flipped_triangles: bool, optional
    :param target_surfaces: Surface(s) which contain the triangles that you want to be marked by the brush.
    :type target_surfaces: trimatic.Surface | [trimatic.Surface], optional
    :return: Marked triangles.
    :rtype: (trimatic.MarkedTriangles)
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_mark_wave_brush.py
    """
    trimatic.utils.check_param_greater("diameter", diameter, 0.0)
    if target_surfaces is not None:
        trimatic.utils.check_type("target_surfaces", target_surfaces, (trimatic.Surface))

    
    return pymatic.activate_mark_wave_brush(diameter, mark_flipped_triangles, trimatic.utils.single_or_multiple_entities(target_surfaces))

def get_selection():
    """ Gets the currently selected entities in the object tree.

    :return: The tuple of currently selected entities.
    :rtype: (trimatic.Object)
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/interactive/get_selection.py
    """

    return pymatic.get_selection()

def indicate_coordinate():
    """ Allows users to create a point in the 3D area. Filter options in the work area can be used for specific point selection.

    :return: Coordinates of the indicated point.
    :rtype: (float, float, float)
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/interactive/indicate_coordinate.py
    """

    return pymatic.indicate_coordinate()

def message_box(message, title, with_cancel = True):
    """ Pops up a non-blocking (modeless) messagebox that pauzes the script and gives control back to 3-matic. 
    After the user presses OK or Cancel, the script will continue.

    :param message:  Message text in the box.
    :type message: string

    :param title: Title for the messagebox.
    :type title: string

    :param with_cancel: When true, the message box will show OK. When False, the messagebox will show cancel.
    :type with_cancel: bool, optional

    :return: True when user pressed OK, False when user pressed Cancel.
    :rtype: bool

    :example:

    .. literalinclude:: example/interactive/message_box.py
    """

    return pymatic.message_box(message, title, with_cancel)

def suspend_progress():
    """ Prevents "Executing python script' progress bar popping up when running python script. Useful when requesting users input, for example in a PyQT window.

    :return: Successful or not.
    :rtype: bool
    """

    return pymatic.suspend_progress()

def resume_progress():
    """ Resumes "Executing python script' progress bar popping up when running python script.

    :return: Successful or not.
    :rtype: bool
    """

    return pymatic.resume_progress()

def set_selection(entities):
    """ Sets the selection in the object tree to the specified entities.

    :param entities: Either single entity or a list of entities.
    :type entities: trimatic.Object | [trimatic.Object]
    :return: Successful or not
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/interactive/set_selection.py
    """

    return pymatic.set_selection(trimatic.utils.single_or_multiple_entities(entities))
    
    
def activate_local_smoothing(diameter=None, smooth_factor=1.0, target_entity=None):
    """This operation will smooth entities interactively by re-positioning the triangle nodes & triangle edges.
    
    :param diameter: The diameter size for smoothing. If no diameter is provided, the diameter is determined by the camera position. 
    :type diameter: float, optional
    :param smooth_factor: Strength of the smoothing. 
    :type smooth_factor: float, optional
    :param target_entity: Part/surface to be smoothed. If no target entity is provided, all visible entities within the smoothing diameter are smoothed. 
    :type target_entity: trimatic.Surface | trimatic.Part, optional
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_local_smoothing.py
    """
    if diameter is not None:
       trimatic.utils.check_param_greater("diameter", diameter, 0.0)
    trimatic.utils.check_param_in_range("smooth_factor", smooth_factor, 0.1, 1.0)
    if target_entity is not None:
       trimatic.utils.check_type("target_entity", target_entity, (trimatic.Surface, trimatic.Part))
    
    return pymatic.activate_local_smoothing(diameter, smooth_factor, target_entity)

class TrimMethod(Enum):
    """Trim method for trim."""

    remove_inner = "Remove inner"
    """The area inside the trimming outline is removed."""

    remove_outer = "Remove outer"
    """The area outside the trimming outline is removed."""

    preserve_inner_and_outer = "Preserve inner and outer"
    """Part will be cut along the trimming outline."""

def activate_trim(entities, trim_method = TrimMethod.remove_inner, fillet_radius = None):
    """Trims off excess material of parts.

    :param entities: Parts to be trimmed.
    :type entities: trimatic.Part | [trimatic.Part]
    :param trim_method: Method to determine whether the area inside and/or outside the trimming outline will be retained.
    :type trim_method: trimatic.TrimMethod, optional
    :param fillet_radius: Defines the fillet radius added on the corners of the trimming outline.
    :type fillet_radius: float, optional
    :raises: RuntimeError, ValueError
    :example:

    .. literalinclude:: example/interactive/activate_trim.py
    """

    trimatic.utils.check_type("entities", entities, (trimatic.Part,))
    trimatic.utils.check_type("trim_method", trim_method, (TrimMethod,))

    if fillet_radius is not None:
        trimatic.utils.check_param_greater("fillet_radius", fillet_radius, 0.0)

    return pymatic.activate_trim(trimatic.utils.single_or_multiple_entities(entities), trim_method.value, fillet_radius)
