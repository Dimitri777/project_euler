"""
Project Euler - Problem 30
Digit fifth powers

Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:
Find the sum of all the numbers that can be written as the sum
of fifth powers of their digits.

Solved with help of Claude AI (claude.ai)
"""

def solve():
    # Upper bound: 9^5 * 7 = 413343 (7 digits), so 999999 is safe
    return sum(
        n for n in range(2, 1000000)
        if n == sum(int(d)**5 for d in str(n))
    )

if __name__ == "__main__":
    print(f"Problem 30: Sum of digit fifth powers = {solve()}")
