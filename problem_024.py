"""
Project Euler - Problem 24
Lexicographic permutations

A permutation is an ordered arrangement of objects.
What is the millionth lexicographic permutation of the digits 0-9?

Solved with help of Claude AI (claude.ai)
"""

from itertools import islice, permutations

def solve():
    perms = permutations('0123456789')
    millionth = next(islice(perms, 999999, None))
    return ''.join(millionth)

if __name__ == "__main__":
    print(f"Problem 24: Millionth lexicographic permutation = {solve()}")
