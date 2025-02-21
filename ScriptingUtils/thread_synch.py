import sys
import inspect
import threading

from functools import wraps

from ScriptingUtils import toggle_script_listener

# This wrapper will be used by threaded trimatic module


def perform_on_main_thread(func):
    @wraps(func)
    def caller(*args, **kwargs):
        # parse away named parameters (as we don't supported those (yet?))
        new_args = list(args)
        for key in kwargs.keys():
            new_args.append(kwargs[key])
        if threading.current_thread() is not threading.main_thread():
            # this part is used when called from RPyC (external interpreter)
            toggle_script_listener.script_listener_send_queue.put(
                {'func': func, 'args': new_args, 'member': True})
            result = toggle_script_listener.script_listener_receive_queue.get()
            if isinstance(result, Exception):
                # Special workaround handling since Python 3.10
                # See: https://github.com/python/cpython/issues/96352
                if isinstance(result, AttributeError):
                    result.obj = None
                raise result
        else:
            # this part is used during processing of toggle_script_listener.script_listener_send_queue
            # or when called from within 3-matic's interpreter
            result = func(*new_args, **{})
        return result
    return caller


def wrap_type_attributes(type):
    for member_name, member in inspect.getmembers(type):
        if not '__' in member_name:
            if callable(member):
                setattr(type, member_name, perform_on_main_thread(member))
            elif isinstance(member, property):
                setattr(type, member_name, property(perform_on_main_thread(member.__get__),
                                                    perform_on_main_thread(
                                                        member.__set__),
                                                    perform_on_main_thread(member.__delattr__)))
                new_member = getattr(type, member_name)
                new_member.__doc__ = member.__doc__
