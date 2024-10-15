import streamlit as st
from datetime import date
import random

# Customize page
st.set_page_config(page_title="Special Website for You ❤️", page_icon="🌹", layout="centered")

# Header with greeting and animation
st.title("Hey, Love! 💕")
st.subheader("Welcome to your special place on the web.")
st.markdown("**Every click, just for you.** 🥰")

# Background music (optional)
st.markdown(
    """
    <audio controls autoplay>
      <source src="https://www.example.com/background-music.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True
)

# Random love message
messages = [
    "You are my sunshine on a cloudy day. ☀️",
    "Being with you feels like a dream. 💫",
    "Every moment with you is priceless. 🕰️"
]
st.markdown(f"**Today's Message:** {random.choice(messages)}")

# Memory timeline with images
st.markdown("## Our Best Moments Together")
col1, col2 = st.columns(2)

with col1:
    st.image("moment1.jpg", caption="Our First Date", width=300)

with col2:
    st.image("moment2.jpg", caption="That Special Trip", width=300)

# Fun quiz
st.markdown("## Test Your Knowledge! 🤓")
q1 = st.radio("Where did we first meet?", ["Cafe", "Library", "Mall"])
if q1 == "Cafe":
    st.success("Correct! 😍")
else:
    st.error("Oops, try again! 😉")

# Interactive drawing canvas (optional)
st.markdown("## Leave a Cute Doodle 🎨")
canvas_result = st.canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Background color
    stroke_width=3,
    height=200,
    width=400,
    drawing_mode="freedraw",
    key="canvas",
)

# Footer
st.markdown("Made with 💖 just for you.")
