import streamlit as st

# logo
col1, col2, col3, col4, col5 = st.columns(5)
with col5:
    st.image('nebenan-logo.jpg', width=75)
    
st.markdown("""
<h2>
    <span style="color: #201649;">How to work with </span>
    <span style="color: #FE9DE1;">layouts </span>
    <span style="color: #201649;">and</span>
    <span style="color: #FE9DE1;">containers </span>
    <span style="color: #201649;">?</span>
</h2>
""", unsafe_allow_html=True)

# st.columns example
st.write("### Columns")
st.code("""
col1, col2, col3 = st.columns(3)

col1.write("This is column 1")
col2.write("This is column 2")
col3.write("This is column 3")
""", language="python")

col1, col2, col3 = st.columns(3)
col1.write("This is column 1")
col2.write("This is column 2")
col3.write("This is column 3")

st.divider()

# # st.container example
# st.write("### st.container")
# st.code("""
# with st.container():
#     st.write("This is inside a container")
#     st.button("A button inside the container")
# """, language="python")

# with st.container():
#     st.write("This is inside a container")
#     st.button("A button inside the container")

# st.divider()

# # st.empty example
# st.write("### st.empty")
# st.code("""
# import time

# placeholder = st.empty()

# for i in range(10):
#     placeholder.text(f"Iteration {i}")
#     time.sleep(1)
# """, language="python")

# placeholder = st.empty()
# for i in range(10):
#     placeholder.text(f"Iteration {i}")
#     time.sleep(1)

# st.divider()

# st.expander example
st.write("### Expander")
st.code("""
with st.expander("➡️ Expand to see more"):
    st.write("This content is hidden until you expand.")
""", language="python")

with st.expander("➡️ Expand to see more"):
    st.write("This content is hidden until you expand.")

st.divider()

# st.form example
st.write("### Form")
st.code("""
with st.form(key='my_form'):
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age', min_value=0)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name: {name}, Age: {age}")
""", language="python")

with st.form(key='my_form'):
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age', min_value=0)
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name: {name}, Age: {age}")

st.divider()

# st.sidebar example
st.write("### Sidebar")
st.code("""
st.sidebar.title("Sidebar")
st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
""", language="python")

st.sidebar.title("Sidebar")
st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

st.divider()

# st.tabs example
st.write("### Tabs")
st.code("""
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Hello")
    
with tab2:
    st.write("Hello again!")
    
with tab3:
    st.write("Helloooo")
""", language="python")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Hello")

with tab2:
    st.write("Hello again!")

with tab3:
    st.write("Helloooo")

