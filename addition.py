import MainExceptions
def mainloop(nums):
    if nums != []:
        sm = 0
        for i in nums:
            sm+=int(i)
        return {'result': sm, 'colorize': None, 'embedding': True}
    else: raise MainExceptions.NoArgumentSet