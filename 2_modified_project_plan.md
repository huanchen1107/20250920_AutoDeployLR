# Project Plan for HW1-1: Linear Regression with Streamlit

## HW1-1: Interactive Linear Regression Visualizer

### Features:
1.  **Data Generation:**
    -   Generate `n` data points (x, y) where `n` is a user-selectable value between 100 and 1000.
    -   The relationship between x and y will be defined by `y = ax + b + noise`.
    -   `a`: User-selectable coefficient between -10 and 10.
    -   `noise`: Normally distributed noise `N(0, var)`, where `var` (variance) is user-selectable between 0 and 1000.

2.  **Linear Regression Visualization:**
    -   Plot the generated data points.
    -   Draw the calculated linear regression line in **red**.

3.  **Outlier Identification:**
    -   Identify and label the top 5 outliers (points furthest from the regression line).

4.  **User Interface:**
    -   Implement the application using **Streamlit** for an interactive web interface.
    -   Allow users to adjust parameters (`n`, `a`, `var`) via sliders or input fields.
    -   Display the generated plot and regression results.
