import streamlit as st

# Title and Subtitle for the app
st.title("👋 Welcome to the Fun Profile Builder!")
st.subheader("Please provide some basic details about yourself.")

# Collecting user inputs
name = st.text_input("What's your name?", "")
age = st.number_input("How old are you?", min_value=1, max_value=100, step=1)
qualification = st.selectbox(
    "Your highest qualification:",
    ["High School", "Diploma", "Undergraduate", "Postgraduate", "PhD"]
)
skills = st.text_area("List your skills (comma-separated)", "")

# Submit button
if st.button("Submit"):
    # Display the results with the fun message
    if name.strip():
        st.success(f"Your profile is ready, {name} BSDK! 😎")
    else:
        st.warning("Please enter your name to complete the profile.")
