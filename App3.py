import streamlit as st

# Fun title and subtitle
st.title("🎉 Welcome to Your Fun Profile 🎉")
st.subheader("Let's learn some fun things about you! 😁")

# Collecting user inputs in a playful way
name = st.text_input("What's your name?", "")
food = st.text_input("🍕 What's your favorite food?")
dream = st.text_area("🌟 What's your biggest dream?")
hobby = st.text_input("🎨 What's your favorite hobby?")
superpower = st.text_input("🦸 If you could have one superpower, what would it be?")

# Submit button with fun message
if st.button("Submit"):
    if name.strip():
        # Playful prank message
        st.balloons()  # Adds a balloon effect for fun!
        st.success(f"Nice to know all this, {name}! 🎉")
        st.error("But... Go and study first! 📚🤣")
    else:
        st.warning("Oops! I need to know your name first. 😅")

