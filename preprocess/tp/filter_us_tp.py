import pandas as pd

# File names
input_file = '../../datasets/tp/2015.csv'
output_file = '../../preprocess/tp/filtered_us_tp_2015.csv'

# Read the CSV file with only relevant columns
df = pd.read_csv(input_file, header=None, usecols=[0, 1, 2, 3], names=['station', 'date', 'type', 'value'])

# Filter rows where the station code starts with 'US' and type is relevant
filtered_df = df[
    (df['station'].str.startswith('US')) &
    (df['type'].isin(['PRCP', 'TMAX', 'TMIN', 'TAVG']))
]

# Pivot table to merge rows with the same station and date
merged_df = filtered_df.pivot(index=['station', 'date'], columns='type', values='value').reset_index()

# Convert 'date' column to datetime format and then to 'YYYY-MM-DD' string format
merged_df['date'] = pd.to_datetime(merged_df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')

# Reorder and keep only the desired columns
merged_df = merged_df[['station', 'date', 'TMIN', 'PRCP', 'TMAX', 'TAVG']]

merged_df = merged_df.rename(columns={'TMIN': 'tmin'})
merged_df = merged_df.rename(columns={'PRCP': 'prcp'})
merged_df = merged_df.rename(columns={'TMAX': 'tmax'})
merged_df = merged_df.rename(columns={'TAVG': 'tavg'})

# Export the merged data to a new CSV file
merged_df.to_csv(output_file, index=False)

print(f'Merged records exported to {output_file}')
