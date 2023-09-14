import time
import requests
import streamlit as st




st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Code Mentor")


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