from Calculator.Calculator import Calculator
from PopulationSampling.CochransFormula import cochran
from PopulationSampling.FindSampleSize import find_sample_size
from PopulationSampling.RandomSampling import random_sampling

class PopSampling(Calculator):
    data = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []

    def __init__(self):
        super().__init__()

    def cochran(self, data1, data2, data3, data4):
        self.result = cochran(data1, data2, data3, data4)
        return self.result

    def find_sample_size(self, data):
        self.result = find_sample_size(data)
        return self.result

    def random_sampling(self, x, y):
        self.result = random_sampling(x, y)
        return self.result

    pass
