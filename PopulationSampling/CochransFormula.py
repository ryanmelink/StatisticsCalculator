# Cochran’s Sample Size Formula
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared


# = ((Z-Value)^2 * (p) * (q)) / (e)^2


def cochran(p, q, z, e):
    try:
        data1 = multiplication(p, q)
        data2 = squared(z)
        data3 = multiplication(data1, data2)
        data4 = squared(e)
        return division(data3, data4)

    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Check data inputs")
