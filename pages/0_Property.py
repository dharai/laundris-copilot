# Laundris Property Analytics

from typing import Any
import numpy as np
import plost

from urllib.error import URLError

import altair as alt
import pandas as pd

import inspect
import textwrap

import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Property `Dashboard`')

# Row A
st.markdown('# Laundris Value Add')
col1, col2, col3 = st.columns(3)
col1.metric("Labor Cost Saved", "$14K YTD", "3K MTD")
col2.metric("Reduced Linen Loss", "12% YTD", "3% MTD")
col3.metric("Reduced Linen Cost", "24% YTD", "7% MTD")

# Row B
st.markdown('# ')
st.markdown('### Inventory optimization')
st.markdown('# ')
st.markdown('### Rag out predictions')
st.markdown('# ')
st.markdown('### Reorder predictions')
st.markdown('# ')
