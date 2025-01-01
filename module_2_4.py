
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for numbers in numbers:
    is_primes = True
    if numbers <= 1:
        is_primes = False
    else:
        for i in range(2, int(numbers  ** 0.5) +1):
            if numbers % i == 0:
                is_primes = False
                break
        if is_primes:
            primes .append(numbers)
        else:
            not_primes.append(numbers)
print(primes)
print(not_primes)