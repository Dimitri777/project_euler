"""
Project Euler - Problem 26
Reciprocal cycles

Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.

Solved with help of Claude AI (claude.ai)
"""

def cycle_length(d):
    remainders = {}
    remainder = 1
    position = 0
    while remainder != 0:
        if remainder in remainders:
            return position - remainders[remainder]
        remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1
    return 0

def solve():
    max_len, result = 0, 0
    for d in range(2, 1000):
        length = cycle_length(d)
        if length > max_len:
            max_len, result = length, d
    return result

if __name__ == "__main__":
    print(f"Problem 26: d with longest recurring cycle = {solve()}")
