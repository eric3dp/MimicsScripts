import pymatic
import trimatic.utils
from collections.abc import Callable


# ----- subscribe -----
def obj_created_subscribe(callable_object):
    """Subscribe to object created callback notification.

    :param callable_object: User defined function
    :type callable_object: Callable
    :return: True if callback notification was successfully subscribed.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/subscription/obj_created_subscribe.py
    """

    trimatic.utils.check_type("callback", callable_object, (Callable)) 
    return pymatic.obj_created_subscribe(callable_object)

def obj_deleted_subscribe(callable_object):
    """Subscribe to object deleted callback notification.

    :param callable_object: User defined function
    :type callable_object: Callable
    :return: True if callback notification was successfully subscribed.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/subscription/obj_deleted_subscribe.py
    """

    trimatic.utils.check_type("callback", callable_object, (Callable)) 
    return pymatic.obj_deleted_subscribe(callable_object)

def obj_label_changed_subscribe(callable_object):
    """Subscribe to object renamed callback notification.

    :param callable_object: User defined function
    :type callable_object: Callable
    :return: True if callback notification was successfully subscribed.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/subscription/obj_label_changed_subscribe.py
    """

    trimatic.utils.check_type("callback", callable_object, (Callable)) 
    return pymatic.obj_label_changed_subscribe(callable_object)

def obj_visual_state_changed_subscribe(callable_object):
    """Subscribe to object visual state changed callback notification.

    :param callable_object: User defined function
    :type callable_object: Callable
    :return: True if callback notification was successfully subscribed.
    :rtype: bool
    :raises: RuntimeError, ValueError

    :example:

    .. literalinclude:: example/subscription/obj_visual_state_changed_subscribe.py
    """

    trimatic.utils.check_type("callback", callable_object, (Callable)) 
    return pymatic.obj_visual_state_changed_subscribe(callable_object)


# ----- unsubscribe -----
def obj_created_unsubscribe():
    """Unsubscribe from object created callback notification.

    :return: True if callback notification was successfully unsubscribed.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_created_unsubscribe.py
    """

    return pymatic.obj_created_unsubscribe()

def obj_deleted_unsubscribe():
    """Unsubscribe from object deleted callback notification.

    :return: True if callback notification was successfully unsubscribed.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_deleted_unsubscribe.py
    """

    return pymatic.obj_deleted_unsubscribe()

def obj_label_changed_unsubscribe():
    """Unsubscribe from object renamed callback notification.

    :return: True if callback notification was successfully unsubscribed.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_label_changed_unsubscribe.py
    """

    return pymatic.obj_label_changed_unsubscribe()

def obj_visual_state_changed_unsubscribe():
    """Unsubscribe from object visual state changed callback notification.

    :return: True if callback notification was successfully unsubscribed.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_visual_state_changed_unsubscribe.py
    """

    return pymatic.obj_visual_state_changed_unsubscribe()


# ----- status -----
def obj_created_status():
    """Check subscription status for object created callback notification.

    :return: True if subscribed to callback notification.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_created_status.py
    """

    return pymatic.obj_created_status()

def obj_deleted_status():
    """Check subscription status for object deleted callback notification.

    :return: True if subscribed to callback notification.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_deleted_status.py
    """

    return pymatic.obj_deleted_status()

def obj_label_changed_status():
    """Check subscription status for object label changed callback notification.

    :return: True if subscribed to callback notification.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_label_changed_status.py
    """

    return pymatic.obj_label_changed_status()

def obj_visual_state_changed_status():
    """Check subscription status for object visual state changed callback notification.

    :return: True if subscribed to callback notification.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/subscription/obj_visual_state_changed_status.py
    """

    return pymatic.obj_visual_state_changed_status()