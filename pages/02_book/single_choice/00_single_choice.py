import streamlit as st
import streamlit_book as stb

st.title("Single Choice Question")
st.header("Question with minimal arguments")

stb.single_choice("What does pandas (the library) stands for?",
                    ["The cutest bear", "Panel Data", 
                    "Pure Adamantium Numeric Datasets And Stuff", "PArties & DAtaSets"],
                    1)