#Select N number of items from a list without a seed

from random import randint

class ListItemNoSeed:
    @staticmethod
    def list_items(the_list):
        length = len(the_list)
        position = randint(0, length-1)
        return the_list[position]
