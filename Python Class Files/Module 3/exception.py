def div(x,y):
    try:
        if y ==0 :
            return x/y
    except 'zero' :
        print('Zero')

div(3,4)
div(3,0)


# try :
#     raise 'zero' , (3,0)
# except 'zero': print("zero arugment")
# except 'zero', data : print(data)