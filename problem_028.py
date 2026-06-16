"""
Project Euler - Problem 28
Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed. What is the sum of the numbers on the diagonals
in a 1001 by 1001 spiral formed in the same way?

Solved with help of Claude AI (claude.ai)
"""

def solve():
    total = 1
    current = 1
    for step in range(2, 1002, 2):
        for _ in range(4):
            current += step
            total += current
    return total

if __name__ == "__main__":
    print(f"Problem 28: Sum of diagonal numbers in 1001x1001 spiral = {solve()}")
