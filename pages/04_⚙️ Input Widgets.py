import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# BUTTONS
st.header("Buttons")

# Example of st.button
st.code('''if st.button("Click Me"):
    st.write("Button was clicked!")''')
if st.button("Click Me"):
    st.write("Button was clicked!")

# Example of st.download_button
st.code('''st.download_button(
    label="Download CSV",
    data=df.to_csv(),
    file_name="data.csv",
    mime="text/csv"
)''')
df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.download_button(
    label="Download CSV",
    data=df.to_csv(),
    file_name="data.csv",
    mime="text/csv"
)

# # Example of st.feedback
# st.code('''st.feedback("This is a feedback message!")''')
# st.feedback("This is a feedback message!")

# Example of st.form_submit_button
st.code('''with st.form(key='my_form'):
    st.text_input("Your Name")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write("Form submitted!")''')
with st.form(key='my_form'):
    st.text_input("Your Name")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write("Form submitted!")

# Example of st.link_button (Hypothetical)
st.code('''st.markdown("[Link Button](https://example.com) [Click Here](https://example.com)")''')
st.markdown("[Link Button](https://example.com) [Click Here](https://example.com)")

# Example of st.page_link (Hypothetical)
st.code('''st.markdown("[Page Link](https://example.com) [Go to Page](https://example.com)")''')
st.markdown("[Page Link](https://example.com) [Go to Page](https://example.com)")

# SELECTIONS
st.header("Selections")

# Example of st.checkbox
st.code('''if st.checkbox("Check this box"):
    st.write("Checkbox is checked!")''')
if st.checkbox("Check this box"):
    st.write("Checkbox is checked!")

# Example of st.color_picker
st.code('''color = st.color_picker("Pick A Color", "#FF0000")
st.write(f"Selected color: {color}")''')
color = st.color_picker("Pick A Color", "#FF0000")
st.write(f"Selected color: {color}")

# Example of st.multiselect
st.code('''options = st.multiselect("Choose options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected options: {options}")''')
options = st.multiselect("Choose options", ["Option 1", "Option 2", "Option 3"])
st.write(f"Selected options: {options}")

# Example of st.radio
st.code('''choice = st.radio("Select one", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {choice}")''')
choice = st.radio("Select one", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {choice}")

# Example of st.selectbox
st.code('''selection = st.selectbox("Choose one", ["Item 1", "Item 2", "Item 3"])
st.write(f"You selected: {selection}")''')
selection = st.selectbox("Choose one", ["Item 1", "Item 2", "Item 3"])
st.write(f"You selected: {selection}")

# Example of st.select_slider
st.code('''value = st.select_slider("Select a value", options=[1, 2, 3, 4, 5])
st.write(f"Selected value: {value}")''')
value = st.select_slider("Select a value", options=[1, 2, 3, 4, 5])
st.write(f"Selected value: {value}")

# Example of st.toggle (Hypothetical)
st.code('''toggle = st.checkbox("Toggle")
st.write(f"Toggle is {'on' if toggle else 'off'}")''')
toggle = st.checkbox("Toggle")
st.write(f"Toggle is {'on' if toggle else 'off'}")

# NUMERIC
st.header("Numeric")

# Example of st.number_input
st.code('''number = st.number_input("Insert a number", min_value=0, max_value=100, value=25)
st.write(f"Number input: {number}")''')
number = st.number_input("Insert a number", min_value=0, max_value=100, value=25)
st.write(f"Number input: {number}")

# Example of st.slider
st.code('''slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {slider_value}")''')
slider_value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# DATE & TIME
st.header("Date & Time")

# Example of st.date_input
st.code('''date = st.date_input("Select a date", datetime.today())
st.write(f"Selected date: {date}")''')
date = st.date_input("Select a date", datetime.today())
st.write(f"Selected date: {date}")

# Example of st.time_input
st.code('''time = st.time_input("Select a time", datetime.now().time())
st.write(f"Selected time: {time}")''')
time = st.time_input("Select a time", datetime.now().time())
st.write(f"Selected time: {time}")
