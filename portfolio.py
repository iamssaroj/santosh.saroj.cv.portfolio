import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background color of the main content */
        .main {
            background-color: #f4f4f4;
        }

        /* Style for headings */
        h1, h2, h3 {
            color: #0e76a8;
        }

        /* General text color and size */
        .css-10trblm, .css-1v3fvcr {
            font-size: 16px;
            color: #333333;
        }

        /* Button styling */
        .stButton>button {
            background-color: #0e76a8;
            color: white;
            border-radius: 8px;
            padding: 10px 16px;
            border: none;
        }

        /* Remove scrollbars */
        ::-webkit-scrollbar {
            display: none;
        }

        /* Make download buttons visually consistent */
        .stDownloadButton>button {
            background-color: #0e76a8;
            color: white;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

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
    st.progress(90)
    st.write("📊 SQL")
    st.progress(80)
    st.write("🧮 Statistics")
    st.progress(75)

with col2:
    st.write("🤖 Machine Learning")
    st.progress(70)
    st.write("📈 Power BI")
    st.progress(65)
    st.write("🌐 Streamlit")
    st.progress(85)

# Contact Section
st.header("📞 Contact Me")

st.markdown("""
Feel free to connect with me through any of the platforms below:

📧 **Email**: [sarojsantosh5@gmail.com](mailto:sarojsantosh5@gmail.com)  
📱 **Phone**: +91 889-855-2361  
💼 **LinkedIn**: [linkedin.com/in/iamssaroj](https://www.linkedin.com/in/iamssaroj/)  
💻 **GitHub**: [github.com/iamssaroj](https://github.com/iamssaroj)  
""")

# Optional: Contact Form
st.subheader("📬 Send Me a Message")

contact_form = """
<form action="https://formsubmit.co/sarojsantosh5@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px;"><br><br>
    <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px;"><br><br>
    <textarea name="message" placeholder="Your message" rows="5" required style="width: 100%; padding: 10px;"></textarea><br><br>
    <button type="submit" style="background-color:#0e76a8; color:white; padding:10px 20px; border:none; border-radius:6px;">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
