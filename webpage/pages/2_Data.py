from PIL import Image
import requests
import streamlit as st

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
img_divvy_logo = Image.open("images/divvy_logo.png")
img_osrm_logo = Image.open("images/osrm_logo.png")
img_openweath_logo = Image.open("images/openweath_logo.png")

# --- About the Data ---
# Divvy bike data
with st.container():
    st.title("About the Data")
    st.write("---")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_divvy_logo)
    with text_column:
        st.subheader("Divvy Bike Data")
        st.markdown('''
        The Divvy bike data set is provided by Divvy on a monthly bases and can be found on [their website](https://ride.divvybikes.com/system-data).
        
        The data contains trip information such as:
        - Trip start day and time
        - Trip end day and time
        - Trip start station
        - Trip end station
        - Rider type (Member, Single Ride, and Day Pass)

        For our use case, we have limited the data set to only the month of September 2022 and rides that only have a start and end station. 
        We have also taken a random sample of 5,000 rides per day.
                ''')
        st.write("##")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_osrm_logo)
        with text_column:
            st.subheader("Open Source Routing Machine (OSRM) API")
            st.markdown('''
            To get estimated trip time, we used the OSRM API. 
            This API combines sophisticated routing algorithms with the open 
            and free road network data of the OpenStreetMap (OSM) project. 
            To calculate the shortest path for a bike ride, we pass the start 
            and end station's latitude and longitude to return the estimated 
            duration (in seconds) and distance (in meters).
                    ''')
            st.write("##")
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_openweath_logo)
        with text_column:
            st.subheader("OpenWeather API")
            st.markdown('''
            To gather historical weather data, we used [OpenWeather's One Call API](https://openweathermap.org/api/one-call-3#data). 
            
            We gathered the following data points from the API:
            - Temperature (in Fahrenheit)
            - Humidity
            - Wind Speed
            - Weather
            - Precipitation of rain/snow

            Due to the cost per call model, we decided to limit our cost by only using the latitude and longitude of the center of Chicago (41.87, -87.62) and only pulling back 24 hours of data per day (total of 720 API calls).
                    ''')
