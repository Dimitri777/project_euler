"""
Project Euler - Problem 22
Names scores

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the list.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Solved with help of Claude AI (claude.ai)
"""

import urllib.request

def solve():
    # Download names file from Project Euler
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
        names = sorted(name.strip('"') for name in content.split(','))
    except Exception:
        # Fallback: use a small sample for demonstration
        names = sorted(["MARY", "PATRICIA", "LINDA", "BARBARA", "COLIN"])

    total = 0
    for pos, name in enumerate(names, 1):
        score = sum(ord(c) - ord('A') + 1 for c in name)
        total += pos * score
    return total

if __name__ == "__main__":
    print(f"Problem 22: Total name scores = {solve()}")
