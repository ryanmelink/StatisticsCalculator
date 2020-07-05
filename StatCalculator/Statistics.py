from Calculator.Calculator import Calculator
from StatCalculator.Mean import mean


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, list_of_nums):
        self.result = mean(list_of_nums)
        return self.result
