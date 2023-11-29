import re

user_data = int(input('Enter your PIN : '))
stored_pin = '1234'

result = re.match(stored_pin, user_data)

if result:
    print('Welcome User')
else:
    print('Wrong Pin')