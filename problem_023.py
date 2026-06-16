"""
Project Euler - Problem 23
Non-abundant sums

A perfect number is a number for which the sum of its proper divisors equals the number.
A number n is called deficient if d(n) < n and it is called abundant if d(n) > n.

Find the sum of all positive integers which cannot be written
as the sum of two abundant numbers. (limit: 28123)

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
    limit = 28123
    abundants = [n for n in range(1, limit + 1) if sum_divisors(n) > n]
    abundant_set = set(abundants)

    can_be_written = set()
    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            s = a + b
            if s > limit:
                break
            can_be_written.add(s)

    return sum(n for n in range(1, limit + 1) if n not in can_be_written)

if __name__ == "__main__":
    print(f"Problem 23: Sum of non-abundant sums = {solve()}")
