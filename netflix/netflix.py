import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Netflix Listings Analysis')
st.write('Dataset from Kaggle')

st.subheader('Importing Dataset')

try:
    df = pd.read_csv('netflix/netflix_titles.csv')
    st.write(df)
except Exception as e:
    st.write(e)

st.subheader('Group Data by Type')

out_type = df['type'].value_counts()\
                        .to_frame()\
                        .rename({'type': 'count'}, axis=1)
st.write(out_type)

fig = px.bar(out_type, x=out_type.index, y='count')
st.write(fig)