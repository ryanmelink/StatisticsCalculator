#Select a random item from a list

from random import randint

class SelectRandomItem:

    @staticmethod
    def select_random_item(alist):
        length=len(alist)
        position = randint(0, length-1)
        return alist[position]
