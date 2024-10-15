import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing

# Title and description
st.title("🏠 Linear Regression App - Predict California House Prices")
st.markdown("""
This app demonstrates **Linear Regression** using the California Housing dataset.
You can visualize the relationship between variables, train a regression model, and predict house prices.
""")

# Load dataset
@st.cache_data
def load_data():
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame
    return df

df = load_data()
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Sidebar for selecting features
st.sidebar.header("⚙️ Model Settings")
test_size = st.sidebar.slider("Test Data Size (%)", 10, 50, 20) / 100
random_state = st.sidebar.number_input("Random State", value=42)

# Data visualization: Correlation heatmap
st.subheader("📈 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Select features and target
st.sidebar.header("🔍 Select Features")
all_features = df.columns[:-1].tolist()
selected_features = st.sidebar.multiselect("Choose features for prediction", all_features, default=all_features[:3])

if selected_features:
    X = df[selected_features]
    y = df["MedHouseVal"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Display metrics
    st.subheader("📋 Model Performance")
    st.write(f"**Mean Squared Error:** {mean_squared_error(y_test, y_pred):.2f}")
    st.write(f"**R² Score:** {r2_score(y_test, y_pred):.2f}")

    # Plot predictions vs actual values
    st.subheader("📊 Predictions vs Actual Values")
    fig2, ax2 = plt.subplots()
    ax2.scatter(y_test, y_pred, alpha=0.7)
    ax2.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
    ax2.set_xlabel('Actual')
    ax2.set_ylabel('Predicted')
    st.pyplot(fig2)

    # Sidebar input for predictions
    st.sidebar.header("🔮 Make Predictions")
    new_data = [st.sidebar.number_input(f"Enter {feature}", value=float(X[feature].mean())) for feature in selected_features]
    
    if st.sidebar.button("Predict"):
        prediction = model.predict([new_data])[0]
        st.sidebar.write(f"**Predicted Price:** ${prediction * 1000:.2f}")

else:
    st.warning("Please select at least one feature to build the model.")
