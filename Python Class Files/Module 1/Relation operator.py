#WAP to find out the biggest among three number using relational operator

a=int(input('Enter the First Number: '))
b=int(input('Enter the Second Number: '))
c=int(input('Enter the Third Number: '))

if(a>b and a>c):
    print(a,'is biggest among all')
elif(b>a and b>c):
    print(b,'is biggest among all the numbers')
else:
    print(c,'is biggest')


