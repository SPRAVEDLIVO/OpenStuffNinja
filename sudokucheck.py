import sudoku, toembed
def mainloop(arglist, protected= True):
    assert len(arglist) == 2
    msg = arglist[1]
    arg = msg.content.split(' ')[1]
    return sudoku.check(arg, str(msg.author.id))