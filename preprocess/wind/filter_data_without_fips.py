import pandas as pd

# Load the CSV file
df = pd.read_csv('./fips_wind_no_na.csv')

# Filter rows where 'fips' is not missing
filtered_df = df[df['fips'].notna()]

filtered_df.to_csv('fips_wind_no_na.csv', index=False)

print("Filtered data saved to 'fips_wind_no_na.csv'")