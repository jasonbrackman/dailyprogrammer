from typing import List


def strip_zeroes(items: List) -> List:
    """
    Optional Warmup 1: eliminating 0's.
    Given a sequence of answers, return the same set of answers with all the 0's removed.
    """
    return [i for i in items if i != 0]


def sort_descending(items: List) -> List:
    """
    Optional Warmup 2: descending sort
    Given a sequence of answers, return the sequence sorted in descending order, so that the first
    number is the largest and the last number is the smallest.
    """

    return sorted(items, reverse=True)


def is_value_greater_than_length(length: int, items: List) -> bool:
    """
    Given a number N and a sequence of answers, return true if N is greater than the number of answers
    (i.e. the length of the sequence), and false if N is less than or equal to the number of answers.
    """
    return length > len(items)


def warmup4(length: int, items: List) -> List:
    """
    Optional Warmup 4: front elimination
    Given a number N and a sequence in descending order, subtract 1 from each of the first N answers
    in the sequence, and return the result. For instance, given N = 4 and the sequence [5, 4, 3, 2, 1],
    you would subtract 1 from each of the first 4 answers (5, 4, 3, and 2) to get 4, 3, 2, and 1.
    The rest of the sequence (1) would not be affected:

    You may assume that N is greater than 0, and no greater than the length of the sequence. Like in
    warmup 1, it's okay if you want to reorder the answers in your result.

    """
    result = []

    for index, item in enumerate(items):
        result.append(item - (index < length))  # Bool is True/False or 1/0

    return result


def hh(items: List) -> bool:
    """
    Challenge: the Havel-Hakimi algorithm
    Perform the Havel-Hakimi algorithm on a given sequence of answers. This algorithm will return true
    if the answers are consistent (i.e. it's possible that everyone is telling the truth) and false if
    the answers are inconsistent (i.e. someone must be lying):

    1. Remove all 0's from the sequence (i.e. warmup1).
    2. If the sequence is now empty (no elements left), stop and return true.
    3. Sort the sequence in descending order (i.e. warmup2).
    4. Remove the first answer (which is also the largest answer, or tied for the largest) from the
       sequence and call it N. The sequence is now 1 shorter than it was after the previous step.
    5. If N is greater than the length of this new sequence (i.e. warmup3), stop and return false.
    6. Subtract 1 from each of the first N elements of the new sequence (i.e. warmup4).
    7. Continue from step 1 using the sequence from the previous step.

    Eventually you'll either return true in step 2, or false in step 5.

    You don't have to follow these steps exactly: as long as you return the right answer, that's fine. Also, if you answered the warmup questions, you may use your warmup solutions to build your challenge solution, but you don't have to.
    """
    while True:
        items = strip_zeroes(items)
        items = sort_descending(items)
        if not items:
            return True

        n = items.pop(0)
        if is_value_greater_than_length(n, items):
            return False
        items = warmup4(n, items)


assert strip_zeroes([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) == [5, 3, 2, 6, 2, 7, 2, 5]
assert strip_zeroes([4, 0, 0, 1, 3]) == [4, 1, 3]
assert strip_zeroes([1, 2, 3]) == [1, 2, 3]
assert strip_zeroes([0, 0, 0]) == []
assert strip_zeroes([]) == []

assert sort_descending([5, 1, 3, 4, 2]) == [5, 4, 3, 2, 1]
assert sort_descending([0, 0, 0, 4, 0]) == [4, 0, 0, 0, 0]
assert sort_descending([1]) == [1]
assert sort_descending([]) == []

assert is_value_greater_than_length(7, [6, 5, 5, 3, 2, 2, 2]) is False
assert is_value_greater_than_length(5, [5, 5, 5, 5, 5]) is False
assert is_value_greater_than_length(5, [5, 5, 5, 5]) is True
assert is_value_greater_than_length(3, [1, 1]) is True
assert is_value_greater_than_length(1, []) is True
assert is_value_greater_than_length(0, []) is False

assert warmup4(4, [5, 4, 3, 2, 1]) == [4, 3, 2, 1, 1]
assert warmup4(11, [14, 13, 13, 13, 12, 10, 8, 8, 7, 7, 6, 6, 4, 4, 2]) == [13, 12, 12, 12, 11, 9, 7, 7, 6, 6, 5, 6, 4, 4, 2]
assert warmup4(1, [10, 10, 10]) == [9, 10, 10]
assert warmup4(3, [10, 10, 10]) == [9, 9, 9]
assert warmup4(1, [1]) == [0]

assert hh([5, 3, 0, 2, 6, 2, 0, 7, 2, 5]) is False
assert hh([4, 2, 0, 1, 5, 0]) is False
assert hh([3, 1, 2, 3, 1, 0]) is True
assert hh([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]) is True
assert hh([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12]) is True
assert hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]) is False
assert hh([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]) is False
assert hh([2, 2, 0]) is False
assert hh([3, 2, 1]) is False
assert hh([1, 1]) is True
assert hh([1]) is False
assert hh([]) is True