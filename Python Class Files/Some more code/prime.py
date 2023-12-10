def find_primes(a, b):
    primes = []
    for num in range(a, b + 1):
        if num > 1:  # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:  # if the number is divisible by any number between 2 and itself, it is not prime
                    break
            else:
                primes.append(num)
    return primes

a = 1
b = 10
print("The prime numbers between", a, "and", b, "are", find_primes(a, b))
