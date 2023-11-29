def print_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
        i += 1
    return primes

# Test the function
n = int(input('Enter the number: '))
print(f"The first {n} prime numbers are: {print_primes(n)}")
