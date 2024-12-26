import unittest
from main import Calculate

class TestCalculate(unittest.TestCase):
    def test_annual_interest(self):
        calc = Calculate(100000, 2, 10)
        expected_annual_interest, expected_total = calc.ann_int()
        self.assertEqual(len(calc.ann_int()), 2)
        self.assertAlmostEqual(expected_annual_interest, 4614.49, places=2)
        self.assertAlmostEqual(expected_total, 110747.82, places=2)

    def test_difference_in_interest(self):
        calc = Calculate(100000, 2, 10)
        arr, total = calc.diff_int()
        self.assertEqual(len(arr), 24)
        self.assertAlmostEqual(total, 110416.67, places=2)
        # assert 1 == 0

if __name__ == '__main__':
    unittest.main()
