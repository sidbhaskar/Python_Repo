f=open('newFile.txt','w')
print('Enter text (@ at end): ')
while str!= '@':
    str = input()
    if(str!= '@'):
        f.write( str+ '\n')
f.close()