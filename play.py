import download, asyncio, os, discord, utils
from toembed import AsyncConstructor
speccom = ['viewqueue', 'queue', 'test']
FILE_FORMAT_TOCKEN = '.mp3'
#We will wait for a while for FFmpegOpusAudio will be available and edit some scripts for high speed boost
queue = {'globs': {'Playing':False, 'looped':False, 'globposis':0, 'ConnectedTo':None}, 'tracklist': {}}
#Function to form queue after file downloading
def FormQueue(url, chnid):
    globs = queue.get('globs')
    tracklist = queue.get('tracklist')
    globs.update({'globposis':globs.get('globposis')+1})
    tracklist.update({url:[chnid, str(globs.get('globposis'))+FILE_FORMAT_TOCKEN]})
    print(queue)
#Checking if queue is done
def QueueCheck():
    return len(queue.get('tracklist').keys())
def GetVoice(ID):
    return queue.get('tracklist').get(ID)[0]
def GetVoiceTrackNum(ID):
    return queue.get('tracklist').get(ID)[1]
def FetchVoiceClient(guild):
    return guild.voice_client
#Finalizing playing for future connections
async def PlayFinalizer(source, chnl, client):
    #Async wait for playing to complete
    while queue.get('globs').get('Playing') == True:
        await asyncio.sleep(5)
        print(queue)
    else:
        tracklist = queue.get('tracklist')
        globs = queue.get('globs')
        await chnl.disconnect()
        if globs.get('looped') == False:
            os.remove('queue/'+GetVoiceTrackNum(source))
            del tracklist[source]
            globs.update({'ConnectedTo':None})
            print(queue)
        await play(client)
        print(queue)
#Playing some audio with queue support
async def play(client):
    if QueueCheck() > 0:
        globs = queue.get('globs')
        # After play, information about previous soundtrack will be deleted by finalizer, so, we just can access first track in the tracklist ([0] index )
        if len(queue.get('tracklist').keys()) > 0:
            a = list(queue.get('tracklist').keys())[0]
            if globs.get('looped') == False:
                globs.update({'ConnectedTo':GetVoice(a)})
            chnl = client.get_channel(GetVoice(a))
            tr = GetVoiceTrackNum(a)
            print(queue)
            vc = await chnl.connect()
            source = discord.FFmpegPCMAudio('queue/'+tr)
            globs.update({'Playing':True})
            vc.play(source, after=lambda e: globs.update({'Playing':False}))
            await PlayFinalizer(a, vc, client)
        else:
            return
    else:
        return
async def mainloop(arglist, protected = True):
    #Form requests first
    global client; client = arglist[0]; msg = arglist[1]; content = msg.content.split(' ')
    if msg.author.voice == None: return await AsyncConstructor(msg, {'result':'You are not in a voice channel!', 'colorize':utils.Colors.red})
    voice = msg.author.voice.channel.id
    cont = content
    content = content[1:]
    #checking
    print(cont, content)
    if cont == ['&play']:
        await msg.channel.send(resume(arglist))
    elif content[0] not in speccom:
        url = ' '.join(content[0:])
        download.mainloop(url, queue.get('globs').get('globposis')+1)
        if len(queue.get('tracklist').keys()) == 0: 
            FormQueue(url, voice)
            await msg.channel.send(':play_pause: Playing: ``'+url+'``')
            await play(client)
        else:
            FormQueue(url, voice)
    if content[0] in speccom:
        return await AsyncConstructor(msg, {'result':'\n'.join(list(queue.get('tracklist').keys()))})
def skip():
    if len(queue.get('tracklist').keys()) > 0:
        queue.get('globs').update({'Playing':False})
        return ':fast_forward: Skipped'
    else:
        return ':fast_forward: Nothing to skip!'
def pause(arglist):
    msg = arglist[1]
    client = FetchVoiceClient(msg.author.guild)
    if client != None:
        client.pause()
        return ':pause_button: Paused'
    else:
        return ':pause_button: Nothing to pause!'
def resume(arglist):
    msg = arglist[1]
    client = FetchVoiceClient(msg.author.guild)
    if client != None:
        client.resume()
        return ':play_pause: Resumed'
    else:
        return ':play_pause: Nothing to resume!'
def loop():
    if queue.get('globs').get('looped'):
        queue.get('globs').update({'looped':False})
        return ':repeat: Enabled'
    else:
        queue.get('globs').update({'looped':True})
        return ':repeat: Disabled'