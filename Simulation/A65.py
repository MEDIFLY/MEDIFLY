# A65.py - Algorithm 65: Prediction of Drop Offset Using AI Model

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Frontend Simulation (with plot) – 5 iterations
# --------------------------------------------------

# Simulated inputs: [wind_speed (m/s), altitude (m), velocity (m/s)]
test_inputs = np.array([
    [2.0,  100.0, 10.0],
    [3.5,  120.0, 12.0],
    [1.2,   80.0,  9.0],
    [4.1,  150.0, 13.5],
    [2.8,   90.0, 11.0]
])

# Expected outputs: drop_offset (m)
expected_offsets = np.array([5.5, 8.1, 4.2, 9.3, 6.7])

# Train the model (for simulation purposes)
model = LinearRegression()
model.fit(test_inputs, expected_offsets)

# Predict the drop offsets
predicted_offsets = model.predict(test_inputs)

# Print predictions (frontend output)
print("\n--- Drop Offset Predictions ---")
for i in range(5):
    print(f"Iteration {i+1}: Input = {test_inputs[i]} -> Predicted Drop Offset = {predicted_offsets[i]:.2f} m")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(range(1, 6), expected_offsets, 'go--', label='Actual Offset')
plt.plot(range(1, 6), predicted_offsets, 'ro-', label='Predicted Offset')
plt.title("AI Model Prediction vs Actual Drop Offset")
plt.xlabel("Iteration")
plt.ylabel("Drop Offset (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Backend Hardware Integration Logic
# --------------------------------------------------

# Simulated real-time drone data (would come from sensors in hardware)
def get_real_time_drone_data():
    # Example: values from onboard sensors
    wind_speed = 3.0      # in m/s
    altitude = 110.0      # in meters
    velocity = 11.5       # in m/s
    return np.array([[wind_speed, altitude, velocity]])

# Predict drop offset from real-time drone data
real_time_input = get_real_time_drone_data()
predicted_drop_offset = model.predict(real_time_input)[0]

# Output for hardware system
print("\n--- Backend AI Drop Offset Prediction ---")
print(f"Real-Time Input: {real_time_input.flatten()}")
print(f"Predicted Drop Offset = {predicted_drop_offset:.2f} meters")

# You would now use `predicted_drop_offset` to adjust your payload release point
