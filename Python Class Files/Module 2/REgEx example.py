import re

s = 'The rain in Spain. This is a Python Program'
pattern= 'program/Z'
result = re.findall(pattern,s)
print(result)
