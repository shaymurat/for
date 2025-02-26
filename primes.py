numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue

    is_prime = True

    j = 0
    while len(primes) > 0 and primes[j] <= i // 2:
        if i % primes[j] == 0:
            is_prime = False
            break
        j += 1

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Primes:', primes)
print('Not Primes:', not_primes)
