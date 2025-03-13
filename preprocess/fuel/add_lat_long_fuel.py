import pandas as pd

# Load the fuel data
fuel_data = pd.read_csv("./filtered_data_with_date.csv")

# Load the site location data
site_location_data = pd.read_csv("../../datasets/fuel/site_metadata.csv")

# Merge the datasets on Site ID
merged_data = pd.merge(
    fuel_data,
    site_location_data[["Site ID", "Latitude", "Longitude"]],  # Select only relevant columns
    left_on="SiteId",  # Column in fuel data
    right_on="Site ID",  # Column in site location data
    how="left"  # Keep all rows from fuel data
)

# Save the merged data to a new CSV file
merged_data.to_csv("fuel_data_with_lat_long.csv", index=False)

print("Merged CSV saved as 'fuel_data_with_lat_long.csv'")