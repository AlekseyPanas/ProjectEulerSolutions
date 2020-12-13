"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math


def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


primes = [2]
n = 3

while primes[-1] < 2000000:
    if prime(n):
        primes.append(n)

    print(primes[-1])

    n += 1

print(sum(primes) - 2000003)
