import googletrans, MainExceptions
translator = googletrans.Translator()
def mainloop(arglist):
    assert (arglist[0] != '' and arglist[1] != '' and arglist != [] and arglist[2:] != []) or (arglist[0] == 'detect' and arglist[1:]!=[])
    if arglist[0] != 'detect':
        scr = arglist[0]
        dest = arglist[1]
        content = ' '.join(arglist[2:])
        return translator.translate(text=content, dest=dest,src=scr).text
    elif arglist[0] == 'detect':
        content = ' '.join(arglist[1:])
        return translator.detect(content).lang
    else: raise MainExceptions.UnknownType