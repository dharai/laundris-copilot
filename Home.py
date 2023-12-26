# Laundris Analytics App

import streamlit as st
from streamlit.logger import get_logger

from demo_echarts import ST_DEMOS

LOGGER = get_logger(__name__)


def main():
    st.set_page_config(
        page_title="Dashboard",
        page_icon=":chart_with_upwards_trend:",
    )

    st.write("# Welcome to Laundris AI Analytics")

    st.markdown(
        """
        Laundris AI is self-guided AI-Based linen operations suite
        for hospitality property or laundry facility.
        **👈 Select a demo from the sidebar** to see our demos
        of what Laundris can do!
        ### Want to learn more?
        - Check out laundris.com
        - Jump into our app laundris.app to signup
        - Ask a question in our [Laundris community](https://laundris.com)
        ### See our app demos
        - Use Laundris to [manage your hotel property
          autonomously](https://laundris.com)
        - Explore ways to [manage your laundry facility](https://laundris.com)
    """
    )


if __name__ == "__main__":
    main()
    with st.sidebar:
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://laundris.app" target="_blank"><img src="../laundris-logo.png" alt="Laundris Logo" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.sidebar.success("Select a dashboard below.")

