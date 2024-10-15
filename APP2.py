import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Kumar Aditya | Portfolio", page_icon="🎯", layout="centered")

# CSS Styling for Customization
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 50px; color: #ff6347;
        font-weight: bold; text-align: center;
    }
    .subheader { 
        font-size: 18px; 
        color: #555;
        text-align: center;
    }
    .contact {
        margin-top: 10px;
        text-align: center;
    }
    .section-title {
        font-size: 30px;
        margin: 20px 0;
        color: #1e90ff;
    }
    .footer {
        text-align: center;
        font-style: italic;
        color: #aaa;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section with Photo (Optional)
st.markdown('<h1 class="title">Kumar Aditya</h1>', unsafe_allow_html=True)
st.subheader("🚀 Data Science Enthusiast | Python Developer | Machine Learning Practitioner")

# Contact Information
st.markdown('<div class="contact">📞 +91 7205985622 | ✉️ [adityapupun535@gmail.com](mailto:adityapupun535@gmail.com)</div>', unsafe_allow_html=True)
st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/kumar34aditya/) | [💻 GitHub](https://github.com/Kumar21Aditya)")

# Career Objective Section
st.markdown('<h2 class="section-title">🎯 Career Objective</h2>', unsafe_allow_html=True)
st.write(
    """
    Analytical beginner with expertise in data collection, cleansing, and analysis. 
    Proficient in Python, SQL, and data visualization tools. Skilled in deriving actionable insights, 
    improving operational efficiency, and enabling data-driven decision-making with strong communication skills.
    """
)

# Education Section
st.markdown('<h2 class="section-title">🎓 Education</h2>', unsafe_allow_html=True)
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

# Skills Section
st.markdown('<h2 class="section-title">💻 Technology Known</h2>', unsafe_allow_html=True)
st.write(
    """
    - **Languages**: Python, SQL, NumPy, Pandas, Matplotlib, Seaborn, Streamlit  
    - **Tools & Software**: PowerBI, Tableau, MS-Excel  
    - **Core Skills**: Machine Learning, Data Science, EDA, Web Scraping, Automation
    """
)

# Internship Section
st.markdown('<h2 class="section-title">🛠️ Internships</h2>', unsafe_allow_html=True)
st.markdown("""
1. **U R Rao Satellite Centre, ISRO** (June 2024 - July 2024)  
   - Telemetry Data Analysis & Modelling with 95% prediction accuracy.  

2. **SAMSUNG Innovation Campus** (June 2023 - August 2023)  
   - Developed a disease prediction site with ML algorithms for diseases like heart disease and diabetes.

3. **Central Tool and Training Centre (CTTC)** (June 2023 - July 2023)  
   - Completed projects in data cleaning, EDA, and statistical analysis with dashboards in Power BI.
""")

# Projects Section with Optional Image
st.markdown('<h2 class="section-title">🧑‍💻 Academic Projects</h2>', unsafe_allow_html=True)

st.markdown("""
1. **Disaster Response Intelligence** (July 2024 - Present)  
   - Real-time message classification for disaster response with 36 categories.

2. **RainPredict - Intelligent Rainfall Forecasting** (Jan 2024 - May 2024)  
   - Forecasted rainfall using ML models for agricultural planning.
""")

st.image("https://source.unsplash.com/600x300/?data,technology", caption="Building with Passion 🚀", use_column_width=True)

# Certifications Section
st.markdown('<h2 class="section-title">📜 Certifications</h2>', unsafe_allow_html=True)
st.write("""
- Google Data Analytics Professional Certification - Google  
- AI & ML Workshop Certification - IIT Bhubaneswar  
- Remote Sensing Data Analytics on Agriculture - ISRO  
- Kaggle Data Analyst Certification - Kaggle
""")

# Soft Skills & Hobbies Section
st.markdown('<h2 class="section-title">🤝 Soft Skills & Hobbies</h2>', unsafe_allow_html=True)
st.write("""
- **Soft Skills**: Quick Learner, Team Player  
- **Hobbies**: Cooking, Sports
""")

# Personal Information Section
st.markdown('<h2 class="section-title">📝 Personal Information</h2>', unsafe_allow_html=True)
st.write("""
- **Date of Birth**: 01/04/2004  
- **Father’s Name**: Mr. Keshab Chandra Behera  
- **Languages Known**: English, Hindi, Odia  
- **Permanent Address**: Balasore, Odisha  
""")

# Footer
st.markdown('<div class="footer">📍 Gunupur, Odisha | 📅 14/10/2024 | Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
