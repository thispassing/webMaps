import folium
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

def radius_producer(RAD):
    if RAD < 1000:
        return '5'
    elif 1000<= RAD < 2000:
        return '6'
    elif 2000<= RAD < 3000:
        return '7'
    elif 3000<= RAD < 4000:
        return '8'
    else:
        return '9'

map = folium.Map(location=[41.28,-110.54], zoom_start=6, tiles="Stamen Toner")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" m", radius=radius_producer(el), 
    fill=True, fill_color=color_producer(el), fill_opacity=0.7, color='grey'))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 100000000
else 'red' if 100000000 <= x['properties']['POP2005'] < 300000000 else 'blue'}))

# fg.add_child(plt.text( -170, -58,'Where people talk about #Surf\n\nData collected on twitter by @R_Graph_Gallery during 300 days\nPlot realized with Python and the Basemap library',
# ha='left', va='bottom', size=9, color='#555555'))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")
