import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Load your data into a DataFrame
data = pd.read_csv("./fuel_data_with_lat_long.csv")  # Replace with your file path

# Load the U.S. county boundaries shapefile
counties = gpd.read_file("../tp/cb_2022_us_county_500k/cb_2022_us_county_500k.shp")  # Replace with your shapefile path

# Convert your data to a GeoDataFrame
geometry = [Point(xy) for xy in zip(data["Longitude"], data["Latitude"])]
gdf = gpd.GeoDataFrame(data, geometry=geometry, crs="EPSG:4326")  # Assuming WGS84 coordinates

# Perform a spatial join to find the county for each point
gdf = gpd.sjoin(gdf, counties, how="left", predicate="within")  # Use 'predicate' instead of 'op'

# Extract relevant columns (e.g., county name and FIPS code)
gdf = gdf[["Fuel Type", "Category", "Sample Avg Value", "Date", "NAME", "GEOID"]]  # Adjust column names as needed
gdf.rename(columns={"Fuel Type": "fuel_type","Category": "category","Sample Avg Value": "value","NAME": "county", "GEOID": "fips"}, inplace=True)


# Save the updated DataFrame to a new CSV file
gdf.to_csv("fips_tp_data.csv", index=False)
print("County and FIPS Code added successfully!")