# ALGORITHM 26: Obstacle State Initialization
# --------------------------------------------------------------
# FRONTEND (Simulation + Plot)

import matplotlib.pyplot as plt

# Drone initial position
drone_position = (0.0, 0.0)

# Obstacle initial position
obstacle_position = (2.5, 2.0)  # (x, y) in meters

# Plot setup
plt.figure(figsize=(6, 6))
plt.title("Obstacle and Drone Position - Algorithm 26")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)

# Plot drone
plt.scatter(*drone_position, c='blue', s=100, label='Drone')
plt.text(drone_position[0] + 0.2, drone_position[1] + 0.2, "Drone", fontsize=9)

# Plot obstacle
plt.scatter(*obstacle_position, c='red', s=100, label='Obstacle')
plt.text(obstacle_position[0] + 0.2, obstacle_position[1] + 0.2, "Obstacle", fontsize=9)

# Visual path line
plt.plot([drone_position[0], obstacle_position[0]], [drone_position[1], obstacle_position[1]], 'k--', label='Line of Sight')

plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.legend()
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# BACKEND (State Initialization)

def initialize_obstacle_state():
    print("\n🪨 [Backend] Obstacle State Initialized")
    print(f"Obstacle Position: X = {obstacle_position[0]} m, Y = {obstacle_position[1]} m")

# Execute backend
initialize_obstacle_state()
