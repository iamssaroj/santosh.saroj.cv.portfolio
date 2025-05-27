import streamlit as st

# Page configuration
st.set_page_config(page_title="Santosh Saroj | Portfolio", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        /* Set light background */
        .stApp {
            background-color: #f0f8ff;
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
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("📂 Project")

    st.subheader("🔍 Crime Rate Predictor")

    st.write("""
    This project develops a **Logistic Regression** model to predict future crime rate based on different states data.
    It uses socio-economic indicators like:
    - Population Density
    - Per Capita Income
    - Literacy Rate
    - Unemployment Rate
    - Drug Addiction Rate

    The goal is to predict the crime risk level to help policymakers allocate resources effectively and improve safety measures.
    """)

    st.markdown("**Key Features:**")
    st.markdown("""
    - Data sourced from official government databases (PIB, RBI, MoSPI)  
    - Feature selection based on correlation and importance  
    - Logistic regression model building and evaluation  
    - Visualization of prediction results  
    - Interactive user interface for inputting data  
    """)

    st.markdown("**Technologies Used:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit")

    # GitHub and Demo links
    st.markdown("[📂 View Code on GitHub](https://github.com/iamssaroj/crime-rate-predictor)")
    # If you have a demo link, add here:
    st.link_button("▶️ Live Demo", "https://crime-rate-predictor-vfw37ir4xbmccjikfcmooi.streamlit.app/")
 
    st.markdown("</div>", unsafe_allow_html=True)

# Court Cases Clustering Project Section
st.markdown("<div class='card'>", unsafe_allow_html=True)
with st.container():
    st.header("📂 Project")

    st.subheader("📑 Court Cases Clustering")

    st.write("""
    This project applies **Natural Language Processing (NLP)** and **Machine Learning** techniques to cluster similar court case PDFs automatically.
    
    Key functionalities include:
    - Upload multiple court case PDF documents
    - Extract and preprocess text from PDFs
    - Generate embeddings for documents using NLP models
    - Apply clustering algorithms (like K-Means or DBSCAN) to group similar cases
    - Visualize clusters and allow exploration through an interactive web app
    
    This tool helps legal professionals quickly identify related cases and research precedents efficiently.
    """)

    st.markdown("**Technologies Used:** Python, PyMuPDF, SpaCy, Scikit-learn, Sentence Transformers, Streamlit")

    # GitHub and Demo links (replace with your URLs)
    st.markdown("[📂 View Code on GitHub](https://github.com/iamssaroj/court-cases-clustering)")
    st.markdown("[▶️ Live Demo](https://court-cases-clustering-demo.streamlit.app/)")
    
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
