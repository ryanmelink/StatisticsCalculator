import unittest
from StatCalculator.Statistics import Statistics
from CSVReader.CSVReader import CSVReader
from pprint import pprint



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Statistics = Statistics()

    # To test instantiation of calculator class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.Statistics, Statistics)

    #Testing mean
    def test_mean(self):
        test_data = CSVReader('/Tests/Data_Statistics/Mean_Data.csv').data
        for row in test_data:
            self.assertEqual(self.Statistics.mean(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Mean']))
            self.assertEqual(self.Statistics.result, float(row['Mean']))
        test_data.clear()

    #Testing median
    def test_median(self):
        test_data = CSVReader('/Tests/Data_Statistics/Median_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.Statistics.median(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), float(row['Median']))
            self.assertEqual(self.Statistics.result, float(row['Median']))
        test_data.clear()

    #Testing mode
    def test_mode(self):
        test_data = CSVReader('/Tests/Data_Statistics/Mode_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.Statistics.mode(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), int(row['Mode']))
            self.assertEqual(self.Statistics.result, int(row["Mode"]))
        test_data.clear()

    #Testing variance (population)
    def test_variance(self):
        test_data = CSVReader('/Tests/Data_Statistics/Variance_Data.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.Statistics.variance(row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']), round(float(row['Variance']), 2))
            self.assertEqual(self.Statistics.result, round(float(row['Variance']), 2))
        test_data.clear()
