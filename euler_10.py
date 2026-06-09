# Project Euler - Problem 10: Summation of Primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

LIMIT = 2_000_000

def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Return a list of all primes below `limit` using the Sieve of Eratosthenes."""
    is_prime = bytearray([1]) * limit
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i, v in enumerate(is_prime) if v]

def sum_primes_below(limit: int) -> int:
    return sum(sieve_of_eratosthenes(limit))

if __name__ == "__main__":
    answer = sum_primes_below(LIMIT)
    print(f"Problem 10 answer: {answer}")
