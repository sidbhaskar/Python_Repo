class general : pass
class specfic1(general): pass
class specfic2(general): pass
def raiser0():
    x = general()
    raise x
def raiser1():
    raise specfic1
def raiser2():
    x = specfic2
    raise x
for fuc in (raiser0,raiser1,raiser2):
    try : fuc()
    except general :
        import sys; print('caught : '), sys.exc_info()

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except general:
        import sys
        print("Caught: ",sys.exc_type)



# def division(x, y):
#     try:
#         return x/y;
#     except ZeroDivisionError:
#         print("Division by zero")
#
# # print(division(5,2))
# division(5,0)

# try:
#     try:
#         print(3/0)
#     finally: print("Finish")
# except: print("Catch Exception")

# try:
#     raise 'zero'((3, 0))
# raise 'zero': print("Zero Argument")
# except :
#     'zero'(data):
#         print(data)

# class General:
#     pass
# class Specific1(General):
#     pass
# class Specific2(General):
#     pass
# def raiser0():
#     x = General()
#     raise x
# def raiser1():
#     raise Specific1
# def raiser2():
#     X = Specific2
#     raise X

# import sys
# def bye():
#     sys.exit(40)
#     try:
#         bye()
#     except:
#         print("got it")
#     print("continue")
#
# MyDictionary = {...}
# try:
#     x = MyDictionary['ok']
# except:
#     x = None


# # Write a program to creat and open a file and write a line of text
# f = open("python.txt", 'a')
# str = input("Enter a text to be added in the file: ")
#
# f.write(str)
# f.close()
