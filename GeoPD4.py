import pandas as pd

import geopandas as gpd

import matplotlib.pyplot as plt

ver_pad = pd.__version__

print(ver_pad)

cities_geo_data1 = {
    "City": ["New York City", "Sao Paulo", "Tokyo", "Lagos", "Sydney"],
    "Population": [8419600, 12325232, 13929286, 15000000, 5312163],
    "Latitude": [40.7128, -23.5505, 35.6895, 6.5244, -33.8688],
    "Longitude": [-74.0060, -46.6333, 139.617, 3.3792, 151.2093]
}

cities_df = pd.DataFrame(cities_geo_data1)

data_query1 = cities_geo_data1["City"]
print(data_query1)

data_query2 = cities_df
print(data_query2)

data_query3 = cities_df[["City", "Population"]]
print(data_query3)

data_query3Point5 = type(cities_geo_data1)
print(data_query3Point5)

Geo_Shape = gdf = gpd.GeoDataFrame(
    cities_df,
        geometry = gpd.points_from_xy(cities_df["Longitude"],
            cities_df["Latitude"]))
print(Geo_Shape)

data_query4 = Geo_Shape.type
print(data_query4)

Geo_Shape.info()

data_query5 = Geo_Shape.geometry
print(data_query5)

data_query6 = type(Geo_Shape.geometry)
print(data_query6)

image_query1 = Geo_Shape['geometry'][0]
print(image_query1)

ax1 = Geo_Shape.plot(figsize=(10,10))
plt.title("Major Cities as Points")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

