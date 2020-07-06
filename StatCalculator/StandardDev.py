from Calculator.Squared_root import squared_root
from StatCalculator.Variance import variance


def stand_dev(num):
    try:
        variance_float = variance(num)
        x = round(squared_root(variance_float), 5)
        return int(x)
    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")