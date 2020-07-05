import unittest
from StatCalculator.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Statistics = Statistics()

    def test_instantiate_statcalculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

