#### D8 Spring 2025 Disc 10 
# Center / Spread and Normal Distribution
#### Sean Villegas

# Review 

## SD and Normal Curve

Standard Normal Curve will always have: 
- Symmetric about 0:
    - Mean of 0
    - Median of 0 
- This implies that it has a Standard Deviation of 1 
- Chebs Bounds are _weaker bounds_ because they work for **all distributions** 
- Normal Distributions follow these guidelines:
    - Avg ± 1 = 68% 
    - Avg ± 2 = 95%
    - Avg ± 3 = 99.7%

## Central Limit Theorem 
CLT:
1. Must have large samples
2. Must be sampled `with_replacement`
3. It is the averages of the sum 

## Variability of Sample Mean 
<center>Formula</center>


$$\text{Standard Deviaion of All possible Sample Means = } \text{Population Standard Deviation /}\sqrt\text{sample size}$$

This measures:
1. How many sample means vary depending on obtained sample
2. The smaller the SD, the more accurate the estimate
3. This is **different** from _`sample SD` and `population sd`_

Vocab: 
- `Proportion` is the average of `1` and `0` (just proportion of 1s in the array)
- The `standard deviation` of binary populations are 0.5 due to math, regardless of proportions of `1's`

$$\text{Equation of Population Data = }\sqrt\text{Proportion of 0s * Proportion of 1}$$

## Choosing Sample Size
You choose a sample size when:
- You need to estimate population parameter, conduct bootstrap, obtain bootstrap estimates. If the width of our 95% Confidence Interval is small, it means our estimates are more precise
    - **You want to limit variability of estimate**
- Create a confidence interval based on the middle 95% being within 2 SDs of the mean. The center is `± 2 SDs`; which would equal` ± 4 SDs` **total width**
- The width of the confidence interval is: 
$$\text{width of 95\% C = 4 * SD of population /}\sqrt\text{sample size}$$

#### Question 1.1
### Measuring Area and Bounds 

Suppose vehicle speeds on a highway are normally distributed with mean 90mph and SD 10mph. Using the table above,  what is the approximate probability that a randomly chosen car is going more than 100mph? 
Hint: The total area under the normal curve is 1 

Steps:
1. Apply the Normal Distribution Averages 
2. Bins are separated by the Standard deviation of 10
3. From the mean, subtract by standard deviation to find the points of inflection 
    - That area represents the 68%  
4. Then, we only care about the upper bound, so that shaded area is `.68-1.00` --> 32
5. .32 is the total area of both regions, meaning we must divide to get the upper bound. Which is 16% for a random care that is going more than 100mph

#### Question 2.1
### Distribution Relationship with CLT and quantifying Center

Suppose you simulate the proportion of purple flowered plants in a sample of 200 plants (from Mendels 75% purple and 25% white flower plant population) using `sample_proportions` 1000 times. Then, you plotted the distribution of the proportion of purple flowered plants from each of the 1000 trials. What would the distribution look like? Where would the distribution be centered?

1. The distribution would look normally distributed, but roughly due to small sample proportions of 1000 sample size 

Steps to calculate the center (i.e. `symmetric about n`):
2. Understand the problem statement defines the **true proportion** for us already. Meaning all we need to do is convert it to a decimal and you will have the answer i.e. **center**

$$\text{75\% ---> 0.75} $$

#### Section 3
### Understanding Standard Deviation and Mean, Inflection Points, Sample SD vs SD of Sample Mean and Sample size

**3.1** Suppose we sample repeatedly from the population. If we increase the sample size, what happens to the distribution of the sample mean? Does it become narrower or wider? Where is it centered? 

1. Based on the formula of **Standard Deviation of all Sample Means**, we know that having a wider sample size will make a more narrow distribution of the sample mean, due to the square rooting of sample size. 
2. It will be centered around the average of population mean

**3.2** If you had a sample size of 100, but wanted to increase accuracy by a factor of 4, what should the new sample size be? 

1. Problem set is asking for you to increase the accuracy by a factor of 4, so you need to alter the sample size to increase by factor of 4 
$$\text{1/4 * SD of all Possible Sample Means /} \sqrt\text{n}$$
2. Cancel out the Standard Deviations, and solve for n; realizing that for an accuracy of 4, we would need 16. Problem statement becomes
$$\text{4}^2\text{(100)}$$

**3.3** State the difference between the sample SD and the SD of sample means. Which of these is effected by sample size? 
1. Sample SD is a population parameter that is observed from the dataset that we take multiple bootstraps of, applying CLT 
2. SD of Sample Size is a statement of the normal distribution of SD for all possible sample means 

**3.4** Suppose we have a sample with a mean of 40 and an SD of 10. Which one of the histograms below is more likely an empirical distribution of the means of 10000 bootstrap resamples, each of size 100, from the sample? 

1. We have a mean of 40 and SD of 10, with a sample size of 100
2. Thus, use our Standard Deviation Error Problem Set Up 

$$\text{Standard Deviation of All Possible Sample Means = 10/ } \sqrt\text{100}$$

3. 10/10 == 1, so we now the SD Of all possible sample means is 1. 
4. Subtract that from the mean, and you will find the points of inflection for the graph. 40 is the mean, thus 30 and 50 are the points of inflection. Find the graph that depicts that

**3.5** Based on the sample from above, there is a ___ % chance that the next resampled mean lies within the range [38, 42]. This question is not about parameter.

- I went wrong thinking this question was regarding the area percentiles; which is not wrong, just need to think of frame Average ± SD

1. This is regarding a normal distribution and the Average ± SD
2. We say that the next resample is 95% chance because Avg ± 2 is within that, compared to the Avg ± 1 which is 68%

**4.4** Suppose a redwood forest has trees whos average height is 200 ft with SD of 30 ft. A random sample with replacement of 400 trees is taken. 

1. There is roughly a 68% chance that the average height of the sample lies within range 200 ± ____

- Answer: 1.5; calculate the standard deviation of all sample means using the exhausted formula for that given data 

#### Section 5
### Getting Population Parameters with Bootstrapping, and with Confidence Interval at most of `XYZ`
Experiment: 
1. Pineapple on Pizza, Yes / No Binary Data
2. You need to estimate the population proportion of students who like pineapple on their pizza 
3. The estimate must have a confidence interval of 0.05

**5.1** Suppose the population SD of the proportion of students who like pineapple on pizza is 0.1. What sample size do you need to achieve a 95% confidence interval width of at most 0.05

1. $$\text{4 * SD of Population / }\sqrt\text{Sample Size }\text{≤ 0.05}$$
2. $$\text{4 * 0.1 / }\sqrt\text{Sample Size }\text{≤ 0.05}$$
3. $$\text{0.4 / 0.5 }\text{≤ }\sqrt\text{Sample Size }$$
4. $$\text{(0.4 / 0.5 )}^2\text{= }\text{Sample Size }$$
5. $$\text{Sample Size = 0.64}$$

**5.2** Suppose you do not know the population SD of the students who like pineapple on their pizza. Would it still be possible to calculate the minimum sample size needed? If so, what sample size would you need to obtain a 95% confidence interval of width at most 0.05

**RECALL** that binary data will always have a representation of 0.5. Thus, we still have the general SD of the population. Just alter the steps

1. $$\text{4 * SD of Population / }\sqrt\text{Sample Size }\text{≤ 0.05}$$
2. $$\text{4 * 0.5 / }\sqrt\text{Sample Size }\text{≤ 0.05}$$
3. $$\text{2 / 0.05 }\text{≤ }\sqrt\text{Sample Size }$$
4. $$\text{(2 / 0.05)}^2\text{= }\text{Sample Size }$$
5. $$\text{Sample Size = 1600}