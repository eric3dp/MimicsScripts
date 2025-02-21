### auto generated
import inspect
from pymatic import conn3m
def resume_logging(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
def suspend_logging(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
### auto generated
