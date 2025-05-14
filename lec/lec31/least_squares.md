#### D8 Sp25; Lecture by GSI's 
# Least Squares
#### Sean Villegas

Chapters:

- [15.3](https://inferentialthinking.com/chapters/15/3/Method_of_Least_Squares.html)
- [15.4](https://inferentialthinking.com/chapters/15/4/Least_Squares_Regression.html)

## Review
1. Regression lines must be memorized 

## New Material 
- Building off last weeks lecture: 

### how well are we predicting _y_?

## New formula: 
y<sub>predicted</sub> is called a **_fitted value_**

$$\text{error = y}_{actual}\text{ -- y}_{predicted}$$

- **Note:** this can be computed after our helper functions, and simply subtracting the array columns to get the `error`

- These errors can be ±
- We want **magnitude** of error 
    - (the absolute value of the error)
    - In laymans terms: How far away are our predicted values from the actual y values

### How do we summarize all the errors?

_With Root Mean Squared Error (RMSE); calculate starting backwards_
- mean is taken by `np.average`
- square root is calculated by `**0.5`

$$\text{error = y}_{actual}\text{ -- y}_{predicted}$$

1. Square each error to avoid cancellation
$$\text{(error)}^2$$
2. Take the mean of the squared errors
$$\text{mean((error)}^2\text{)}$$
3. Take the square root of these errors
$$\sqrt{{mean((error)}^2\text{)}}$$
4. **Result**: RMSE
    - Root Mean Squared Error

**<center>Note</center>**
- You can see just the MSE (mean Squared Error); meaning you do not need to take the square root of it 

## Least Squares Lines
- for RMSE:
    - Minimizes root mean squared error
- for MSE
    - Minimizes among all mean squared error possible lines 

### Numerical Optimization Uses after applied above steps for closest linear regression
- find the **least squares line** and it is approximate (meaning not the true value, but pretty close ).
    - works for other models besides linear regression 

Data8 Has a custom function that: 
- outputs the arguments that minimize the value of the passed in function
```python
from ucb import data8

"""
rmse(slope, intercept)
minimize(rmse)
"""
minimize(func) # outputs an array([slope, intercept]) if rmse has two variables within it; depends on the function
```
- `array([slope, intercept])` 
    - tells us the line that minimizes the RMSE
        - in other words we find the least squares line

### How does the least squares line relate to the regression line?

Answer: They are the same

- The regression line is the only line that minimizes RMSE!

**<center>Names for Linear Regression Line</center>**
- Least squares line
- “Best fit” line
- Regression Line


