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

# ---- LOAD ASSETS ----
img_team = Image.open("images/team_info.png")


with st.container():
    st.title("About Us:")
    st.subheader("This project was created by [Nick Drake](https://github.com/DrakeData), [Kaite Gaertner](https://github.com/katiegaertner), and [Carlin Gerstenberger](https://github.com/carlin-gerstenberger) for MSDS 436.")
    st.image(img_team)