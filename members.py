def mainloop(clientlist, protected=True):
    client = clientlist[0]
    return 'I found '+f"{len(client.guilds)}"+' servers\nYou can increase this value by adding bot to your server!\nType &link to get the link'