from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

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
lottie_bike = load_lottieurl('https://assets4.lottiefiles.com/private_files/lf30_rixr9r00.json')
img_divvy_logo = Image.open("images/divvy_logo.png")
img_osrm_logo = Image.open("images/osrm_logo.png")
img_openweath_logo = Image.open("images/openweath_logo.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Human Flow in Chicago")
    # st.subheader("Created by Kaite Gaertner, Carlin Gerstenberger, and Nicholas Drake")
    st.write('''As a leading bike share service in the city of Chicago, [Divvy's data](https://ride.divvybikes.com/system-data) offers unique opportunities to model human flow patterns.
            Our internal team will leverage Divvy's data to create insights into human movement in Chicago. 
            These insights will directly increase Divvy's enterprise value through internal projects and resale opportunities.''')

# --- Use Case ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Project Use Case")
        st.write("##")
        st.write(
            '''
            Humans travel places, and accurately modeling human flow introduces illuminating opportunities to derive insights as well as act on those insights. Divvy’s bike rental data carries internal as well as external value beyond simple trip rationale, and the organization aims to leverage this information to introduce greater customer satisfaction as well as generate additional revenue streams.

            - **Delivery Optimization** - Bike rental data will be combined with advanced machine learning techniques to predict and recommend bike deliveries on a per-station basis, split across normal use as well as unusually high-use days (i.e. holidays, sporting events, concerts, etc…).
            - **Data as Revenue** - Grasping how many humans are where at what time unlocks the potential to monetize on a locational basis. Divvy seeks to quantify high-traffic zones over time of day in order to sell this data to real estate developers and other parties interested in highest-sales potential pedestrian locations.
            '''
        )
    with right_column:
        st_lottie(lottie_bike, height=500, key="biking")

# --- About the Data ---
# Divvy bike data
with st.container():
    st.write("---")
    st.header("About the Data")
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

        For our usecase, we have limited the data set to only the month of September 2022 and rides that only have a start and end station. 
        We have also taken a random sample of 5,000 rides per day.
                ''')
        st.write("##")
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_osrm_logo)
        with text_column:
            st.subheader("Open Source Routing Machine (OSRM) API")
            st.markdown('''
            To get estimated trip time, we used the [OSRM API](http://project-osrm.org/docs/v5.10.0/api/#general-options). This API combines sophisticated routing algorithms with the open and free road network data of the OpenStreetMap (OSM) project. 
            To calulate the shortest path for a bike ride, we pass the start and end station's latitude and longitude to return the estimated duration (in seconds) and distance (in meters).
                    ''')
            st.write("##")
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_openweath_logo)
        with text_column:
            st.subheader("OpenWeather API")
            st.markdown('''
            To gather historical weather data, we used [OpenWeather's One Call API](https://openweathermap.org/api/one-call-3#data). 
            
            We gathered the following data points from the API:
            - Tempature (in Fahrenheit)
            - Humidity
            - Wind Speed
            - Weather
            - Precipitation of rain/snow

            Due to the cost per call model, we decided to limit our cost by only using the latitude and longitude of the center of Chicago (41.87, -87.62) and only pulling back 24 hours of data per day (total of 720 API calls).
                    ''')
