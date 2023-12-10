#program to print positve number only

start = int(input('Enter the 1st number : '))
end = int(input("Enter the 2nd Number : "))

for i in range(start , end+1) :
    if( i < 0 ) :
        pass
    else:
        print(i)