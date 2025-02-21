### auto generated
import inspect
from pymatic import conn3m
def create_group(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
def create_sub_group(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
### auto generated
