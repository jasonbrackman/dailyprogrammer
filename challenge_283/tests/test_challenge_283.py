import sys
import pytest
from challenge_283 import anagram_detector

@pytest.mark.parametrize('phrase, anagram, expected', [("Clint Eastwood", "Old West Action", True),
                                                       ("parliament", "partial man", False)])

def test_verify_anagram(phrase, anagram, expected):
    result = anagram_detector.is_anagram(phrase, anagram)
    assert result is expected


@pytest.mark.parametrize('input, expected',
                         [(['wisdom', '?', 'mid sow'], True), (['Seth Rogan', '?', 'Gathers No'], True),
                          (['Reddit', '?', 'Eat Dirt'], False), (['Schoolmaster', '?', 'The classroom'], True),
                          (['Astronomers', '?', 'Moon starer'], False),
                          (['Vacation Times', '?', "I'm Not as Active"], True),
                          (['Dormitory', '?', 'Dirty Rooms'], False)])
def test_interface(input, expected):
    args = ['-', '-w', input[0], '-{} +'.format(input[1]), '-a', input[2]]
    sys.argv = args
    result = anagram_detector.interface()

    assert result is expected