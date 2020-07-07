#How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

#Sample Size = (^p * ^q) * (Za2 / E)^2

from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Squared import squared

def find_sample_size(p, q, w):
    try:
        za2 = 1.96
        E = division(w, 2)
        data1 = multiplication(p, q)
        data2 = division(za2, E)
        data3 = squared(data2)
        return float(multiplication(data1, data3))

    except ZeroDivisionError:
        print("Error! Can't Divide by 0")
    except ValueError:
        print("Error! Check your data inputs")