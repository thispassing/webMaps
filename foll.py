import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
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

map = folium.Map(location=[41.28,-110.54], zoom_start=6, tiles="OpenStreetMap")

fg = folium.FeatureGroup(name="My Map")

# for lt, ln, el in zip(lat, lon, elev):
#   fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon=folium.Icon(color=color_producer(el))))

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" m", radius=radius_producer(el), 
    fill=True, fill_color=color_producer(el), fill_opacity=0.7, color='grey'))

# fg.add_child(folium.Marker(location=[39.16,-76.73], popup="Here", icon=folium.Icon(color='black')))
# fg.add_child(folium.Marker(location=[39.40,-76.56], popup="Towson", icon=folium.Icon(color='blue')))
# fg.add_child(folium.Marker(location=[39.215,-76.86], popup="Columbia", icon=folium.Icon(color='black')))


map.add_child(fg)

map.save("Map2.html")
