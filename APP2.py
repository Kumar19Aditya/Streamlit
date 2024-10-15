import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Hey Love! ❤️",
    page_icon="🌸",
    layout="centered",
)

# Header
st.title("🌷 Hey, Beautiful! 🌷")
st.subheader("Welcome to your special little place on the web ✨")
st.write("**Just for you, because you deserve the best!** 🥰")

# Random Cute Message
messages = [
    "You are the best thing that's ever happened to me 💖",
    "I love you more than words can express 😘",
    "Every moment with you feels like magic 🌟",
    "You make my world so much better ❤️",
]
st.markdown(f"### **💌 Today's Message:** {random.choice(messages)}")

# Image Section
st.markdown("## **Our Sweet Moments Together**")
st.image("https://source.unsplash.com/600x300/?couple,romantic", caption="Our Journey Together 💕", use_column_width=True)

# Fun Button Interaction
if st.button("Press for a Surprise! 🎁"):
    st.balloons()
    st.write("💬 **Surprise!** Just wanted to say, you are my everything.")

# Footer
st.write("Made with 💖 by Aditya.")
