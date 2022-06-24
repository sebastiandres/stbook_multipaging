import streamlit as st
import streamlit_book as stb

def main():
    # Streamlit webpage properties
    st.set_page_config(layout="wide", page_icon="📚", page_title="stb multipaging demo")

    st.title("Streamlit Book - Multipaging Demo")

    # Comments
    st.markdown("""This is a streamlit app that shows different multipaging options. The native multipaging provided by streamlit is [well documented](https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app).
TLDR; just put your pages in `pages/` folder.""")   
    st.markdown("""
* On `single page` a single page is displayed.
* On `chapter`, a multi-page with arrows for navigation is displayed.
* On `book`, a book with sidebar menu with full navigation options. 
""")

    # Feedback
    stb.floating_button("https://sebastiandres.xyz")

if __name__ == "__main__":
       main()