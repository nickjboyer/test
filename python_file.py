
#### this is the line that works to run streamlit
#py -m streamlit run python_file.py

import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.info("this is some test text")


with col2:
    st.title("Nick Boyer")
    content = """
        I'm so cool
            """
    
    st.info(content)


content2 = """
    add some sort of footer
"""
st.write(content2)


