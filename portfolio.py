import streamlit as st

# Title and Image - About Me Section
col1, col2 = st.columns([1, 3])
with col1:
    st.image("image.jpg", caption="Santosh Hariram Saroj", width=150)
with col2:
    st.title("SANTOSH HARIRAM SAROJ")
    st.write("""
    Aspiring data analyst with a background in finance and mathematics. 
    Currently pursuing a Master’s in Management Studies (Finance) and certified 
    in business analysis and financial accounting.

    Experienced in teaching mathematics with strong analytical and problem-solving skills. 
    Looking to apply data skills to support business insights and decision-making.
    """)

# Projects Section with Card Style
st.header("📂 Projects")
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Customer Churn Prediction")
    st.write("🔍 Predicts which customers are likely to leave using logistic regression and decision trees.")
    
with col2:
    st.subheader("2️⃣ Stock Price Prediction")
    st.write("📈 Predicts stock prices using historical data and time series forecasting.")

# Certifications Section in Columns
st.header("📜 Certifications")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("✔️ Business Analysis Fundamentals by Microsoft")
    with open("ba_certificate.pdf", "rb") as f:
        st.download_button("📄 Download Certificate", f, file_name="Business_Analysis_Certificate.pdf")

with col2:
    st.write("✔️ Financial Accounting by SWAYAM (IIMB)")
    with open("accounting_certificate.pdf", "rb") as f:
        st.download_button("📄 Download Certificate", f, file_name="Accounting_Certificate.pdf")

with col3:
    st.write("✔️ Python for Data Science by IITM (NPTEL)")
    with open("python_certificate.pdf", "rb") as f:
        st.download_button("📄 Download Certificate", f, file_name="Python_Certificate.pdf")

# Skills Section in Bullet Grid
st.header("🛠️ Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("- ✅ Python")
    st.write("- 📊 SQL")
    st.write("- 🧮 Statistics")

with col2:
    st.write("- 🤖 Machine Learning")
    st.write("- 📈 Power BI")
    st.write("- 🌐 Streamlit")

# Contact Section with Emojis
st.markdown("""
**📧 Email**: [sarojsantosh5@gmail.com](mailto:sarojsantosh5@gmail.com)  
**📱 Phone**: +91 889-855-2361  
**💻 GitHub**: [github.com/iamssaroj](https://github.com/iamssaroj)  
**🌍 LinkedIn**: [linkedin.com/in/iamssaroj](https://www.linkedin.com/in/iamssaroj/)
""")

