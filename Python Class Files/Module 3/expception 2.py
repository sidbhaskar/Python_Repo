class general : pass
class specfic1(general): pass
class specfic2(general): pass
def raiser0():
    x = general()
    raise x
def raiser1():
    raise specfic1
def raiser2():
    x = specfic2
    raise x
for fuc in (raiser0,raiser1,raiser2):
    try : fuc()
    except general :
        import sys; print('caught : '), sys.exc_info()