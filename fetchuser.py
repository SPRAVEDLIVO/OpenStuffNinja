import toembed, MainExceptions
async def fetcher(client, user):
    return await client.fetch_user(user)
async def mainloop(arglist, protected = True):
    client = arglist[0]
    msg = arglist[1]
    content = msg.content.split(' ')
    if content is not None and content != []:
        res = await fetcher(client, int(content[1]))
        return await msg.channel.send(embed=toembed.mainloop(result=str(res), author=msg.author))
    else:
        raise MainExceptions.NoArgumentSet
    return 