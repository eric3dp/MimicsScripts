from trimatic.align import *
from trimatic.analyze import *
from trimatic.cad_link import *
from trimatic.curve import *
from trimatic.data import *
from trimatic.design import *
from trimatic.file import *
from trimatic.group import *
from trimatic.finish import *
from trimatic.fix import *
from trimatic.interactive import *
from trimatic.lattice import *
from trimatic.logging import *
from trimatic.mark import *
from trimatic.measure import *
from trimatic.preferences import *
from trimatic.remesh import *
from trimatic.sketch import *
from trimatic.ssm import *
from trimatic.subscription import *
from trimatic.surface import *
from trimatic.texturing import *
from trimatic.uv import *
from trimatic.view import *

#import all modules from plugins
from .plugins import *

#for autocomplete to find it (jedi does only static evaluation and doesn't work with setattr to create it at runtime)
from trimatic.types import *

#generate doc bindings and trimatic types
import pymatic
import inspect
import trimatic.proxy as proxy
import trimatic.types as types
from ScriptingUtils import thread_synch

name, entity = None, None
for name, entity in inspect.getmembers(types):
    if inspect.isclass(entity) and hasattr(pymatic, name):
        #for each class in trimatic.types, if there is corresponding pymatic type,
        # 1. set document string with _bind_proxy (basically copies __doc__ from trimatic.types.xyz to pymatic.xyz
        # 2. hijack pymatic types and set their modules to trimatic 
        # 3. overwrite the trimatic.xyz attribute with pymatic.xyz
        new_type = proxy._bind_proxy(getattr(pymatic, name), entity)
        setattr(trimatic, name, new_type)
        if not hasattr(pymatic, 'external_module'):
            thread_synch.wrap_type_attributes(new_type)
