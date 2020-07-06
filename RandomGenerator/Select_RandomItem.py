#Select a random item from a list

from random import randint

class SelectRandomItem:

    @staticmethod
    def select_random_item(thelist, ranges):
        list2 = []
        length=len(thelist)
        for each in range(ranges):
            position = randint(0, length-1)
            thelist.append(thelist[position])
        return list2
