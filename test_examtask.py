from datetime import datetime, timedelta
import unittest
from examtask import days_until_new_year

class TestDaysUntilNewYear(unittest.TestCase):

    def test_days_until_new_year(self):
        days_left = days_until_new_year()
        self.assertGreaterEqual(days_left, 0)

    def test_days_until_new_year_with_mocked_date(self):
        mocked_current_date = datetime(2022, 12, 20)
        days_left = days_until_new_year(mocked_current_date)
        self.assertEqual(days_left, 12)  # Якщо сьогодні 20 грудня, то до нового року залишиться 12 днів

if __name__ == '__main__':
    unittest.main()
