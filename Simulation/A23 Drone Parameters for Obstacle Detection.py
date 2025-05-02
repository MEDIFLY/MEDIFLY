# ALGORITHM 23: Drone Parameters for Obstacle Detection
# ------------------------------------------------------
# FRONTEND (Simulation + Plot)

import matplotlib.pyplot as plt

# Drone parameter definitions
drone_speed = 5.0  # meters/second
drone_altitude = 10.0  # meters
detection_range = 4.0  # meters

# Plotting detection range
plt.figure(figsize=(6, 6))
plt.title("Drone Detection Range - Algorithm 23")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

# Plot drone at origin
plt.scatter(0, 0, c='blue', label='Drone')

# Detection circle
detection_circle = plt.Circle((0, 0), detection_range, color='blue', fill=False, linestyle='--', label='Detection Range')
plt.gca().add_patch(detection_circle)

plt.legend()
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# BACKEND (Hardware Initialization Logic)

def set_drone_parameters():
    print("\n🛠️ [Backend] Drone Parameters Initialized for Obstacle Detection")
    print(f"Speed: {drone_speed} m/s")
    print(f"Altitude: {drone_altitude} meters")
    print(f"Detection Range: {detection_range} meters")

# Execute backend
set_drone_parameters()
