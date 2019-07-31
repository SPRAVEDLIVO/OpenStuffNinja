import shittyleveling, os, toembed, math, MainExceptions
def geometrical(n):
    return 25*n*(1+n)

def mainloop(arglist, protected = True):
    msg = arglist[1]
    content = msg.content.split(' ')
    if content[1] != []:
        lvl = shittyleveling.Leveling(msg.author.id)
        if content[1] == 'info':
            filenames = os.listdir('leveling/')
            lvl.ProfileCreate() if str(msg.author.id)+'.txt' not in filenames else 0
            values = lvl.ReadValues()
            return {'result':'Lvl: '+values[0]+'\nExp: '+values[1]+'\nUnused: '+values[2], 'embedding':True}
        elif content[1] == 'enterkey':
            lvl.ProfileCreate() if str(msg.author.id)+'.txt' not in os.listdir() else 0
            key = content[2]
            keying = shittyleveling.Key()
            lvl = shittyleveling.Leveling(msg.author.id)
            vals = lvl.ReadValues()
            crntlvl = int(vals[0])
            crntunused = int(vals[2])
            if keying.DeleteKey(key) == True:
                lvl.UpdateValues(crntlvl+1,'lvl')
                lvl.UpdateValues(crntunused+1, 'unused')
                return {'result':'Key was successfully activated!', 'colorize':0x33cc33, 'embedding':True}
            else:
                return {'result':'No key found!', 'colorize':0xff0000, 'embedding':True}
        elif content[1] == 'checkup':
            lvl.ProfileCreate() if str(msg.author.id)+'.txt' not in os.listdir() else 0
            lvl = shittyleveling.Leveling(msg.author.id)
            vals = lvl.ReadValues()
            crntlvl = int(vals[0])
            crntxp = int(vals[1])
            crntunused = int(vals[2])
            if crntxp >= geometrical(crntlvl):
                lvl.UpdateValues(str(crntlvl+1), 'lvl')
                lvl.UpdateValues(geometrical(crntlvl)-crntxp, 'exp')
                lvl.UpdateValues(str(crntunused+1), 'unused')
                return {'result':'Lvl up!', 'colorize':0x33cc33, 'embedding':True}
            else:
                return {'result':'You need ' + str((geometrical(crntlvl) - crntxp)) + ' xp for next level!', 'colorize':0xff0000, 'embedding':True}
    else:
        raise MainExceptions.NoArgumentSet