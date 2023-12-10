def fibonacci(i):
  if i <= 1 :
    return i
  else:
    return fibonacci(i - 1) + fibonacci(i - 2)

series = int(input("Enter no : "))
for i in range(series) :
  print(fibonacci(i) , end = " ")