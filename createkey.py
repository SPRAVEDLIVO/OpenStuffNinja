import shittyleveling, hashlib, random, utils, string
def mainloop(arglist, protected = True):
    msg = arglist[1]
    if utils.AdminlistChecker(str(msg.author.id), 'Admin'):
        inst = shittyleveling.Key()
        let = string.ascii_lowercase + string.digits
        st = ''
        for _ in range(random.randint(5, 30)):
            st += random.choice(let+str(_*2))
        hs = hashlib.md5(st.encode('utf-8')).hexdigest()
        inst.AddKey(hs)
        return {'result': 'Your key: '+hs, 'embedding':True, 'lined':False}