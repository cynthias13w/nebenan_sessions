import streamlit as st
from text import *

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Nebenan",
    page_icon="📦")

def page_home():
    st.markdown('<h1 style="color: #CAE85D;">Nebenan</h1>', unsafe_allow_html=True)
    st.markdown("""<h3 style="color: #FE9DE1;">Streamlit Learning Session</h3>""", unsafe_allow_html=True)
    st.markdown("""
            Streamlit: An open-source Python library that makes it easy to create interactive web apps for data science and machine learning projects.

            ## Key Features

            - **Simple**: Build web apps with just a few lines of Python.
            - **Interactive Widgets**: Easily add sliders, buttons, etc.
            - **Real-time Updates**: Apps update automatically with code or data changes.
            - **Data Visualization**: Integrates with visualisation packages such as Matplotlib, Seaborn, Plotly.
            - **Easy Deployment**: Share apps with a link using Streamlit Cloud.

            ## Example: Simple App

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
