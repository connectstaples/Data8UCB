#### Data8 Spring 2025
# Election Pollsters Example `0, 1` Tests
#### Sean Villegas


[Chapter](https://inferentialthinking.com/chapters/14/6/Choosing_a_Sample_Size.html)

## Review
- The Central Limit Theorem says that the probabilities for the sample proportion are roughly normally distributed.
    - centered at the population proportion of 1’s
    - with an SD equal to the SD of the population of 0’s and 1’s 
        - divided by the square root of the sample size.

- Adjusting the **Standard Deviation** will allow the `standard deviation / √sample size` to change the bins in a histogram. E.g.
    - A population has average 70 and SD 10. One of the histograms below is the empirical distribution of the averages of 10000 random samples of size 100 drawn from the population. Which one? 

    - Steps for above problem
        - Look at the bins
        - See which one is skewed 
        - Adjust the SD to match the bins
        - Average will stay the same

- Look at the other options, how can I change the question statement to make the wrong questions right? Prof Sanchez writes it in that logic 
- The Central Limit Theorem is a statement about averages
- Prof is allergic to reporting one number, so you use the Confidence Interval 

## New Material 

**Proportions are averages** 
`data = [0, 1, 0, 0, 1, 0, 1, 1, 0, 0]`

Representing the above data:
- Sum: 4 
- Average: 0.4 (proportion of `1`'s)

_If the population consists of 1s and 0s:_ 
- the population average is the proportion of 1s in the population.
- The sample average is the proportion of 1s in the sample

**How many Standard Deviations long is the 95% Confidence Interval?**
_a line bar with 5 total confidence interval bars_
- When asked this question, subtract 1 by the bars in the number line and you will have how _**long**_ it is 

## Finding the total width of an interval 
_say you had a Confidence Interval of 4 **AND** you wanted a total interval width of 0.01_

`4 * population standard deviation / √sample size` 

**How do you choose the sample size given an interval width?**
_quick maths steps_
```
1. 0.01 = 4 * population standard deviation / √sample size

2. √sample size = 4 * population standard deviation / 0.01
```

Last Step: 
3. sample size = (4 * population SD / 0.01)<sup>2</sup>

## Applying with 0/1 Data
_the SD of 0/1 population is at most 0.5_

sample size ≥ (4 * 0.5/0.01)<sup>2</sup>

- Which equals: `40000`


## Election Demo 

- the `Margin of Error` is half the width of the Confidence Interval on the number line 

**Question**: How can a poll of only 1,004 Americans represent 260 million people only a 3 percent margin of error? 

- Assume a 95% confidence level, the `confidence interval` is **4** Standard Deviations long 
- Our sample size is **1004**
- The standard deviation is at most **0.5**

The above observations imply:

1. width = 4 * 0.5/√1004 => 0.063

_Furthermore_

2. width = (4 * 0.5/√1004)<sup>2</sup> => 0.315 => Roughly 3 percent margin of error



_choosing a sample size given an interval width_ 
```python
# population of size 10

number_of_ones = 2
zero_one_population = np.append(np.ones(number_of_ones), np.zeros(10 - number_of_ones))

print('Standard Deviation:', np.round(np.std(zero_one_population),2))

"""
Output from np.ones/np.zeros function

Standard Deviation: 0.4

array([ 1.,  1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
"""
```

_function that does above_ 

```python
def sd_of_zero_one_population(number_of_ones):
    """Returns the SD of a population 
    that has 10 elements: num_ones with value 1 and (10 - num_ones) with value 0"""
    zero_one_population = np.append(np.ones(number_of_ones), 
                                    np.zeros(10 - number_of_ones))
    return np.std(zero_one_population)

possible_ones = np.arange(11)
zero_one_pop = Table().with_columns(
    'Number of Ones', possible_ones,
    'Proportion of Ones', possible_ones / 10
)

sds = zero_one_pop.apply(sd_of_zero_one_population, 'Number of Ones')
zero_one_pop = zero_one_pop.with_column('Pop SD', sds)


zero_one_pop.scatter('Proportion of Ones', 'Pop SD')
# data will be quadrapuling, the data appears to be the tallest when half of the data is 1, and half of the data is 0. The population standard deviation is 0.5 
```

- The above functions will show how we can understand what the `0/1 population SD` is in the following equations

