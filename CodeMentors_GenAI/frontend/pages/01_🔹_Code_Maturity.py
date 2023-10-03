import streamlit as st
import Home
st.set_page_config(
    page_title="Code Mentor - Code Maturity", page_icon="🔹", layout="wide"
)


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

def main():
    try:
        
        col1, col2, col3,col4 = st.columns(4)

        with col1:
            if add_languagebox != '':
                st.write(f'👋 Hello {add_languagebox}!')
            else:
                st.write('👈  Please choose  **add_languagebox**!')

        with col2:
            if add_documnetextebox != '':
                st.write(f'{add_documnetextebox} is your favorite **emoji**!')
            else:
                st.write('👈 Please choose an **add_documnetextebox**!')

        with col3:
            if uploaded_standard_file != '':
                st.write(f'🍴 **{uploaded_standard_file}** is your favorite **uploaded_standard_file**!')
            else:
                st.write('👈 Please choose  **uploaded_standard_file**!')

        with col4:
            if uploaded_code_file != '':
                st.write(f'🍴 **{uploaded_code_file}** is your favorite **uploaded_code_file**!')
            else:
                st.write('👈 Please choose  **uploaded_code_file**!')
         files = {"file": image.getvalue()} #file details
        res = requests.post(f"http://localhost:8080/{codematurity}", files=files)
        img_path = res.json()
        image = Image.open(img_path.get("name"))
        st.image(image)        
        st.write("Generating code maturity...")
         
    except AttributeError:
        st.warning("Please login to access this page")


if __name__ == "__main__":
    main()
