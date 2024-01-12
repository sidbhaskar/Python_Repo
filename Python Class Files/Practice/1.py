import re

pattern = 'a...s$'
test_string = 'abyss'
result = re.match(pattern,test_string)
if result :
    print('Matched')
else :
    print('nahh')