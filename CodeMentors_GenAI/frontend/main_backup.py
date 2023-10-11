import time
import requests
import streamlit as st
from PIL import Image

st.set_option("deprecation.showfileUploaderEncoding", False)

# Heading for the Sidebar
# Add a styled heading to the sidebar
st.sidebar.markdown(
    """
    <style>
    .sidebar-title {
        font-size: 30px;
        color: #FF5733; /* You can set your desired text color */
        text-transform: uppercase;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.write('<p class="sidebar-title">CODE MENTOR</p>', unsafe_allow_html=True)


# add language box
add_languagebox = st.sidebar.selectbox(
    "Please select the language?",
    ("SQL", "Python")
)

# add document extension box
add_documnetextebox = st.sidebar.selectbox(
    "Please select the coding standard document type?",
    ("text", "excel","pdf","none")
)

#Check the value of documentbox and show the file uploader accordingly
if add_documnetextebox in "none":
    st.session_state.disabled = True
    uploaded_standard_file = st.sidebar.file_uploader("Upload the coding standard document", type=["text", "xlsx", "csv","pdf"],
                                                     disabled=st.session_state.disabled)
else:
    uploaded_standard_file = st.sidebar.file_uploader("Upload the coding standard document", type=["text", "xlsx", "csv","pdf"])
    
# Add a Code file uploader widget
uploaded_code_file = st.sidebar.file_uploader("Upload the respective code file :page_facing_up:", type=["text", "xlsx", "csv","pdf"])


# Add an Image
#image = Image.open('C:\\Users\\azmatul.azam\\Documents\\codementor.jpg')

image = Image.open('.//codementor.jpg')
st.image(image)

m = st.markdown("""
<style>
div.stButton > button:click {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

#Add the respective buttons
col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button("Code Assessment")

with col2:
    button2 = st.button('Reviewed Code')

with col3:
    button3 = st.button('Code Optimization')

if button1:
     st.markdown(''':rainbow[Button1 clicked!]''')
     content = ('''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
     st.text_area(content)
        
if button2:
     st.markdown(''':rainbow[Button2 clicked!]''')
     st.balloons()
        
if button3:
     st.markdown(''':rainbow[Button3 clicked!]''')
     st.balloons()


if st.button("codematurity"):   
        files = {"file": image.getvalue()} #file details
        res = requests.post(f"http://localhost:8080/{codematurity}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image)        
        st.write("Generating code maturity...")
elif st.button("correctcodegeneration"):   
        files = {"file": image.getvalue()} #file details
        res = requests.post(f"http://localhost:8080/{correctcodegeneration}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image)        
        st.write("Generating Corrected generation details...")
elif st.button("optimizedcode"):   
        files = {"file": image.getvalue()} #file details
        res = requests.post(f"http://localhost:8080/{optimizecode}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image)        
        st.write("Generating optimized code...")
