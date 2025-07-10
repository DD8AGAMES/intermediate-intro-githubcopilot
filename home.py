
import streamlit as st

# Set a vibrant background using custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        min-height: 100vh;
        overflow-x: hidden;
    }
    .stApp {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        min-height: 100vh;
        position: relative;
    }
    /* Decorative circles */
    .decor-circle {
        position: fixed;
        border-radius: 50%;
        opacity: 0.25;
        z-index: 0;
        filter: blur(2px);
    }
    #circle1 {
        width: 220px; height: 220px;
        background: #f7797d;
        top: -60px; left: -60px;
    }
    #circle2 {
        width: 160px; height: 160px;
        background: #f6d365;
        bottom: 40px; right: 40px;
    }
    #circle3 {
        width: 120px; height: 120px;
        background: #a1c4fd;
        top: 60px; right: -40px;
    }
    #circle4 {
        width: 90px; height: 90px;
        background: #c2e9fb;
        bottom: 120px; left: 30px;
    }
    .stTextInput > div > div > input {
        background: #222831;
        color: #fff;
        border: 2px solid #fda085;
        border-radius: 8px;
        font-size: 1.05em;
    }
    .stTextInput > div > div > input::placeholder {
        color: #bdbdbd;
        opacity: 1;
    }
    .stButton > button {
        background: #f7797d;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        transition: background 0.2s;
    }
    .stButton > button:hover {
        background: #f6d365;
        color: #222;
    }
    </style>
    <div id=\"circle1\" class=\"decor-circle\"></div>
    <div id=\"circle2\" class=\"decor-circle\"></div>
    <div id=\"circle3\" class=\"decor-circle\"></div>
    <div id=\"circle4\" class=\"decor-circle\"></div>
    """,
    unsafe_allow_html=True
)

st.title("Tutor Signup Form")

# Use a single column with a custom label style for better alignment
st.markdown(
    """
    <style>
    .form-label {
        display: block;
        font-weight: bold;
        font-size: 1.1em;
        margin-bottom: 4px;
        margin-top: 18px;
        color: #222831;
        letter-spacing: 0.5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

first_name = st.text_input(label="First Name", key="first_name", label_visibility="visible")
background = st.text_input(label="Background", key="background", label_visibility="visible")
courses = st.text_input(label="List of courses", key="courses", label_visibility="visible")
email = st.text_input(label="Email address", key="email", label_visibility="visible")
last_name = st.text_input(label="Last Name", key="last_name", label_visibility="visible")

if st.button("Sign Up"):
    st.success(f"Thank you for signing up, {first_name}!")