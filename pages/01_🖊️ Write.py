import streamlit as st

# Example of st.title
st.title("Streamlit Feature Showcase")
st.code('st.title("Streamlit Feature Showcase")')

# Example of st.header
st.header("1. Headers and Subheaders")
st.code('st.header("1. Headers and Subheaders")')

# Example of st.subheader
st.subheader("Subheader Example")
st.code('st.subheader("Subheader Example")')

# Example of st.markdown
st.markdown("""
### 2. Markdown Text

Markdown allows you to format text using special syntax, like **bold**, _italic_, and more.

- **Bold**: `**text**`
- _Italic_: `_text_`
- [Link](https://streamlit.io)
""")
st.code('''st.markdown("""
### 2. Markdown Text

Markdown allows you to format text using special syntax, like **bold**, _italic_, and more.

- **Bold**: `**text**`
- _Italic_: `_text_`
- [Link](https://streamlit.io)
""")''')

# Example of FORMATTED TEXT
st.header("3. Formatted Text")
st.markdown("""
- **Bold Text**: **Streamlit is awesome!**
- _Italic Text_: _Streamlit is awesome!_
- `Code Snippet`: `import streamlit as st`
""")
st.code('''st.markdown("""
- **Bold Text**: **Streamlit is awesome!**
- _Italic Text_: _Streamlit is awesome!_
- `Code Snippet`: `import streamlit as st`
""")''')

# Example of st.caption
st.header("4. Caption")
st.caption("This is a caption, useful for adding small notes or descriptions.")
st.code('''st.caption("This is a caption, useful for adding small notes or descriptions.")''')

# Example of st.code
st.header("5. Code Snippet")
code = '''def hello():
    print("Hello, Streamlit!")
'''
st.code(code, language='python')
st.code('''code = """def hello():
    print("Hello, Streamlit!")
"""\nst.code(code, language='python')''')

# Example of st.divider
st.header("6. Divider")
st.write("Here is a section divider:")
st.divider()
st.code('''st.divider()''')

# Example of st.echo
st.header("7. Echo")
st.write("Using st.echo to display the code along with its output:")
with st.echo():
    # Code here will be both displayed and executed
    x = 42
    st.write(f"The answer is {x}")
st.code('''with st.echo():
    # Code here will be both displayed and executed
    x = 42
    st.write(f"The answer is {x}")''')

# Example of st.latex
st.header("8. LaTeX")
st.write("Render mathematical expressions using LaTeX:")
st.latex(r'''
     a^2 + b^2 = c^2
''')
st.code('''st.latex(r"""
a^2 + b^2 = c^2
""")''')

# Example of st.text
st.header("9. Text")
st.text("This is simple text without any formatting.")
st.code('''st.text("This is simple text without any formatting.")''')
