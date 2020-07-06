### Find a Sample Size (without Standard Deviation)
To do this, you will need to calculate certain variables which will allow you to ultimately determine your sample size.

### Example
**41%** of Jacksonville residents said they have been in a hurricane.  How many adults should be surveyed to estimate the true proportion of adults who have been in a hurricane?
 * Confidence Interval = 95%
 * Width = 6%

Follow the below steps to find a sample size using only the Confidence Interval and Width

#### Step 1 - Determine the necessary variables
**Za2**:  Divide the Confidence Interval (95%) by 2 and use the value to lookup the area in the Z-table.

    za2 = 0.95 / 2
    za2 = 0.475
    za2 = 1.96
    
*Za2 = **1.96** because it is the closest z-score*
    
**E(Margin of Error)**: Divide the width (6%) by 2

    E = 0.06 / 2
    E = 0.03

**^p**: Use the provided percentage (41%)

    ^p = 0.41

**^q**: Subtract ^p(0.41) from 1

    ^q = 1 - 0.41
    ^q = 0.59
    
#### Step 2 - Multiply ^p by ^q

    = 0.41 * 0.59
    = 0.2419
    
#### Step 3 - Divide Za2 by E

    = 1.96 / 0.03 = 65.3333
    
#### Step 4 - Square the Value from Step 3

    = 65.3333 * 65.3333
    = 4268.4444
    
#### Step 5 - Multiply Step 2 by Step 4

    = 0.2419 * 4268.4444
    = 1032.536
    
**1,032** adults should be surveyed
