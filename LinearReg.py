import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Set title for the app
st.title("Simple Linear Regression App")

# User input: Training Data
st.subheader("Enter Training Data")
X_values = st.text_input("Enter X values (comma-separated):", "1, 2, 3, 4, 5")
Y_values = st.text_input("Enter Y values (comma-separated):", "2, 4, 6, 8, 10")

# User input: Value to Predict
st.subheader("Prediction")
X_new = st.number_input("Enter a value to predict:")

# Process data if valid input is provided
try:
    X = np.array([float(x) for x in X_values.split(",")]).reshape(-1, 1)
    Y = np.array([float(y) for y in Y_values.split(",")])

    # Fit the Linear Regression Model
    model = LinearRegression()
    model.fit(X, Y)

    # Make a prediction
    prediction = model.predict([[X_new]])

    # Display the result
    st.write(f"Predicted Y value: {prediction[0]:.2f}")

except ValueError:
    st.error("Please enter valid numeric values for X and Y.")

