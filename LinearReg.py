import streamlit as st

# Set page configuration
st.set_page_config(page_title="User Details App", page_icon="📝", layout="centered")

# Title and subtitle
st.title("📝 User Details Form")
st.subheader("Enter your details below")

# Form to collect user details
with st.form("user_form"):
    name = st.text_input("Name", max_chars=50)
    email = st.text_input("Email", max_chars=50)
    age = st.slider("Age", min_value=10, max_value=100, step=1)
    bio = st.text_area("Short Bio", height=100)
    submitted = st.form_submit_button("Submit")

# If the form is submitted, display the details attractively
if submitted:
    st.success("Details Submitted Successfully!")
    
    # Displaying user info
    st.header("🎉 Here's what you entered:")
    st.markdown(f"""
        <div style='
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        '>
            <h2 style='text-align: center; color: #4CAF50;'>{name}</h2>
            <p style='text-align: center; font-size: 18px;'><strong>Email:</strong> {email}</p>
            <p style='text-align: center; font-size: 18px;'><strong>Age:</strong> {age}</p>
            <blockquote style='font-size: 16px; font-style: italic; text-align: center;'>{bio}</blockquote>
        </div>
    """, unsafe_allow_html=True)

    # Optional: Display profile image or avatar (dummy image for now)
    st.image("https://via.placeholder.com/150", caption="User Avatar", width=150, use_column_width=False)
