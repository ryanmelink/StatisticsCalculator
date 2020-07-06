#How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

from Calculator.Squared_root import squared_root
from StatCalculator.Mean import mean

def find_sample_size(num):
    try:
        num_values = len(num)
        z = 1.96
        stand_dev = 15
        avg = mean(num)
        return round(avg + (z * stand_dev / squared_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error! Can't Divide by 0")
    except ValueError:
        print("Error! Check your data inputs")