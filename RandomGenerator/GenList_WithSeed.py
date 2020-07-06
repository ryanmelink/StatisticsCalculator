#Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
from random import seed
from random import randint
from random import uniform


class GenListWithSeed:
    @staticmethod
    def list_int (x, y, ranges, nut):
        if isinstance(x, float):
            return list_float(x, y, ranges, nut)
        series = []
        seed(nut)
        for each in range(ranges):
            number = randint(x, y)
            series.append(number)
        return series

    @staticmethod
    def list_float (x, y, ranges, nut):
        series = []
        seed (nut)
        for each in range (ranges):
            number = uniform(x,y)
            series.append(number)
        return series


