import unittest
from PopulationSampling.PopSampling import PopSampling
from CSVReader.CSVReader import CSVReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.PopSampling = PopSampling()

    # To test instantiation of PopSampling class
    def test_instantiate_statistics_calculator(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    # Testing Cochran
    def test_cochran(self):
        test_data = CSVReader('/Tests/Data_PopSampling/Cochran_Data.csv').data
        for row in test_data:
            #pprint(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']))
            self.assertEqual(self.PopSampling.cochran(row['Z'], row['p'], row['q'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopSampling.result, int(row['Sample']))
        test_data.clear()

    # Testing FindSample
    def test_find_sample_size(self):
        test_data = CSVReader('/Tests/Data_PopSampling/FindSample_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopSampling.find_sample_size(row['P'], row['q'], row['za2'], row['e']), int(row['Sample']))
            self.assertEqual(self.PopSampling.result, int(row['Sample']))
        test_data.clear()


    # Testing ConfidenceInterval
    def test_conf_int(self):
        test_data = CSVReader('/Tests/Data_PopSampling/ConfInt_Data.csv').data
        for row in test_data:
            self.assertEqual(self.PopSampling.conf_int(row['a'], row['b'], row['c'], row['d'], row['e']), float(row['ConfInt']))
            self.assertEqual(self.PopSampling.result, float(row['ConfInt']))
        test_data.clear()
