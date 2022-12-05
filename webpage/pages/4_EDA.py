from PIL import Image
import requests
import streamlit as st
import pandas as pd
import folium
from folium import plugins
from folium.plugins import MarkerCluster

# ---- MAIN TAB SECTION ----
# emoji cheatsheet: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="MSDS 436: Final Project", 
    page_icon=":bike:", 
    layout="wide"
    )

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----


# --- EDA ---
# Load in the data

low_traffic_df = pd.read_csv('https://raw.githubusercontent.com/katiegaertner/Fraud-Detection/main/low_traffic_stations.csv')
low_traffic_df['max_daily_traffic'] = low_traffic_df['max_departure'] + low_traffic_df['max_arrival']


# Divvy bike data
with st.container():
    st.title("Exploratory Data Analysis (EDA)")
    st.write("On this page, we will dig deeper into the data to get a better \
    understanding of it.")
    
    with st.container():
        st.write("---")