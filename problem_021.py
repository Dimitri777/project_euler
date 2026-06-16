"""
Project Euler - Problem 21
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n.
If d(a) = b and d(b) = a, where a ≠ b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

Find the sum of all the amicable numbers under 10000.

Solved with help of Claude AI (claude.ai)
"""

def sum_divisors(n):
    if n < 2:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

def solve():
    result = 0
    for a in range(2, 10000):
        b = sum_divisors(a)
        if b != a and sum_divisors(b) == a:
            result += a
    return result

if __name__ == "__main__":
    print(f"Problem 21: Sum of amicable numbers under 10000 = {solve()}")
