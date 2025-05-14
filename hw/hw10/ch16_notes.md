#### D8 Sp25 Prof Sanchez
# Ch 16 Notes and Lecture Review
#### Sean Villegas
[Chapter 16](https://inferentialthinking.com/chapters/16/Inference_for_Regression.html)

## Review 

### Prediction: 

**How can we predict the outcome of a new individual?**
- Find others who are like that individual and whose outcomes you know 
    - Use the above outcomes as a first pass

**What type of variable are we trying to predict?**
- If numerical we perform a regression task.
- If categorical we perform a classification task.

**Making informed guesses is Prediction** 
- We use a dataset of complete information, and we predict based on incomplete information 

**We effectively evaluate our prediction machine by using _some_ of the data to build the model**
- We split our dataset into two parts
    - Training set
    - Fit the prediction machine with this data
- We then test the set to valuate the prediction machine with this data

**We split data randomly**
- The training set is larger than the testing set

**Evaluating our prediction machine**
- For each row in the testing data set you plug the predictor variable values into the machine
- In turn will give us a y<sub>predicted</sub> for each row
- Then calculate the evaluation metric by using the y<sub>actual</sub> values in the testing set with the y<sub>predicted</sub> that was computed


## Regression Inference 
1. We observed a slope based on our sample of points.
2. But what if the sample scatter plot got its slope just by chance?
3. What if the true line is actually flat?!

**Null and Alternative Hypothesis** 
- Null: Slope of the true line is at 0 
- Alternative: Slope of the true line is something other than 0

### Testing
1. Create a bootstrap confidence interval for the slope 
2. If the interval contains 0 i.e. `percentile()` returns 0 you **retain** null
3. If the interval does not contain 0 from our `percentile` func, then you **reject** the null

**Can we predict the response of a new individual who is not in our sample?**
_the regression line is our estimate of the truth_ 
- Running a regression on the data we have will gives us one prediction per observation.
- But if we had different data:
    - the prediction might be different.
- This suggests that we must bootstrap again to create a confidence interval for the true prediction 

### Confidence Interval for true prediction 
1. Take a bootstrap sample of the data
2. Run a regression and get a prediction of our new observation from each
3. Repeat this process many times and put these predictions on a histogram
4. Use the `percentile` method for the interval.

**The prediction interval depends on the value of x**
- The predicted values of y depend on the value on x 
- The width of the prediction interval also depends on x
- Whats normally found: 
    - intervals are wider for values of x that are further away from the mean of x.

