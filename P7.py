"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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


num = 2
prime_count = 0
current_prime = -1
while prime_count < 10001:
    if prime(num):
        prime_count += 1
        current_prime = num
        print(prime_count, current_prime)
    num += 1
    print(num)

print(current_prime)
