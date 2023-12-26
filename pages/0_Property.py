# Laundris Property AI Demo


from typing import Any

import numpy as np

#from streamlit.hello.utils import show_code
import pandas as pd
import plost

from urllib.error import URLError

import altair as alt
import pandas as pd

import inspect
import textwrap

import streamlit as st
import json
from streamlit_echarts import st_echarts
from streamlit_echarts import JsCode

from demo_echarts import ST_DEMOS
from demo_pyecharts import ST_PY_DEMOS

#from streamlit.hello.utils import show_code

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Property `Dashboard`')

st.sidebar.markdown('''
---
''')


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

demo, url = (
            ST_DEMOS['line']
        )

def render_basic_area_chart():
    options = {
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": [820, 932, 901, 934, 1290, 1330, 1320],
                "type": "line",
                "areaStyle": {},
            }
        ],
    }
    st_echarts(options=options)

demo()
sourcelines, _ = inspect.getsourcelines(demo)