# ALGORITHM 27: Obstacle Detection Function
# --------------------------------------------------------------
# FRONTEND (Simulation + Plot)

import matplotlib.pyplot as plt
import math

# Drone and obstacle positions
drone_position = (0.0, 0.0)
obstacle_position = (2.5, 2.0)

# Detection radius
detection_radius = 3.0  # meters

# Distance calculation
distance = math.sqrt((drone_position[0] - obstacle_position[0])**2 +
                     (drone_position[1] - obstacle_position[1])**2)

# Plot setup
plt.figure(figsize=(6, 6))
plt.title("Algorithm 27: Obstacle Detection Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)

# Plot drone
plt.scatter(*drone_position, c='blue', s=100, label='Drone')
plt.text(drone_position[0] + 0.2, drone_position[1] + 0.2, "Drone")

# Plot obstacle
plt.scatter(*obstacle_position, c='red', s=100, label='Obstacle')
plt.text(obstacle_position[0] + 0.2, obstacle_position[1] + 0.2, "Obstacle")

# Plot detection zone
circle = plt.Circle(drone_position, detection_radius, color='cyan', alpha=0.2, label='Detection Radius')
plt.gca().add_patch(circle)

# Plot line between drone and obstacle
plt.plot([drone_position[0], obstacle_position[0]], [drone_position[1], obstacle_position[1]],
         'gray', linestyle='--')

# Check if obstacle is detected
if distance <= detection_radius:
    plt.text(0.5, 4.5, "Obstacle Detected!", fontsize=12, color='green')
else:
    plt.text(0.5, 4.5, "No Obstacle in Range", fontsize=12, color='red')

plt.legend()
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# BACKEND (Obstacle Detection Logic)

def detect_obstacle(drone_pos, obstacle_pos, radius):
    dist = math.sqrt((drone_pos[0] - obstacle_pos[0])**2 +
                     (drone_pos[1] - obstacle_pos[1])**2)
    if dist <= radius:
        print("✅ [Backend] Obstacle Detected within radius!")
        return True
    else:
        print("❌ [Backend] No obstacle detected.")
        return False

# Execute backend
detect_obstacle(drone_position, obstacle_position, detection_radius)
