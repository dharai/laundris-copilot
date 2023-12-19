import time

import numpy as np

import streamlit as st


def plotting_demo():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


#st.set_page_config(page_title="Plotting Demo", page_icon="📈")
#st.markdown("# Facility Rag Out Prevention")
#st.sidebar.header("Rag outs")
#st.write(
#    """Shows the facility managed rag outs"""
#)


# Row A
st.markdown('# Laundris Value Add')
col1, col2, col3 = st.columns(3)
col1.metric("Labor Cost Saved", "$54K YTD", "7K MTD")
col2.metric("On-Time Processing", "17% YTD", "5% MTD")
col3.metric("Accurate Inventory Tracking", "98% YTD", "100% MTD")

# Row B
st.markdown('### Laundris AI advantages for Facility')
st.write(
    """Shows the facility managed rag outs"""
)

plotting_demo()
