# AI Model 6: ANN-Based Trajectory Optimization

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

# FRONTEND: Simulate Trajectory Data
np.random.seed(0)

# Start and end positions
start = np.array([0, 0])
end = np.array([10, 10])

# Simulate flight path data with noise
x_points = np.linspace(start[0], end[0], 50)
y_points = x_points + np.random.normal(0, 1, 50)  # add deviation

# Combine into feature matrix
X = x_points.reshape(-1, 1)
y = y_points

# Train ANN model to learn this pattern
model = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=1000)
model.fit(X, y)

# Predict smooth trajectory
predicted_y = model.predict(X)

# Calculate error
mse = mean_squared_error(y, predicted_y)
print(f"Mean Squared Error: {mse:.4f}")

# Plot 1: Training Data vs ANN Prediction
plt.figure(figsize=(6, 4))
plt.scatter(X, y, color='blue', label='Noisy Data')
plt.plot(X, predicted_y, color='red', label='ANN Prediction')
plt.title("ANN Trajectory Optimization")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# BACKEND: Real-time simulation of UAV following predicted path
import time

print("\nSimulated UAV Position Updates:")
for i in range(0, len(X), 5):
    x_real = X[i][0]
    y_real = predicted_y[i]
    print(f"UAV Position → X: {x_real:.2f}, Y: {y_real:.2f}")
    time.sleep(0.2)  # simulate real-time update

# Plot 2: Full UAV Path from Start to End
plt.figure(figsize=(6, 4))
plt.plot(X, predicted_y, color='green', linestyle='--', marker='o')
plt.title("Optimized UAV Flight Path")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.tight_layout()
plt.show()
