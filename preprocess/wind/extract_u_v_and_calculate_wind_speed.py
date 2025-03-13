import xarray as xr
import numpy as np
import pandas as pd

# Load the u-wind and v-wind files with chunking
u_wind_file = '../../datasets/wind/uwnd.sig995.2015.nc'
v_wind_file = '../../datasets/wind/vwnd.sig995.2015.nc'
u_data = xr.open_dataset(u_wind_file, engine='h5netcdf')
v_data = xr.open_dataset(v_wind_file, engine='h5netcdf')

# Extract u-wind and v-wind variables
u_wind = u_data['uwnd']
v_wind = v_data['vwnd']

# Convert u-wind and v-wind to DataFrames
u_df = u_wind.to_dataframe(name='u_wind').reset_index()
v_df = v_wind.to_dataframe(name='v_wind').reset_index()

# Merge the u-wind and v-wind DataFrames on time, lat, and lon
combined_df = pd.merge(u_df, v_df, on=['time', 'lat', 'lon'])

# Calculate wind speed
combined_df['wind_speed'] = np.sqrt(combined_df['u_wind']**2 + combined_df['v_wind']**2)

# Rename the 'time' column to 'date'
combined_df = combined_df.rename(columns={'time': 'date'})
combined_df = combined_df.rename(columns={'lat': 'latitude'})
combined_df = combined_df.rename(columns={'lon': 'longitude'})

# Convert longitude to -180° to 180° range (optional)
# Convert longitude (0° to 360° → -180° to 180°)
combined_df['longitude'] = ((combined_df['longitude'] + 180) % 360) - 180

# Adjust latitude to ensure it is within -90° to 90°
combined_df['latitude'] = combined_df['latitude'].apply(lambda x: x - 180 if x > 90 else x + 180 if x < -90 else x)

# Keep only the required columns
combined_df = combined_df[['date', 'latitude', 'longitude', 'u_wind', 'v_wind', 'wind_speed']]

# Save the combined data to a CSV file
combined_df.to_csv('./wind_with_lat_lon.csv', index=False)

# Display the first few rows of the combined DataFrame
print(combined_df.head())