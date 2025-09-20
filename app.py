import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Interactive Linear Regression Visualizer", layout="wide")

st.title("HW1-1: Interactive Linear Regression Visualizer")

# Sidebar for user inputs
st.sidebar.header("Configuration")

# 1. Data Generation Parameters
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 500)
coefficient_a = st.sidebar.slider("Coefficient 'a' (y = ax + b + noise)", -10.0, 10.0, 2.0, 0.1)
noise_variance = st.sidebar.slider("Noise Variance (var)", 0, 1000, 100)

# Generate data
np.random.seed(42) # for reproducibility
x = np.random.rand(n_points) * 10
y_true = coefficient_a * x + 5 # b = 5 for now, can be made configurable later
noise = np.random.normal(0, np.sqrt(noise_variance), n_points)
y = y_true + noise

# Create a DataFrame for easier handling
df = pd.DataFrame({'x': x, 'y': y})

st.subheader("Generated Data and Linear Regression")

# Perform Linear Regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

# Calculate residuals for outlier detection
residuals = np.abs(y - y_pred)
df['residuals'] = residuals

# Identify top 5 outliers
outliers = df.nlargest(5, 'residuals')

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['x'], df['y'], label='Generated Data', alpha=0.6)
ax.plot(df['x'], y_pred, color='red', label='Linear Regression', linewidth=2)

# Label outliers
for i, row in outliers.iterrows():
    ax.annotate(f'Outlier {i}', (row['x'], row['y']), textcoords="offset points", xytext=(0,10), ha='center', color='purple')
    ax.scatter(row['x'], row['y'], color='purple', s=100, edgecolors='black', zorder=5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Linear Regression with Outliers")
ax.legend()
st.pyplot(fig)

st.subheader("Model Coefficients")
st.write(f"Coefficient (a): {model.coef_[0]:.2f}")
st.write(f"Intercept (b): {model.intercept_:.2f}")

st.subheader("Top 5 Outliers")
st.dataframe(outliers[['x', 'y', 'residuals']])
