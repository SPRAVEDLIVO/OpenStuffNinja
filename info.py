import os, configparser, json
import discord
def mainloop():
    embed = discord.Embed(title="Info", description="``Information about all commands``", color=0xeee657)
    categories = referenseloop()
    for categorie in categories.keys():
        items = '``'+', '.join(categories.get(categorie))+'``'
        embed.add_field(name=categorie.upper()+':', value=items, inline=False)
    return embed
def createcat():
    cat = {}
    config = configparser.ConfigParser()
    config.read('information.txt')
    for section in config.sections():
        cat.update({config.get(section, 'category'): []})
    return cat
def referenseloop():
    filelist = os.listdir()
    config = configparser.ConfigParser()
    config.read('information.txt')
    categories = createcat()
    for file in filelist:
        for section in config.sections():
            shortpath = os.path.splitext(file)[0]
            if shortpath == section:
                categorie = config.get(shortpath, 'category')
                categories.get(categorie).append(shortpath)
    return categories