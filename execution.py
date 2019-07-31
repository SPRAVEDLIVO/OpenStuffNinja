"""
:module execution: module, where we convert code into magic spells
"""
import os, description, importlib, inspect, MainExceptions, utils
files = os.listdir()
modules = {}
"""
:global debugging: if enabled, any exception in code will stop the programm
:global banned: scripts not to import
"""
debugging = False
banned = ['execution', 'main', 'information', 'description', 'utils', 'MainExceptions', 'toembed']
"""
Script to import all python files in folder
"""
for file in files:
    sp = os.path.splitext(file)[0]
    if '.py' in file and sp not in banned:
        modules.update({sp: importlib.import_module(sp)})
"""
Function example:
env: /somemodule.py
def mainloop(args, bool protected):
    ...
    Code
    ...
    return {'result': `ResultOfCode`, 'colorize': `ColorInHex`, 'embedding': `True`}
:param protected: if in function args, your function will be able to send messages and uses client expressions
:param args: if protected in funcion args, will be: [client, message], else, will be just content of message
"""
def dynamic_exec(module, args):
    if module in modules.keys():
        modularget = modules.get(module)
        try: arg = inspect.getargspec(modularget.mainloop).args
        except DeprecationWarning: pass
        try:
            if not 'protected' in arg:
                if len(arg) >= 1:
                    msg = args[1]
                    cont = msg.content.split(' ')
                    del cont[0]
                    return modularget.mainloop(cont)
                else:
                    return modularget.mainloop()
            if 'protected' in arg:
                return modularget.mainloop(args)
        except Exception as e:
            if debugging == False:
                if description.section_avalibale(module, 'usage') !=False:
                    return 'Usage: '+description.section_avalibale(module, 'usage')
                else:
                    print(e)
                    return {"result":'Command does not exist', 'colorize':utils.Colors.red, 'embedding':True}
            else:
                raise e
    else:
        return {"result":'Command does not exist', 'colorize':utils.Colors.red, 'embedding':True}
def dynamic_import(module):
    if module in modules.keys():
        modules.update({module: importlib.import_module(module)})
    else:
        raise ImportError
def dynamic_reload(module):
    if module in modules.keys():
        modules.update({module: importlib.reload(modules.get(module))})
    else:
        raise ImportError