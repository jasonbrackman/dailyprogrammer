from typing import NamedTuple, List
from itertools import permutations
import time


class Vec(NamedTuple):
    x: int = 0
    y: int = 0
    z: int = 0


def fit1(d1: Vec, d2: Vec) -> int:
    return (d1.x // d2.x) * (d1.y // d2.y)


def fit2(d1: Vec, d2: Vec) -> int:
    a = (d1.x // d2.x) * (d1.y // d2.y)
    b = (d1.x // d2.y) * (d1.y // d2.x)
    return a if a > b else b


def fit3(d1: Vec, d2: Vec) -> int:
    options = permutations([d2.x, d2.y, d2.z])
    results = [(d1.x // x) * (d1.y // y) * (d1.z // z) for x, y, z in options]
    return max(results)


def fitn(items1: List, items2: List) -> int:
    """Will be slow for large combinatorials..."""
    options = permutations(items2)
    results = 0
    for option in options:
        result = 1
        pieces = (a // b for a, b in zip(items1, option))
        for piece in pieces:
            result *= piece
        results = result if result > results else results
    return results

t1 = time.monotonic()
assert fit1(Vec(5, 100), Vec(6, 1)) == 0
assert fit1(Vec(12, 34), Vec(5, 6)) == 10
assert fit1(Vec(25, 18), Vec(6, 5)) == 12
assert fit1(Vec(10, 10), Vec(1, 1)) == 100
assert fit1(Vec(12345, 678910), Vec(1112, 1314)) == 5676

assert fit2(Vec(25, 18), Vec(6, 5)) == 15
assert fit2(Vec(12, 34), Vec(5, 6)) == 12
assert fit2(Vec(12345, 678910), Vec(1112, 1314)) == 5676
assert fit2(Vec(5, 5), Vec(3, 2)) == 2
assert fit2(Vec(5, 100), Vec(6, 1)) == 80
assert fit2(Vec(5, 5), Vec(6, 1)) == 0

assert fit3(Vec(10, 10, 10), Vec(1, 1, 1)) == 1000
assert fit3(Vec(12, 34, 56), Vec(7, 8, 9)) == 32
assert fit3(Vec(123, 456, 789), Vec(10, 11, 12)) == 32604
assert fit3(Vec(1234567, 89101112, 13141516), Vec(171819, 202122, 232425)) == 174648

assert fitn([3, 4], [1, 2]) == 6
assert fitn([123, 456, 789], [10, 11, 12]) == 32604
assert fitn([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21]) == 1883443968

"""
This is secretly a maximum matching problem. We want to match each crate dimension
X to some box dimension Y, maximizing the product of floor(X / Y). This is equivalent
to maximizing the sum of log(floor(X / Y)).
"""

# assert fitn([
#     180598, 125683, 146932, 158296, 171997, 204683, 193694, 216231, 177673, 169317,
#     216456, 220003, 165939, 205613, 152779, 177216, 128838, 126894, 210076, 148407],
#     [1984, 2122, 1760, 2059, 1278, 2017, 1443, 2223, 2169, 1502, 1274, 1740, 1740,
#      1768, 1295, 1916, 2249, 2036, 1886, 2010]) == 4281855455197643306306491981973422080000
print(f"[Completed in {time.monotonic() - t1}]")