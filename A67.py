# A67.py – Algorithm 67: Execution of Optimal Drop Point Calculation

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Frontend Simulation + Visualization
# ------------------------------

# Step 1: Simulate drone's current positions (x, y)
drone_positions = np.array([
    [100.0, 50.0],
    [150.0, 60.0],
    [200.0, 55.0],
    [250.0, 58.0],
    [300.0, 53.0]
])

# Step 2: Simulate AI predicted drop offsets (in meters)
predicted_offsets = np.array([5.5, 8.0, 4.5, 7.2, 6.1])

# Step 3: Function to calculate drop point
def calculate_drop_point(position, offset):
    return position + np.array([offset, 0.0])  # motion along +x

# Step 4: Loop for 5 iterations
print("\n--- Frontend Execution of Optimal Drop Point Calculation ---")
drop_points = []
for i in range(5):
    drone_pos = drone_positions[i]
    offset = predicted_offsets[i]
    drop_point = calculate_drop_point(drone_pos, offset)
    drop_points.append(drop_point)
    print(f"Iteration {i+1}: Drone Pos = {drone_pos}, Offset = {offset} → Drop Point = {drop_point}")

# Convert list to array for plotting
drop_points = np.array(drop_points)

# Step 5: Plot the drone path and drop points
plt.figure(figsize=(8, 5))
plt.plot(drone_positions[:, 0], drone_positions[:, 1], 'bo-', label='Drone Positions')
plt.plot(drop_points[:, 0], drop_points[:, 1], 'ro--', label='Drop Points')
plt.title("Optimal Drop Point Execution - Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------
# Backend Hardware Integration
# ------------------------------

# Get real-time drone GPS position (simulated)
def get_drone_position():
    return np.array([180.0, 54.0])  # example GPS in meters

# Get predicted offset from AI model (simulated)
def get_offset_from_ai():
    return 6.7  # in meters

# Execute full logic
def execute_optimal_drop_point():
    current_pos = get_drone_position()
    offset = get_offset_from_ai()
    drop_point = calculate_drop_point(current_pos, offset)
    return current_pos, offset, drop_point

# Run backend
print("\n--- Backend Execution ---")
curr, offs, final_drop = execute_optimal_drop_point()
print(f"Real-Time Drone Pos: {curr}")
print(f"Predicted Offset: {offs} m")
print(f"Computed Drop Point: {final_drop}")
