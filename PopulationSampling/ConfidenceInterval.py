#Confidence Interval For a Sample
#X  ±  Z (s/√n)

from Calculator.Squared_root import squared_root
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from StatCalculator.Mean import mean
from StatCalculator.StandardDev import stand_dev

def confidence_interval(data):
    try:
        zvalue = 1.960
        nLen = len(data)
        nMean = mean(data)
        sd = stand_dev(data)
        conf_int = multiplication(zvalue, (division(squared_root(nLen), sd)))
        x = round(float(conf_int), 1)
        return str(str(nMean) + "+" + str(x))

    except ZeroDivisionError:
        print("Error! Cannot Divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")

