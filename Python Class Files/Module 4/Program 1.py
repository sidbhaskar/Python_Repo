# WAP that accepts filename as an input from the user. Open the file and count the number of times a character appears in the file

filename = input('Enter file name : ')
f = open(filename,'w')
while str!= '@':
    str = input()
    if(str!= '@'):
        f.write( str+ '\n')
data = f.readlines()
c = data.count('hi')
f.close()
print(c)