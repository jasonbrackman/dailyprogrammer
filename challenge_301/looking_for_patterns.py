import itertools


def search_for_pattern(pattern, word):
    if len(word) < len(pattern):
        return False

    repetition_pattern, usage_pattern = get_repetition_and_usage_as_strings(pattern.strip())
    repetition_word, usage_word = get_repetition_and_usage_as_strings(word.strip())

    if repetition_pattern not in repetition_word:
        return False
    else:
        start = repetition_word.index(repetition_pattern)
        end = len(repetition_word)
        did_match, _ = match_pattern(usage_pattern, usage_word[start:end])
        return did_match


def get_repetition_and_usage_as_strings(pattern):
    _test_pattern = [list(g) for k, g in itertools.groupby(pattern.strip())]

    _test_nums = (''.join([str(len(item)) for item in _test_pattern]),
                  ''.join([item[0] for item in _test_pattern])
                  )

    return _test_nums


def match_pattern(pattern, string):
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
    print(search_for_pattern('', 'nasoe'))
