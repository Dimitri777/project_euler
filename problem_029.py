"""
Project Euler - Problem 29
Distinct powers

Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5.
How many distinct values of a^b are there for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

Solved with help of Claude AI (claude.ai)
"""

def solve():
    return len({a**b for a in range(2, 101) for b in range(2, 101)})

if __name__ == "__main__":
    print(f"Problem 29: Distinct powers = {solve()}")
