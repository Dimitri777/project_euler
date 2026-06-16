"""
Project Euler - Problem 20
n! digit sum

10! = 10 × 9 × ... × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Solved with help of Claude AI (claude.ai)
"""

import math

def solve():
    factorial = math.factorial(100)
    result = sum(int(d) for d in str(factorial))
    return result

if __name__ == "__main__":
    print(f"Problem 20: Sum of digits in 100! = {solve()}")
