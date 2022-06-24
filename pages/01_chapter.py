import streamlit as st
import streamlit_book as stb

show_code = st.checkbox("Show code", False, key="chapter")
with stb.echo("above", show_code):
    stb.set_chapter_config(path="pages/01_chapter")

    

