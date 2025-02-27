import pymatic

def suspend_logging():
    """Suspend logger messages in the logger window.

    :return: True if logging suspended successfully.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/logging/suspend_logging.py
    """


    return pymatic.suspend_logging()

def resume_logging():
    """Resume logger messages in the logger window.

    :return: True if logging resumed successfully.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/logging/resume_logging.py
    """


    return pymatic.resume_logging()
