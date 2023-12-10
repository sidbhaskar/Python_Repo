import re

s = "Hello this is a python program :)"

match = re.search('is',s)

print("staring : ",match.start())
print("Ending  : ",match.end())