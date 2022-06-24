import streamlit as st
import streamlit_book as stb

show_code = st.checkbox("Show code", False, key="single_page")
with stb.echo("above", show_code):
    import streamlit as st
    import streamlit_book as stb
    import numpy as np
    import pandas as pd

    st.title("Single Page")

    st.subheader("Maybe some data")
    N = 10
    df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
    st.dataframe(df)  # Same as st.write(df)

    st.subheader("Maybe some plots")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

    # Feedback
    stb.floating_button("https://sebastiandres.xyz")
