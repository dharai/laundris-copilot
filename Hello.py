# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Dashboard",
        page_icon="👋",
    )

    st.write("# Welcome to Laundris Co-Pilot 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Laundris Co-Pilot is self-guided AI-Based linen operations suite
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
