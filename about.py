import streamlit as st

st.set_page_config(page_title="About - KellCare Nursing Home", layout="wide")

st.markdown(
    """
    <h1 style='color: #1976d2; text-align: center;'>About KellCare Nursing Home</h1>
    <h3 style='color: #444; text-align: center;'>Compassionate Care, Exceptional Service</h3>
""",
    unsafe_allow_html=True,
)

st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80", use_column_width=True)

st.write("""
KellCare Nursing Home is dedicated to providing a safe, comfortable, and nurturing environment for seniors. Our mission is to ensure every resident receives personalized care tailored to their unique needs, while fostering a sense of community and belonging.

**Our Services:**
- 24/7 skilled nursing care
- Rehabilitation and therapy programs
- Nutritious meals and dietary support
- Recreational and social activities
- Housekeeping and laundry services
- Pet-friendly environment

**Why Choose KellCare?**
- Highly trained and compassionate staff
- Modern, clean, and secure facilities
- Focus on dignity, respect, and independence
- Strong family and community involvement

**Contact Us:**
- 📍 123 Main Street, Asheville, NC
- ☎️ (828) 555-1234
- ✉️ info@kellcare.com

We invite you to visit our facility and experience the KellCare difference!
""")
