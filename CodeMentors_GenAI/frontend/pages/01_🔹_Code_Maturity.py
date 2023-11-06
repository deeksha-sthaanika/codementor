import streamlit as st
# st.set_page_config(
#     page_title="Code Mentor - Code Maturity", page_icon="🔹", layout="wide"
# )
import Home as hm
import requests
from fastapi import FastAPI, File, UploadFile
import os
import io
from utilities import Utility as fn




st.markdown("<h1 style='text-align: center; color: black;padding: 1% 1% 1% 1%;background-color: #a2d5f2;'>Code Maturity</h1>", unsafe_allow_html=True)
style="""
.css-184tjsw p{
font-weight:bold
}
.js-plotly-plot .plotly, .js-plotly-plot .plotly div {
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
# div.stButton > button:first-child{
#  background-color:#28B1F5;
#    color:white;   
# }
st.markdown(f"<style>{style}</style>",unsafe_allow_html=True)
footer="""<style>.footer {
position: fixed;
left: 50;
bottom: 0;
width: 100%;
background-color: white;
color: grey;
text-align: left;
}
</style><div class="footer"><p>CodeMentor</p></div>"""
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

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(219,226,233,0.8);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 10% 10% 10% 10%;
   border-radius: 25px;
   color: rgb(30, 103, 119);
   width: 180px;
   height: 110px;
   overflow-wrap: break-word;
}
/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: rgba(35,86,131);
   font-size: 16px;
   font-weight:bold
}
div[data-testid="metric-container"] > div[data-testid="stMetricValue"] > div {
   font-size: 19px;
   color:rgba(28, 34, 80)
}
</style>
"""
, unsafe_allow_html=True)
style_table="""
thead tr th:first-child {display:none;}
tbody th {display:none;}
thead{
background-color:#336699;
font-size: 19px;
font-weight:bold
}
tbody{
font-size: 19px;
font-weight:bold;
background-color:AliceBlue
}
.css-81oif8{
font-size: 19px;
font-weight:bold
}
.css-a51556{
    color:white
}
"""
st.markdown(f"<style>{style_table}</style>",unsafe_allow_html=True)

# Streamlit interface
def main():

    try:
        selected_lang=st.session_state.code_lang
        selected_doc_type=st.session_state.doc_type
        if st.session_state.file_std and st.session_state.file_code:
            col3,col4 = st.columns(2)

            with col3:
                with st.expander(f"🔎 View standard file content ({selected_doc_type})"):
                    file_std1=io.BytesIO(st.session_state.file_std.read())
                    if selected_doc_type=='text':
                        contents_std=st.session_state.file_std.getvalue()
                    elif selected_doc_type=='pdf':
                        contents_std=fn.readPdf(file_std1)
                    elif selected_doc_type=='docx':
                        contents_std=fn.readDoc(file_std1)
                    elif selected_doc_type=='csv':
                        contents_std=fn.readCsv(file_std1)
                    elif selected_doc_type=='excel':
                        contents_std=fn.readExcel(file_std1)
                    st.code(contents_std)

            with col4:
                with st.expander(f"🔎 View {selected_lang} code file content"):
                    st.code(st.session_state.file_code.getvalue(),selected_lang)


            files = {
                    'file_std': st.session_state.file_std,
                    'file_code': st.session_state.file_code
                    }

            data = {'lang':selected_lang ,'type':selected_doc_type}

            if st.button("Format Code as per Standards"):
                response = requests.post("http://127.0.0.1:8000/Format_Code/", files=files,data=data)
                # st.write(response.content)
                if response.status_code==200:
                    try:
                        with st.expander(f"🔎 View {selected_lang} file content as per standards"):
                            content=response.json()
                            st.code(content["result"]["completition"],selected_lang)
                            st.download_button(
                                label="Download Code",
                                data=content["result"]["completition"],
                                file_name='Formatted_Code_'+st.session_state.file_code.name,
                                mime='text/csv',
                            )
                    except:
                        content=response.json()
                        st.error(str(content["result"]["response_code"])+': '+content["result"]["message"]["_message"])
                else:
                    st.error("Couldn't fetch the result. Please try again")

        else:
            st.info('👈 Please Upload files in home page to continue')
       
    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    main()
