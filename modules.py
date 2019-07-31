import execution, utils, MainExceptions
from toembed import Constructor
def mainloop(arg, protected = True):
    assert arg != []
    assert len(arg) == 2
    msg = arg[1]
    cont = msg.content.split(' ')
    touse = cont[2]
    command = cont[1]
    if utils.AdminlistChecker(str(msg.author.id), 'Admin'):
        if command == 'inject' or command == 'import':
            try:
                execution.dynamic_import(touse)
                return {'result':'Success!','colorize':utils.Colors.green, 'embedding':True}
            except ImportError:
                return {'result':'Unable to import.','colorize':utils.Colors.red, 'embedding':True}
        elif command == 'reload':    
            try:
                execution.dynamic_reload(touse)
                return {'result':'Success!','colorize':utils.Colors.green, 'embedding':True}
            except ImportError:
                return {'result':'Unable to reload.','colorize':utils.Colors.red, 'embedding':True}
        else:
            raise MainExceptions.NoArgumentSet
    else:
        return {'result':utils.Messages.permserror,'colorize':utils.Colors.red, 'embedding':True}