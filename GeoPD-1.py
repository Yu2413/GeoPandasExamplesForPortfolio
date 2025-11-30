import geopandas as gpd
import matplotlib.pyplot as plt

map1 = gpd.read_file(r"C:/Users/Yu241/Downloads/cb_2023_us_state_20m/cb_2023_us_state_20m.shp")
# Load shapefile

print(map1.columns)
print(map1['STATENS'].unique())
# Filter: check that STATENS exists and what it looks like

print(map1[['NAME', 'STATENS', 'GEOID']].drop_duplicates())

query1 = map1.query("NAME == 'Ohio'")
# Example filter

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
# Create figure + axis

query1.plot(ax=ax, edgecolor='black', cmap='Set3')
# Plot the filtered geometry

ax.set_title("Selected State")
ax.set_axis_off()
# Optional: tidy up

plt.show()