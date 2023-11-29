#WAP  to check if the email id entered is valid or not
import re

email = input('Enter your Email: ')
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
result = re.match(pattern,email)
if result :
    print('Correct')
else :
    print('Incorrect')