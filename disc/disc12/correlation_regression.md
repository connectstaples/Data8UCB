#### D8 Sp25 
# Correlation and Regression
#### Sean Villegas

#

## Association
- **Association** is the relationship between two variables. It does not have to be linear
    - e.g. it can be exponential, or non linear on a graph 

## Correlation
- **Correlation** denotes (sign of) _linear association_ between two variables
- **Correlation does not imply causation**

## Formula for _r_
- **_r_ is related to linear regression**
- **_r_ is related/represented by correlation coefficient** 
- The average (`np.mean`) of the product x and y when both variables are in standard units
- _r_ is a number **without units** because its computed with standard units (which has no units)
- Standard Units help you quantify the relationship between two variables on different units and scales
- r is unaffected by switching axes; e.g.:
    - $$\text{x * y = y * x}$$
    - Furthermore, correlation is a measure of spread around line, switching axes wont change the spread around the line

Standard Units equation: 
$$\text{standard units = [x - average of x] / [standard deviation]}$$

Standard Units in code: 
```python
def standard_units(xyz):
    "Convert any array of numbers to standard units."
    return (xyz - np.mean(xyz))/np.std(xyz)  
```
- For problems regarding SU, you are usually given average of x and standard deviation

## Regression 

**Correlation Coefficient**
- The equation for the regression line can be calculated using _r_. 
- Formula: $$\text{y = slope * x + intercept}$$

```python
def correlation(t, x, y):
    return np.mean(standard_units(t.column(x))*standard_units(t.column(y)))
```

**Standard Units**
- Visually, scatter plot and regression line look the same. 
- Essentially, standard units and original units shouldn't effect the visual output with `scatterplot`

**Calculating Regression line when x and y are in standard units** 
$$\hat{y}\equiv\text{y}_{standard units}$$
$$\hat{y}\text{ = r * x}_\text{standard units}$$

**Calculating Regression line when x and y are in original units** 
1. Calculate the correlation coefficient, _r_
2. Calculate slope _m_ 
$$\text{slope of regression line = r * [SD of y / SD of X]}$$
3. Calculate intercept 
$$\text{intercept of the regression line = [average of y] - [slope * average of x]}$$   
 - In code this is 
    ```python
    def intercept(tbl, x_label, y_label):
        return np.mean(y_label - slope) * np.mean(x_label)
    ```

## Root Mean Squared Errors
 - Work backwards in equation i.e.


1. Error
2. Squared Error
3. Mean Squared Error
4. Square Root to work with normal numbers 
5. **Math Notation:**

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2}

\\
\equiv
\\

\text{RMSE} = \sqrt{ residual_{1}^{2} + residual_{1}^{2} + residual_{1}^{2} ... / n }
$$

- Root mean square error (RMSE) is the residuals' standard deviation, or the average difference between the projected and actual values produced by a statistical model. Remainders stand for the separation between the data points and the regression line

## Section 1


**Problem 1**

Say you have a table: 

| Tater Tots Consumed | Satisfaction |
| --- | --- |
| 10 | 8| 
| 10 | 8| 
| 8 | 12| 
| 40 | 4| 

Complete the function `su` that:
1. takes in array of numbers
2. outputs the array in su
3. calculate correlation coefficient between Tater Tots Consumed and Satisfaction; assigned to corr_coeff
```python
def su(some_array):
    return (array - np.mean(array)) / np.std(array)

consume_su = su(tatter.column("Tater Tots Consumed"))
satisfaction = su(tatter.column("Satisfaction"))
corr_coeff = np.mean(consume_su * satisfaction)
```

# 

**Problem 2**

Suppose you have a correlation coefficient _r_ to be equal to 0.743. What can you conclude about the association between the number of tater tots consumed and a persons satisfaction? 

- Strong association between the two variables of number of tater tots consumed and persons satisfaction, implying linear regression 

#

**Problem 3**
_true or false section_ 

- A high value of _r_ shows that a change in _x_ causes a change in _y_
    - **False**, correlation coefficient does not infer causation

- If we switch the axes of a plot, the correlation coefficient will not change  
    - **True**, the relationship between the two will still show. If one variable predicts the other, the other will do the same due to correlation 

## Section 2
**Problem:** You have a table of 100 most streamed songs. `energy` column represents songs perceived energy level as percentage, and `danceability` column represents how suitable the song is for dancing in percentage 

Stats given: 
- `energy` column has mean of 64.75 and standard deviation of 16.53
- `danceability` column has mean of 65.97 and standard deviation of 14.56 
- The `correlation coefficient` between energy and danceability is 0.31

### 2.1
Write an equation for the regression line of the data in the table, with intention of predicting an unseen `danceability` percentage given an observed energy percentage

1. We need to find percentage of danceability, with our already given energy % 
3. Goal: We want to predict danceability given energy.  ut if we don’t know energy at all, our best guess for any song’s danceability would just be the mean danceability,  that’s the center of the cloud of points.

Once we do know energy, we adjust our guess up or down from the mean of danceability, depending on the correlation between energy and danceability.
**<center>Predicted Y Formula </center>**
4. $$\text{predicted y = mean of y + r * (x - mean of
 x / SD of x) * SD of y}$$
5. In other words:
    - $$\hat{y}\text{ = a + b * x}$$
    - $$\text{b = r * [SD of y / SD of x]}$$
    - $$\text{a = mean of y - b * mean of x}$$
    _y intercept is calculated in a to always show that it passes through that point_ 

**<center>Math:</center>** 

Step 1:
$$\text{b = 0.31 * [14.56 / 16.53]}\implies{b = 0.273}$$
Step 2: 
$$\text{65.97 - [0.273] * 64.75}\implies{ a = 48.29325}$$
    Note:
    We're not subtracting the mean of danceability to predict it.
    
    We're using it to calculate the intercept, so that the line is centered correctly 
Step 3: 
$$\text{48.29325 + 0.273 * energy mean}$$
$$\hat{y}\text{ = 65.97}$$

### 2.2
Using the regression line, what would we predict the danceability to be for a song that had an energy of 90? 

Use this formula: 

- $$\text{y = mx + b}$$

Where:
- `m` (m slope) = 0.273 (from slope of regression line equation)
- Energy `x` = 90 
- intercept b is 48.29

So: 
$$\text{y = 0.273(90) + 48.29}\implies\text{y = 72.86}$$

### 2.3
Suppose we calculate our regression line in standard units. Would it be appropriate to use this regression line to predict a danceabillity for which our observed energy in standard units is -2?

**Original answer**: No, we would need to convert it to standard units, to verify if the observed energy is in -2

**AI**: Yes, it is mathematically valid to use the regression line in standard units to predict a value when the observed energy is -2 standard units.

- However, if -2 is far outside the typical range of the data (i.e., an extreme value), then the prediction may be unreliable. This is known as extrapolation. 

**My Takeaway:** In other words think of ± -2 SD out from mean, and how that is an outlier for the data. We wouldn't want to use that to predict the data

$$\hat{y}\text{ = r * x}_\text{standard units}$$
$$\hat{y}\text{ = 0.31 * -2}_\text{standard units}\implies\hat{y}\text{ - 0.62}$$

## Section 3

**3.1** Write a func that takes in array of observed values, an array of predictions, and returns RMSE 

```python
def RMSE(observed, predicted):
    error_res = observed - predicted
    squared_error = error_res**2 
    mse = np.mean(squared_error)
    return square_root = np.sqrt(mse) # convert back to standard units to quantify 
```

**3.2** In the calculation of the root mean squared error, why is it important for us to square the residuals before taking the mean? 
- Essentially, we must cancel out the 0's, and negatives before taking the mean of the subtracted arrays. 

**3.3** While both are valid (MSE and RMSE), why do we use RMSE over MSE? 
- Because RMSE lets us quantify data in a better way when referring to the calculations. 