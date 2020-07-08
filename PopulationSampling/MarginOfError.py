from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Squared_root import squared_root
from StatCalculator.StandardDev import standard_deviation

#Margin of Error = (σ / (√n)) * z


def margin(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        data = [a, b, c, d, e]

        n = len(data)
        stand_dev = standard_deviation(a, b, c, d, e)
        sqr_n = round(squared_root(n), 2)
        value1 = stand_dev / sqr_n
        z = int(1.96)
        result = round((value1 * z), 1)
        return result

    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")