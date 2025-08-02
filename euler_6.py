# https://projecteuler.net/problem=6

import numpy as np

a = np.arange(1, 101)

result = np.sum(a)**2 - np.sum(a**2)

print(result)

