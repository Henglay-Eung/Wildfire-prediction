import pandas as pd
import joblib

# Load the trained model and scaler
model_filename = 'fire_size_model.pkl'
scaler_filename = 'scaler.pkl'
model = joblib.load(model_filename)
scaler = joblib.load(scaler_filename)

# Load new data for testing
new_data = pd.read_csv('./test_data.csv')  # Replace with the path to your new data

# Preprocess the new data (ensure it matches the training data format)
# Convert the 'date' column to datetime format
new_data['date'] = pd.to_datetime(new_data['date'])

# Option 1: Convert 'date' to timestamp (number of seconds since the epoch)
new_data['date'] = new_data['date'].astype(int) / 10**9  # Convert to seconds

# Option 2: Extract features such as year, month, day from 'date' (if used during training)
# new_data['year'] = new_data['date'].dt.year
# new_data['month'] = new_data['date'].dt.month
# new_data['day'] = new_data['date'].dt.day

# Select the same features used during training
X_new = new_data[['date', 'percent', 'fips', 'tmax', 'tmin', 'tavg', 'prcp', 'wind_u', 'wind_v', 'aws']]

# Standardize the new data using the same scaler
X_new_scaled = scaler.transform(X_new)

# Make predictions
predictions = model.predict(X_new_scaled)

# Add predictions to the new data DataFrame
new_data['predicted_fire_size'] = predictions

# Save the results to a new CSV file
