from typing import List
from collections import Counter


def yield_word():
    with open(r'./data/enable1.txt', 'rt') as lines:
        for line in lines:
            yield line.strip()


WORDS = dict()
for word in yield_word():
    word_length = len(word)
    if word_length not in WORDS:
        WORDS[word_length] = []
    WORDS[word_length].append(word)


def quick_reject(s1: str, s2: str) -> bool:
    current = 3
    for idx in range(3):
        if s1[idx] not in s2:
            current -= 1
    # print(s1, s2, current)
    return current > 0


def funnel(first: str, second: str) -> bool:
    """
    Given two strings of letters, determine whether the second can be made
    from the first by removing one letter. The remaining letters must stay in
    the same order.
    """

    for index, _ in enumerate(first):
        word = ''.join([x for i, x in enumerate(first) if i != index])
        if second == word:
            return True
    return False


def bonus(word: str) -> List[str]:
    """
    Given a string, find all words from the enable1 word list that can be made
    by removing one letter from the string. If there are two possible letters you
    can remove to make the same word, only count it once. Ordering of the output
    words doesn't matter.
    """
    results = list()
    # for line in yield_word():
    for line in WORDS[len(word)-1]:
        if quick_reject(word, line):
            if funnel(word, line):
                results.append(line)

    # sorted only to be make testing easier
    return sorted(results)


assert funnel("leave", "eave") is True
assert funnel("reset", "rest") is True
assert funnel("dragoon", "dragon") is True
assert funnel("eave", "leave") is False
assert funnel("sleet", "lets") is False
assert funnel("skiff", "ski") is False

assert bonus("dragoon") == ["dragon"]
assert bonus("boats") == sorted(["oats", "bats", "bots", "boas", "boat"])
assert bonus("affidavit") == []


if __name__ == "__main__":
    for word in WORDS[5]:
        # if len(word) >= 5:
            result = bonus(word)
            if len(result) >= 5:
                print(word, result)
