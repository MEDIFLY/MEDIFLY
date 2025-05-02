# ----------------------------------------------------
# Algorithm 64: Instantiation of AI Model
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# =======================
# FRONTEND: Simulation
# =======================

# Define a mock dataset for training the AI model (simplified)
# This dataset simulates the relationship between input parameters and drop offset
X = np.array([
    [1.5, 0.5, 100.0, 10.0, 5.0, 25.0],  # Example: [drone_weight, payload_weight, drop_height, drop_speed, wind_speed, temperature]
    [1.7, 0.6, 110.0, 11.0, 6.0, 24.0],
    [1.6, 0.55, 105.0, 9.0, 4.5, 26.0],
    [1.8, 0.45, 120.0, 12.0, 5.5, 22.0],
    [1.9, 0.4, 130.0, 10.5, 5.2, 23.0]
])

y = np.array([5.0, 6.0, 4.5, 6.5, 7.0])  # Example: drop offset (target value)

# Instantiate the AI model (Linear Regression)
ai_model = LinearRegression()

# Train the AI model on the mock dataset
ai_model.fit(X, y)

# Simulate the input parameters for prediction
input_data = np.array([
    [1.6, 0.55, 110.0, 11.0, 5.5, 25.0],  # New drone parameters to predict drop offset
    [1.7, 0.6, 120.0, 10.5, 5.2, 24.0],
    [1.5, 0.5, 100.0, 9.5, 6.0, 26.0],
    [1.8, 0.4, 130.0, 12.0, 5.7, 23.0],
    [1.9, 0.45, 140.0, 10.5, 5.3, 22.5]
])

# Make predictions based on the new input data
predictions = ai_model.predict(input_data)

# 🎨 Plot the AI model predictions vs actual drop offsets
plt.figure(figsize=(10, 5))

# Plotting the actual vs predicted drop offsets
plt.plot(range(1, 6), y, 'bo-', label="Actual Drop Offsets")
plt.plot(range(1, 6), predictions, 'ro-', label="Predicted Drop Offsets")

plt.title("AI Model Predictions vs Actual Drop Offsets")
plt.xlabel("Iteration")
plt.ylabel("Drop Offset (meters)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: AI Model Instantiation:")

# Simulate backend logic for using the AI model
for i in range(5):
    # Using the AI model to predict drop offset
    prediction = ai_model.predict(input_data[i].reshape(1, -1))
    print(f"[BACKEND] Iteration {i+1}: Predicted Drop Offset = {prediction[0]:.2f} meters")

print("\n✅ AI Model Instantiated and Predictions Generated Successfully.")
