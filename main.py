import info, description, toembed, execution, discord, MainExceptions
DISCORD_BOT_TOKEN = '#'
client = discord.Client()
COMMAND_TOCKEN = '&'
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
def load_opus_lib(opus_libs=OPUS_LIBS):
    if discord.opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            discord.opus.load_opus(opus_lib)
            return
        except OSError:
            pass
        raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("Structure rewrite")
    load_opus_lib()
    await client.change_presence(status=discord.Status.online, activity=game)
speccom = ['help', 'info']
@client.event
async def on_message(message):
    if message.content.startswith(COMMAND_TOCKEN) and message.author.bot == False:
        msg = list(message.content)
        del msg[:len(COMMAND_TOCKEN)]
        msg = ''.join(msg).split(' ')
        command = msg[0]
        args = msg[1:]
        if command not in speccom:
            executed = execution.dynamic_exec(command, [client, message])
            datatype = type(executed)
            if datatype == dict:
                result = executed.get('result')
                embedding = True if executed.get('lined') == None else executed.get('lined')
                lined = True if executed.get('lined') == None else executed.get('lined')
                if embedding == False:
                    if executed.get('colorize') == None:
                        await message.channel.send(result)
                else:
                    if executed.get('colorize') == None:
                        await message.channel.send(embed=toembed.mainloop(result=result, author=message.author, lined=lined))
                    else:
                        await message.channel.send(embed=toembed.mainloop(result=result, author=message.author, color=executed.get('colorize'), lined=lined))
            elif datatype == str or (datatype == dict and executed.get("settings") == 'default'):
                if datatype == dict:
                    lined = True if executed.get('lined') == None else executed.get('lined')
                    await message.channel.send(embed=toembed.mainloop(result=executed, author=message.author, lined=lined))
                else:
                    await message.channel.send(embed=toembed.mainloop(result=executed, author=message.author))
            else:
                await executed
        elif command in speccom:
            if len(args) == 0:
                await message.channel.send(embed=info.mainloop())
            else:
                try:
                    await message.channel.send(embed=description.mainloop(args))
                except: message.channel.send(embed='``Command does not exist.``')
    return
client.run(DISCORD_BOT_TOKEN)