import unittest
from main import BankInterest

class TestBankInterest(unittest.TestCase):
    def test_annual_interest(self):
        bank = BankInterest(100000, 2, 10)
        expected_annual_interest, expected_total = bank.ann_int()
        self.assertEqual(len(bank.ann_int()), 2)
        self.assertAlmostEqual(expected_annual_interest, 4614.49, places=2)
        self.assertAlmostEqual(expected_total, 110747.82, places=2)

    def test_difference_in_interest(self):
        bank = BankInterest(100000, 2, 10)
        arr, total = bank.diff_int()
        self.assertEqual(len(arr), 24)
        self.assertAlmostEqual(total, 110416.67, places=2)

if __name__ == '__main__':
    unittest.main()
