from pathlib import Path
import csv
import plotly.express as px

path = Path('EQ_Data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extracts latitudes, longitudes and brightness.

latitudes, longitudes, brightnesses = [], [], []
for row in reader:

    try:
        latitude = float(row[0])
        longitude = float(row[1])
        brightness = float(row[2])
    except ValueError:
        print(f"Missing data")
    else:
        latitudes.append(latitude)
        longitudes.append(longitude)
        brightnesses.append(brightness)

title = 'World Fires'

fig = px.scatter_geo(lat=latitudes, lon=longitudes, size=brightnesses, title=title,

                     labels={'color': 'salmon'},
                     projection='natural earth',

                     )
fig.show()
