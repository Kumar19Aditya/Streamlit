import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Kumar Aditya | Portfolio", page_icon="🎯", layout="wide")

# Sidebar Style
st.markdown("""
    <style>
    .sidebar .sidebar-content { padding: 0; }
    .box {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #444;
        border-radius: 8px;
        padding: 10px;
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

# Sidebar Navigation Logic
options = [
    "Home", "Career Objective", "Education", "Skills & Technology", 
    "Internships", "Projects", "Certifications", 
    "Soft Skills & Hobbies", "Personal Information"
]

# Create empty container for sidebar options to use dynamic styling
selected_option = st.sidebar.empty()
selected = None

# Render the sidebar with interactive boxes
for option in options:
    if selected == option:
        selected_option.markdown(f'<div class="box selected">{option}</div>', unsafe_allow_html=True)
    else:
        if st.sidebar.button(option):
            selected = option
            selected_option.markdown(f'<div class="box selected">{option}</div>', unsafe_allow_html=True)
            break  # Stop after selecting one option

# Display Content Based on Selection
def display_content(option):
    if option == "Home":
        st.subheader("Welcome to my Portfolio!")
        st.write("Explore my projects, skills, certifications, and more through the menu on the left.")
    elif option == "Career Objective":
        st.subheader("🎯 Career Objective")
        st.write("Analytical beginner with expertise in data collection, cleansing, and analysis...")
    elif option == "Education":
        st.subheader("🎓 Education")
        st.table({
            "Degree": ["B.Tech (CSE)", "+2 Science", "10th"],
            "Institute": [
                "GIET University", 
                "Royal Higher Secondary School of Science and Technology, Bhubaneswar", 
                "S.N High School, Basta, Balasore"
            ],
            "Year": ["2025", "2021", "2019"],
            "Score": ["7.96 CGPA", "85%", "80%"]
        })
    elif option == "Skills & Technology":
        st.subheader("💻 Skills & Technology")
        st.write("""
            - **Languages**: Python, SQL, NumPy, Pandas, Matplotlib, Seaborn, Streamlit  
            - **Tools & Software**: PowerBI, Tableau, MS-Excel  
            - **Core Skills**: Machine Learning, Data Science, EDA, Web Scraping, Automation
        """)
    elif option == "Internships":
        st.subheader("🛠️ Internships")
        st.markdown("""
        1. **U R Rao Satellite Centre, ISRO** (June 2024 - July 2024)  
           - Telemetry Data Analysis & Modelling with 95% prediction accuracy.

        2. **SAMSUNG Innovation Campus** (June 2023 - August 2023)  
           - Developed a disease prediction site with ML algorithms for diseases like heart disease and diabetes.

        3. **CTTC Bhubaneswar** (June 2023 - July 2023)  
           - Completed projects in data cleaning, EDA, and statistical analysis with dashboards in Power BI.
        """)
    elif option == "Projects":
        st.subheader("🧑‍💻 Projects")
        st.markdown("""
        1. **Disaster Response Intelligence** (July 2024 - Present)  
           - Real-time message classification for disaster response with 36 categories.

        2. **RainPredict - Intelligent Rainfall Forecasting** (Jan 2024 - May 2024)  
           - Forecasted rainfall using ML models for agricultural planning.
        """)
    elif option == "Certifications":
        st.subheader("📜 Certifications")

        col1, col2 = st.columns(2)
        with col1:
            st.image("certificate1.png", caption="Google Data Analytics Certification", use_column_width=True)
        with col2:
            st.image("certificate2.png", caption="AI & ML Workshop - IIT Bhubaneswar", use_column_width=True)
        with col1:
            st.image("certificate3.png", caption="Remote Sensing Analytics - ISRO", use_column_width=True)
        with col2:
            st.image("certificate4.png", caption="Kaggle Data Analyst Certification", use_column_width=True)
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

# Display Content
if selected:
    display_content(selected)
else:
    st.subheader("Welcome to my Portfolio!")
    st.write("Use the menu on the left to explore my work.")

