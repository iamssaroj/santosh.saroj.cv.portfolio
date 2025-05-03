
import streamlit as st

st.title("SANTOSH HARIRAM SAROJ")

st.image("image.jpg", caption="Santosh Hariram Saroj", width=150)

st.header("About Me")
st.write(""" Aspiring data analyst with a background in finance and mathematics. Currently pursuing a Master’s in Management Studies (Finance) and certified in business analysis and financial accounting. 
Experienced in teaching mathematics with strong analytical and problem-solving skills. Looking to apply data skills to support business insights and decision-making.""")

st.header("Projects")
st.subheader("1. Customer Churn Prediction")
st.write("Predicts which customers are likely to leave.")


st.header("Certifications")

st.write("📌 Business Analysis Fundamentals By Microsoft")
try:
    with open("ba_certificate.pdf", "rb") as file:
        st.download_button(label="📄 Download Certificate", data=file, file_name="Business_Analysis_Certificate.pdf", mime="application/pdf")
except FileNotFoundError:
    st.error("❌ Certificate file 'ba_certificate.pdf' not found!")

st.write("📌 Financial Accounting and Analysis by SWAYAM (IIMB)")
try:
    with open("accounting_certificate.pdf", "rb") as file:
        st.download_button(label="📄 Download Certificate", data=file, file_name="Accounting_Certificate.pdf", mime="application/pdf")
except FileNotFoundError:
    st.error("❌ Certificate file 'accounting_certificate.pdf' not found!")

st.write("📌 Python for Data Science by IITM (NPTEL)")
try:
    with open("python_certificate.pdf", "rb") as file:
        st.download_button(label="📄 Download Certificate", data=file, file_name="Python_Certificate.pdf", mime="application/pdf")
except FileNotFoundError:
    st.error("❌ Certificate file 'python_certificate.pdf' not found!")


st.header("Skills")
st.write("""
- ✅ Python
- 📊 SQL
- 🤖 Machine Learning
- 📈 Power BI
- 🌐 Streamlit
""")

st.header("Contact Me")
st.write("Email: sarojsantosh5@gmail.com | phone: +91 889-855-2361 | GitHub: github.com/iamssaroj")
