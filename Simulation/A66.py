# A66.py – Algorithm 66: Calculation of Exact Drop Point

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ------------------------------
# Frontend Simulation + Plotting
# ------------------------------

# Simulated drone positions (x, y) in meters
drone_positions = np.array([
    [100.0, 50.0],
    [150.0, 60.0],
    [200.0, 55.0],
    [250.0, 58.0],
    [300.0, 53.0]
])

# Simulated AI model predicted drop offsets
drop_offsets = np.array([5.5, 8.0, 4.5, 7.2, 6.1])

# Calculate exact drop points (assuming motion along +x)
drop_points = drone_positions + np.column_stack((drop_offsets, np.zeros(5)))

# Print all values
print("\n--- Drop Point Calculation (Frontend Simulation) ---")
for i in range(5):
    print(f"Iteration {i+1}: Drone Position = {drone_positions[i]}, Offset = {drop_offsets[i]} -> Drop Point = {drop_points[i]}")

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(drone_positions[:, 0], drone_positions[:, 1], 'bo-', label='Drone Position')
plt.plot(drop_points[:, 0], drop_points[:, 1], 'ro--', label='Drop Point')
plt.title("Drone Path and Payload Drop Points")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------
# Backend Hardware Integration
# ------------------------------

# Simulated real-time drone position (from GPS module)
def get_current_drone_position():
    x = 180.0  # meters
    y = 54.0   # meters
    return np.array([x, y])

# Simulated AI-predicted drop offset (from previous algorithm)
def get_ai_predicted_offset():
    return 6.7  # meters

# Calculate exact drop point in real-time
current_position = get_current_drone_position()
predicted_offset = get_ai_predicted_offset()

# Assuming straight flight along x-axis
exact_drop_point = current_position + np.array([predicted_offset, 0.0])

# Output drop point for hardware targeting system
print("\n--- Backend Drop Point Calculation ---")
print(f"Current Drone Position: {current_position}")
print(f"Predicted Offset: {predicted_offset} m")
print(f"Exact Drop Point: {exact_drop_point}")
