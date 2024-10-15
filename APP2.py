import streamlit as st

# Page Configuration
st.set_page_config(page_title="Kumar Aditya | Portfolio", page_icon="🚀", layout="centered")

# Header
st.title("Kumar Aditya 🚀")
st.subheader("Data Science & Machine Learning Enthusiast | Python Developer")
st.write("📞 +91 7205985622 | ✉️ [adityapupun535@gmail.com](mailto:adityapupun535@gmail.com)")
st.write("[LinkedIn](https://www.linkedin.com/in/kumar34aditya/) | [GitHub](https://github.com/Kumar21Aditya)")

# Career Objective
st.markdown("## 🎯 **Career Objective**")
st.write(
    """
    Analytical beginner with expertise in data collection, cleansing, and analysis. 
    Proficient in Python, SQL, and data visualization tools. Skilled in deriving actionable insights, 
    improving operational efficiency, and facilitating data-driven decision-making for business growth 
    with strong communication and problem-solving skills.
    """
)

# Education Section
st.markdown("## 🎓 **Education**")
st.table(
    {
        "Degree": ["B.Tech (CSE)", "+2 Science", "10th"],
        "Institute": [
            "GIET University",
            "Royal Higher Secondary School of Science and Technology, Bhubaneswar",
            "S.N High School, Basta, Balasore",
        ],
        "Year": ["2025", "2021", "2019"],
        "Score": ["7.96 CGPA", "85%", "80%"],
    }
)

# Technology Known
st.markdown("## 💻 **Technology Known**")
st.write("""
- **Languages**: Python, SQL, NumPy, Pandas, Matplotlib, Seaborn, Streamlit  
- **Tools & Software**: PowerBI, Tableau, MS-Excel  
- **Core Skills**: Machine Learning, Data Science, Statistical Analysis, EDA, Web Scraping, Automation
""")

# Internships Section
st.markdown("## 🛠️ **Internships**")
st.markdown("""
1. **U R Rao Satellite Centre, ISRO** (June 2024 - July 2024)  
   *Project*: Telemetry Data Analysis & Modelling  
   - Achieved over 95% accuracy in predictive modeling and anomaly detection.  
   - Conducted EDA and optimized operational efficiency.

2. **SAMSUNG Innovation Campus** (June 2023 - August 2023)  
   *Project*: Multiple Disease Predictor  
   - Developed a disease prediction site using Streamlit and ML algorithms.  
   - Improved healthcare accessibility with data-driven predictions.

3. **Central Tool and Training Centre (CTTC), Bhubaneswar** (June 2023 - July 2023)  
   - Conducted various minor projects involving data cleaning, EDA, and statistical analysis.  
   - Built dashboards using Power BI and Excel.
""")

# Academic Projects Section
st.markdown("## 🧑‍💻 **Academic Projects**")
st.markdown("""
1. **Disaster Response Intelligence: Real-Time Message Classification** (July 2024 - Present)  
   - Classifies messages into 36 categories, helping emergency responders prioritize needs.  

2. **RainPredict - Intelligent Rainfall Forecasting** (Jan 2024 - May 2024)  
   - Forecasts rainfall using historical weather data and ML algorithms, aiding agricultural planning.
""")

# Certifications Section
st.markdown("## 📜 **Certifications / Technical Event Participation**")
st.write("""
- Google Data Analytics Professional Certification - Google  
- AI & ML Workshop Certification - IIT Bhubaneswar  
- Remote Sensing Based Data Analytics on Agriculture - ISRO  
- Kaggle Data Analyst Certification - Kaggle
""")

# Soft Skills & Hobbies
st.markdown("## 🤝 **Soft Skills & Hobbies**")
st.write("""
- **Soft Skills**: Quick Learner, Team Player  
- **Hobbies**: Cooking, Sports
""")

# Personal Information
st.markdown("## 📝 **Personal Information**")
st.write("""
- **Date of Birth**: 01/04/2004  
- **Father’s Name**: Mr. Keshab Chandra Behera  
- **Languages Known**: English, Hindi, Odia  
- **Permanent Address**: Balasore, Odisha  
""")

# Footer
st.markdown("---")
st.write("📍 **Place**: Gunupur, Odisha | **Date**: 14/10/2024")
st.markdown("Made with 💖 using Streamlit")
