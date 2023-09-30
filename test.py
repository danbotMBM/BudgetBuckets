import unittest
import budget
from datetime import datetime

class TestBudgetMethods(unittest.TestCase):
    def test_creation(self):
        a = budget.bucket("Food", 500, budget.TF.monthly, datetime(2023, 4, 4))
        self.assertTrue(a in budget.buckets.values())
        self.assertTrue(a.name in budget.buckets.keys())

if __name__ == '__main__':
    unittest.main()