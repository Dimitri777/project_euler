"""
Project Euler - Problem 25
1000-digit Fibonacci number

What is the index of the first term in the Fibonacci sequence
to contain 1000 digits?

Solved with help of Claude AI (claude.ai)
"""

def solve():
    a, b = 1, 1
    index = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        index += 1
    return index

if __name__ == "__main__":
    print(f"Problem 25: Index of first 1000-digit Fibonacci number = {solve()}")
