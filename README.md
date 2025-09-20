# Interactive Linear Regression Visualizer

This project is a Streamlit web application that allows users to interactively visualize linear regression. Users can adjust parameters such as the number of data points, the coefficient of the linear relationship, and the amount of noise, and see how these changes affect the regression line and the identification of outliers.

## Demo Site

The application is deployed on Streamlit Cloud and can be accessed here: [https://aiotda.streamlit.app/](https://aiotda.streamlit.app/)

## Project Summary

This project was developed to provide an interactive tool for understanding linear regression. The development process involved setting up a Streamlit application, creating a virtual environment, installing dependencies, and implementing the core features of the application. The project was then deployed to Streamlit Cloud.

## Development Log

This section provides a summary of the development steps taken, as recorded in `0_devLog.md`.

*   **1.0-2.0:** Initial setup, including the creation of the development log (`0_devLog.md`) and the to-do list (`Todo.md`).
*   **3.0-4.0:** Modification and verification of the project plan.
*   **5.0:** Execution of the project plan, starting with the creation of the Streamlit application (`app.py`).
*   **6.0-11.0:** Troubleshooting and resolving issues related to running the Streamlit application, including the creation of `requirements.txt`, setting up a virtual environment, and installing dependencies.
*   **12.0-13.0:** Successfully running the Streamlit application.

## To-Do List for Linear Regression Implementation

This section outlines the general steps for implementing a linear regression model, as detailed in `Todo.md`.

### 1. Data Preparation
- [ ] Load the dataset (e.g., from CSV, NumPy array).
- [ ] Handle missing values (if any).
- [ ] Split data into training and testing sets.
- [ ] Feature scaling (if necessary, e.g., StandardScaler).

### 2. Model Implementation
- [ ] Implement the Linear Regression model from scratch (if required).
  - [ ] Initialize weights and bias.
  - [ ] Define the hypothesis function (h(x) = wx + b).
  - [ ] Define the cost function (Mean Squared Error).
  - [ ] Implement Gradient Descent for optimization.
    - [ ] Calculate gradients.
    - [ ] Update weights and bias.

### 3. Training
- [ ] Train the model using the training data.
- [ ] Monitor convergence (e.g., plot cost function over iterations).

### 4. Evaluation
- [ ] Make predictions on the test set.
- [ ] Calculate evaluation metrics:
  - [ ] Mean Squared Error (MSE)
  - [ ] R-squared (R2 Score)
- [ ] Visualize predictions vs. actual values.

### 5. Prediction
- [ ] Create a function to make predictions on new, unseen data.

### 6. Documentation and Reporting
- [ ] Document the code.
- [ ] Write a report summarizing the implementation, results, and conclusions.
