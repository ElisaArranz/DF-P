import time
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/housing.csv')
df_oce = df['ocean_proximity'].unique()

with st.sidebar:
    selection = st.selectbox(label="Proximidad al océano: ", options=df_oce)
    mask = df['ocean_proximity'] == selection
    st.write("Has seleccionado ", selection, ", marika!!!")
    with st.spinner("Loading..."):
        time.sleep(5)
        st.success("Done!")

df_filter = df[mask]
df_filter
plo = px.scatter(df_filter, x='median_house_value', y='households', color="population", size_max=15, height=700, title=selection)
plo