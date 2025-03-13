import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load your data
print("+++++++++++++ loading data")
data = pd.read_csv('./test_data.csv')

# Convert numeric columns to proper numeric format
print("+++++++++++++ converting columns to numeric format")
data[['tmax', 'tmin', 'tavg', 'wind_u', 'wind_v', 'percent', 'aws', 'prcp']] = data[['tmax', 'tmin', 'tavg', 'wind_u', 'wind_v', 'percent', 'aws', 'prcp']].apply(pd.to_numeric, errors='coerce')

# Handle missing values (replace NaNs with 0)
# print("+++++++++++++ handling missing values")
# data = data.fillna(0)

# Extract the features and target variables
print("+++++++++++++ Extracting features")
X = data[['tmax', 'tmin', 'tavg', 'wind_u', 'wind_v', 'percent', 'aws', 'percent']]  # Example features
y = data['fire_size']  # Target variable

# Check for NaN in X and y
# if X.isnull().sum().any() or y.isnull().sum() > 0:
#     print("Warning: Missing values in the data. Filling NaNs...")
#     X = X.fillna(method='ffill')  # Fill NaN in features
#     y = y.fillna(method='ffill')  # Fill NaN in target

# Scale the features
print("+++++++++++++ Scaling features ")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Build a simple feedforward neural network model
model = Sequential()

# Define the model
model = Sequential()
model.add(Dense(64, input_dim=X_scaled.shape[1], activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))  # Explicitly set linear activation

print("+++++++++++++ Compiling model")
# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

import joblib
joblib.dump(scaler, 'scaler.pkl')


# Train the model
print("+++++++++++++ Training model")
history = model.fit(X_scaled, y, epochs=2000, batch_size=32)  

# Make predictions on the entire dataset
print("+++++++++++++ Predicting")
y_pred = model.predict(X_scaled)

# Check for NaN values in predictions
if np.isnan(y_pred).any():
    print("Warning: NaN values in the predictions")

# Evaluate performance: Mean Squared Error and R-squared
print("+++++++++++++ Calculating mse")
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")

# Optional: Plot training loss over epochs
# import matplotlib.pyplot as plt
# plt.plot(history.history['loss'], label='Train Loss')
# plt.xlabel('Epochs')
# plt.ylabel('Loss')
# plt.legend()
# plt.show()

# Save the model (optional)
model.save('wildfire_predictor_model_tensorflow.h5')
