"""
Project Euler - Problem 27
Quadratic primes

Euler discovered the remarkable quadratic formula: n² + n + 41
Find the product of the coefficients a and b for the quadratic expression
n² + an + b, where |a| < 1000 and |b| ≤ 1000, that produces the maximum
number of primes for consecutive values of n, starting with n = 0.

Solved with help of Claude AI (claude.ai)
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes(a, b):
    n = 0
    while is_prime(n*n + a*n + b):
        n += 1
    return n

def solve():
    max_count, result = 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            count = count_primes(a, b)
            if count > max_count:
                max_count, result = count, a * b
    return result

if __name__ == "__main__":
    print(f"Problem 27: Product a*b = {solve()}")
