import unittest
from PopulationSampling.PopSampling import PopSampling
from CSVReader.CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    test_CochranFormula = CSVReader('Tests/Data_PopSample/CochranFormula_Test.csv').data
    test_FindSampleSize = CSVReader('')
    test_ConfidenceInterval = CSVReader('')
    test_MarginOfError = CSVReader('')
    test_RandomSampling = CSVReader('')

    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_popsample(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_Cochran(self):
        for row in self.test_CochranFormula:
            self.assertEqual(self.PopSampling.cochran(float((row['p'])), float(row['q']), float(row['z']), float(row['e'])),float(row['a']))
            self.assertEqual(self.PopSampling.result, float(row['a']))

    #def test_confidence_interval(self):
        for row in self.test_ConfidenceInterval:

    #def test_find_sample_size(self):
        for row in self.test_FindSampleSize:

    #def test_margin_of_error(self):
        for row in self.test_MarginOfError:

    #def test_random_sampling(self):
        for row in self.test_RandomSampling:
            series = [row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']]







if __name__ == '__main__':
    unittest.main()
