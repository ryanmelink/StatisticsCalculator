from Calculator.Calculator import Calculator
from PopulationSampling.CochransFormula import cochran


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
