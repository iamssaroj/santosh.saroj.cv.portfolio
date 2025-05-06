import streamlit as st

# Custom CSS for button hover and footer
st.markdown("""
    <style>
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
            margin-top: 50px;
            font-size: 14px;
            color: gray;
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

# Title and Image - About Me Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("image.jpg", caption="Santosh", width=150)
with col2:
    st.markdown("""
        <h1 style='white-space: nowrap; margin-bottom: 10px;'>SANTOSH ANJALI HARIRAM SAROJ</h1>
    """, unsafe_allow_html=True)
    st.write("""
    Aspiring data analyst with a background in finance and mathematics. 
    Currently pursuing a Master’s in Management Studies (Finance) and certified 
    in business analysis and financial accounting.

    Experienced in teaching mathematics with strong analytical and problem-solving skills. 
    Looking to apply data skills to support business insights and decision-making.
    """)

# Projects Section with Tabs
st.header("📂 Projects")
tab1, tab2 = st.tabs(["Customer Churn Prediction", "Stock Price Prediction"])

with tab1:
    st.subheader("1️⃣ Customer Churn Prediction")
    st.write("🔍 Predicts which customers are likely to leave using logistic regression and decision trees.")

with tab2:
    st.subheader("2️⃣ Stock Price Prediction")
    st.write("📈 Predicts stock prices using historical data and time series forecasting.")

# Certifications Section with Expanders
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

# Skills Section with Progress Bars
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

# Contact Section
st.header("📞 Contact Me")

st.markdown("""
Feel free to connect with me through any of the platforms below:

📧 **Email**: [sarojsantosh5@gmail.com](mailto:sarojsantosh5@gmail.com)  
📱 **Phone**: +91 889-855-2361  
💼 **LinkedIn**: [linkedin.com/in/iamssaroj](https://www.linkedin.com/in/iamssaroj/)  
💻 **GitHub**: [github.com/iamssaroj](https://github.com/iamssaroj)  
""")

# Footer Section
st.markdown("""
    <div class="footer">
        <p>Follow me on <a href="https://www.linkedin.com/in/iamssaroj/" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/iamssaroj" target="_blank">GitHub</a></p>
        <hr>
        <p>© 2025 Santosh Anjali Hariram Saroj • Built with ❤️ using Streamlit</p>
    </div>
""", unsafe_allow_html=True)
