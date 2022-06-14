import streamlit as st
import streamlit_book as stb

def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_icon="📚", page_title="stb multipaging demo")

       # Comments
       st.markdown("This is the streamlit_app.py file.")
       st.markdown("Here you configure the app and some properties.")
       st.markdown("Use the sidebar to navigate to the different types of pages.")      

if __name__ == "__main__":
       main()