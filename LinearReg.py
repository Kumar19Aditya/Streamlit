import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Set the title and layout
st.set_page_config(page_title="Sample Dashboard", page_icon="📊", layout="wide")
st.title("📊 Interactive Data Dashboard")

# Sample data generation
np.random.seed(42)
data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=50),
    "Sales": np.random.randint(100, 500, size=50),
    "Profit": np.random.randint(20, 100, size=50),
    "Category": np.random.choice(['Electronics', 'Clothing', 'Groceries'], size=50)
})

# Sidebar Filters
st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox("Select Category", data["Category"].unique())
filtered_data = data[data["Category"] == selected_category]

# Metrics Display
st.subheader(f"📈 Metrics for {selected_category}")
total_sales = filtered_data["Sales"].sum()
total_profit = filtered_data["Profit"].sum()
avg_profit = filtered_data["Profit"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales}")
col2.metric("Total Profit", f"${total_profit}")
col3.metric("Avg Profit", f"${avg_profit:.2f}")

# Line Chart - Sales Trend
st.subheader("📅 Sales Trend")
fig, ax = plt.subplots()
ax.plot(filtered_data["Date"], filtered_data["Sales"], marker='o', color='teal')
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
st.pyplot(fig)

# Pie Chart - Profit Distribution by Category
st.subheader("🍕 Profit Distribution by Category")
fig_pie = px.pie(data, values='Profit', names='Category', title='Profit by Category')
st.plotly_chart(fig_pie, use_container_width=True)

# Data Table Display
st.subheader("📝 Filtered Data")
st.dataframe(filtered_data)

# Add Footer
st.markdown("""
    <hr style='border: 1px solid #D3D3D3;'>
    <p style='text-align: center;'>Built with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)
