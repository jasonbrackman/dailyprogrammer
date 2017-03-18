import string
import argparse
import collections


def is_anagram(word, anagram):
    source = collections.Counter(letter for letter in word.lower() if letter in string.ascii_lowercase)
    target = collections.Counter(letter for letter in anagram.lower() if letter in string.ascii_lowercase)
    if len(source) == len(target):
        for k, v in target.items():
            if source[k] != v:
                return False
        return True
    return False


def interface():
    parser = argparse.ArgumentParser(description='Check if one word is an anagram for another.')
    parser.add_argument('-w', '--word', help='Original Word', required=True)
    parser.add_argument('-?', '--operator', help='is anagram of operator', required=True)
    parser.add_argument('-a', '--anagram', help='Anagram based on the word', required=True)

    args = parser.parse_args()
    return is_anagram(args.word, args.anagram)

if __name__ == "__main__":
    interface()
