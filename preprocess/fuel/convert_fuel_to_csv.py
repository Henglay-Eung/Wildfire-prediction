import pandas as pd
import os

# Define the relative path to the file
relative_path = '../../datasets/fuel/fuel_with_fips.xlsx'

# Convert the relative path to an absolute path
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
input_file = os.path.join(base_dir, relative_path)

# Check if the file exists
if not os.path.exists(input_file):
    print(f"Error: File not found at {input_file}")
    exit(1)

# Read the .xlsx file
df = pd.read_excel(input_file)

# Drop the "Unnamed: 0" column (if it exists)
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Specify the output .csv file path
output_file = os.path.join(base_dir, '../../processed_datasets/fuel/fuel.csv')

# Save the DataFrame to a .csv file
df.to_csv(output_file, index=False)

print(f"File '{input_file}' has been converted to '{output_file}'.")