# ALGORITHM 24: Obstacle Detection Parameters
# -------------------------------------------
# FRONTEND (Simulation + Plot)

import matplotlib.pyplot as plt
import random

# Obstacle definitions
num_obstacles = 5
obstacle_positions = [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(num_obstacles)]
obstacle_size = 0.5  # in meters

# Plotting
plt.figure(figsize=(6, 6))
plt.title("Obstacle Positions - Algorithm 24")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

# Plot obstacles
for i, (x, y) in enumerate(obstacle_positions):
    plt.scatter(x, y, c='red')
    plt.text(x + 0.2, y + 0.2, f"O{i+1}", fontsize=8)

# Detection range for reference
detection_range = 4.0
drone_pos = (0, 0)
plt.scatter(*drone_pos, c='blue', label='Drone')
plt.gca().add_patch(plt.Circle(drone_pos, detection_range, fill=False, linestyle='--', color='blue', label='Detection Range'))

plt.legend()
plt.grid(True)
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.tight_layout()
plt.show()

# -------------------------------------------
# BACKEND (Obstacle Parameter Setup)

def initialize_obstacle_parameters():
    print("\n🛠️ [Backend] Obstacle Detection Parameters Initialized")
    print(f"Number of Obstacles: {num_obstacles}")
    print(f"Obstacle Size: {obstacle_size} m")
    print("Obstacle Positions (X, Y):")
    for i, pos in enumerate(obstacle_positions, 1):
        print(f"  Obstacle {i}: {pos}")

# Execute backend logic
initialize_obstacle_parameters()
