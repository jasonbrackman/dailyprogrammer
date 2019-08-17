# python 3.6.0

from typing import List
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t = time.process_time()
        result = func(*args, **kwargs)
        elapsed_time = time.process_time() - t
        print(f"[{func.__name__}()] Elapsed Time: {elapsed_time:06f}")

        return result

    return wrapper


def yield_word():
    with open(r'./data/enable1.txt', 'rt') as lines:
        for line in lines:
            yield line.strip()


@timeit
def create_cache(courseness=10):
    """
    :param courseness: # you can overfit for the list, higher/lower # creates more to search
    :return:
    """
    cache = dict()
    for word in yield_word():
        # set up a dict that contains quick lookup of:
        #   [len][prefix][words]
        word_length = len(word)
        count = cache.setdefault(word_length, {})
        alpha = count.setdefault(word[0:courseness], [])
        alpha.append(word)
    return cache


MAGIC = 10  # used in other areas of script
WORDS = create_cache(courseness=MAGIC)


def funnel(first: str, second: str) -> bool:
    """
    Given two strings of letters, determine whether the second can be made
    from the first by removing one letter. The remaining letters must stay in
    the same order.
    """

    for index in range(len(first)):
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
    char_count = len(word) - 1
    search_section = WORDS[char_count]

    word_list = []

    prefix = word[0:MAGIC+1]
    for i in range(MAGIC+1):
        pfx = list(prefix)
        if i < len(pfx):
            pfx[i] = ''
        pfx = ''.join(pfx)
        word_list += search_section.get(pfx, [])

    results = [word2 for word2 in set(word_list) if funnel(word, word2)]

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


@timeit
def bonus2() -> int:
    count = 0
    for word in yield_word():
        if len(word) >= 5 and len(word)-1 in WORDS:
            result = bonus(word)
            if len(result) >= 5:
                count += 1
                print(f"[{count:02}] {word}: {result}")

    return count


if __name__ == "__main__":
    # best on my laptop is ~3.5s
    assert bonus2() == 28
