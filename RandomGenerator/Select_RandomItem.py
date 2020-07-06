#Select a random item from a list

from random import randint

class SelectRandomItem:

    @staticmethod
    def select_random_item(thelist):
        length=len(thelist)
        position = randint(0, length-1)
        return thelist[position]
