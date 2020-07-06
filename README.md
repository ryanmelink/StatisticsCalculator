# Team Project 2 - Statistics Calculator

## NJIT IS 601-850
## Group Members: Kelly Blackledge and Monica Nelson

## Travis CI
[![Build Status](https://travis-ci.com/kb8njit/StatisticsCalculator.svg?branch=master)](https://travis-ci.com/github/kb8njit/StatisticsCalculator)

### Project Plan
1. Calculator Object    
    1. Properties      
        1. Result  
    1. Math Operations Static Class  
        1. Methods  
            1. Addition   
            1. Subtraction  
            1. Multiplication  
            1. Division  
            1. Squared  
            1. Square Root  
            1. Mean  
            1. Median  
            1. Mode  
            1. Variance  
            1. Standard Deviation  
            1. Z-Score  
    1. Methods  
        1. Addition - calls static addition method    
        1. Subtraction - calls static subtraction method  
        1. Multiplication - calls static multiplication method  
        1. Division - calls static division method  
        1. Squared - calls static squared method  
        1. Square Root - calls static square root method    
        1. Mean - calls static mean method  
        1. Median - calls static median method  
        1. Mode - calls static mode method  
        1. Variance - calls static variance method  
        1. Standard Deviation - calls static standard deviation method  
        1. Z-Score - calls static z-score method  
    1. Operations Classes    
        1. Addition  
            1. Methods  
                i. Sum 2 numbers  
        1. Subtraction  
            1. Methods  
                i. Subtract 2 numbers  
        1.  Multiplication  
            1. Methods  
                i. Multiply 2 numbers  
        1. Division  
            1. Methods  
                i. Divide 2 numbers  
        1. Square  
            1. Methods  
                i. Multiply number by itself  
        1. Square Root  
            1. Methods  
                i. Take the square root of a number  
        1. Mean  
            1. Methods  
                i. Take the sum of a list of numbers and divide by the length of the list  
        1. Median  
            1. Methods  
                i. Middle number in a group of numbers organized from smallest to largest
        1. Mode  
            1. Methods  
                i. Number that appears the most often in a group of numbers 
        1. Variance  
            1. Methods  
                i. The square of the standard deviation  
        1. Standard Deviation  
            1. Methods  
                i. The square root of the sum of the difference between a group of numbers and the mean divided by the length of the list  
        1. Z-Score  
            1. Methods  
                i. Subtract one number from the mean then divide by the standard deviation  

### Task List
| To Do | In Progress | Review | Done |  
| --- | --- | --- | ---|  
| Set up Skeleton project | Kelly | 7/2/2020 | 7/2/2020 |  
| Make modules | Kelly | 7/2/2020 | 7/2/2020 |  
| Set up Travis | Kelly | 7/2/2020 | 7/2/2020|  
| Set up FileUtilities | Kelly | 7/2/2020 | 7/2/2020 |  
| Set up Dockerfile | Kelly | 7/2/2020 | 7/2/2020 |  
| Set up Requirements.txt | Kelly | 7/2/2020 | 7/2/2020 |  
| Make Development Branch | Kelly | 7/2/2020 | 7/2/2020 |  
| **MAKE CALCULATOR** | --- | --- | ---|  
| Make addition static class | Monica | 7/3/2020 | 7/3/2020 |  
| Make add method calling static class | Monica | 7/5/2020 | 7/5/2020 |  
| Test add method | Monica | 7/5/2020 | 7/5/2020 |  
| Make subtraction static class | Monica | 7/3/2020 | 7/3/2020 |
| Make subtract method calling static class | Monica | 7/5/2020 | 7/5/2020 |
| Test subtract method |  Monica | 7/5/2020 | 7/5/2020 |
| Make multiplication static class | Monica | 7/3/2020 | 7/3/2020 |
| Make multiply method calling static class | Monica | 7/5/2020 | 7/5/2020 |
| Test multiply method |  Monica | 7/5/2020 | 7/5/2020 | 
| Make division static class | Monica | 7/3/2020 | 7/3/2020 | 
| Make divide method calling static class | Monica | 7/5/2020 | 7/5/2020 |  
| Test divide method |  Monica | 7/5/2020 | 7/5/2020 |
| Make squared static class | Monica | 7/3/2020 | 7/3/2020 |  
| Make square method calling static class | Monica | 7/5/2020 | 7/5/2020 | 
| Test square method |  Monica | 7/5/2020 | 7/5/2020 |  
| Make squared root static class | Monica | 7/3/2020 | 7/3/2020 |
| Make square root method calling static class | Monica | 7/5/2020 | 7/5/2020 | 
| Test square root method |  Monica | 7/5/2020 | 7/5/2020 | 
| **MAKE STATISTICS MODULE** | --- | --- | ---| 
| Make Modules | Kelly | 7/2/2020 | 7/2/2020| 
| Make test .csv files for statistics | --- | --- | ---|  
| Test .csv files using statistics library | --- | --- | ---|
| Make mean static class | --- | --- | ---|  
| Make mean method calling static class | --- | --- | ---|  
| Test mean method | --- | --- | ---|    
| Make median static class | --- | --- | ---|  
| Make median method calling static class | --- | --- | ---|  
| Test median method | --- | --- | ---| 
| Make mode static class | --- | --- | ---|  
| Make mode method calling static class | --- | --- | ---|  
| Test mode method | --- | --- | ---| 
| Make variance static class | --- | --- | ---|  
| Make variance method calling static class | --- | --- | ---|  
| Test variance method | --- | --- | ---| 
| Make standard deviation static class | --- | --- | ---|  
| Make standard deviation method calling static class | --- | --- | ---|  
| Test standard deviation method | --- | --- | ---| 
| Make z-score static class | --- | --- | ---|  
| Make z-score method calling static class | --- | --- | ---|  
| Test z-score method | --- | --- | ---| 
**MAKE POPULATION SAMPLING MODULE** | --- | --- | ---| 
| Make Modules | Kelly | 7/5/2020 | 7/5/2020| 
| Make cochran's formula static class | --- | --- | ---|  
| Make cochran's formula method calling static class | --- | --- | ---|  
| Test cochran's formula method | --- | --- | ---|    
| Make confidence interval static class | --- | --- | ---|  
| Make confidence interval method calling static class | --- | --- | ---|  
| Test confidence interval method | --- | --- | ---| 
| Make sample size static class | --- | --- | ---|  
| Make sample size method calling static class | --- | --- | ---|  
| Test sample size method | --- | --- | ---| 
| Make margin of error static class | --- | --- | ---|  
| Make margin of error method calling static class | --- | --- | ---|  
| Test margin of error method | --- | --- | ---| 
| Make random sampling static class | --- | --- | ---|  
| Make random sampling method calling static class | --- | --- | ---|  
| Test random sampling method | --- | --- | ---| 
**MAKE RANDOM GENERATOR MODULE** | --- | --- | ---| 
| Make Modules | Kelly | 7/5/2020 | 7/5/2020| 
| Make GenList with Seed static class | Monica | 7/6/2020 | 7/6/2020 |  
| Make GenList with Seed method calling static class | Monica | 7/6/2020 | 7/6/2020 |   
| Test GenList with Seed method | Monica | 7/6/2020 | 7/6/2020 | 
| Make GenNum no Seed static class | Monica | 7/6/2020 | 7/6/2020 | 
| Make GenNum no Seed method calling static class | Monica | 7/6/2020 | 7/6/2020 | 
| Test GenNum no Seed method | Monica | 7/6/2020 | 7/6/2020 | 
| Make GenNum with Seed static class | Monica | 7/6/2020 | 7/6/2020 |   
| Make GenNum with Seed method calling static class | Monica | 7/6/2020 | 7/6/2020 |  
| Test GenNum with Seed method | Monica | 7/6/2020 | 7/6/2020 | 
| Make ListItems no Seed static class | Monica | 7/6/2020 | 7/6/2020 | 
| Make ListItems no Seed method calling static class | Monica | 7/6/2020 | 7/6/2020 |   
| Test ListItems no Seed method | Monica | 7/6/2020 | 7/6/2020 | 
| Make ListItems with Seed static class | Monica | 7/6/2020 | 7/6/2020 |   
| Make ListItems with Seed method calling static class | Monica | 7/6/2020 | 7/6/2020 |  
| Test ListItems with Seed method | Monica | 7/6/2020 | 7/6/2020 | 
| Make Select Random Item static class | Monica | 7/6/2020 | 7/6/2020 | 
| Make Select Random Item method calling static class | Monica | 7/6/2020 | 7/6/2020 |  
| Test Select Random Item method | Monica | 7/6/2020 | 7/6/2020 | 
| Make Set Seed Random Select static class | Monica | 7/6/2020 | 7/6/2020 |   
| Make Set Seed Random Select method calling static class | Monica | 7/6/2020 | 7/6/2020 |   
| Test Set Seed Random Select method | Monica | 7/6/2020 | 7/6/2020 | 

### Changelog