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
    st.title("Project Models")
    # st.subheader("Created by Kaite Gaertner, Carlin Gerstenberger, and Nicholas Drake")
    st.write('This page will contain model information')
    
    with st.container():
        st.write("---")
        st.header('Station Optimizatoin')
        # Create tabs
        tab1, tab2 = st.tabs(["Low Traffic Stations", "Bike Relocation"])
        with tab1:
                # Load in the data
                low_traffic_df = pd.read_csv('https://raw.githubusercontent.com/katiegaertner/Fraud-Detection/main/low_traffic_stations.csv')
                low_traffic_df['max_daily_traffic'] = low_traffic_df['max_departure'] + low_traffic_df['max_arrival']

                # Create a folium map centered on "downtown Chicago"
                low_traffic_map = folium.Map(location = (41.8781, -87.6298),zoom_start = 11)
                marker_cluster_a = MarkerCluster().add_to(low_traffic_map)

                for index, row in low_traffic_df.iterrows():
                    # location of station
                    station_location = (row['station_lat'],row['station_lng'])
                    station = row['station_name']
                    max_arrival = row['max_arrival']
                    max_departure = row['max_departure']
                            
                    # Create the marker and add it to the map.
                    folium.Marker(location = station_location, 
                    popup =\
                    folium.Popup(html=f"Divvy Station: {station} had {max_arrival} arrivals and {max_departure} departures on its highest traffic day in September",max_width=450)).\
                    add_to(marker_cluster_a)

                map_column, text_column = st.columns((1,2))
                with map_column:
                    st_map = st_folium(low_traffic_map)
                with text_column:
                    st.write("The interactive map allows users to zoom in to \
                    identify local patterns, as well as select  specific stations \
                        to see their performance on their highest traffic day.")
        with tab2:
                # Load in the data
                bike_relocation = pd.read_csv('https://raw.githubusercontent.com/katiegaertner/Fraud-Detection/main/bike_relocation.csv')
                bike_relocation['difference'] = bike_relocation['difference'].astype(int)

                # Create a folium map centered on "downtown Chicago"
                bike_relocation_map = folium.Map(location =(41.8781, -87.6298),zoom_start=11)
                marker_cluster_b = MarkerCluster().add_to(bike_relocation_map)

                # Create a marker for each station that requires bike relocation--"green" for bike surplus and "red" for bike deficit.
                for index, row in bike_relocation.iterrows():
                    station_name = row['station_name']
                    difference = row['difference']
                    loc = (row['station_lat'],row['station_lng'])
                    if difference > 0: 
                        folium.Marker(location=loc,popup = folium.Popup(html = f"Pick Up {int(difference)} bike(s) from {station_name}", sticky = True),\
                        icon=folium.Icon(color='green', icon='minus-sign'),).add_to(marker_cluster_b)
                    elif difference < 0:
                        folium.Marker(location=loc, popup = folium.Popup(html = f"Deliver {int(abs(difference))} bikes(s) to {station_name}", sticky = True),\
                        icon=folium.Icon(color='red',icon='plus-sign'),).add_to(marker_cluster_b)

                map_column, text_column = st.columns((1,2))
                with map_column:
                    st_map = st_folium(bike_relocation_map)
                with text_column:
                    st.write("The interactive map allows users to zoom in \
                         to identify local patterns, as well as select specific \
                        stations to see their projected surplus/deficit. \
                        Stations marked with the red (+) marker are flagged for \
                        bike pick up, while stations marked with the green (-) \
                        are flagged for bike delivery.")
                    st.write("Bike delivery and pick up \
                        drivers can use this map to identify where to relocate \
                         bikes within specific neighborhoods. For example \
                        drivers would pick up 43 bikes from Canal St. \
                        and Harrison, and relocate 41 of those bikes to Financial \
                        Pl and Ida B Wells Dr.")
                    st.markdown("**If the map doesn't load, please refresh page.**")
        with st.container():
            st.write("---")
            st.header('Human Flow')
            tab1, tab2 = st.tabs(["Human Flow", "High Volume Traffic"])