# https://projecteuler.net/problem=7
"""
By listing the first six prime numbers:
2,3,5,7,11,13 , we can see that the
6th prime is 13.
What is the 10001st prime number?
"""

def is_prime(n):
    # Checks if a number is prime.
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    # Finds the nth prime number.
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(find_nth_prime(10001))

