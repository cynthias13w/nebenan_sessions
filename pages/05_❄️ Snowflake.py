import streamlit as st
import os
from snowflake.snowpark import Session
import pandas as pd

# logo
col1, col2, col3, col4, col5 = st.columns(5)
with col5:
    st.image('nebenan-logo.jpg', width=75)

st.snow()

st.markdown("""
<h2>
    <span style="color: #201649;">Integration with </span>
    <span style="color: #98CBD6;">Snowflake ❄️</span>
</h2>
""", unsafe_allow_html=True)

st.markdown("""
Streamlit can connect to Snowflake, enabling you to build apps that interact directly with your Snowflake data. This allows you to:

- **Query Snowflake Data**: Run SQL queries on Snowflake and visualize the results in your Streamlit app.
- **Data Processing**: Combine Snowflake's data warehousing capabilities with Streamlit's app-building simplicity.
- **Secure Access**: Manage data access securely through Snowflake's user management and authentication.

### Example:

```python
import streamlit as st
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT'
)

# Run a query
cur = conn.cursor()
cur.execute("SELECT * FROM your_table")
data = cur.fetchall()

# Display data in Streamlit
st.write(data)
            """)

# connection_parameters = {
#     "account": os.environ.get('snowflake_account'), 
#     "user": os.environ.get('snowflake_user'),
#     "password": os.environ.get('snowflake_password'),
#     }
# session = Session.builder.configs(connection_parameters).create()
# query=
# result = session.sql(query)
# data = result.collect()
# df = pd.DataFrame(data)