# importing libraries needed (pandas for data manipulation, os for file, and folium for graph)
import pandas as pd
import os
import folium

# obtaining file from computer
state_geo = os.path.join('C:/Users/vivia/Downloads/us-states.json')
# opening data file
state_cases = f"C:/Users/vivia/Downloads/statesCasesCurrent.csv"
# storing data in variable and reading it in as a pandas data frame
state_data = pd.read_csv(state_cases)

# creating a map, initializing start location and initial zoom
map = folium.Map(location=[34, -80], zoom_start=8)
folium.Choropleth(
     geo_data=state_geo,
     name="choropleth",
     data=state_data,
     columns=["state", "confirmed_cases"], # getting data from specific columns
     key_on="feature.properties.name",
     fill_color="BuPu", # setting color of map
     fill_opacity=0.7,
    line_opacity=0.2,
   legend_name="confirmed cases (total)", # setting text for legend
).add_to(map) # adding choropleth to map
map
map.save("map.html") # saving to html
