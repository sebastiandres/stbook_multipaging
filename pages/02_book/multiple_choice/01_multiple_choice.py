import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Multiple Choice Question")
st.header("Question with custom behavior")

stb.multiple_choice("I typically ask recruiters to point out which of these are pokemons",
                    {"ditto":True,
                        "jupyter":False,
                        "pyspark":False,
                        "scikit":False,
                        "metapod":True,
                        "vulpix":True},
                    success='Indeed!', 
                    error="Gotta catch them all!", 
                    button='Check MY answer'
                    )