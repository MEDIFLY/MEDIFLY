# AI Model 16: Hybrid AI Networks for UAV Operations

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor

# FRONTEND: Simulate hybrid AI network control for UAV operations
n = 100
time = np.linspace(0, 10, n)

# Simulate UAV sensor data (position, speed, environmental factors)
uav_position = np.sin(time) * 100  # Simulated position data (x-axis)
uav_speed = np.cos(time) * 10  # Simulated speed data (m/s)
env_factors = np.random.normal(0, 2, n)  # Simulated environmental noise

# Combine the data for input to hybrid AI networks
inputs = np.column_stack((uav_position, uav_speed, env_factors))

# Hybrid AI networks: A combination of Neural Network and Random Forest for control
nn = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000)
rf = RandomForestRegressor(n_estimators=100)

# Train the models on the data
nn.fit(inputs, uav_position + uav_speed)  # Neural Network to predict control command
rf.fit(inputs, uav_position + uav_speed)  # Random Forest for another prediction approach

# Predictions from the models
nn_predictions = nn.predict(inputs)
rf_predictions = rf.predict(inputs)

# BACKEND: Real-time decision-making and optimization
def optimize_decision(nn_pred, rf_pred):
    # Combine the results from both models and choose the best option
    return (nn_pred + rf_pred) / 2  # Simple hybrid model output

hybrid_decision = optimize_decision(nn_predictions, rf_predictions)

# Print status of the AI network predictions and decision
print(f"Final Neural Network Prediction: {nn_predictions[-1]:.2f}")
print(f"Final Random Forest Prediction: {rf_predictions[-1]:.2f}")
print(f"Hybrid Decision Output: {hybrid_decision[-1]:.2f}")

# Plot 1: UAV Position and Speed Over Time
plt.figure(figsize=(8, 4))
plt.plot(time, uav_position, label='UAV Position', color='blue')
plt.plot(time, uav_speed, label='UAV Speed', color='red')
plt.title("UAV Position and Speed")
plt.xlabel("Time (s)")
plt.ylabel("Position / Speed")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Hybrid AI Network Predictions vs Actual Data
plt.figure(figsize=(8, 4))
plt.plot(time, nn_predictions, label='Neural Network Prediction', color='green')
plt.plot(time, rf_predictions, label='Random Forest Prediction', color='orange')
plt.plot(time, hybrid_decision, label='Hybrid Decision', color='purple')
plt.title("Hybrid AI Network Predictions")
plt.xlabel("Time (s)")
plt.ylabel("Predicted Control Output")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
