import streamlit as st
from io import StringIO

st.title("File execute test")
st.write("Choose python file to display")

uploaded_file = st.file_uploader("Choose a file", type=["py"])

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.code(string_data, language="python")
    exec(string_data)