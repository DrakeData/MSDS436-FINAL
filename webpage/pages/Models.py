from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.graph_objects as go
import pandas as pd

# --- Data Frame ---
# df_paths_c = pd.read_csv('DATA/202209_divvy_cas.csv')
# df_paths_m = pd.read_csv('DATA/202209_divvy_mem.csv')
# df_paths = pd.read_csv('DATA/202209_divvy_paths.csv')

st.set_page_config(
    page_title="MSDS 436: Final Project", 
    page_icon=":bike:", 
    layout="wide"
    )

with st.container():
    st.title("Project Models")
    # st.subheader("Created by Kaite Gaertner, Carlin Gerstenberger, and Nicholas Drake")
    st.write('This page will contain model information')


# Plotly example
# fig = go.Figure()

# #Plot casual riders' popular paths in red.
# for i in range(len(df_paths_c[:1000])):
#     fig.add_trace(
#         go.Scattergeo(
#             locationmode = 'USA-states',
#             lon = [df_paths_c['start_lng'][i], df_paths_c['end_lng'][i]],
#             lat = [df_paths_c['start_lat'][i], df_paths_c['end_lat'][i]],
#             mode = 'lines',
#             line = dict(width = 1,color = 'red'),
#             opacity = float(df_paths_c['cnt'][i]) / float(df_paths['cnt'].max()),
#         )
#     )

#Plot members' popular paths in blue.
# for i in range(len(df_paths_m[:1000])):
#     fig.add_trace(
#         go.Scattergeo(
#             locationmode = 'USA-states',
#             lon = [df_paths_m['start_lng'][i], df_paths_m['end_lng'][i]],
#             lat = [df_paths_m['start_lat'][i], df_paths_m['end_lat'][i]],
#             mode = 'lines',
#             line = dict(width = 1,color = 'blue'),
#             opacity = float(df_paths_m['cnt'][i]) / float(df_paths['cnt'].max()),
#         )
#     )   

# fig.update_layout(
#     title_text = 'Divvy Bike Sharing Popular Paths',
#     showlegend = False,
#     geo = dict(
#         scope = 'north america',
#         projection_type = 'azimuthal equal area',
#         showland = True,
#         showsubunits = True,
#         landcolor = 'rgb(243, 243, 243)',
#         countrycolor = 'rgb(204, 204, 204)',
#         fitbounds = 'locations',
#     ),
# )

# st.plotly_chart(fig)