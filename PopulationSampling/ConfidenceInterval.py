from StatCalculator.StandardDev import standard_deviation
from StatCalculator.Mean import mean
from Calculator.Squared_root import squared_root

#Confidence Interval For a Sample
#X  ±  Z (s/√n)

def conf_int(a, b, c, d, e):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        data = [a, b, c, d, e]

        n = len(data)
        z = int(1.96)
        x = mean(a, b, c, d, e)
        s = standard_deviation(a, b, c, d, e)

        num1 = squared_root(n)
        num2 = s / num1
        num3 = z * num2
        result = round((x - num3), 2)
        return result

    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")
