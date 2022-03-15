import json
from plotly.graph_objs import Layout
from plotly import offline

file_name = 'data/all_month.geojson'
with open(file_name) as f:
    eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(eq_data, f, indent=4)

mags, lons, lats, titles = [], [], [], []
for feature in eq_data['features']:
    properties = feature['properties']
    mag = properties['mag']
    if mag is not None and mag >= 0:
        mags.append(mag)
        lons.append(feature['geometry']['coordinates'][0])
        lats.append(feature['geometry']['coordinates'][1])
        titles.append(properties['title'])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': titles,
    'marker': {
        'size': [mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
