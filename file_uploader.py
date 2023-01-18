import streamlit as st
from io import StringIO
from PIL import Image

st.title("File uploader test")
st.write("Choose a .py, .jpg or a .txt file")

uploaded_file = st.file_uploader("Choose a file", type=["py", "jpg", "txt"])
    
if uploaded_file is not None:
    
    filename = uploaded_file.name

    pythonscript = (filename.find(".py"))
    textfile = (filename.find(".txt"))
    jpgfile = (filename.find(".jpg"))
    h = 0

    if h <= pythonscript:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.code(string_data, language=("python"))
        run_file_button = st.checkbox("Run python script")
        if run_file_button is True:
            new_string_data = string_data.replace("st.set_page_config", "#")
            exec(new_string_data)
    elif h <= textfile:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)
    elif h <= jpgfile:
        image = Image.open(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)