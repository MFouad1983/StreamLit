import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Hello, Streamlit!")
st.write("Hello, Streamlit!")
df=px.data.gapminder();
st.write(df)
with st.sidebar:
    selectedAtt = st.selectbox( 'Select a numeric column to display:',    ['lifeExp', 'pop', 'gdpPercap'])
    selectedCountry = st.multiselect('Select a numeric column to display:',df['country'].unique())
    st.image("Life-Expectancy-550x298.png")
st.plotly_chart(px.line(df[df['country']=='Egypt'],x='year',y='lifeExp'))

c1,c2,c3 = st.columns(3)
with c1:
    st.write("Column 1")
c2.write("Column 1")