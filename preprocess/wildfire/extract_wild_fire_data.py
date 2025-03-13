import sqlite3
import pandas as pd

# Path to your SQLite database
db_path = '../../datasets/wildfire/FPA_FOD_20170508.sqlite'

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Write a SQL query to fetch the data
query = """
SELECT DISCOVERY_DATE, LATITUDE, LONGITUDE, FIPS_CODE, FIRE_SIZE, FIRE_SIZE_CLASS, STATE 
FROM Fires;
"""

# Load the query result into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Map state abbreviation to state FIPS code
state_fips_map = {
    'AL': '01', 'AK': '02', 'AZ': '04', 'AR': '05', 'CA': '06', 'CO': '08', 'CT': '09', 
    'DE': '10', 'FL': '12', 'GA': '13', 'HI': '15', 'ID': '16', 'IL': '17', 'IN': '18', 
    'IA': '19', 'KS': '20', 'KY': '21', 'LA': '22', 'ME': '23', 'MD': '24', 'MA': '25', 
    'MI': '26', 'MN': '27', 'MS': '28', 'MO': '29', 'MT': '30', 'NE': '31', 'NV': '32', 
    'NH': '33', 'NJ': '34', 'NM': '35', 'NY': '36', 'NC': '37', 'ND': '38', 'OH': '39', 
    'OK': '40', 'OR': '41', 'PA': '42', 'RI': '44', 'SC': '45', 'SD': '46', 'TN': '47', 
    'TX': '48', 'UT': '49', 'VT': '50', 'VA': '51', 'WA': '53', 'WV': '54', 'WI': '55', 
    'WY': '56'
}
# Filter out rows where FIPS_CODE is None or missing
df = df.dropna(subset=['FIPS_CODE'])

# Create the full FIPS code by combining state and county codes
df['FIPS_CODE'] = df['STATE'].map(state_fips_map) + df['FIPS_CODE'].astype(str).str.zfill(3)



# Save the DataFrame as a CSV file
output_csv_path = '../../processed_datasets/wildfire/wildfire.csv'
df.to_csv(output_csv_path, index=False)

print(f"Data has been extracted and saved to '{output_csv_path}'.")