#Generate a random number with a seed between a range of two numbers - Both Integer and Decimal

from random import seed
from random import randint
from random import uniform

class GenNumWithSeed:

    @staticmethod
    def random_int(a, b, nut):
        seed(nut)
        if isinstance(a, float):
            return GenNumWithSeed.random_float
        return randint(a, b)

    @staticmethod
    def random_float(a, b, nut):
        seed(nut)
        return uniform(a, b)
