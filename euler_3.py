# https://projecteuler.net/problem=3
"""

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

