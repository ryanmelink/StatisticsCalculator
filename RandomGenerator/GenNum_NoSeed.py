#Generate a random number without a seed between a range of two numbers - Both Integer and Decimal

from random import randint
from random import uniform

class GenNumNoSeed:

    @staticmethod
    def random_int(a, b):
        if isinstance(a, float):
            return GenNumNoSeed.random_float
        return randint(a, b)

    @staticmethod
    def random_float(a, b):
        return uniform(a, b)
