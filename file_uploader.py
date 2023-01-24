import streamlit as st
from PIL import Image

st.set_page_config("File Uploader", layout=("wide"))

st.title("File uploader test")
st.write("Choose a .py, .jpg or a .txt file")

uploaded_file = st.file_uploader("Choose a file", type=["py", "jpg", "txt"])

if uploaded_file is not None:
    filename = uploaded_file.name

    if filename.endswith(".py"):
        with uploaded_file as f:
            code_string = f.read().decode("utf-8")
            if st.checkbox("Show source code", False):
                st.code(code_string, language=("python"))
            new_code_string = code_string.replace("st.set_page_config", "#")
            if st.checkbox("Run python script", False):
                exec(new_code_string)

    elif filename.endswith(".txt"):
        with uploaded_file as f:
            st.write(f.read().decode("utf-8"))

    elif filename.endswith(".jpg"):
        image = Image.open(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
