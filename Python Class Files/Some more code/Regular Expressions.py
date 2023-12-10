import re

s = "The rain in spain. This is a python program"
pattern = 'program\Z'
result = re.findall(pattern,s)
x = re.findall('ai',s)

print(x)
print(result)
