import sys

def unload_external_modules():
    modules_keys = []
    #don't unload builtins and don't unload trimatic and pymatic modules.
    #also don't unload modules which start with '_' as they're special and don't unload modules found in sys.path
    excluded_modules = ('trimatic', 'pymatic', '_', 'ScriptingUtils.thread_synch', 'ScriptingUtils.qt_3matic_app', 'ScriptingUtils.toggle_script_listener') + sys.builtin_module_names
    for module_name in sys.modules.keys():
        if module_name.startswith(excluded_modules):
            continue
        module = sys.modules[module_name]
        #some modules use __file__
        if hasattr(module, '__file__') and module.__file__:
            # skip module in installed python location 
            if sys.prefix in module.__file__:
                continue
        #others use __path__
        if hasattr(module, '__path__'):
            skip = False
            for path in module.__path__:
                # skip module having path at installed python location
                if path is not None and sys.prefix in path:
                    skip = True
                    break

            if skip:
               continue
        modules_keys.append(module_name)
    #by deleting the module, it will be unloaded, when possible
    for module_name in modules_keys:
        del sys.modules[module_name]

if __name__ == "__main__":
    unload_external_modules()