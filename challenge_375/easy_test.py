import unittest
import easy


class MyTestCase(unittest.TestCase):
    def new_number_using_strings(self):
        self.assertIsInstance(easy.new_number(0), int)

    def test_new_number_1_plus(self):
        self.assertEqual(easy.new_number(1), 2)

    def test_new_number_10_plus(self):
        self.assertEqual(101, easy.new_number(90))

    def test_new_number_1000(self):
        self.assertEqual(2111, easy.new_number(1000))

    def test_new_number_999909(self):
        self.assertEqual(10101010110, easy.new_number(999909))


if __name__ == '__main__':
    unittest.main()
