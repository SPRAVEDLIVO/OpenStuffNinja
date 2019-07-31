import shittyleveling, os, discord, toembed, MainExceptions, asyncio, utils
async def fetch_user(user, client):
    return await client.fetch_user(user)
def mainloop(arglist, protected = True):
    client = arglist[0]
    msg = arglist[1]
    content = msg.content.split(' ')
    if content != [] and len(content) >= 1:
        lvl = shittyleveling.Leveling(str(msg.author.id))
        link = shittyleveling.Link(str(msg.author.id))
        if content[1] == 'add':
            values = lvl.ReadValues()
            if int(values[2]) > 0:
                lvl.UpdateValues(int(values[2])-1, 'unused')
                link.FileSetter(str(content[2]))
                return {'result':'Success!', 'colorize':0x33cc33}
            else:
                return msg.channel.send(embed=toembed.mainloop(result='You have no used lvls!', author=msg.author,color=0xff0000))
        if content[1] == 'remove':
            if link.CheckLink(content[2]) == True:
                link.FileRemover(content[2])
                lvl.UpdateValues(int(values[2])+1, 'unused')
                return {'result':'Success!', 'colorize':0x33cc33}
            else:
                return {'result':'There is no link with ID '+' '.join(content[2:]), 'colorize':0xff0000}
        if content[1] == 'get':
            d = {}
            filelist = os.listdir('linking/')
            if len(filelist) > 0:
                for i,f in enumerate(filelist):
                    with open('linking/'+f, 'r') as fl:
                        literall = [x for x in [x.replace('\n', '') for x in fl.readlines()] if x]
                        d.update({filelist[i].replace('.txt', ''): ', '.join(literall)})
                ms = [cat + ' => ' + d.get(cat) for cat in d.keys()]
                res = '\n'.join(ms)
                return res
            else:
                return 'No links to develer.'
        if content[1] == 'send':
            try:
                asyncio.create_task(MyLittleSender(msg, content, client))
                return {'result':'Success!', 'colorize':0x33cc33}
            except AssertionError:
                return {'result':"Argument link is not set!", 'colorize':utils.Colors.red}
            except MainExceptions.NotEnoughPermissions:
                return {'result':utils.Messages.permserror, 'colorize':utils.Colors.red}
    else: raise MainExceptions.NoArgumentSet
async def MyLittleSender(msg, content, client):
    if utils.AdminlistChecker(str(msg.author.id), 'Deleverer') == True:
        assert content[3] != None
        attachments = msg.attachments
        usr = await fetch_user(str(content[2]), client)
        for attachment in attachments:
            await attachment.save('tempattach/'+attachment.filename)
            await usr.send(content = ' '.join(content[3:]), file = discord.File('tempattach/'+attachment.filename))
            os.remove('tempattach/'+attachment.filename)
        newl = shittyleveling.Link(msg.author.id)
        newl.FileRemover(content[3])
    else: raise MainExceptions.NotEnoughPermissions
    return