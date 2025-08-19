import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(layout="wide", page_title="India Choropleth Map")

st.title("🗺️ India State-wise Choropleth Map")

with open("india-simple.geojson", "r", encoding="utf-8") as file:
    india_geojson = json.load(file)

df = pd.read_csv("state_data2.csv")

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
selected_metric = st.sidebar.selectbox("Select column to visualize:", numeric_columns)

fig = px.choropleth(
    df,
    geojson=india_geojson,
    featureidkey="properties.name",  
    locations="State",               
    color=selected_metric,
    color_continuous_scale="Viridis",
    title=f"India State-wise {selected_metric} Map"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

 # Display map
st.plotly_chart(fig, use_container_width=True)

# Display data table
with st.expander("📊 Show Raw Data"):
    st.dataframe(df)
