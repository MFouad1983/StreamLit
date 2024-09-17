import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Test",layout="wide",
                   initial_sidebar_state="expanded")
st.sidebar.write(" Hello Egypt 2024")
df= px.data.gapminder()
aa=st.sidebar.selectbox("select country",df.columns)

st.write(" The Dash "+aa)
st.dataframe(df.head(100))
