import streamlit as st

# App title and layout
st.set_page_config(page_title="Binit Louda", page_icon="🌟", layout="centered")

# Title and subtitle
st.title("🌟 Welcome to Binit Louda 🌟")
st.subheader("Please enter your details below:")

# User Input Form
with st.form("user_details_form"):
    name = st.text_input("Your Name", placeholder="Enter your name")
    age = st.number_input("Your Age", min_value=1, max_value=100)
    bio = st.text_area("Short Bio", placeholder="Tell us something about yourself...")
    submitted = st.form_submit_button("Submit")

# Display User Input
if submitted:
    st.success("Thank you for submitting your details! 🎉")
    st.markdown(
        f"""
        <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
            <h2 style="text-align: center;">👤 {name}</h2>
            <p style="text-align: center;"><strong>Age:</strong> {age}</p>
            <p style="text-align: center;"><strong>Bio:</strong> {bio}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Optional Message
    st.write("🌟 Have a great day! 🌟")
