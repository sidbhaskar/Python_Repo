#WAP using input function to check weather the given day is weekend or not

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = input("Enter the day: ")

if day in working_days:
    print(day + " is a working day.")
else:
    print(day + " is a weekend Holiday.")
