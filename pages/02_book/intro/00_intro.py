import streamlit as st
import streamlit_book as stb

st.header("Book: multiple connected pages")
st.markdown("""
You need several chapters.

Use `stb.set_book_config` to set the path and other book configurations.
The pages can live anywhere you like, but I recommend to use "./docs/" or "./pages/subdir/".
""")

