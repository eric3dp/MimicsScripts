import pymatic

def suspend_usage_data_collection():
    """Suspends usage data collection on next launch of 3-matic.

    :return: True if usage data collection suspended successfully.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/preferences/suspend_usage_data_collection.py
    """


    return pymatic.suspend_usage_data_collection()

def resume_usage_data_collection():
    """Resumes usage data collection on next launch of 3-matic.

    :return: True if usage data collection resumed successfully.
    :rtype: bool
    :raises: RuntimeError

    :example:

    .. literalinclude:: example/preferences/resume_usage_data_collection.py
    """


    return pymatic.resume_usage_data_collection()
