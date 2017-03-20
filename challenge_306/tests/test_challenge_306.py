import pytest
from challenge_306 import gray_code


def test_convert_int_to_binary_array():
    tests = [1, 5, 10, 23, 44, 60, 128, 100234]
    expected = ['1', '101', '1010', '10111', '101100', '111100', '10000000', '11000011110001010']
    for test, expect in zip(tests, expected):
        value = gray_code.convert_int_to_binary_array(test)
        value = ''.join(value)
        assert value == expect


def test_gen_gray_code():
    tests = [1, 3, 5]
    expected = [1, 10, 111]
    for test, expect in zip(tests, expected):
        value = gray_code.gen_gray_code(test)
        value = int(''.join(str(v) for v in value))
        assert value == expect

