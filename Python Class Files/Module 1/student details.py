#To store the values(name, reg no, subjects[3]) of student using list, tuples, dict and print the values

name= input('Enter your name: ')
Regno = input('Enter your Reg No.: ')
Sub1=input('Enter 1st Sub :')
Sub2=input('Enter 2nd Sub :')
Sub3=input('Enter 3rd Sub :')

l=[name,Regno,Sub1,Sub2,Sub3]
t=(name,Regno,Sub1,Sub2,Sub3)
d={'name':name,'Reg' : Regno,'Subject':l[2:]}

print(l)
print(t)
print(d)