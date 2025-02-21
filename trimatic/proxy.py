import collections
import sys
import pymatic

def _bind_proxy(cls, proxy):
    # Simple safety check to prevent binding mismatched types. May require a more reliable approach if
    # this is prone to errors
    if cls.__qualname__ != proxy.__qualname__:
        raise TypeError("Binding target class and proxy type mismatch." + cls.__qualname__ + " vs. " + proxy.__qualname__)

    if hasattr(proxy, '__doc__'):
        cls.__doc__ = proxy.__doc__

    for name in proxy.members:
        # __qualname__ and __module__ are implicitly included always. Need to skip them as their respective
        # docstring attributes are read-only and will disrupt the binding process
        if name.startswith("__"):
            continue

        if hasattr(cls, name):
            method = getattr(cls, name)
            if method:
                srcmethod = getattr(proxy, name)
                method.__doc__ = srcmethod.__doc__

    return cls


class _BaseProxy(type):
    """Generates a class variable 'members' to track the list of methods declared in the proxy class
    This is used in tbe binding process to limit tha attribute search so that most built-in attributes
    and magic-functions are excluded from inspection

    Note: This meta-class definition is based on the Python PEP 3115 sample
    """

    # __prepare__ can be omitted as order of method declaration is not important. Enabling it makes
    # debugging a bit easier.
    #@classmethod
    #def __prepare__(metacls, name, bases, **kwds):
    #    return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = type.__new__(cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result
