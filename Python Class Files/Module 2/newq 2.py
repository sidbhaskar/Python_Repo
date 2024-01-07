# WAP to handle the exception handling in ATM debit process, the costomur is tring the withdraw access form the limit

try:
    amount = int(input('Enter the amount to debit: '))
    limit = 50000
except (amount > limit):
    print('Amount exceeds')
finally:
    print('Contact the bank for more information')





