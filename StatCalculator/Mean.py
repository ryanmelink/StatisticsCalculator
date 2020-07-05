from Calculator.Addition import addition
from Calculator.Division import division

def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = addition(total, num)
    return division((len(list_of_nums)), total)
