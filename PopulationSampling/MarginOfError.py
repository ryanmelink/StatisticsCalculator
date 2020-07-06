from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared_root import squared_root

#Margin of Error = (σ / (√n)) * z

def margin_of_error(n, x, s):
    try:
        z_value = 1.96
        n1 = squared_root(n)
        n2 = division(n1, s)
        n3 = multiplication(n2, z_value)
        return round(float(n3), 2)
    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")