import itertools


def search_for_pattern(pattern, word):
    """
    Breaks down a string into a series of character representations to then see if the same pattern is
    repeated in the string word passed in.  This is looking for a pattern match and not a specific
    character  to character match.

    :param pattern: Repeating characters to compare against the given word
    :param word: Word to determine if it matches given pattern
    :return: bool
    """
    if len(word) < len(pattern):
        return False

    repetition_pattern, usage_pattern = get_repetition_and_usage_as_strings(pattern.strip())
    repetition_word, usage_word = get_repetition_and_usage_as_strings(word.strip())

    if repetition_pattern not in repetition_word:
        return False
    else:
        start = repetition_word.index(repetition_pattern)
        end = start + len(repetition_pattern)
        did_match, _ = match_pattern(usage_pattern, usage_word[start:end])
        return did_match


def get_repetition_and_usage_as_strings(string):
    """
    Breaks down words into a basic pattern of how many times a character is interupted followed by the
    character. So 'aaba' becomes '2a1b1a'.
    This is then split into its repetition ID and character structure, like '211', 'aba'.
    :param string:
    :return: tuple -> repetition id string and characters used string
    """
    _test_pattern = [list(g) for k, g in itertools.groupby(string.strip())]

    _test_nums = (''.join([str(len(item)) for item in _test_pattern]),
                  ''.join([item[0] for item in _test_pattern])
                  )

    return _test_nums


def match_pattern(pattern, string):
    """
    Attempts to find and replace each letter in a string based on a pattern string.
    - both the pattern and the string are the same length
    - pattern characters are only replaced once, so a pattern of 'aaabaaa'
    :param pattern: A series of characters, 'xxyx', 'xyx', xyzxyy'
    :param string: Any string of characters 'jason', 'arbitrary', 'seeking', 'gibberish'
    :return: bool, mangled string used to determine pattern match
    """
    assert len(pattern) == len(string), "Expected same length strings, but received {}, {}".format(pattern, string)
    seen = []
    for index, character in enumerate(pattern):
        if character not in seen:
            string = string.replace(string[index], character)
            seen.append(character)

    pattern_matched = True if pattern in string else False

    return pattern_matched, string


def main():
    pattern = 'XXYYX'
    with open('words.txt', 'rt') as handle:
        for word in handle:
            if search_for_pattern(pattern, word):
               print(word.strip())


if __name__ in "__main__":
    main()

