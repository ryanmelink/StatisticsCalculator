from Calculator.Calculator import division
from StatCalculator.StandardDev import standard_deviation

#Z-Score is the score minus the mean score (score - mean score) divided by the standard deviation

def z_score(score, stdev, meanscore):
    try:
        score = int(score)
        stdev = int(stdev)
        meanscore = int(meanscore)

        #Score minus mean score
        difference = (score-meanscore)

        #Divide by Standard Deviation
        result = division(stdev, difference)

        return round(result, 2)

    except ZeroDivisionError:
        print("Error!  Cannot divide by 0")
    except ValueError:
        print("Error! Invalid data inputs")
