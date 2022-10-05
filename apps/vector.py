import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector")
    
    in_csv = 'https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv'  

    m = leafmap.Map(tiles="stamentoner")
    m.add_xy_data(in_csv, x="longitude", y="latitude", layer_name="World Cities")
    
    m.to_streamlit(height=700)
