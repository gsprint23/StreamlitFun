import streamlit as st
import numpy as np
import pandas as pd



st.write(
    """
    # My First Streamlit Webpage

    Supports markdown :) Here is a live update
    """
)

# to run app in browser: streamlit run main_app.py
# to to settings to enable live update on save

df = pd.read_csv("data.csv")
# st.write(df)
# st.table(df) # static table, shows all and can scroll
# st.dataframe(df) # same as st.write(df) when df is passed in
# can draw charts directly into webpage

options = st.selectbox("Which option do you want", options=["show plotting", "show slider"])
if options == "show plotting":
    sample_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.write(sample_df)
    if st.checkbox("Show plotting feature"):
        st.line_chart(sample_df)
    # st.pyplot() will work as well

    # streamlit re-runs everything like python script from top to bottom every single time
    # interact with something or refresh page
    # might be a problem due to inefficieny...
    # streamlit does support caching with decorators
    cb_val = st.checkbox("my checkbox")
    st.write("checkbox state:", cb_val)
else:
    slider_val = st.slider("x")
    st.write("2 * slider value:", 2 * slider_val)

# can get text input, such as for input to ML model