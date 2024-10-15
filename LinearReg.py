import streamlit as st

# Page Configurations
st.set_page_config(page_title="Kumar Aditya's Portfolio", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Resume", "Projects", "Skills", "Contact"])

# Home Section
if page == "Home":
    st.title("Kumar Aditya")
    st.write("Aspiring Data Scientist & Business Development Professional")
    st.image("assets/profile.jpg", width=300)
    st.markdown(
        """
        Hi, I'm **Kumar Aditya**. I have experience working with **ISRO** on satellite data analysis and have 
        developed expertise in **data science, machine learning**, and **business development** roles. 
        Explore this portfolio to learn more about me and my work.
        """
    )

# Resume Section
elif page == "Resume":
    st.header("Resume")
    st.subheader("Education")
    st.write("- **GIET University, Gunupur** – B.Tech in Computer Science")

    st.subheader("Experience")
    st.write(
        """
        - **ISRO (U R Rao Satellite Centre)**  
            *Telemetry Data Analysis and Modeling for spacecraft operations.*
        - **Central Tool Room & Training Centre (CTTC)**  
            *Internship with hands-on technical skills development.*
        """
    )

    st.subheader("Certifications")
    st.write("- Data Science for Engineers – **NPTEL**")

    st.download_button("Download Resume", "data/your_resume.pdf", "Download")

# Projects Section
elif page == "Projects":
    st.header("Projects")
    
    st.subheader("Disaster Message Classification")
    st.write(
        """
        - **Objective:** Categorize disaster messages to assist emergency responders.  
        - **Technologies:** Python, Streamlit, Machine Learning.  
        - [GitHub Repository](https://github.com/your-github/disaster-classification)
        """
    )
    
    st.subheader("Telemetry Data Analysis (ISRO)")
    st.write(
        """
        - **Objective:** Analyze and model satellite telemetry data for performance consistency.  
        - **Technologies:** Python, SQL, Pandas.
        """
    )
    
    st.subheader("Machine Learning Repository")
    st.write(
        """
        - **Objective:** Repository of machine learning algorithms with advanced concepts.  
        - [GitHub Repository](https://github.com/your-github/ml-repository)
        """
    )

# Skills Section
elif page == "Skills":
    st.header("Technical Skills")
    st.write(
        """
        - **Programming:** Python, Kotlin, SQL  
        - **Libraries:** NumPy, Pandas, Scikit-Learn, TensorFlow, Keras  
        - **Data Visualization:** Tableau, Matplotlib, Seaborn  
        - **Android Development:** Kotlin, Android Studio  
        - **Tools:** GitHub, Streamlit, MS Excel  
        """
    )

# Contact Section
elif page == "Contact":
    st.header("Get in Touch")
    st.write("📧 Email: your-email@example.com")
    st.write("[LinkedIn](https://linkedin.com/in/your-linkedin-profile)")
    st.write("[GitHub](https://github.com/your-github)")

    contact_form = """
    <form action="https://formspree.io/f/your-form-id" method="POST">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder="Your Email" required>
      <textarea name="message" placeholder="Your Message"></textarea>
      <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
