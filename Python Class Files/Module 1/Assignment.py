def print_positive_numbers(start, end):
    for num in range(start, end+1):
        if num > 0:
            print(num)

# Test the function
start = -10
end = 10
print("The positive numbers between", start, "and", end, "are:")
print_positive_numbers(start, end)
