import unittest
from PopulationSampling.PopSampling import PopSampling
from CSVReader.CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    test_CochranFormula = CSVReader('Tests/Data_PopSample/CochranFormula_Test.csv').data
    test_FindSampleSize = CSVReader('Tests/Data_PopSample/FindSampleSize_Test.csv').data
    test_ConfidenceInterval = CSVReader('Tests/Data_PopSample/ConfidenceInterval_Test.csv').data
    test_MarginOfError = CSVReader('Tests/Data_PopSample/MarginOfError_Test.csv').data
    test_RandomSampling = CSVReader('Tests/Data_PopSample/RandomSampling_Test.csv').data

    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_popsample(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_Cochran(self):
        for row in self.test_CochranFormula:
            self.assertEqual(
                self.PopSampling.cochran(float((row['p'])), float(row['q']), float(row['z']), float(row['e'])),
                float(row['a']))
            self.assertEqual(self.PopSampling.result, float(row['a']))

    def test_confidence_interval(self):
        for row in self.test_ConfidenceInterval:
            list = []
            for keys in row.keys():
                if keys == "ci":
                    continue
                list.append(int(row[keys]))
            self.assertEqual(self.PopSampling.confidence_interval(list), str(row['ci']))

    def test_find_sample_size(self):
        for row in self.test_FindSampleSize:
            self.PopSampling.find_sample_size(float(row['p']), float(row['q']), float(row['E']))
            self.assertEqual(self.PopSampling.result, (row['Sample']))

    def test_margin_of_error(self):
        for row in self.test_MarginOfError:
            self.PopSampling.margin_of_error(int(row['n']), int(row['x']), int(row['s']))
            self.assertEqual(self.PopSampling.result, float(row['MargErr']))

    def test_random_sampling(self):
        for row in self.test_RandomSampling:
            series = [row['Value1'], row['Value2'], row['Value3'], row['Value4'], row['Value5']]
            value = self.PopSampling.random_sampling(series, int(row['Choose']))
            self.assertEqual(len(value), int(row['Choose']))


if __name__ == '__main__':
    unittest.main()
