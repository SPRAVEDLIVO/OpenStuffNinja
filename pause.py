import play
def mainloop(arglist, protected = True):
    return {'result': play.pause(arglist), 'lined':False}