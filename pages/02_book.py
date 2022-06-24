import streamlit as st
import streamlit_book as stb
from pathlib import Path

# Streamit book properties
show_code = st.checkbox("Show code", False, key="book")
with stb.echo("above", show_code):
       stb.set_book_config(
                            menu_title="Book Configuration",
                            menu_icon="lightbulb",
                            options=[
                                   "Intro",
                                   "True/False Question",
                                   "Single Choice Question",
                                   "Multiple Choice Question",
                                   "To Do List",
                                   ], 
                            paths=[
                                   "pages/02_book/intro", 
                                   "pages/02_book/true_or_false", 
                                   "pages/02_book/single_choice",
                                   "pages/02_book/multiple_choice",
                                   "pages/02_book/to_do_list", 
                                   ],
                            icons=[
                                   "",
                                   "paint-bucket",
                                   "signpost-2",
                                   "ui-radios",
                                   "ui-checks",
                                   ],
                            )