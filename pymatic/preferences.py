### auto generated
import inspect
from pymatic import conn3m
def resume_usage_data_collection(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
def suspend_usage_data_collection(*args):
    frame = inspect.currentframe()
    method = frame.f_code.co_name
    result = conn3m.send_command(method, args)
    return result
### auto generated
