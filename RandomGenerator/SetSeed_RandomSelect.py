#Set a seed and randomly.select the same value from a list

from random import seed
from RandomGenerator.Select_RandomItem import SelectRandomItem

class SetSeedRandomSelect:

    @staticmethod
    def set_random_seed_select(thelist, ranges, nut):
        seed(nut)
        thelist2 = SelectRandomItem.select_random_item(thelist, ranges)
        return thelist2
