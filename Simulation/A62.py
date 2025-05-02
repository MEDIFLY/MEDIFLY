# ----------------------------------------------------
# Algorithm 62: Function to Calculate Optimal Drop Point
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =======================
# FRONTEND: Simulation
# =======================

# Simulate drone parameters (same as before)
drone_params = {
    "altitude": 15.0,  # in meters
    "velocity": 8.0,  # in m/s
    "wind_speed": 4.0,  # in m/s
}

# Optimal drop point calculation function
def calculate_optimal_drop_point(drop_offset, drone_params):
    """Calculate the optimal drop point based on the drop offset."""
    # Simulate the horizontal displacement (distance) based on drop offset
    horizontal_displacement = drop_offset * np.cos(np.radians(30))  # Using 30-degree release angle
    vertical_displacement = drone_params["altitude"] * np.sin(np.radians(30))  # Vertical displacement
    
    # The final optimal drop point coordinates (x, y)
    drop_point = (horizontal_displacement, vertical_displacement)
    return drop_point

# Simulate drop offset prediction for 5 iterations
drop_offsets = []
optimal_drop_points = []

for i in range(5):
    # Simulate slight changes in drone parameters
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)
    
    # Simulate drop offset calculation from the AI model (simplified here)
    drop_offset = (drone_params["wind_speed"] * 0.7 + drone_params["altitude"] * 0.5 + drone_params["velocity"] * 0.3)
    drop_offsets.append(drop_offset)
    
    # Calculate the optimal drop point based on the predicted drop offset
    drop_point = calculate_optimal_drop_point(drop_offset, drone_params)
    optimal_drop_points.append(drop_point)
    print(f"Iteration {i+1}: Drop Offset = {drop_offset:.2f} meters, Optimal Drop Point = {drop_point}")

# 🎨 Plot the optimal drop points over iterations
plt.figure(figsize=(10, 5))

# Plotting the optimal drop points
x_points = [point[0] for point in optimal_drop_points]
y_points = [point[1] for point in optimal_drop_points]
plt.plot(x_points, y_points, 'bo-', label="Optimal Drop Points")
plt.title("Optimal Drop Points Over Iterations")
plt.xlabel("Horizontal Displacement (meters)")
plt.ylabel("Vertical Displacement (meters)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Optimal Drop Point Calculation:")

# Simulate optimal drop point calculation for backend integration
for i in range(5):
    # Calculate the drop offset (simplified)
    drop_offset = (drone_params["wind_speed"] * 0.7 + drone_params["altitude"] * 0.5 + drone_params["velocity"] * 0.3)
    
    # Calculate the optimal drop point based on drop offset
    optimal_drop_point = calculate_optimal_drop_point(drop_offset, drone_params)
    
    # Simulate real-time changes to drone parameters
    drone_params["altitude"] += np.random.uniform(-0.5, 0.5)
    drone_params["velocity"] += np.random.uniform(-1.0, 1.0)
    drone_params["wind_speed"] += np.random.uniform(-2.0, 2.0)
    
    print(f"[BACKEND] Iteration {i+1}: Drop Offset = {drop_offset:.2f} meters, Optimal Drop Point = {optimal_drop_point}")

print("\n✅ Optimal Drop Point Calculation Processed Successfully.")
