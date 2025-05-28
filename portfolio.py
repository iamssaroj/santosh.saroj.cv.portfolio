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
        .project-card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
            margin-bottom: 25px;
        }
        .project-title {
            font-size: 22px;
            font-weight: 600;
            color: #333333;
        }
        .project-tech {
            font-size: 14px;
            color: #555;
            margin-bottom: 10px;
        }
        .project-links a {
            margin-right: 15px;
            text-decoration: none;
            color: #0366d6;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header
st.header("📂 Projects")

# --- Project 1: Crime Rate Predictor
with st.container():
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'>🔍 Crime Rate Predictor</div>
        <p>This project develops a <strong>Logistic Regression</strong> model to predict crime risk levels in Indian states based on socio-economic indicators such as:</p>
        <ul>
            <li>Population Density</li>
            <li>Per Capita Income</li>
            <li>Literacy Rate</li>
            <li>Unemployment Rate</li>
            <li>Drug Addiction Rate</li>
        </ul>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Official data sources (PIB, RBI, MoSPI)</li>
            <li>Feature selection via correlation analysis</li>
            <li>Visualization and evaluation of results</li>
            <li>Interactive user input panel</li>
        </ul>
        <p class='project-tech'><strong>Technologies:</strong> Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit</p>
        <div class='project-links'>
            <a href='https://github.com/iamssaroj/crime-rate-predictor' target='_blank'>📂 GitHub</a>
            <a href='https://crime-rate-predictor-vfw37ir4xbmccjikfcmooi.streamlit.app/' target='_blank'>▶️ Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Project 2: Fire Risk Detection
with st.container():
    st.markdown("""
    <div class='project-card'>
        <div class='project-title'>🔥 Fire Risk Detection in Mumbai Suburbs</div>
        <p>This project uses a <strong>Logistic Regression</strong> model to predict potential fire incidents in Mumbai suburbs based on multiple factors like:</p>
        <ul>
            <li>Historical fire data</li>
            <li>Weather conditions</li>
            <li>Population density</li>
            <li>Proximity to industrial zones</li>
        </ul>
        <p><strong>Key Features:</strong></p>
        <ul>
            <li>Geospatial and public data integration</li>
            <li>Binary classification of risk zones</li>
            <li>Interactive map visualizations</li>
            <li>Streamlit dashboard with real-time prediction</li>
        </ul>
        <p class='project-tech'><strong>Technologies:</strong> Python, Pandas, Scikit-learn, Plotly, Folium, Streamlit</p>
        <div class='project-links'>
            <a href='https://github.com/iamssaroj/fire-risk-detector' target='_blank'>📂 GitHub</a>
            <a href='https://fire-risk-mumbai.streamlit.app/' target='_blank'>▶️ Live Demo</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


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
    Feel free to connect with me through any of the platforms below:

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
