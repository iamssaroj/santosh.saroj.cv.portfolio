import streamlit as st

# Set custom background color for the whole page
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue background */
    }
    </style>
""", unsafe_allow_html=True)

# Title and Image Section
st.markdown("""
    <div style="background-color: #b0e0e6; padding: 20px;">
        <h1 style="text-align:center; color: #2f4f4f;">SANTOSH HARIRAM SAROJ</h1>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("image.jpg", caption="Santosh Hariram Saroj", width=150)
with col2:
    st.write("""
    Aspiring data analyst with a background in finance and mathematics. 
    Currently pursuing a Master’s in Management Studies (Finance) and certified 
    in business analysis and financial accounting.
    """)

# Projects Section with Background Color
st.markdown("""
    <div style="background-color: #ffebcd; padding: 20px;">
        <h2 style="color: #2f4f4f;">📂 Projects</h2>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("1️⃣ Customer Churn Prediction")
    st.write("🔍 Predicts which customers are likely to leave using logistic regression and decision trees.")
with col2:
    st.subheader("2️⃣ Stock Price Prediction")
    st.write("📈 Predicts stock prices using historical data and time series forecasting.")

# Certifications Section with Color
st.markdown("""
    <div style="background-color: #f0f8ff; padding: 20px;">
        <h2 style="color: #2f4f4f;">📜 Certifications</h2>
    </div>
""", unsafe_allow_html=True)

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

# Skills Section with Color
st.markdown("""
    <div style="background-color: #ffebcd; padding: 20px;">
        <h2 style="color: #2f4f4f;">🛠️ Skills</h2>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.write("- ✅ Python")
    st.write("- 📊 SQL")
    st.write("- 🧮 Statistics")

with col2:
    st.write("- 🤖 Machine Learning")
    st.write("- 📈 Power BI")
    st.write("- 🌐 Streamlit")

# Contact Section with Emojis and Color
st.markdown("""
    <div style="background-color: #b0e0e6; padding: 20px;">
        <h2 style="color: #2f4f4f;">📬 Contact Me</h2>
    </div>
""", unsafe_allow_html=True)

st.write("""
📧 Email: sarojsantosh5@gmail.com  
📱 Phone: +91 889-855-2361  
💻 GitHub: [github.com/iamssaroj](https://github.com/iamssaroj)
""")
