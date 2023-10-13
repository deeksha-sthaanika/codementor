import streamlit as st
st.set_page_config(page_title="Code Mentor", page_icon="🌀", layout="wide")
from typing import Any, Dict
from PIL import Image
import os
import requests
from fastapi import FastAPI, File, UploadFile

image = Image.open('.//codementor.jpg')
st.image(image)

st.markdown("<h1 style='text-align: center;color: #098BCB;'>Welcome to Code mentor", unsafe_allow_html=True)
style="""
.css-184tjsw p{
font-weight:bold
}
.css-163ttbj
{
    background-color:#cae7f7
}
.css-1hverof:hover,
{
   background-color:#FED8B1 
}
/*logout */
.css-zrs5io
{
   background-color:#F06055;
   color:white; 
}
.css-l6i7ys
{
  background-color:#1a98d7;
   color:white;  
}
.css-1053j7q:focus:(:active) {
  background-color:#5EC5F7;
   color:white;

"""

st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
footer="""<style>.footer {
position: fixed;
left: 50;
bottom: 0;
width: 20%;
background-color: white;
color: grey;
text-align: left;
}
</style><div class="footer"><p>Code Mentor</p></div>"""
st.markdown(footer,unsafe_allow_html=True)
st.markdown("""
<style>div.stButton > button:hover {
    background-color: #28B1F5;
    color:white;
    }
div.stButton > button:focus {
    background-color:#E0FFFF;
    color:white;
    }
div.stButton > button:active {
    background-color: #E0FFFF;
    color:white;
    }
</style>""", unsafe_allow_html=True)


try:
    
    st.sidebar.info("Choose a page!")
    st.markdown(
        """
    This app provides insights on a demo Code Best Practices.

    ### Get started!

    👈 Provide the details and then Select a page in the sidebar!
        """
    )

    st.sidebar.write('<p class="sidebar-title">CODE MENTOR</p>', unsafe_allow_html=True)


    # add language box
    if 'code_lang' not in st.session_state:
        add_languagebox = st.sidebar.selectbox("Please select the language?",("SQL", "Python"),key='lang_box1')
    else:
        add_languagebox = st.sidebar.selectbox("Please select the language?",("SQL", "Python"),key='lang_box2')
    st.session_state.code_lang=add_languagebox

    # add document extension box
    if 'doc_type' not in st.session_state:
        add_documnetextebox = st.sidebar.selectbox("Please select the coding standard document type?",("text", "excel","pdf","csv","docx"),key='doc_box1')
    else:
        add_documnetextebox = st.sidebar.selectbox("Please select the coding standard document type?",("text", "excel","pdf","csv","docx"),key='doc_box2')
    st.session_state.doc_type=add_documnetextebox
        
    # Add a Code standard file uploader widget
    if 'file_std' not in st.session_state:
        uploaded_file = st.sidebar.file_uploader("Upload the coding standard document",key='file_std_key')   
    else:
        uploaded_file = st.sidebar.file_uploader("Upload the coding standard document",key='file_std_key')
    st.session_state.file_std=uploaded_file

    # Add a Code file uploader widget
    if 'file_code' not in st.session_state:
        uploaded_file = st.sidebar.file_uploader("Upload the respective code file :page_facing_up:",key='file_code_key')   
    else:
        uploaded_file = st.sidebar.file_uploader("Upload the respective code file :page_facing_up:",key='file_code_key')
    st.session_state.file_code=uploaded_file
  
    
except Exception as e:
    st.error(e) 