import streamlit as st
import streamlit_book as stb

st.title("True or False Question")
st.header("Question with all optional arguments")

stb.true_or_false("Are you a cyborg?", False, 
                    success='Pfiuuuuu!!!', 
                    error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                    button='Check MY answer')
