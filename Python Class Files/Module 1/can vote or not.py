#WAP to check weather the candidate is eligible for voting or not

from datetime import datetime, timedelta

now = datetime.now()
DOB = input('Enter your DOB in (YYYY-MM-DD): ')
birthday = datetime.strptime(DOB, "%Y-%m-%d")
diff = now - birthday
age = diff.days // 365
if(age>=18):
    print('You are eligible')
else:
    print('Not Eligible')


