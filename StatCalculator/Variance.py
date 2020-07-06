from Calculator.Squared import squared
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from StatCalculator.Mean import mean

def variance(data):
    try:
        calculateMean = mean(data)
        distanceArray = []
        meanDeviationValue = 0

        for item in data:
            distanceArray.append(abs(subtraction(item, calculateMean)))

        num_values = len(data)
        x = 0
        for i in distanceArray:
            x = x + squared(i)
        return int(division(num_values, x))
        #may need to switch the values for division
    except ZeroDivisionError:
        print("Error! Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")
