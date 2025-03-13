import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load your data into a DataFrame
data = pd.read_csv("./wind_with_lat_lon.csv")  # Replace with your file path

# Load the U.S. county boundaries shapefile
counties = gpd.read_file("../tp/cb_2022_us_county_500k/cb_2022_us_county_500k.shp")  # Replace with your shapefile path

# Convert your data to a GeoDataFrame
geometry = [Point(xy) for xy in zip(data["longitude"], data["latitude"])]
gdf = gpd.GeoDataFrame(data, geometry=geometry, crs="EPSG:4326")  # Assuming WGS84 coordinates

# Perform a spatial join to find the county for each point
gdf = gpd.sjoin(gdf, counties, how="left", predicate="within")  # Use 'predicate' instead of 'op'

# Extract relevant columns (e.g., county name and FIPS code)
gdf = gdf[["date", "u_wind", "v_wind", "wind_speed", "NAME", "GEOID"]]  # Adjust column names as needed
gdf.rename(columns={"NAME": "county", "GEOID": "fips"}, inplace=True)

# Save the updated DataFrame to a new CSV file
gdf.to_csv("fips_wind_data.csv", index=False)
print("County and FIPS Code added successfully!")