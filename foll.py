import folium
map = folium.Map(location=[38.98,-76.50], zoom_start=8, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[39.16,-76.73],[39.40,-76.56],[39.215,-76.86]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Here", icon=folium.Icon(color='black')))

# fg.add_child(folium.Marker(location=[39.16,-76.73], popup="Here", icon=folium.Icon(color='black')))
# fg.add_child(folium.Marker(location=[39.40,-76.56], popup="Towson", icon=folium.Icon(color='blue')))
# fg.add_child(folium.Marker(location=[39.215,-76.86], popup="Columbia", icon=folium.Icon(color='black')))


map.add_child(fg)

map.save("Map2.html")
