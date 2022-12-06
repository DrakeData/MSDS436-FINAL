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
    with st.container():
        st.write("---")
        st.header('Station Optimization')
        # Create tabs
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
            st.markdown('''Low-traffic stations were identified by 
            aggregating the maximum daily departures and maximum 
            daily arrivals for each station for the month of September. 
            Stations with less than four maximum daily departures or 
            less than four maximum daily arrivals were identified as 
            "low-traffic" and flagged for further research and possible 
            closure.
            ''')
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
            st.markdown('''We use Divvy ride and weather data to 
            identify opportunities for internal cost savings by 
            predicting station over and under supply to anticipate 
            bike transfer needs using the following predictive features: 
            weekday (binary), average daily temperature, average daily 
            windspeed, total daily rain, day of the week, one-day ride 
            count lag, two-day ride count lag, and a one-hot encoding 
            of a weather description (“clear”, “clouds”, “drizzle”, 
            “mist”, “rain”, “thunderstorm” and “smoke”).''')
            
            st.markdown('''Two ordinary least squares regression models were 
            performed on each station: one for daily arrivals and 
            one for daily departures. These predictions were pushed 
            into a single data frame and their differentials calculated. 
            The forecasted differential identifies stations with a 
            predicted overage supply, and stations with a predicted 
            bike shortage—these forecasts will inform bike relocation 
            efforts (see the interactive bike relocation map), and 
            prevent lost rental opportunities due to bike shortage at 
            high-demand stations.''')
            st.write("##")
        with st.container():
            st.write("---")
            st.header('Human Flow')
            st.markdown("**NOTE:** This map takes a little time to load.")
    # Load in the data
    df = pd.read_csv("https://raw.githubusercontent.com/DrakeData/raw_data_files/main/202209_divvy_distance_weather_v2.csv")
    #folium map for ride start/stop
    ride_map = folium.Map(location =(41.8781, -87.6298),zoom_start=11)

    marker_cluster = MarkerCluster().add_to(ride_map)

    for (lat,lng, id) in zip(df['start_lat'][0:1000], df['start_lng'][0:1000], df['ride_id'][0:1000]):
        folium.Marker(location=(lat,lng),popup=
                        folium.Popup(html="lat: %s <br> long: %s<br> ride iD: %s"
                        %(lat,lng, id)),icon=folium.Icon(color='green',
                        icon='ok-sign'),).add_to(marker_cluster)

    for (lat,lng, id) in zip(df['end_lat'][0:1000], df['end_lng'][0:1000], df['ride_id'][0:1000]):
        folium.Marker(location=(lat,lng),popup=
                        folium.Popup(html="lat: %s <br> long: %s <br> ride iD: %s"
                        %(lat,lng, id)),icon=folium.Icon(color='red',
                        icon='remove-sign'),).add_to(marker_cluster)   
    
    start_latlng = list(zip(df['start_lat'], df['start_lng']))
    end_latlng = list(zip(df['end_lat'], df['end_lng']))
    points=list(zip(start_latlng, end_latlng))
    folium.PolyLine(points[0:1000], color="red", weight=1.5, opacity=0.7).add_to(ride_map)
    
    map_column, text_column = st.columns((1,2))
    with map_column:
        st_map = st_folium(ride_map)
    with text_column:
        st.markdown('''
        The purpose of utilizing machine learning for Chicago 
        bicycle travel is to predict ride time for any given 
        start/end station, day, time, and quadrant of interest. 
        An actual ride time that has a significantly higher value 
        than predicted ride time can be used to indicate 
        propensity-to-buy. When overlaid with thousands of other 
        trips, common routes can be established in order to highlight 
        areas for business investment, marketing strategies, and 
        low-hanging fruit pedestrian sales opportunities. This is 
        additionally substantiated by the large volume.
        ''')

