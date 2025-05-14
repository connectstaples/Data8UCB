##### D8 Lec 26, Prof Sanchez 
## Normal Distribution 
#### Sean Villegas

Readings: 
- [Normal Curve & SD](https://inferentialthinking.com/chapters/14/3/SD_and_the_Normal_Curve.html)
- [Central Limit Theorem](https://inferentialthinking.com/chapters/14/4/Central_Limit_Theorem.html)


### Review

- ```where(..., contained()) # checks arrays contains a specific value or if a value is present in the array```
- The **Standard Deviation** of an array is defined as the "root mean square of the deviations" where the deviations are the difference between the original elements and their average.
- You can also use the function `np.std` to compute the SD of values in an array

## How can we quantify natural concepts like “center” and “variability”?
     Answer: Both mean and median quantify center
 -  When quantifying the center and mean:
    - You must take the **standard deviation** because it measures how **spread out** data points are around the mean.

1. Deviations from Average:
- We subtract the mean from each data point to see how far each value is from the center. This step highlights variability—whether values are close to or far from the mean.

2. Square:
- If we simply summed the deviations, positive and negative values would cancel out, leading to a misleading measure of spread. Squaring each deviation ensures all values are positive, emphasizing larger deviations more (since squaring amplifies bigger differences).

3. Mean (Variance):
- Taking the average of these squared deviations gives us the variance—a measure of average squared distance from the mean. Variance tells us about the spread but in squared units, which can be unintuitive.

4. Square Root (Standard Deviation):
- The square root brings us back to the original units of the data. This makes interpretation easier—if your data is in meters, the standard deviation is also in meters.

**Chebyshevs Inequality**

_no matter shape of distribution these rules apply, you can apply this to guesstimate bell curves as well_ 
- the proportion of values in the range “mean ± z SDs” is at least 
1 - (1/z<sup>2</sup>) 

| Range | Proportion | 
| ---  | --- |
| mean ± 2 SDs | at least 1 - 1/4 = 3/4    (75%)| 
| mean ± 3 SDs | at least 1 - 1/9 = 8/9   (88.88…%) | 
| mean ± 4 SDs | at least 1 - 1/16 = 15/16 (93.75%) | 
| mean ± 5 SDs | at least 1 - 1/25 = 24/25  (96%) | 


# New Material 
## Why do many of the empirical distributions that we generate come out bell shaped?
- If the distribution is bell shaped, almost all of the values lie within
three standard deviations from the mean

**Bell Shape and Distributions with Chebyshevs rules**
| Range | All distributions of Chebyshevs | Bell Shaped distributions
| ---  | --- | --- | 
| mean ± 1 SDs | at least 0  | about 68% | 
| mean ± 2 SDs | at least 75%  | about 95% |
| mean ± 3 SDs | at least 88.88…%  | about 99.73% |

```python
def chebyshev(num_SDs):
    # returns the least proportion of the data in +/- num_SDs
    z = num_SDs
    return 1 - 1/z**2  

chebyshev(make_array(1, 2, 3)) 
# array([ 0.        ,  0.75      ,  0.88888889])

# get the average of a column 
birth_weight_mean = np.average(births.column('Birth Weight'))

# get the standard deviation of column 
birth_weight_sd = np.std(births.column('Birth Weight'))

# now test, within 1, 2, 3 standard deviations
    # *** Increment by multiplying the index

# 1 standard deviation test
births.where('Birth Weight', are.between(birth_weight_mean - birth_weight_sd,
                                        birth_weight_mean + birth_weight_sd)).num_rows/births.num_rows
# 2 standard deviation test
births.where('Birth Weight', are.between(birth_weight_mean - 2*birth_weight_sd,
                                        birth_weight_mean + 2*birth_weight_sd)).num_rows/births.num_rows
# 3 standard deviation test
births.where('Birth Weight', are.between(birth_weight_mean - 3*birth_weight_sd,
                                        birth_weight_mean + 3*birth_weight_sd)).num_rows/births.num_rows


```

**Task** Empirically verify that for a bell shaped distribution, the proportion of values within 1, 2 and 3 SDs of the mean is 68, 95, and 99 75 percent, respectively.

## Central Limit Theorem 
**If a sample is large and drawn at random with replacement, the probability distribution of the sample average is roughly Normal** 

### Statements when analyzing the CLI (if bell shaped distribution)
_which of these statements is correct (multiple)_ 

Hint: if a distribution is bell-shaped, what type of curve does it follow?

1. We see the Central Limit Theorem (CLT) in action because the distributions of the sample means are bell-shaped.
2. We see the Law of Averages in action because the distributions of the sample means look like the distribution of the population.
3. One of the conditions for CLT is that we have to draw a small random sample with replacement from the population.
4. One of the conditions for CLT is that we have to draw a large random sample with replacement from the population.
5. One of the conditions for CLT is that the population must be normally distributed.

- **Central Limit Theorem** 
    1. Defines one distribution that always follows a normal distribution.
    2. The distribution of the sums and means of all large random samples drawn with replacement (and thus are independent from one another) from a single distribution (regardless of the distribution’s original shape) will be **normally distributed.**

CLI is important because it describes: 
- how the Normal distribution is connected to random sample averages.
- You must care about sample averages:
    - because they estimate population averages and population averages are often what we are interested in.

**Task:** Show that the empirical distribution of the sample mean approaches a bell shape as the sample size (for each statistic used to create the distribution) increases.

Though the CLT is a statement about the probability distribution of the statistic, the empirical distribution will look roughly like the probability distribution when the repetition size is large. 

```python
def one_sample_mean(sample_size):
    """ 
    Takes a sample from the population of flights 
    and computes its mean
    """
    sampled_flights = united.sample(sample_size)
    return np.mean(sampled_flights.column('Delay'))

def ten_thousand_sample_means(sample_size):
    means = make_array()
    for i in np.arange(10000):
        mean = one_sample_mean(sample_size)
        means = np.append(means, mean)
    return means

def plot_sample_mean_distribution(sample_size):
    sample_means = ten_thousand_sample_means(sample_size)
    
    Table().with_column('Mean of ' + str(sample_size) + ' flight delays', 
                        sample_means).hist(bins=20)

    print('Population Average:', population_parameter)

plot_sample_mean_distribution(np.arrange(400)) # as you increase n, the average will become a centered bell curve
```

**Questions**

After rolling 1,000,000 fair 6-sided dice, which of these histograms would you expect to have a bell shape?

1. The histogram of outcomes of these million rolls

2. The histogram that results from computing the average outcome of these million rolls

3. The histogram that results from:
    - splitting the outcomes into 1,000 groups of 1,000 (in the order they occurred) and computing the average outcome of each group

```python
# *** for question 1 ***

die = make_array(1,2,3,4,5,6)
one_million_die_rolls = np.random.choice(die,size = 1000000)

Table().with_columns('Die Spot', one_million_die_rolls).hist(bins = np.arange(1,8)) # will output a graph of the same probabilities because of with_replacement=False
one_million_die_average = np.average(one_million_die_rolls) # compute each average for the questions

# *** for question 2 ***
Table().with_columns('Average', one_million_die_average).hist(bins = np.arange(1,8))
plots.title('This is not much of a histogram!'); # this will output one bar of the averages 

# *** for question 3 *** 
group_averages = make_array() # will be a computed average of bootstraps that creates a bell shaped distribution because `group_averages` is an array of all the averages within 1000 blocks 
start = 0
for i in np.arange(1000):
    group_average = np.average(one_million_roll_table.take(np.arange(start, start + 1000)).column('Die Spot'))
    group_averages = np.append(group_averages, group_average)
    start = start + 1000
Table().with_columns('Average', group_averages).hist()
```

## Relationships between population SD, sample SD, and SD of sample means change with varying sample size. Which of the following is true? 
- Hint 1: The sample SD is different from the SD of sample means.

        1. Sample SD gets smaller with increasing sample size.
        2. Sample SD gets larger with increasing sample size.
        3. Sample SD becomes more consistent with population SD with increasing sample size.
        4. SD of sample means gets smaller with increasing sample size.
        5. SD of sample means gets larger with increasing sample size.
        6. SD of sample means stays the same with increasing sample size.