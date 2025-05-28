import streamlit as st

# Page configuration
st.set_page_config(page_title="Santosh Saroj | Portfolio", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        /* Set background color and subtle texture */
        .stApp {
            background-color: #F0F2F6;
            background-image: url("https://www.transparenttextures.com/patterns/white-wall.png");
            background-size: cover;
        }

        /* Style headings */
        h1, h2, h3 {
            color: #0e76a8;
        }

        /* Section card styling */
        .card {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }

        /* Button styling with hover */
        div[data-testid="stButton"] > button {
            background-color: #0e76a8;
            color: white;
            border-radius: 8px;
            padding: 10px 16px;
            border: none;
            transition: all 0.3s ease;
        }

        div[data-testid="stButton"] > button:hover {
            background-color: #0c5f7a;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            padding: 20px 0;
            font-size: 14px;
            color: gray;
            margin-top: 40px;
        }

        .footer a {
            color: #0e76a8;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# About Me Section
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("image.jpg", caption="Santosh", width=150)
    with col2:
        st.markdown("<h1 style='margin-bottom: 5px;'>SANTOSH ANJALI HARIRAM SAROJ</h1>", unsafe_allow_html=True)
        st.write("""
        Aspiring data analyst with a background in finance and mathematics. 
        Currently pursuing a Master’s in Management Studies (Finance) and certified 
        in business analysis and financial accounting.

        Experienced in teaching mathematics with strong analytical and problem-solving skills. 
        Looking to apply data skills to support business insights and decision-making.
        """)

# Projects Section
st.markdown("""
    <style>
        .project-title {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }
        .project-tech {
            font-size: 14px;
            color: #555;
            margin-top: 10px;
        }
        .project-links a {
            display: inline-block;
            margin-right: 15px;
            margin-top: 10px;
            text-decoration: none;
            font-weight: 500;
            color: #0366d6;
        }
    </style>
""", unsafe_allow_html=True)

st.header("📂 Projects")

# --- Project 1
with st.expander("🔍 Crime Rate Predictor"):
    st.markdown("""
    <div class='project-title'>Crime Rate Predictor</div>
    This project develops a Logistic Regression model to predict crime risk levels in Indian states based on:
    - Population Density
    - Per Capita Income
    - Literacy Rate
    - Unemployment Rate
    - Drug Addiction Rate

    **Key Features:**
    - Government data (PIB, MoSPI)
    - Feature selection and model evaluation
    - Visual analytics + interactive inputs

    <div class='project-tech'><strong>Technologies:</strong> Python, Pandas, Scikit-learn, Streamlit</div>

    <div class='project-links'>
        <a href='https://github.com/iamssaroj/crime-rate-predictor' target='_blank'>📂 GitHub</a>
        <a href='https://crime-rate-predictor-vfw37ir4xbmccjikfcmooi.streamlit.app/' target='_blank'>▶️ Live Demo</a>
    </div>
    """, unsafe_allow_html=True)

# --- Project 2
with st.expander("📊 FIRInsight"):
    st.markdown("""
    <div class='project-title'>FIRInsight (inprogress)</div>
    This project uses knowledge of NLP techniques to automatically group FIRs based on similarity in the type of crime:

    - Gather a dataset of FIRs in text or PDF format  
    - Ensure diversity: FIRs from multiple regions, languages, and crime types  
    - Collect FIRs through police department websites  
    - Use RTI applications to obtain anonymized FIR data for research/education  

    **Key Features:**
    - Text-Based FIR Clustering  
    - Natural Language Processing (NLP) Pipeline  
    - Unsupervised Machine Learning Model  
    - Cluster Interpretation  
    - Cluster Visualization  

    <div class='project-tech'><strong>Technologies:</strong> Python, Scikit-learn, Folium, Streamlit</div>

    <div class='project-links'>
        <a href='https://github.com/iamssaroj/fir-clustering' target='_blank'>📂 GitHub</a>
        <a href='https://firinsight.streamlit.app/' target='_blank'>▶️ Live Demo</a>
    </div>
    """, unsafe_allow_html=True)

# --- Example Project 3 (Future)
with st.expander("🏥 Smart Emergency Medical Assistance System (SEMAS)"):
    st.markdown("""
    <div class='project-title'>Smart Emergency Medical Assistance System (SEMAS-inprogress)</div>
    ✅ Project Objective:
    To develop an AI-based system that can provide real-time, personalized hospital/clinic recommendations during a medical emergency by analyzing the patient’s known medical history and symptoms, and matching them with nearby healthcare facilities with the required specialization and resources.

    **Key Features:**
    - Patient profile integration (e.g. chronic diseases, allergies)
    - Real-time GPS and hospital data usage
    - Symptom-to-specialist mapping
    - Multilingual voice/text interface
    - Alert generation to emergency contacts

    <div class='project-tech'><strong>Technologies:</strong> Python, Pandas, Scikit-learn, Streamlit</div>

    <div class='project-links'>
        <a href='https://github.com/iamssaroj/movie-recommender' target='_blank'>📂 GitHub</a>
        <a href='https://movie-recommender-app.streamlit.app/' target='_blank'>▶️ Live Demo</a>
    </div>
    """, unsafe_allow_html=True)

# Experience Section
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("💼 Experience")

    with st.expander("📚 Social Science & Mathematics Educator | Part time (2022 – Present)"):
        st.write("""
        - Provided coaching in Social Science & mathematics to students from 8th to 10th grade.
        - Customized lesson plans to match individual learning styles and academic goals.
        - Developed strong communication and analytical skills while simplifying complex concepts.
        """)

    with st.expander("📊 AI Intern | Microsoft(CSR) (Apr 2025 – May 2025)"):
        st.write("""
        - Conducted exploratory data analysis and created visual dashboards.
        - Assisted in building a predictive model using Python and scikit-learn.
        - Gained experience working with real datasets and presenting insights to mentors.
        """)

    with st.expander("💻 Freelancer | Data Projects on GitHub"):
        st.write("""
        - Created data-driven projects such as a Crime Rate Predictor and FIRInsight app.
        - Designed and deployed interactive web apps using Streamlit.
        - Maintained clean, readable code and documentation for public use.
        """)
    st.markdown("</div>", unsafe_allow_html=True)

# Certifications Section
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📜 Certifications")

    with st.expander("✔️ Business Analysis Fundamentals - Microsoft"):
        with open("ba_certificate.pdf", "rb") as f:
            st.download_button("📄 Download Certificate", f, file_name="Business_Analysis_Certificate.pdf")

    with st.expander("✔️ Financial Accounting - SWAYAM (IIMB)"):
        with open("accounting_certificate.pdf", "rb") as f:
            st.download_button("📄 Download Certificate", f, file_name="Accounting_Certificate.pdf")

    with st.expander("✔️ Python for Data Science - IITM (NPTEL)"):
        with open("python_certificate.pdf", "rb") as f:
            st.download_button("📄 Download Certificate", f, file_name="Python_Certificate.pdf")
    st.markdown("</div>", unsafe_allow_html=True)

# Skills Section
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🛠️ Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.write("✅ Python")
        st.progress(30)
        st.write("📊 SQL")
        st.progress(20)
        st.write("🧮 Statistics")
        st.progress(75)

    with col2:
        st.write("🤖 Machine Learning")
        st.progress(10)
        st.write("📈 Power BI")
        st.progress(5)
        st.write("🌐 Streamlit")
        st.progress(5)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📞 Contact Me")

    st.markdown("""
    Feel free to connect with any of the platforms below:

    📧 **Email**: [sarojsantosh5@gmail.com](mailto:sarojsantosh5@gmail.com)  
    📱 **Phone**: +91 889-855-2361 
    """)

    with open("Santosh_Saroj_Resume.pdf", "rb") as resume_file:
        st.download_button(
            label="📄 Download Resume",
            data=resume_file,
            file_name="Santosh_Saroj_Resume.pdf",
            mime="application/pdf"
        )
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>Follow me on <a href="https://www.linkedin.com/in/iamssaroj/" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/iamssaroj" target="_blank">GitHub</a></p>
        <hr>
        <p>© 2025 Santosh Anjali Hariram Saroj • Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
