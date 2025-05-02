# ALGORITHM 25: Drone State Initialization for Obstacle Detection
# --------------------------------------------------------------
# FRONTEND (Simulation + Plot)

import matplotlib.pyplot as plt

# Initialize drone position and heading
drone_position = (0.0, 0.0)  # (x, y) in meters
drone_heading_deg = 0        # in degrees (0 = facing right)

# Plot
plt.figure(figsize=(6, 6))
plt.title("Drone Initial State for Obstacle Detection - Algorithm 25")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.grid(True)

# Plot drone
plt.scatter(*drone_position, c='blue', s=100, label='Drone')
plt.text(drone_position[0]+0.2, drone_position[1]+0.2, "Drone", fontsize=9)

# Draw heading direction
arrow_length = 1.0
dx = arrow_length
dy = 0
plt.arrow(drone_position[0], drone_position[1], dx, dy, head_width=0.2, head_length=0.3, fc='green', ec='green', label='Heading')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.legend()
plt.tight_layout()
plt.show()

# --------------------------------------------------------------
# BACKEND (State Initialization)

def initialize_drone_state():
    print("\n🛠️ [Backend] Drone State Initialized for Obstacle Detection")
    print(f"Initial Position: X = {drone_position[0]} m, Y = {drone_position[1]} m")
    print(f"Initial Heading: {drone_heading_deg} degrees")

# Execute backend
initialize_drone_state()
