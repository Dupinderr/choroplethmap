import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.set_page_config(layout="wide", page_title="India Choropleth Map")

# App Title
st.title("🗺️ India State-wise Choropleth Map")

# Step 1: Load GeoJSON file
with open("india-simple.geojson", "r", encoding="utf-8") as file:
    india_geojson = json.load(file)

# Step 2: Load CSV file
df = pd.read_csv("state_data2.csv")

# Sidebar options for color scale column
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
selected_metric = st.sidebar.selectbox("Select column to visualize:", numeric_columns)

# Step 3: Plot Choropleth map
fig = px.choropleth(
    df,
    geojson=india_geojson,
    featureidkey="properties.name",  # Confirm this matches your GeoJSON key
    locations="State",               # Column in CSV
    color=selected_metric,
    color_continuous_scale="Viridis",
    title=f"India State-wise {selected_metric} Map"
)

# Step 4: Update layout
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

# Step 5: Display map
st.plotly_chart(fig, use_container_width=True)

# Optional: Display data table
with st.expander("📊 Show Raw Data"):
    st.dataframe(df)
