#### D8 Spring 2025 HW08
# 
#### Sean Villegas 

# 


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