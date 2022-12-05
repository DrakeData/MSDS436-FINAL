from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_folium import st_folium
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

with st.container():
    st.title("Recommendation")
    # st.subheader("Created by Kaite Gaertner, Carlin Gerstenberger, and Nicholas Drake")
    st.write('This page will contain model information')