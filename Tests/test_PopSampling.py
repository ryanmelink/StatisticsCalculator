import unittest
from PopulationSampling.PopSampling import PopSampling
from CSVReader.CSVReader import CSVReader

class MyTestCase(unittest.TestCase):
    test_CochranFormula = CSVReader('Tests/Data_PopSample/CochranFormula.csv').data

    def setUp(self):
        self.PopSampling = PopSampling()

    def test_instantiate_popsample(self):
        self.assertIsInstance(self.PopSampling, PopSampling)

    def test_Cochran(self):
        for row in self.test_CochranFormula:
            self.assertEqual(self.PopSampling.cochran(float((row['p'])), float(row['q']), float(row['z']), float(row['e'])), float(row['a']))
            self.assertEqual(self.PopSampling.result, float(row['a']))
