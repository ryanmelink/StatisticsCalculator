# How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

from Calculator.Squared import squared
from Calculator.Multiplication import multiplication
from Calculator.Division import division


# Sample Size = (^p * ^q) * (Za2 / E)^2


def find_sample_size(p, q, za2, e):
    try:
        p = float(p)
        q = float(q)
        za2 = float(za2)
        e = float(e)

        num1 = multiplication(p, q)
        num2 = division(e, za2)
        num3 = squared(num2)
        result = multiplication(num1, num3)
        return result

    except ZeroDivisionError:
        print('Error! Cannot divide by 0')
    except ValueError:
        print('Error! Invalid data entry')
