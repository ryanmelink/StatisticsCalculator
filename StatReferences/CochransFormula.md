### What is a Cochran's Sample Size Formula?
The Cochran Formula allows you to calculate an ideal sample size given a *desired level of precision*, and the estimated proportion of the attribute present in the population.

The *desired level of precision* is also known as the "Margin of Error".


### The Cochran Formula

https://www.statisticshowto.com/wp-content/uploads/2018/01/cochran-1.jpeg

e = Margin of Error (the desired level of precision)
p = the estimated proportion of the population which has the attribute
q = 1 - p

*The z-value is found in a Z Table*

### Example Equation

You are performing a study on the inhabitants of a large town, and want to determine how many households serve breakfast in the mornings

We will assume that half of the families serve breakfast, which gives us the "maximum variability".

    p = 0.5
    q = 1 - 0.5
    
We want to have 95% confidence, and at least +/- 5% (0.05) precision.

*95% Confidence Level gives a Z-Value of **1.96**.*
 
    = ((Z-Value)^2 * (p) * (q)) / (e)^2
    = ((1.96)^2) * (0.5) * (1 - 0.5)) / (0.05)^2
    = ((3.84) * (0.5) * (0.5)) / (0.0025)
    = 0.96 / 0.0025
    = 384

A random sample of **384** households in your target population should be enough to give you the confidence levels needed.


### Functions Used in Cochran's Formula

 * Calculator
   * Subtraction
   * Multiplication
   * Division
   * Square
 



[Link to Statisticshowto.com](https://www.statisticshowto.com/probability-and-statistics/find-sample-size/#Cochran)