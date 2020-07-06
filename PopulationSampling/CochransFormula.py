#Cochran’s Sample Size Formula
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division

#= ((Z-Value)^2 * (p) * (q)) / (e)^2


def cochran(p, q, z, e):
    try:
        n1 = multiplication(p, q)
        n2 = z * z
        n3 = multiplication(n1, n2)
        n4 = e * e
        rCochran = division(n4, n3)
        return float(rCochran)
    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Check data inputs")