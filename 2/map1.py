import folium
import pandas as pd

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles='Mapbox Bright')
data=pd.read_csv('Volcanoes_USA.txt')

lat=list(data.LAT)
lon=list(data.LON)
elev=list(data.ELEV)

def color_producer(value):
    if value<1000:
        return '#00ff00'
    elif 1000<=value<3000:
        return '#ff7f00'
    else:
        return '#ff0000'

fg1=folium.FeatureGroup(name='Volcanoes')
for lt,ln,el in zip(lat,lon,elev):
    fg1.add_child(folium.CircleMarker(location=[lt,ln],radius=6,
    popup=str(el) +' m',fill_opacity=0.7,fill=True,color='grey',
    fill_color=color_producer(el)))

fg2=folium.FeatureGroup(name='Population')
fg2.add_child(folium.GeoJson(open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())

map.save('Map1.html')
