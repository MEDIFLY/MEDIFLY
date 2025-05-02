# AI Model 11: AI-Based Precision Payload Drop

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulate UAV flight path and drop conditions
n = 50
time = np.linspace(0, 10, n)
uav_position = np.array([np.sin(time), np.cos(time)])  # UAV path in 2D (x, y)
payload_weight = 5  # in kilograms
wind_speed = 15  # in km/h
wind_direction = np.pi / 4  # in radians (45 degrees)

# Calculate drop point based on UAV position and wind effect
wind_effect = wind_speed * np.array([np.cos(wind_direction), np.sin(wind_direction)])
drop_point = uav_position[:, -1] + wind_effect  # Adding wind effect to the last position

# Compensation for UAV weight and center of gravity (simplified)
uav_weight = 10  # in kilograms
center_of_gravity_offset = payload_weight / uav_weight * 0.1  # a simplified factor
adjusted_drop_point = drop_point + center_of_gravity_offset

# BACKEND: Output final drop point and adjust flight path
print(f"Calculated Drop Point (before adjustment): {drop_point}")
print(f"Adjusted Drop Point (with wind and CG compensation): {adjusted_drop_point}")

# Plot 1: UAV Path and Drop Points
plt.figure(figsize=(8, 6))
plt.plot(uav_position[0], uav_position[1], label='UAV Path', color='blue')
plt.scatter(drop_point[0], drop_point[1], color='red', label='Drop Point (Raw)')
plt.scatter(adjusted_drop_point[0], adjusted_drop_point[1], color='green', label='Adjusted Drop Point')
plt.title("UAV Path and Payload Drop Points")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Wind Effect and Drop Point Adjustment
plt.figure(figsize=(8, 4))
plt.quiver(uav_position[0, -1], uav_position[1, -1], wind_effect[0], wind_effect[1], angles='xy', scale_units='xy', scale=1, color='orange')
plt.scatter(adjusted_drop_point[0], adjusted_drop_point[1], color='green', label='Adjusted Drop Point')
plt.title("Wind Effect and Drop Point Adjustment")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
