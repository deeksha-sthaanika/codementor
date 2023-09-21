import time
import requests
import streamlit as st

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
    ":one: Please select the language?",
    ("SQL", "Python")
)

# add document extension box
add_documnetextebox = st.sidebar.selectbox(
    ":two: Please select the coding standard document type?",
    ("text", "excel","pdf","none")
)

# Add a file uploader widget
uploaded_standard_file = st.sidebar.file_uploader(":three: Upload the coding standard document :+1:", type=["text", "xlsx", "csv","pdf"])

# Add a file uploader widget
uploaded_code_file = st.sidebar.file_uploader(":four: Upload the respective code file :page_facing_up:", type=["text", "xlsx", "csv","pdf"])

#Add the respective buttons
col1, col2, col3 = st.columns(3)

with col1:
    button1 = st.button('Code Assessment')

with col2:
    button2 = st.button('Reviewed Code')

with col3:
    button3 = st.button('Code Optimization')

if button1:
     st.write("Button1 clicked!")
     content = ('''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
     st.text_area(content)
        
if button2:
     st.write("Button2 clicked!")
        
if button3:
     st.write("Button3 clicked!")


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
