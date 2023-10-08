import streamlit as st
st.set_page_config(page_title="Code Mentor", page_icon="🌀", layout="wide")
from typing import Any, Dict
from PIL import Image

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
    uploaded_code_file = st.sidebar.file_uploader("Upload the respective code file :page_facing_up:", type=["text", "xlsx", "csv","pdf",".py",".sql"])
    
    

    
    
except Exception as e:
    st.error(e) 