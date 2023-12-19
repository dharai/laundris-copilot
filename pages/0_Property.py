# Laundris Property AI Demo


from typing import Any

import numpy as np

import streamlit as st
#from streamlit.hello.utils import show_code
import pandas as pd
import plost

from urllib.error import URLError

import altair as alt
import pandas as pd

import streamlit as st
#from streamlit.hello.utils import show_code

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Property `Dashboard`')

st.sidebar.markdown('''
---
''')


# Row A
st.markdown('### Laundris Value Add')
col1, col2, col3 = st.columns(3)
col1.metric("Labor Cost Saved", "$14K YTD", "3K MTD")
col2.metric("Reduced Linen Loss", "12% YTD", "3% MTD")
col3.metric("Reduced Linen Cost", "24% YTD", "7% MTD")

# Row B

