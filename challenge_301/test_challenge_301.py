import pytest
import looking_for_patterns


@pytest.fixture(scope='session')
def words():
    with open('words.txt', 'rt') as handle:
        words_ = [word.strip() for word in handle]

    return words_


@pytest.mark.parametrize('pattern, expected', [
    ('XXYY', ['aarrgh', 'aarrghh', 'addressee', 'addressees', 'balloons', 'belleek']),
    ('XXYYZZ', ['bookkeeper', 'bookkeepers', 'bookkeeping', 'bookkeepings']),
    ('XXYYX', ['addressees', 'betweenness', 'betweennesses', 'colessees', 'fricassees', 'greenness',
               'greennesses', 'heelless', 'keelless', 'keenness', 'keennesses', 'lessees', 'wheelless'])
])
def test_search_for_pattern(words, pattern, expected):
    results = [word for word in words if looking_for_patterns.search_for_pattern(pattern, word) is True]
    for item in expected:
        assert item in results
