import streamlit as st

# ---- MAIN TAB SECTION ----
# emoji cheatsheet: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="MSDS 436: Final Project", 
    page_icon=":bike:", 
    layout="wide"
    )

# --- Arch Details ---
# Divvy bike data
with st.container():
    st.title("Project Architecture")
    st.write("---")
    st.write("The architecture shown below represents a combination of \
        Proof-of-Concept (PoC) structure and eventual production environment. \
        The established architecture is a skeleton for scalable project value \
        delivery. Current project state includes local consumption of static \
        data, locally-developed and tested models, a GitHub repository for \
        initial DevOps management, and a Docker-containerized public deployment \
        via Streamlit and the AWS cloud.")
    st.write("##")
    st.write("Future state would include additional DevOps functionality, \
         as well as cloud-based MLOps tool utilization for model monitoring, \
         infrastructure auto-scaling, and backend model artifact API delivery.")
    st.write("##")
    st.image("https://lucid.app/publicSegments/view/cee8ca61-ba43-44e4-b2ad-314cc020608c/image.png")
