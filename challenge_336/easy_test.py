import unittest
from challenge_336 import easy

class Cannibal(unittest.TestCase):
    input_ = """7 2
    21 9 5 8 10 1 3
    10 15
    """

    def test_format_input(self):
        queries, values = easy.format_input(self.input_)
        assert queries == [10, 15]
        assert values == [21, 10, 9, 8, 5, 3, 1]

    @staticmethod
    def test_collect_combined_values():
        results = easy.get_results([10], [21, 10, 9, 8])
        assert results[10] == [1, 1, 1], "Got: {}".format(results[10])

    @staticmethod
    def test_collect_combined_values_longer():
        results = easy.get_results([10], [21, 10, 9, 8, 7, 1, 2])
        assert results[10] == [1, 1, 1, 1], "Got: {}".format(results[10])


if __name__ == "__main__":
    unittest.main()