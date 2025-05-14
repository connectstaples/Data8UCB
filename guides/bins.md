#### D8 Prof Sanchez 
# Categorical Distributions, Binning 
#### Sean Villegas

[Ch 7.2.1](https://inferentialthinking.com/chapters/07/2/Visualizing_Numerical_Distributions.html)

<style>

    .tnr {
        font-family:"Times New Roman";
        font-size: 16px;
    }

</style>

## Binning Data
The counts of individuals (i.e. rows) in the bins can be computed using the bin method
- compared to the group method used in the case of categorical data.
- The bin method takes as its argument a `column label` or `index`, and an optional argument in which you can specify the bins that you want.

- It is common to start with something that seems reasonable and then adjust based on the results.


```python

Table.bin(*columns, **vargs)

bin_counts = millions.bin('Adjusted Gross', bins=np.arange(300,2001,100))
bin_counts.show()
```


- From the output above, we see the starting left bin _excluding_ the right bin
- Since the bins split the number line into intervals, they are contiguous (i.e. sharing a common border; touching.)
- So we must be careful about values at the endpoints. By the usual Python convention, each bin **except** the last includes its _left endpoint_ but **NOT** its right endpoint.
- All the counts for this last bin appear in the second-to-last row, and the count for the last row is always zero.
- With quantitative data, the bins don’t have to be equally wide

### To make this point, we will use the notation `[a, b)` to refer to the bin that contains all the values that are greater than or equal to a and strictly less than b.

| bin | Adjusted Gross count |
| --- | --- |
| 300 | 68 | 
| 400 | 60 | 
| 500 | 32 | 



To understand the first row of the table, you have to look at the second row as well:
- These two rows tell us that there were 68 movies in the bin `[300, 400)`. 
    - i.e. 68 movies had adjusted gross receipts of at least 300 million dollars but less than 400 million dollars.
- In general, each element in the Adjusted Gross count column counts all the Adjusted Gross values that are **greater than or equal to the value in bin, but less than the next value in bin.**

## Histograms

**Application:**
- Plot a histogram of the values in column. Defaults to 10 bins of equal width. If bins is specified, it can be a number of bins to use (e.g. `bins=25` will produce a histogram with 25 bins) or an array of values to use as bins (e.g. `bins=make_array(1, 3, 4)` will produce 2 bins: `[1, 3) and [3, 4))`
-  column can be column names as strings or integer indices.


```python
tbl.hist(column)
tbl.hist(column, bins=...)
```

- This figure has two numerical axes. We will take a quick look at the horizontal axis first, and then examine the vertical axis carefully. 
    - For now, just note that the vertical axis does not represent percents.
- `tbl.hist` uses the same endpoint convention as the `bin` method. Bins include the data at their left endpoint, but not the data at their right endpoint, except for the rightmost bin which includes both endpoints.
- When it is a little harder to see exactly where the ends of the bins are situated, (i.e. it is hard to judge exactly where one bar ends and the next begins) $\rightarrow$ 
    - The optional argument `bins` can be used with `hist` to specify the endpoints of the bins exactly as with the bin method.

## Area Principle and Histogram Calculation 

**Area Principle**: The area principle of visualization says that when we represent a magnitude by a figure that has two dimensions, such as a rectangle, then the area of the figure should represent the magnitude.

Histograms follow the area principle and have two defining properties:
1. The bins are drawn to scale and are contiguous (though some might be empty), because the values on the horizontal axis are numerical and therefore have fixed positions on the number line.
2. The area of each bar is proportional to the number of entries in the bin.
    - Property 2 is the key to drawing a histogram
    $\text{area of bar = percent of entries in bin}$
    - Since area represents percents the heights must be mathematically accounted for: $\text{Property of Rectangle} \Rightarrow \text{height} \cdot \text{width of bin}$

    $$\rightarrow \text{height of bar = } \displaystyle\frac{\text{area of bar}}{\text{width of bin}} \text{ = } \displaystyle\frac{\text{percent of entries in bin}}{\text{width of bin}}$$ 

<div class='tnr'>

The units of height are “percent per unit on the horizontal axis.” The height is the percent in the bin relative to the width of the bin.

- So it is called density or crowdedness.

When drawn using this method, the histogram is said to be drawn on the **density scale** 

On this scale:
1. The area of each bar is equal to the percent of data values that are in the corresponding bin.
2. The total area of all the bars in the histogram is 100%. In terms of proportions, we can say that the areas of **all the bars in a histogram “sum to 1”**.

The height of each bar is the percent of elements that fall into the corresponding bin, relative to the width of the bin.
</div>

### Calculate the area of the bins in this table

_there are 200 movies in all_

| bin | Adjusted Gross count |
| --- | --- |
| 300 | 68 | 
| 400 | 60 | 
| 500 | 32 | 

Step 1: Calculate **Percent**

$\text{Percent = }\displaystyle\frac{68}{200} \cdot 100 = 34$

$\equiv \displaystyle\frac{\text{Count in Bin}}{\text{Total Count}} \cdot 100 = Percent $

Step 2: Calculate the **Height** 


$\text{Height = } \displaystyle\frac{34}{100} = 0.34$


### The main reason for plotting density on the vertical axis instead of counts or percents is to be able to compare histograms and approximate them with smooth curves where proportions are represented by areas under the curve.

- Drawing histograms on the **density scale** also allows us to compare histograms that are based on data sets of different sizes or have different choices of bins. 
- In such cases, neither bin counts nor percents may be directly comparable. But if both histograms are drawn to the density scale then areas and densities are comparable.
- The height of a bin is a **rough approximation**. We lose some finer detail when binning that doesn't account for the bins outliers so to speak. 


## Translating idea to code
```python
# add column containing percent in each bin
total_count = sum(histogram_elements.column('count'))
percents = np.round(100*histogram_elements.column('count')/total_count, 2) # the 2 allows us to have percentage then np.round makes that go away
histogram_elements = histogram_elements.with_columns('percent', percents)

# use np.diff to find width of all bins
bin_widths = np.diff(histogram_elements.column('bin'))
num_bins = histogram_elements.num_rows - 1    # the number of bins
histogram_elements = histogram_elements.take(
    np.arange(num_bins)).with_columns(
    'width', bin_widths
)


# we see the 2 again to put height in decimal format 
heights = np.round(
    histogram_elements.column('percent')/histogram_elements.column('width'),2)
histogram_elements = histogram_elements.with_columns('height', heights)
histogram_elements
```

## Difference between Bar charts and Histograms
- Bar charts display one numerical quantity per category.
    - They are often used to display the distributions of categorical variables. 
    - Histograms display the distributions of quantitative variables.
- All the bars in a bar chart have the same width, and there is an equal amount of space between consecutive bars. 
    - The bars can be in any order because the distribution is categorical. The bars of a histogram are contiguous; the bins are drawn to scale on the number line.
- The lengths (or heights, if the bars are drawn vertically) of the bars in a bar chart are proportional to the count in each category.
    - The heights of bars in a histogram measure densities; the areas of bars in a histogram are proportional to the counts in the bins.