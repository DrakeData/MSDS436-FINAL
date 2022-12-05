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
img_spark_eda = Image.open("images/sparkEDA_total.png")
img_map = Image.open("images/map_image.jpg")
img_latlngdist = Image.open("images/latlngdist.png")
img_hist_member_ridetime_dist = Image.open("images/hist_member_ridetime_dist.png")
img_hist_ridetype_ridetime_dist = Image.open("images/hist_ridetype_ridetime_dist.png")
img_ridetime_dist = Image.open("images/ridetime_dist.png")
img_pop_routes = Image.open("images/pop_routes.png")
img_burst_member_ride_day = Image.open("images/burst_member_ride_day.png")
img_member_station_hour = Image.open("images/member_station_hour.png")
img_burst_quadrant_station = Image.open("images/burst_quadrant_station.png")

# --- EDA ---
# Load in the data


# Divvy bike data
with st.container():
    st.title("Exploratory Data Analysis (EDA)")
    st.write("On this page, we will dig deeper into the data to get a better \
    understanding of it.")
    st.markdown('''**NOTE:** EDA was performed in PySpark and Pandas.''')
    with st.container():
        st.write("---")
        st.image(img_spark_eda)
        st.markdown('''The above snip of code demonstrates initial 
        statistics of the Divvy dataset, processed using Spark. 
        Spark was used to level-set on feature characteristics 
        before executing data cleansing, wrangling, and feature 
        enrichment.''')
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_map)
        with text_column:
            st.markdown('''This image represents the initial reference points 
            for historic Chicago. Madison St and State St serve as zeroed lines 
            of demarcation from which Chicago is divided East/West and 
            North/South. While this would be one method in quadrant-izing 
            the map, there are more accurate ways to measure distribution, 
            in order to create quadrants with more balance.''')
        with st.container():
            st.write("---")
            st.write("##")
            st.image(img_latlngdist)
            st.markdown('''In assessing the best way to create ride activity 
            quadrants, Madison St and State St were juxtaposed with the Divvy 
            dataset's mean latitude/longitude values, as well as the 50% 
            quartile values. All 3 are overlaid onto the starting point 
            distribution as shown. Ultimately, the mean value was chosen to 
            represent an initial quadrant approach, as it is the most agile 
            metric, given that ride activity could shift in the future.''')
        with st.container():
            st.write("---")
            st.write("##")
            st.image(img_hist_member_ridetime_dist)
            st.markdown('''This histogram series represents volume of ride time 
            (in seconds) for each of the membership classes, binned by time 
            difference (actual minus predicted. The key insight here is to 
            realize that casual rides carry a much longer right tail of 
            positive time difference, meaning casual riders seem to represent 
            a majority of human flow "peddle-meddling".''')
        with st.container():
            st.write("---")
            st.write("##")
            st.image(img_hist_ridetype_ridetime_dist)
            st.markdown('''These histograms show volume of ridetime per each 
            bike type, and demonstrate how bike type affects time difference 
            assessments. Unsurprisingly, classic bikes were the most popular, 
            and electric bikes carried an average time_diff value below zero, 
            meaning the average ride went faster than predicted. Additionally, 
            docked bikes do not bear much volume weight. This would be 
            interesting data to juxtapose with Divvy's fleet sizes of each bike 
            class, to assess usage and rider preference as opposed to what's 
            available.''')
        with st.container():
            st.write("---")
            st.write("##")
            st.image(img_ridetime_dist)
            st.markdown('''The ride datetime vs. actual time and predicted 
            time proved to be a key visualization in understanding holistic 
            Chicago cycling trends. In general, most Chicago bikers are 
            efficient with their travel - times are less than the OpenStreetMap 
            predicts. However, on weekends, folks seem to flip that trend, 
            taking considerably more time than the estimated travel time 
            predicts. Additionally, on a daily weekday basis, there appears to 
            be moderate travel in the mid-morning hours (7-9am) and moderate 
            travel also occurs in the evenings (5-7pm). The giant travel 
            block mid-Sept 22nd may be due to a White Sox home game!''')
        with st.container():
            st.write("---")
            st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_pop_routes)
        with text_column:
            st.markdown('''The table demonstrating which routes are 
            the most popular. Nearly all are located in the main Chicago 
            downtown area. Several of the top 20 are loops, which could 
            indicate a leisurely weekend ride, a quick errand, or perhaps, 
            in large time difference occasions, a workday commute. Looped 
            routes also make human flow estimation more difficult, as time 
            passage is the only variable that still contributes to potential 
            paths cycled.''')
        with st.container():
            st.write("---")
            st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_burst_member_ride_day)
        with text_column:
            st.markdown('''This sunburst chart demonstrates the distribution 
            across membership class, starting bike station, and day of week. 
            We can see large demand in the main metro area (Streeter Dr, Grand 
            Ave, DuSable Lake Shore, Monroe St, etc...) on Saturdays and 
            Sundays for casual riders, while members appear to utilize the 
            bikes for workday commutes. Additionally, we can see which stations 
            have the most demand across all days, while others only carry 
            demand for some days.''')
        with st.container():
            st.write("---")
            st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_member_station_hour)
        with text_column:
            st.markdown('''Much like the day of week version, this sunburst 
            indicates which times of day show the most traffic, per member 
            class and starting station. Interesting points to show here 
            include the apparent fact that members span a larger station 
            list than casual rides do, and key hours appear to be 6-9am, 
            and 3-6pm.''')
        with st.container():
            st.write("---")
            st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image(img_burst_quadrant_station)
        with text_column:
            st.markdown('''This sunburst simply indicates which stations are 
            most important (aka most used) per quadrant. Again, given that 
            this is a PoC to showcase the ability to box-in key areas of 
            interest, this is an important distinction to understand what 
            station resources are contributing to human flow, and 
            which are not.''')