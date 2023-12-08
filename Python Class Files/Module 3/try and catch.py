import sys

def bye():
    sys.exit(40)
    try :
        bye()
    except:
        print('Got it')
        print('Continue')

mydic = {...}
try : x = mydic['ok']
except : x = None
