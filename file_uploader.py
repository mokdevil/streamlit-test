import streamlit as st
import pandas as pd
from PIL import Image

st.title("File uploader test")
st.write("Choose a .py, .jpeg or a .txt file")

uploaded_file = st.file_uploader("Choose a file", type=["py", "jpeg", "txt", "csv"])

def read_python():
    with uploaded_file as f:
            code_string = read_file(f)
            start_index = code_string.find('st.set_page_config(')
            end_index = code_string.find(')', start_index)
            new_code_string = code_string[:start_index] + code_string[end_index+1:]
            if st.checkbox("Show source code", False):
                st.code(code_string, language=("python"))
            if st.checkbox("Run python script", False):
                exec(new_code_string)

def read_text():
    with uploaded_file as f:
            op = st.selectbox(
                'Select how to display text',
                ("Text", "Code", "Write"))
            if op == "Text":
                st.text(read_file(f))
            elif op == "Code":
                st.code(read_file(f))
            elif op == "Write":
                st.write(read_file(f))

def read_image():
    Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

def read_csv():
    data = pd.read_csv(uploaded_file)
    st.dataframe(data)

def read_file(file):
    return file.read().decode("utf-8")

if uploaded_file is not None:
    filename = uploaded_file.name

    if filename.endswith(".py"):
        read_python()
    elif filename.endswith(".txt"):
        read_text()
    elif filename.endswith(".jpeg"):
        read_image()
    elif filename.endswith(".csv"):
        read_csv()
