# Cochran’s Sample Size Formula
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared import squared


# = ((Z-Value)^2 * (p) * (q)) / (e)^2

def cochran(z, p, q, e):
    try:
        z = float(z)
        p = float(p)
        q = float(q)
        e = float(e)

        num1 = squared(z)
        num2 = multiplication(p, q)
        num3 = squared(e)
        num4 = multiplication(num1, num2)
        result = division(num4, num3)
        return result

    except ZeroDivisionError:
        print('Error!  Cannot divide by 0')
    except ValueError:
        print('Error! Invalid data inputs')

# Z,p,q,e,Sample
# 1.96,0.5,0.5,0.05,384


# num1 = 3.8416
# num2 = 0.25
# num3 = 0.0025
# num4 = 0.9604
# return = 384.16
