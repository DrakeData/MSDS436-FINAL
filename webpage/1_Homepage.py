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

