def mainloop(args):
    sm = 0
    st = ''
    assert len(args) >= 1
    try:
        x = [int(arg) for arg in args]
    except ValueError:
        return "Numbers was excepted, got letters"
    for a in x:
        sm+=a
        st+=str(chr(a))
    return 'Numbers sum: {}\nNumbers as chars: {}'.format(str(sm), st)