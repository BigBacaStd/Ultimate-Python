from importlib.metadata import metadata
from pathlib import Path
import json

import plotly.express as px

#Read data as a string and convert to a Python object.
path = Path('EQ_Data/4.5_day.geojson.json')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('EQ_Data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])


title = all_eq_data['metadata']['title']


fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     labels={'color': 'Salmon'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()