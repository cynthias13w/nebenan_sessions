import streamlit as st
import pandas as pd
import numpy as np

# Example of st.dataframe
st.header("st.dataframe")
st.code('''df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
st.dataframe(df)''')
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
st.dataframe(df)

# # Example of st.data_editor
# st.header("2. st.data_editor")
# st.code('''edited_df = st.data_editor(df)
# st.write("Edited Data:")
# st.dataframe(edited_df)''')
# edited_df = st.data_editor(df)
# st.write("Edited Data:")
# st.dataframe(edited_df)

# # Example of st.column_config
# st.header("3. st.column_config")
# st.code('''st.data_editor(df, column_config={
#     'A': st.column_config.NumberColumn('A', help="Column A")
# })''')
# st.data_editor(df, column_config={
#     'A': st.column_config.NumberColumn('A', help="Column A")
# })

# Example of st.table
st.header("st.table")
st.code('''st.table(df)''')
st.table(df)

# Example of st.metric
st.header("st.metric")
st.code('''st.metric(label="Temperature", value="70 °F", delta="1.2 °F")''')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# Example of st.json
st.header("st.json")
st.code('''sample_json = {
    "name": "Streamlit",
    "features": ["Interactive Widgets", "Real-time Updates", "Easy Deployment"]
}
st.json(sample_json)''')
sample_json = {
    "name": "Streamlit",
    "features": ["Interactive Widgets", "Real-time Updates", "Easy Deployment"]
}
st.json(sample_json)
