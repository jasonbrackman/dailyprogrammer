import string
from collections import Counter
from itertools import combinations_with_replacement, permutations

def smorse(text):
    morse = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
    smorse_map = dict(zip(string.ascii_lowercase, morse))
    return ''.join([smorse_map[x] for x in text.lower()])


assert(smorse("sos") == "...---...")
assert(smorse("daily") == "-...-...-..-.--")
assert(smorse("programmer") == ".--..-.-----..-..-----..-.")
assert(smorse("bits") == "-.....-...")
assert(smorse("three") == "-.....-...")


with open(r'./data/enable1.txt', 'rt') as handle:
    results = {line.strip(): smorse(line.strip()) for line in handle}


def get_pattern(of_length):
    for k, v in results.items():
        for part in v.split('.'):
            if len(part) == of_length:
                return k, v


def get_balanced(of_length=1):
    for k, v in results.items():
        if len(k) == of_length and len(v) % 2 == 0:
            dots = v.count('.')
            dash = v.count('-')
            if dots == dash and k != "counterdemonstrations":
                return k, v


def get_palindrome(of_length=1):
    for k, v in results.items():
        if len(k) == of_length:
            if v == ''.join(reversed(v)):
                return k, v


def find_sequences_not_in_results(of_length=1):
    sequences = []
    for i in range(2 ** of_length):
        b = bin(i)[2:].zfill(of_length)  # Converts i to binary (gets a zero-padded string)
        b = b.replace('0', '.').replace('1', '-')
        sequences.append(b)

    short_list = set([v for v in results.values() if len(v) >= of_length])

    for word in short_list:
        for s in sequences:
            if s in word:
                sequences.remove(s)

    return sequences


count = Counter(results.values())
print(f"Bonus #1: {count.most_common(1)}")
print(f"Bonus #2: {get_pattern(15)}")
print(f"Bonus #3: {get_balanced(of_length=21)}")
print(f"Bonus #4: {get_palindrome(of_length=13)}")
print(f"Bonus #5: {find_sequences_not_in_results(of_length=13)}")
