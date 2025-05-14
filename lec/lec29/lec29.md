#### D8 Spring 2025 Prof Sanchez
# Correlation
#### Sean Villegas
[Chapter 15.1](https://inferentialthinking.com/chapters/15/1/Correlation.html)

## Vocab
- **trend**: how does the second variable change as the first one changes?
- **pattern**: any discernible shape in the scatter. 
- **correlation coefficient**: measure linear association

**Outside of scope for class:**
- Technical def of **r**: First, convert each variable to **standard units**. For each different value of the variables, compute the _product between them_, then take the **average** of these products

## Review

Exploration: 
- Find patterns in data; use visualizations 

Inference: 
 - Hypothesis Test
 - Confidence Interval 
 - Random Samples

Prediction: 
- Make informed guesses about unobserved data (machine learning on other sets of data)


**Question**: Imagine that you have a table which can be also considered as random sample from the population. Which of the following tasks are intended to make a statement about the population as a whole? 
- This question is asking us about the inference **inferential** of the data
    -  This is an inferential task. A confidence interval estimates a range of values for a population parameter (like the mean), based on the sample
    - Hypothesis testing is an inferential procedure. You're using the sample to make a judgment about whether a pattern holds in the entire population.
- Understand which questions are predictive, or descriptive 

Options: 
1. Visualizing the distribution of a variable in the sample 
2. Calculating a confidence interval using the bootstrap percentile method
3. Calculating statistics on the variables in the sample
4. Predicting the value of a variable for a new observation
5. Testing hypothesis involving a variable in the sample when split between two groups of ...


## New Material from Lecture

### Predicting 
- Prediction is based on incomplete data
- Example: **How can you predict the outcome of a new individual?**
    - Find others who are like that individual and whose outcomes you know --> Use those outcomes as a first pass
    - You must find association 
    - __The end goal is to predict one with the other__

### Look for _association_ through `trend`
- **trend**: how does the second variable change as the first one changes?

**Questions to ask:**

For a Positive Trend these questions hold:
- Does it increase when the first variable increases?
- Does it decrease when the first variable decreases?

For a Negative Trend these questions hold: 
- Does it decrease when the first variable increases?
- Does it increase when the first variable decreases?

### Look for _association_ through `pattern`
- **pattern**: any discernible shape in the scatter. 
    - it could be a linear pattern
    - it could be a nonlinear pattern

**Question**: How would the second variable behave in relation to the first variable changing if there were _NO_ association between the two variables? 

**Answer**: If there was no association then the data for the two variables would have no relationship. i.e. they are independent of each other 

**Question**: Which is the best plot method for showing associations in data?

**Answer**: Scatterplot; because:
- The closer the points cluster around a line or curve, the stronger the relationship
- If the points tend to move upwards from left to right, it suggests a positive relationship (as one variable increases, the other tends to increase as well).
    - Vice-versa this applies for negative relationship 
- Quick Identifier of patters like: 
    - linear
    - non-linear
    - no association
    - the strength and direction of the relationship

### _r_ helps measure linear association
- Linear association is known as the **correlation coefficient**
- `-1 ≤ r ≤ 1`
    - closer to -1 implies a **negative trend**
    - closer 1 implies a **positive trend**
- r is unaffected by changing the units on either axis
- is unaffected by switching the axes
- `r_scatter(1)` implies a **perfectly** straight line, instead of highly concentrated line

Why Visualizing with r is important:
 - The lower r (i.e. -0.2), does not automatically imply no association
- The higher r (i.e. 0.8), does not automatically imply linear association 

Important Notes when using: 
- Correlation is not causation
- Outliers can greatly affect the value of r
- Correlations based on aggregated data can be misleading.


## Chapter 15
```python
hybrid = Table.read_table(path_data + 'hybrid.csv')

hybrid.scatter('acceleration', 'msrp') # msrp vs acceleration column

# msrp is on vertical axis (y), acceleration is on horizontal axis (x)

def standard_units(any_numbers):
    "Convert any array of numbers to standard units."
    return (any_numbers - np.mean(any_numbers))/np.std(any_numbers)  

Table().with_columns(
    'mpg (standard units)',  standard_units(suv.column('mpg')), 
    'msrp (standard units)', standard_units(suv.column('msrp'))
).scatter(0, 1)
plots.xlim(-3, 3)
plots.ylim(-3, 3);

r_scatter(0.9) # linear line going upward
r_scatter(-0.2) # linear line going downward
r_scatter(0) # the true data representation of data with no association (average straight line on x axis)

"""The following code below is outside the scope for this class

*** Steps to make r ***
"""

# step 1; have data

x = np.arange(1, 7, 1)
y = make_array(2, 3, 1, 5, 2, 7)
t = Table().with_columns(
        'x', x,
        'y', y
    )

t.scatter(0, 1, s=30, color='red')

# step 2; convert each variable to standard units 

t_su = t.with_columns(
        'x (standard units)', standard_units(x),
        'y (standard units)', standard_units(y)
    )

# step 3; Multiply each pair of standard units.
t_product = t_su.with_column('product of standard units', t_su.column(2) * t_su.column(3))

# step 4; r is the average of the products computed in step 3 

r = np.mean(t_product.column(4)) ## r is the average of the products of standard units
print(r) # As expected, r is positive but not equal to 1.

def correlation(t, x, y):
    """Takes a table and its two columns. The func returns r; the mean of the products of provided column values with the func standard_units 
    """
    return np.mean(standard_units(t.column(x)) * standard_units(t.column(y)))
```

- func `standard_units` is applied to allow for redrawing two scatter plot diagrams, but measured in standard unites
- func `r_scatter(...)` takes a standard unit, simulates scatter plot with correlation very close to r
- func `r_scatter(0)` is an average straight line with no associations. When you look at the graph sideways you will observe the data spread out across all `y` values 
- func `correlation(t, x, y)` takes a table and its two columns. The func returns r; the mean of the products of provided column values in standard units 
    - It can show us the linear association between two variables
    - It **ONLY** measures linear association; e.g. a parabola will not be shown 

## Correlation is affected by outliers
e.g.
```python
line = Table().with_columns(
        'x', make_array(1, 2, 3, 4),
        'y', make_array(1, 2, 3, 4)
    )
line.scatter('x', 'y', s=30, color='r')

correlation(line, 'x', 'y') # 1.0 

## **Outlier Example** ##

outlier = Table().with_columns(
        'x', make_array(1, 2, 3, 4, 5), # notice
        'y', make_array(1, 2, 3, 4, 0) # notice
    )
outlier.scatter('x', 'y', s=30, color='r')

correlation(outlier, 'x', 'y') # 0.0

```

## Ecological Correlations
- An ecological correlation is the correlation between group averages, not individuals.
    - These can overstate the strength of a relationship.
e.g. 

1. You have SAT data for each state, showing average scores in Math and Critical Reading.
2. The correlation between these state averages is very high: 0.985.
3. But this doesn’t mean every student who scores high in Math also scores high in Reading
4. If you looked at individual student scores, the correlation would be much lower.