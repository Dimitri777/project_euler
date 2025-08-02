# https://projecteuler.net/problem=1
'''
If we list all the natural numbers below 10 that are multiples of 3 and 5
# we get 3,5,6 and 9. The sum of these multiples is 24.
# Find the sum of all the multiples of  3 or 5 below  1000.
'''

import numpy as np

# Creating an array of numbers from 1 to 999
numbers = np.arange(1, 1000)

# Finding numbers that are multiples of 3 or 5
multiples = numbers[(numbers % 3 == 0) | (numbers % 5 == 0)]

# Summimg the multiples
sum_multiples = np.sum(multiples)

#Printing the result
print(sum_multiples)
