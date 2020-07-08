#Select N number of items from a list with a seed

from random import randint
from random import seed

class ListItemWithSeed:
    @staticmethod
    def list_items(the_list, nut):
        seed(nut)
        length = len(the_list)
        position = randint(0, length-1)
        return the_list[position]
