# Laundris Analytics App

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Dashboard",
        page_icon=":chart_with_upwards_trend:",
    )

    st.write("# Welcome to Laundris AI Analytics")

    with st.sidebar:
        st.markdown("---")
        st.markdown(
            '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by <a href="https://twitter.com/andfanilo">@andfanilo</a></h6>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="margin-top: 0.75em;"><a href="https://www.buymeacoffee.com/andfanilo" target="_blank"><img src="../laundris-logo.png" alt="Laundris Logo" height="41" width="174"></a></div>',
            unsafe_allow_html=True,
        )
        st.sidebar.success("Select a dashboard below.")


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
    run()
