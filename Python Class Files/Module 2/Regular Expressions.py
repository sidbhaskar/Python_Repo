import re
#module to check if a particular string matches a given regular expression

pattern ='^a...s$'
test_String = 'abyss'
result = re.match(pattern , test_String)
if result :
    print('Regular Expression Successful')
else :
    print('Unsuccessful')
