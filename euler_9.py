# Project Euler - Problem 9: Special Pythagorean Triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
#   a² + b² = c²
#
# For example, 3² + 4² = 9 + 16 = 25 = 5²
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

TARGET = 1000

def find_pythagorean_triplet(target: int) -> int:
    for a in range(1, target // 3):
        for b in range(a + 1, target // 2):
            c = target - a - b
            if c > b and a * a + b * b == c * c:
                return a * b * c
    return -1  # not found

if __name__ == "__main__":
    answer = find_pythagorean_triplet(TARGET)
    print(f"Problem 9 answer: {answer}")
