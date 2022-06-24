import streamlit as st
import streamlit_book as stb
import time
import random

st.title("To Do List")
st.header("Question with custom behavior")

all_task_completed = stb.to_do_list(
                                    tasks={"A":True, "B":False, "C":False}, # mandatory
                                    header="", # optional argument
                                    success="" # optional argument
                                    )
if all_task_completed:
    st.info("Bravo!")            
else:
    st.info("Yes, you can!")            
