try :
    age = int(input('Enter the age: '))
    weight = float(input('Enter the weight: '))
    index = weight/age
    print(index)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Wrong value of age is entered')
finally:
    print('Re-run the program')
    print('Everything is fine')

# WAP to handle the exception handling in ATM debit process, the costomur is tring the withdraw access form the limit
