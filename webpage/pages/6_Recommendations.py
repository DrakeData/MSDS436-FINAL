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

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_bike2 = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_8Gr1sc.json')

with st.container():
    st.title("Recommendations")
    with st.container():
        st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.markdown('''
        ## Data & Collection
        We recommend that the stations identified in this report as 
        “low-traffic” undergo further to determine the profitability 
        of their continued operation. If the stations are found to be 
        operating at a loss, we recommend their closure.

        ## Station Optimization
        Secondly, we recommend the deployment of station bike 
        shortages/surpluses and the associated interactive map to 
        relocation drivers to help plan relocation routes and amounts.

        ## Human Flow
        Thirdly, we recommend expanding our current model to include a 12-month 
        data set. This larger data set will allow us to identify season patterns,
        and create a stronger human flow model. This more robust model will 
        identify high-traffic and high-time-difference areas within the Chicago 
        area. These insights can be assessed for propensity-to-buy mapping and 
        shared with B2C investors and current business owners who may use the 
        who, when, and where of potential bicyclist customers to inform 
        business strategy.

        Finally, we recommend further Machine Learning research using 
        graph data and shortage/surplus predictions to automate 
        relocation routes.
        ''')
    with right_column:
        st_lottie(lottie_bike2, height=500, key="biking2")