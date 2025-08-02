# https://projecteuler.net/problem=5
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from
1 to 20?
"""

import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(n):
    return reduce(lcm, range(1, n + 1))

num = 20
result = smallest_multiple(num)
print("Smallest multiple divisible by all numbers from 1 to 20:", result)
