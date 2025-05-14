#### D8 Spring 2025 HW08
# Sample Sizes and Confidence Intervals Notes
#### Sean Villegas

## Section 1 
1. A community has an average age of 45 years with a standard deviation of 5 years. **We do not know how the ages are distributed.**. In each part below, fill in the blank with a percent that makes the statement true **without further assumptions**, and **explain your answer**.

**Question 1.1.** At least _______% of the people are between 25 and 65 years old. Explain your answer! 

Steps:
- Use Chev's bounds => figure out bounds with mean 
- We know:
    - Mean: 45
    - SD: 5 
    - Lower Bound: `45 - 25 = 20` & `20 // 5 = 4` 
        - In english: So, 25 years is 4 standard deviations below the mean
    - Upper Bound: `65 - 45 = 20` & `20 // 5 = 4`
        - In english: So, 65 years is 4 standard deviations above the mean
    - The range is ± 4 Standard Deviations around the mean <=> `Average ±4 SD`
- Chebyshev’s theorem tells us that for any list, the proportion of entries within 𝑘 standard deviations of the mean (i.e., in the range “`average ± 𝑘 SDs`”) is at least 1 − 1 / 𝑘<sup>2</sup>
    - 1 - 1 / 4<sup>2</sup> = 1 - 1/16 = 15/16 x 100 = 0.9375%
<center>Thus, 0.9375% of people are between 25 to 65 years old</center>

**Question 1.2.** At most _______% of the people have ages that are not in the range 25 years to 65 years. Explain your answer! 
**6.25%**; With the calculated proportion from Question 1, we subtract that by 1 to find the most the proportion could lie within the range of 4 Standard Deviations `1 - 0.9375 = 0.0625 x 100 = 6.24`

**Question 1.3.** At most _______% of the people are more than 65 years old. Explain your answer! 
**6.25%**; However, that is with less assumption.

- The total proportion outside ± 4 SDs is at most 1/4<sup>2</sup> = 1/16 = 0.0625 split across both tails (below 25 and above 65). 
- If the distribution were symmetric, each tail would get half, or 3.125%, but **Chebyshev doesn’t assume symmetry—it’s a worst-case bound** 
- Data Scientists that are trying to examine the standard deviation of only one population parameter (some sort of skew), will take the proportion more than _k_ SDs above the mean which is at most 1 / (k<sup>2</sup> + k) for a tighter bound

## Section 2 

**Question 2.1.** Assign `smallest` to the smallest number of students they should sample to ensure that a **95%** confidence interval for the parameter has a width of no more than 6% from left end to right end.

Steps:
- Use the width which represents the confidence interval outlier of the 95% confidence interval 
- Formula: `width = 4 * 0.5/√n` 
    - Width is 0.06
    - 4 is the standard deviations of the sample proportion (number line)
    - 0.5 is at most what standard deviations of `0-1` population is 
    - √n is what you solve for `sample size` 

1. Divide by 0.06 on both sides
2. Multiply by √n on both sides

_leaves you with_ 
```python
solve_width_per_sample_size = (4 * 0.5/0.06)**2
```

**Question 2.2.** Suppose the data science class decides to construct a 90% confidence interval instead of a 95% confidence interval, but they still require that the width of the interval is no more than 6% from left end to right end. Will they need the same sample size as in 2.1? Pick the right answer and explain further without calculation. 

No, a smaller sample size will work. 

- Even though the calculation would work if we did it again, the main idea I take away from this question is that the _width_ of the Confidence Interval will get narrower due to 90% width
- Meaning that our conclusion of the data will be less accurate because we don't have that big of a sample size, compared to a 95% Confidence Interval. Implying that a smaller sample size would suffice
- Lower confidence level <=> narrower intervals
- Wider confidence level <=> wider intervals


**Question 2.3.** The professor tells the class that a 90% confidence interval for the parameter is constructed exactly like a 95% confidence interval, except that you have to go only **1.65 SDs** on either side of the estimate (±1.65) instead of **2 SDs** on either side (±2). Assign `smallest_num` to the smallest number of students they should sample to ensure that a **90%** confidence interval for the parameter has a **width of no more than 6%** from left end to right end. 

Observe:
- 
- You have a 95% confidence interval, which by the Central Limit Theorems law of a normal distribution is 1.96 (rounded to 2)
    - which is also by Cheb's worst bound being  75% within the ±2 SD's 
- You have a Z multiplier `1.65`
- Your `0-1` population standard deviation
- You need sample size √n 

_Formula_

`0.06 = 2 * 1.65 * 0.5/√n`

```python
solve_width_per_sample_size = (2 * 1.65 * 0.5/0.06)**2
```

**Question 2.4.** This shows that the percentage in a normal distribution that is at most 1.65 SDs above average is about **95%**. Explain why 1.65 is the right number of SDs to use when constructing a **90%** confidence interval. 

[Chapter Relevant](https://inferentialthinking.com/chapters/14/3/SD_and_the_Normal_Curve.html)
- Under a normal distribution these rules apply for looking at it
- We use `stats.norm.cdf(...)` to find area under a curve to the left of ... (i.e. a number `n`)
- Formally, it is called the “cumulative distribution function” of the standard normal curve

Answer: `1.65` is the right number of Standard Deviations when constructing a 90% confidence interval because the normal distribution logic. 90% of the values fall between ±1.65 standard deviations from the mean. This ensures we capture the middle 90% of likely sample means or proportions of the confidence interval, leaving 5% in each ± tail of the distribution


**Question 2.5.** The cell above shows that the proportion that is at most 2.33 SDs above average in a normal distribution is 99%. Assign `option` to the right option to fill in the blank: 

If you start at the estimate and go 2.33 SDs on either side, then you will get a _______% confidence interval for the parameter.

1. 99.5
2. 99
3. 98.5
4. 98

Observe:
- When you go 2.33 standard deviations above the mean, you're capturing 99% of the distribution below that point in a standard normal curve.
- But for a confidence interval, you want the range to be symmetric around the estimate (mean). 
- That means:
    - You go ±2.33 SDs (not just up to 2.33).
    - That captures the middle 99% of the distribution (leaves 0.5% in each tail).

_Find the area under the curve to the left of that number_
```python

cdf = stats.norm.cdf(2.33)

option = 100 - cdf

print(option) # 99.00
```

**Question 3.1.** Ella wants to use 10,000 bootstrap resamples to compute a confidence interval for the proportion of all California voters who will vote Yes.  

Fill in the next cell to simulate an empirical distribution of Yes proportions. Use bootstrap resampling to simulate 10,000 election outcomes, and assign `resample_yes_proportions` to contain the Yes proportion of each bootstrap resample. Then, visualize `resample_yes_proportions` with a histogram. **You should see a bell shaped histogram centered near the proportion of Yes in the original sample.**


```python
sample_yes_prop = make_array()

for i in np.arrange(10000):
    resample = sample_proportions(sample_size, sample_with_proportions.column("Proportion"))
    sample_yes_prop = np.append(sample_yes_prop, resample.item(0))
Table.with_column(Yes Proportions, sample_yes_prop).hist(bins=0.2, .8, 0.1)

# bins are set smaller to visualize the data more accurately 
# item(0) to get the yes vote in the table 
```


## Section 3

**Question 3.3.** Using only the Central Limit Theorem and the numbers of Yes and No voters in our sample of 400, *algebraically* compute the predicted standard deviation of the `resample_yes_proportions` array. Assign this number to `approximate_sd`. **Do not access the data in `resample_yes_proportions` in any way.**

Remember:
1. The standard deviation of the sample means can be computed from the population SD and the size of the sample (the formula above might be helpful). 
2. If we do not know the population SD, we can use the sample SD as a reasonable approximation in its place. 

In a population whose members are represented as either a 0 or 1, there is a simple formula for the **standard deviation of that population**:

_Formula_: 

$$\text{standard deviation of population} = \sqrt{(\text{proportion of 0s}) \times (\text{proportion of 1s})}$$


**Question 3.5.** **Again, without accessing `resample_yes_proportions` in any way**, compute an approximate 95% confidence interval for the proportion of Yes voters in California. **(6 points)**


```python
# Why this doesnt work: Your Confidence Interval must be centered at the sample proportion
# other_lower_limit = approx_pop_sd - 2 * approximate_sd
# other_upper_limit = approx_pop_sd + 2 * approximate_sd

sample_proportion = 210/400
lower_limit = sample_proportion - 2 * approximate_sd
upper_limit = sample_proportion + 2 * approximate_sd
print('lower:', lower_limit, 'upper:', upper_limit)
```


**Background on question:**
The Yes on 68 campaign really needs to know whether they're winning. It's impossible to be absolutely sure without polling the whole population, but they'd be okay if the standard deviation of the sample mean were only 0.005. They ask Ella to run a new poll with a sample size that's large enough to achieve that. (Polling is expensive, so the sample also shouldn't be bigger than necessary.)

$$\text{standard deviation of population} = \sqrt{(\text{proportion of 0s}) \times (\text{proportion of 1s})}$$


```python
approx_sd_of_pop = sqrt((210/400) * (190/400))
sample_size = 9975 
sd_of_all_sample_means = approx_sd_of_pop / sqrt(sample_size)
```

**Question 3.9**. Based off of this, was Ella's sample size approximately the minimum sufficient sample, given her assumption that the sample SD is the same as the population SD? Assign min_sufficient to True if 9,975 was indeed approximately the minimum sufficient sample, and False if it wasn't. 


Observe: 
- from her population of 9975, we get yes the variability of  0.0050 as the correct option
- Note that the approx one is:

    ```python
    >>> from math import sqrt
    >>> sqrt((210/400) * (190/400))
    0.4993746088859545
    ```

_<center> quick maths time </center>_

1. solve for the `standard deviation of all sample means`
2. involves rearranged problem statement 
3. `population standard deviation` is: $$\sqrt{(\text{proportion of 0s}) \times (\text{proportion of 1s})}$$

$$\text{standard deviation of all sample means} = \text{approximate population standard deviation} / \sqrt\text{sample size}$$

4. 
$$ \sqrt\text{sample size}  = \text{approximate population standard deviation} / 0.05$$

5. 
$$ \text{sample size}  = \text{(approximate population standard deviation / 0.05)}^2 $$

6. **Then, you will find the true sample size**