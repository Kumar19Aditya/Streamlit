import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Kumar Aditya | Portfolio", layout="wide")

# Sidebar Style with Red Selection Effect
st.markdown("""
    <style>
    .sidebar .sidebar-content { padding: 0; }
    .box {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #444;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s;
    }
    .box:hover {
        background-color: #444;
    }
    .selected {
        background-color: red !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Options
options = [
    "Home", "Career Objective", "Education", "Skills & Technology",
    "Internships", "Projects", "Certifications",
    "Soft Skills & Hobbies", "Personal Information"
]

# Create Sidebar with Selection Logic
selected = st.sidebar.radio("", options, index=0, format_func=lambda x: f"📌 {x}")

# Dynamic Content Based on Selection
def display_content(option):
    if option == "Home":
        st.title("Welcome to My Portfolio!")
        st.write("Explore my projects, skills, certifications, and more.")
    elif option == "Career Objective":
        st.subheader("🎯 Career Objective")
        st.write(
            "Analytical beginner with expertise in data collection, "
            "cleansing, and analysis. Skilled in deriving actionable "
            "insights, improving efficiency, and facilitating data-driven decision-making."
        )
    elif option == "Education":
        st.subheader("🎓 Education")
        st.table({
            "Degree": ["B.Tech (CSE)", "+2 Science", "10th"],
            "Institute": [
                "GIET University", 
                "Royal Higher Secondary School", 
                "S.N High School, Balasore"
            ],
            "Year": ["2025", "2021", "2019"],
            "Score": ["7.96 CGPA", "85%", "80%"]
        })
    elif option == "Skills & Technology":
        st.subheader("💻 Skills & Technology")
        st.write("""
            - **Languages**: Python, SQL, NumPy, Pandas, Matplotlib, Seaborn, Streamlit  
            - **Tools**: PowerBI, Tableau, MS-Excel  
            - **Core Skills**: Machine Learning, Data Science, EDA, Web Scraping, Automation
        """)
    elif option == "Internships":
        st.subheader("🛠️ Internships")
        st.markdown("""
        1. **U R Rao Satellite Centre, ISRO** (June 2024 - July 2024)  
           - Telemetry Data Analysis & Modelling with 95% prediction accuracy.

        2. **SAMSUNG Innovation Campus** (June 2023 - August 2023)  
           - Developed a disease prediction website using Streamlit.

        3. **CTTC Bhubaneswar** (June 2023 - July 2023)  
           - Completed EDA and statistical analysis projects using Power BI and Excel.
        """)
    elif option == "Projects":
        st.subheader("🧑‍💻 Projects")
        st.markdown("""
        1. **Disaster Response Intelligence** (July 2024 - Present)  
           - Real-time classification of disaster-related messages.

        2. **RainPredict - Intelligent Rainfall Forecasting** (Jan 2024 - May 2024)  
           - Developed rainfall forecasting models using ML techniques.
        """)
    elif option == "Certifications":
        st.subheader("📜 Certifications")
        col1, col2 = st.columns(2)
        with col1:
            st.image("certificate1.png", caption="Google Data Analytics")
            st.image("certificate3.png", caption="Remote Sensing Analytics - ISRO")
        with col2:
            st.image("certificate2.png", caption="AI & ML Workshop - IIT Bhubaneswar")
            st.image("certificate4.png", caption="Kaggle Data Analyst Certification")
    elif option == "Soft Skills & Hobbies":
        st.subheader("🤝 Soft Skills & Hobbies")
        st.write("""
        - **Soft Skills**: Quick Learner, Team Player  
        - **Hobbies**: Cooking, Sports
        """)
    elif option == "Personal Information":
        st.subheader("📝 Personal Information")
        st.write("""
        - **Date of Birth**: 01/04/2004  
        - **Father’s Name**: Mr. Keshab Chandra Behera  
        - **Languages Known**: English, Hindi, Odia  
        - **Permanent Address**: Balasore, Odisha
        """)

# Display the Selected Content
display_content(selected)
