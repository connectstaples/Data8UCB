#### D8 Lec 27, Prof Sanchez 
## The Variability of the Sample Mean
#### Sean Villegas

Readings: 
- [Variability of Sample Mean](https://inferentialthinking.com/chapters/14/5/Variability_of_the_Sample_Mean.html)

Notes:
- Throughout this lab, we have been taking many random samples from a population (in contrast to re-sampling from a sample). However, all of these principles hold for bootstrapped resamples from a single sample. The bootstrap works because it’s like drawing from the original population assuming the sample is representative. If your original sample is relatively large, all of your re-samples will also be relatively large, and so the SD of resampled means will be relatively small.
- It is also important to keep in mind that when doing the bootstrap, our histogram of resample means will be centered around the original sample mean, rather than the population mean (as we don’t have access to the population mean usually)!
- In order to change the variability of your sample mean, you’d have to change the size of the original sample from which you are taking bootstrapped resamples.


Prof Sanchez is allergic to: 
- repeating code
- taking one sample 
    - reporting one number in a sample for sample average

- **The `united` dataset column `Flight Number` values is code, not a number**
- Taking the average of the sample means will result in it being around the population mean `avg sample mean <=> population mean`

## Vocab
- **Distribution of the sample average:** distribution of averages from all the possible samples
- **Empirical Distribution:** is when we have data that lets us take observations, so a finite number that we test with
    - `CLT` lets us make the **Empirical Distribution** look like the **Probability Distribution**
- **Probability Distribution:** is all possible samples of `sample size` tested with

```
SD of all possible sample means = Population SD / √sample size
```




## How is sample size related to the accuracy of an estimate?
- The CLT says that the distribution of the sample average is roughly Normal.
- Central Limit Theorem is important because: 
    - it explains how the normal distribution is connected to random sample averages. 
        - These averages are what people are interested in finding
    - It is easier and less computationally heavy compared to bootstrapping whilst allowing us to make estimates of:
        - the population (with little knowledge of population)

**What is the dist. of the sample average?**
- One random sample -> one sample average

However you must repeat this process `n` amount of times:
- the sample could have come out differently and the sample average might have been different.

- **Distribution of the sample average:** distribution of averages from all the possible samples

## <center>Task</center>
- Construct empirical distributions of the sample average
- The CLT says these should be bell-shaped as the sample size increases. 


### How is sample size related to the accuracy of an estimate?
- Answer: by increasing the sample size the Law of Averages makes the normal distribution more narrow, to represent the true population. The `mean` stays the same

### How to quantify the `true` accuracy based on `sample size`
- Answer: **Standard Deviation** of sample means is the `population standard deviation` divided by the **square root** of the `sample size` 
- **Important Note** If you want to increase the accuracy by a factor `n`, you must take into account the square root calculation. E.g. increasing by two, requires four. Increasing by four, requires 16 etc.

### How is sample size related to the precision of an estimate?
- Answer: The larger the sample size, the smaller the SD of our sample means and the smaller the width of the bell

## Demo Code

```python
def one_sample_mean(sample_size):
    """Take a sample from the population of flights and compute its mean"""
    sampled_flights = united.sample(sample_size)
    return np.mean(sampled_flights.column('Delay'))

def ten_thousand_sample_means(sample_size):
    """Approximate the distribution of the sample mean"""
    means = make_array()
    for i in np.arange(10000):
        mean = one_sample_mean(sample_size)
        means = np.append(means, mean)
    return means
```

### <center>Relationship between width, bell shape, sample size</center>
```python
def plot_sample_means(sample_size):
    """Empirical distribution of random sample means"""
    sample_means = ten_thousand_sample_means(sample_size)
    sample_means_tbl = Table().with_column('Sample Means', sample_means)
    
    # Print some information about the distribution of the sample means
    print("Population SD:", population_sd)
    print("SD of sample means:", np.std(sample_means))
    print("Population SD / SD of sample means:",population_sd/ np.std(sample_means))
    # Plot a histogram of the sample means
    sample_means_tbl.hist(bins=20)
    plots.xlabel('Sample Means')

plot_sample_means(100)

# output: 
"""
Population SD: 39.4801998516
SD of sample means: 3.97060340046
Population SD / SD of sample means: 9.94312346758

## Observe ## 
√100 == 10 
** Formula ** Population Standard Deviation / √Standard Deviation of Sample Means which equals the Standard Deviation of the Sample Means
"""
```

## Questions

### Find the True Statements:

1. The probability distribution of the mean of a large random sample is roughly normal.
2. The bell curve is centered at the population mean.
3. Some of the sample means are higher, and some lower, but the deviations from the population mean are roughly symmetric on either side, as we have seen repeatedly.
4. Formally, probability theory shows that the sample mean is an unbiased estimate of the population mean.

###  Is there a relationship between the sample size and the standard deviation of the sample means? 

_Directly proportional means that as one variable increases, the other increases proportionally, and vice versa. Inversely proportional means that as one variable increases, the other decreases proportionally, and vice versa._

1. The SD of the sample means is inversely proportional to the square root of sample size.
2. The SD of the sample means is directly proportional to the square root of sample size.

