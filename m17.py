# AI Model 17: High-Speed Vision for Obstacle Avoidance

import numpy as np
import matplotlib.pyplot as plt
import cv2

# FRONTEND: Simulate high-speed vision system for obstacle detection
n = 100
time = np.linspace(0, 10, n)

# Simulated UAV camera feed (random noise for obstacles in the environment)
camera_feed = np.random.normal(0, 0.5, (n, 2))  # Simulating 2D image data (X, Y positions)
obstacle_positions = np.random.randint(0, 100, size=(5, 2))  # Random positions for obstacles

# Simulated UAV movement data (position and velocity)
uav_position = np.sin(time) * 50
uav_velocity = np.cos(time) * 5

# BACKEND: Obstacle detection and collision avoidance
def detect_obstacles(feed, obstacles):
    detected = []
    for obstacle in obstacles:
        # Simple detection by checking if obstacles are in the vicinity of the UAV's path
        if any(np.all(np.abs(feed - obstacle) < 5, axis=1)):  # Considered detected if close enough
            detected.append(obstacle)
    return detected

# Detect obstacles from the simulated feed
detected_obstacles = detect_obstacles(camera_feed, obstacle_positions)

# Calculate avoidance path (simple path deviation for demonstration)
def avoid_collision(uav_pos, obstacles):
    avoidance_path = []
    for obstacle in obstacles:
        if np.any(np.abs(uav_pos - obstacle) < 5):  # If close to an obstacle
            avoidance_path.append([uav_pos[0] + 10, uav_pos[1] + 10])  # Deviate position
        else:
            avoidance_path.append(uav_pos)
    return avoidance_path

avoidance_path = avoid_collision(uav_position, detected_obstacles)

# Print the detected obstacles and avoidance path
print(f"Detected Obstacles: {detected_obstacles}")
print(f"Avoidance Path: {avoidance_path[:10]}...")

# Plot 1: UAV Movement and Obstacle Detection
plt.figure(figsize=(8, 4))
plt.plot(uav_position, label='UAV Position', color='blue')
plt.scatter([obstacle[0] for obstacle in detected_obstacles], [obstacle[1] for obstacle in detected_obstacles], 
            color='red', label='Detected Obstacles')
plt.title("UAV Movement and Detected Obstacles")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Avoidance Path vs Original Path
plt.figure(figsize=(8, 4))
plt.plot(uav_position, label='Original UAV Path', color='blue')
plt.plot(avoidance_path, label='Avoidance Path', color='green', linestyle='dashed')
plt.title("UAV Path Before and After Avoidance")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
