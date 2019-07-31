import configparser, discord
def mainloop(string):
    string = ''.join(string)
    config = configparser.ConfigParser()
    config.read('information.txt')
    embed = discord.Embed(title = 'Info', description="``Information about "+string+'``', color=0xeee657)
    cmdlist = ['description', 'usage', 'available']
    for options in config.options(string):
        for cmd in cmdlist:
            if cmd in options:
                inf = config.get(string, cmd)
                embed.add_field(name=cmd.upper()+':',value= '``'+inf+'``', inline=False)
    return embed
def section_avalibale(string, option):
    config = configparser.ConfigParser()
    config.read('information.txt')
    for section in config.sections():
        if string == section:
            return config.get(string, option)
    return False