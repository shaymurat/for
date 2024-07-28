numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(1, len(numbers)):
    is_prime = True

    j = 0
    while len(primes) > 0 and primes[j] <= numbers[i] // 2:
        if numbers[i] % primes[j] == 0:
            is_prime = False
            break
        j += 1

    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('primes:', primes)
print('not_primes:', not_primes)
