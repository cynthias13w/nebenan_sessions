import streamlit as st

st.set_page_config(
    page_title="Nebenan",
    page_icon="📦")

col1, col2, col3, col4, col5 = st.columns(5)
with col5:
    st.image('nebenan-logo.jpg', width=75)
def page_home():
    # st.markdown('<h1 style="color: #CAE85D;">Nebenan</h1>', unsafe_allow_html=True)
    st.markdown("""
    <h3>
        <span style="color: #201649;">Welcome to the </span>
        <span style="color: #FE9DE1;">Streamlit</span>
        <span style="color: #201649;">Learning Session</span>
    </h3>
    """, unsafe_allow_html=True)
    st.markdown("""
            *Streamlit*: An open-source Python library that makes it easy to create interactive web apps for data science and machine learning projects.

            ### Why streamlit?
            - **Bridging the Gap:** Enables data scientists to build web apps without needing web developers.
            - **Simplifying Insight Sharing:** Move beyond static reports to dynamic, interactive apps.
            - **Rapid Prototyping:** Quickly create and test ideas with instant feedback.
            - **Lowering the Barrier to Entry:** Accessible to a wider audience, including non-programmers.
            - **Fostering Collaboration:** Encourages sharing and collaboration within the community.

            ### Key Features

            - **Simple**: Build web apps with just a few lines of Python.
            - **Interactive Widgets**: Easily add sliders, buttons, etc.
            - **Real-time Updates**: Apps update automatically with code or data changes.
            - **Data Visualization**: Integrates with visualisation packages such as Matplotlib, Seaborn and Plotly.
            - **Easy Deployment**: Share apps with a link using Streamlit Cloud, whether they're standalone or connected to Snowflake for data integration.

            #### Example: A Simple App

            ```python
            import streamlit as st
            import pandas as pd
            import numpy as np

            st.title("Simple Streamlit App")
            data = pd.DataFrame({
                'x': np.random.randn(100),
                'y': np.random.randn(100)
            })
            st.line_chart(data)

                """)
if __name__ == "__main__":
    page_home()
