import streamlit as st
import streamlit_book as stb
import time
import random

st.title("To Do List")
st.header("Question with all optional arguments")

stb.to_do_list( 
            tasks={"a":True, "B":False, "c":False}, # mandatory
            header="Description", # optional argument
            success="Pelota increíble - Incredibol - Incrediball - Incredible!" # optional argument
            )