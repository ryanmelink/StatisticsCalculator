#Select N number of items from a list without a seed

from random import randint

class ListItemNoSeed:
    @staticmethod
    def list(series):
        length = len(series)
        position = randint(0, length-1)
        return series[position]