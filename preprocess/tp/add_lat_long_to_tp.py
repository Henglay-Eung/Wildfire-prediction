import pandas as pd

# Load the station data into a DataFrame
station_data = pd.read_csv("../../datasets/tp/filtered_us_stations.csv")  # Replace with your file path

# Load the TP data into a DataFrame
tp_data = pd.read_csv("../tp/filtered_us_tp_2015.csv")  # Replace with your file path

# Merge the two datasets on the 'station' column
merged_data = pd.merge(
    tp_data,
    station_data[["station", "latitude", "longitude", "elevation", "state", "name"]],  # Select only the columns you need
    how="left",
    on="station"
)

# Save the merged data to a new CSV file
merged_data.to_csv("lat_long_tp_data.csv", index=False)
print("Data merged successfully!")