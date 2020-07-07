#Set a seed and randomly.select the same value from a list

from random import seed
from RandomGenerator.ListItems_NoSeed import ListItemNoSeed


class SetSeedRandomSelect:

    @staticmethod
    def pick_from_list_seed(series, realm, nut):
        seed(nut)
        series2 = ListItemNoSeed.list_items(series)
        return series2
