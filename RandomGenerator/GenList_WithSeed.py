#Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
from random import seed
from random import randint
from random import uniform


class GenListWithSeed:
    @staticmethod
    def list_int (a, b, ranges, nut):
        if isinstance(a, float):
            return list_float(a, b, ranges, nut)
        series = []
        seed(nut)
        for each in range(ranges):
            number = randint(a, b)
            series.append(number)
        return series

    @staticmethod
    def list_float (a, b, ranges, nut):
        series = []
        seed (nut)
        for each in range (ranges):
            number = uniform(a,b)
            series.append(number)
        return series


