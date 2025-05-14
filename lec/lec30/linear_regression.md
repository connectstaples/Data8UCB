#### D8 Sp2025 Prof Sanchez 
# Regression 
#### Sean Villegas
#

# Review
Association best plotting mechanism: **scatter plot** 

What is the range of possible _r_?

- `-1 ≤ r ≤ 1` 

Which value of _r_ indicates strongest linear association between x and y? 
Options: 
- 0.75
- -0.8
- -0.6 
- 0
- 0.5
- 0.7
- -0.1 

- Out of all options, `0.75 `would mean be the strongest association 
       - **Fix**: Negative values can be the strongest in this case; correct option is `0.8`

Scatter Plot with **NO** association: 
- X has nothing to do with Y, data is completely spread out
- The average is at 0
# Understanding a more refined prediction method 
_simply, how can we finish the prediction line to be a full on line instead of rough prediction_ 

**Question**: How can we predict y with x using the regression line?
**Answer**:
1. Given a value of x, convert to standard units
2. Use the regression equation $$\text{y}_{SU}\text{= r * }\text{x}_{SU}$$

3. Convert back to the original units of y


# Nearest Neighbor Regression 
Scenario: 
- You have a scatter plot with a red line with `slope=1` linearly drawn crossing both axises 
- Say the data is cut at 1.5 instead of axis 3 (the full axis) with the `slope=1 `
    - `draw_veritical_line(1.5)`
- Will the predicted Y, or _true slope_ be above the red line or below? 
    - **Hint**: Is there more data on the inside of the red line and vertical line cut off or less? 
**<center>Answer</center>**

- The **Predicted Y** of the graph of averages will be below the `slope=1` because there are more points _(plots)_ below the line. Thus implying the average `Y` is less than the predicted `X` 


## Important note regarding the vertical line drawn in
- In scenario, _r_ is `0.5`, `draw_veritical_line(1.5)` and the `predicted Y` converge around 0.75 on the graph. Notice how 1.5 is _half_ of the vertical line. 
- Data is in **standard units**

### Rule
**_IFF we put the data in standard units, and we know the correlation coefficient_**   
 - Meaning we do not need to use the graph of averages
    - Main Takeaway: **"Why don't we just use a line whose slope is equal to the correlation coefficient between the two variables?**


### Equation Representing relationship: 
#
_Linear Regression Line:_
$$\text{Estimate of y}_{\text{standard units}}\text{ = r * x}_{\text{standard units}}$$

Where:
- _r_ correlation coefficient between the data
- `X` has been converted to standard units
- Estimate of Y is stated because generally we are trying to predict that
- **Main Takeaway:** whole idea of the regression effect is just to say that it will deviate less from average than `X` because this slope will _never_ be greater than 1
    - known as the **regression effect** 


## Converting Standard Units to do a Linear Regression Line
- Intercept depends on the slope

Step 1: 
$$\text{Estimate of y}_{\text{standard units}}\text{ = r * x}_{\text{standard units}}$$

Step 2: 
$$\text{y - average of y / SD of y = r * x - average of x/ SD of x}$$

Step 3: 
$$\text{y = (r * (x - average of x / SD of x) * SD of y + average of y}$$

Step 4: 
$$\text{y = ([r * x/SD of x] - [r * average of x/ SD of x]) * SD of y + average of y}$$

Step 5: 
$$\text{y = [r * sd of y / SD of x] * x - [r * SD of y / SD of x] * average of x + average of y}$$
**<center>Note</center>**
- Slope terms are repeated in:

1. The denominator of the first bracket
2. Numerator of the second bracket

Step 6: 
$$\text{y = slope * x - slope * average of x + average of y}$$

Step 7:
_the intercept is within the parenthesis_ 

$$\text{estimate of y = slope * x + (average of y - slope * average of x)}$$

### Correlation Math and Code (Slope and Intercept) 
Math: 
$$\text{slope of the regression line = r * [SD of y / SD of x]}$$
$$\text{intercept of the regression line = average of y - slope * average of x}$$
The three functions below compute the correlation, slope, and intercept. All of them take three arguments:
1. the name of the table
2. the label of the column containing
3. the label of the column containing 
```python
def correlation(t, label_x, label_y):
    return np.mean(standard_units(t.column(label_x))*standard_units(t.column(label_y)))

def slope(t, label_x, label_y):
    r = correlation(t, label_x, label_y)
    return r*np.std(t.column(label_y))/np.std(t.column(label_x))

def intercept(t, label_x, label_y):
    return np.mean(t.column(label_y)) - slope(t, label_x, label_y)*np.mean(t.column(label_x))
```
### Fitted Regression Func
The predictions all lie on the line and are known as the **“fitted values”.** The function fit takes the name of the table and the labels of x and y, returns an array of fitted values, one fitted value for each point in the scatter plot.
```python
def fit(table, x, y):
    """Return the height of the regression line at each x value."""
    a = slope(table, x, y)
    b = intercept(table, x, y)
    return a * table.column(x) + b
```
## Summary 
**Slope** in original units: 
$$\text{r * SD of y/ SD of x}$$

**Intercept** in original units:
$$\text{average of y - slope * average of x}$$

**Represented in code**: 
```python
def standard_units(data):
    "Convert any array of numbers to standard units."
    return (data - np.mean(data))/np.std(data)
```
## Example

A course has a midterm:
1. (average 70; standard deviation 10)
2. Hard final (average 50; standard deviation 12)

- If the scatter diagram comparing midterm & final scores for students has an oval shape with correlation 0.75, then... 
    - What do you expect the average final score would be: for students who scored 90 on the midterm? 60 on the midterm?

```python
# x variable: midterm scores
midterm_mean = 70
midterm_sd = 10

# y variable: final scores
final_mean = 50
final_sd = 12

# Correlation (relates x to y values)
corr = 0.75

# new observation's x value # the only thing you need to alter for the problem statement 
midterm_student = 90

midterm_student_su = (midterm_student - midterm_mean) / midterm_sd # 2.0 

final_student_su = midterm_student_su * corr # 1.5 (twice of 0.75)

final_student = final_student_su * final_sd + final_mean # 68.0 
```