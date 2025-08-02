# https://projecteuler.net/problem=3
"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number600851475143?
"""

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

num = 600851475143
result = largest_prime_factor(num)
print("Largest prime factor of", num, "is:" + str(result))

