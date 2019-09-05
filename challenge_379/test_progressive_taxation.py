import math
import unittest
from challenge_379 import easy_progressive_taxation as progressive_taxation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEquals(progressive_taxation.tax(0), 0)

    def test_tax_10000(self):
        self.assertEquals(progressive_taxation.tax(10_000), 0)

    def test_tax_10009(self):
        self.assertEquals(progressive_taxation.tax(10_009), 0)

    def test_tax_10010(self):
        self.assertEquals(progressive_taxation.tax(10_010), 1)

    def test_tax_12000(self):
        self.assertEquals(progressive_taxation.tax(12_000), 200)

    def test_tax_30000(self):
        self.assertEquals(progressive_taxation.tax(30_000), 2000)

    def test_tax_30100(self):
        self.assertEquals(progressive_taxation.tax(30_100), 2025)

    def test_tax_56780(self):
        self.assertEquals(progressive_taxation.tax(56_789), 8697)

    def test_tax_1234567(self):
        self.assertEquals(progressive_taxation.tax(1_234_567), 473326)

    def test_overall_others(self):
        self.assertAlmostEqual(progressive_taxation.overall(0), 10_000)
        self.assertAlmostEqual(progressive_taxation.overall(0.06), 25000)
        assert math.isclose(progressive_taxation.overall(0.09), 34_375, abs_tol=1)
        assert math.isclose(progressive_taxation.overall(0.32), 256_250, abs_tol=15)
        self.assertAlmostEqual(progressive_taxation.overall(0.4), -1)


if __name__ == '__main__':
    unittest.main()
