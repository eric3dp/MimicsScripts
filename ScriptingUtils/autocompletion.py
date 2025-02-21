import jedi

#fixes issue noticed by Mee Yun when typing class h():\n\t@cl  => raises ValueError somewhere in cache => it is not the code itself but triggered by what was sent to jedi previously
jedi.settings.fast_parser = False
jedi.settings.dynamic_array_additions = False

def autocomplete(text):
    script = jedi.Script(text)
    completions = script.completions()
    builtins = []
    function_arguments = []
    suggestions = []
    for c in completions:
        if c.name.startswith('__'):
            builtins.append(c.name)
        else:
            if c.type == 'function':
                suggestions.append(c.name+'(')
            else:
                if c.name_with_symbols.endswith('='):
                    function_arguments.append(c.name_with_symbols)
                else:
                    suggestions.append(c.name)
    if len(function_arguments) > 0:
        return function_arguments
    else:
        if ( len(suggestions) > 0 ):
            return suggestions
        else:
            return builtins

def get_autocompletions(text: "string to get autocompletion for"):
    suggestions = []
	# Catching all exceptions from jedi and ignoring them. 
	# Efffect is no autocomplete suggestions will be given without filling logger with traceback on every keystroke
    try:
        suggestions = autocomplete(text)
    except:
        pass
    return tuple(suggestions)
    