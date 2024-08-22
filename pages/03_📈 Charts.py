import streamlit as st
import pandas as pd
import numpy as np

# Generating sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Generating sample data for map
map_data = pd.DataFrame({
    'latitude': np.random.uniform(-90, 90, 100),
    'longitude': np.random.uniform(-180, 180, 100)
})

# Example of st.area_chart
st.header("Area Chart")
st.code('''chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.area_chart(chart_data)''')
st.area_chart(chart_data)
st.divider()

# Example of st.bar_chart
st.header("Bar Chart")
st.code('''st.bar_chart(chart_data)''')
st.bar_chart(chart_data)
st.divider()

# Example of st.line_chart
st.header("Line Chart")
st.code('''st.line_chart(chart_data)''')
st.line_chart(chart_data)
st.divider()

# Example of st.map
st.header("Map")
st.code('''map_data = pd.DataFrame({
    'latitude': np.random.uniform(-90, 90, 100),
    'longitude': np.random.uniform(-180, 180, 100)
})
st.map(map_data)''')
st.map(map_data)
st.divider()

# Example of st.scatter_chart
# st.header("st.scatter_chart")
# st.code('''st.scatter_chart(chart_data)''')
# st.scatter_chart(chart_data)
