import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Vector")

    m = leafmap.Map(center=[0, 0], zoom=2)


    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable_geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")


    #in_csv = 'https://raw.githubusercontent.com/giswqs/data/main/world/world_cities.csv'  

    #m = leafmap.Map(tiles="stamentoner")
    #m.add_xy_data(in_csv, x="longitude", y="latitude", layer_name="World Cities")
    
    m.to_streamlit(height=700)
