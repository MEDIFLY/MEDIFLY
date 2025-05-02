# AI Model 7: AI-Powered Obstacle Detection and Avoidance

import matplotlib.pyplot as plt
import numpy as np
import random
import time

# FRONTEND: Simulate UAV and obstacles in 2D space
uav_position = np.array([0, 0])
destination = np.array([10, 10])

# Random obstacle generation (x, y, radius)
obstacles = [
    {"pos": np.array([3, 4]), "r": 1.5},
    {"pos": np.array([6, 6]), "r": 1.2},
    {"pos": np.array([8, 9]), "r": 1.0}
]

# Function to detect obstacle in path
def is_path_blocked(uav_pos, next_pos, obstacle):
    dist = np.linalg.norm(next_pos - obstacle["pos"])
    return dist < obstacle["r"] + 0.5  # 0.5 as buffer

# Path planning with basic avoidance
path = [uav_position.copy()]
step = 0.5
current = uav_position.copy()

while np.linalg.norm(destination - current) > step:
    direction = destination - current
    direction = direction / np.linalg.norm(direction)
    next_pos = current + step * direction
    
    blocked = False
    for obs in obstacles:
        if is_path_blocked(current, next_pos, obs):
            print(f"Obstacle detected at {obs['pos']} → Re-routing...")
            # Simple avoidance: sidestep on y-axis
            next_pos[1] += random.choice([-1, 1]) * obs["r"]
            break
    
    current = next_pos
    path.append(current.copy())

# Convert path to X, Y
path = np.array(path)
x_path, y_path = path[:, 0], path[:, 1]

# Plot 1: Obstacle Map and Avoided Path
plt.figure(figsize=(6, 6))
plt.plot(x_path, y_path, 'g--o', label='UAV Path')
for obs in obstacles:
    circle = plt.Circle(obs["pos"], obs["r"], color='red', alpha=0.4)
    plt.gca().add_patch(circle)
    plt.plot(*obs["pos"], 'rx')
plt.plot(*uav_position, 'bo', label='Start')
plt.plot(*destination, 'ko', label='End')
plt.title("Obstacle Detection and Avoidance Path")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.tight_layout()
plt.show()

# BACKEND: Log decisions and re-routing
print("\n--- UAV Flight Decision Log ---")
for i in range(len(x_path)-1):
    print(f"Step {i+1}: Moving to ({x_path[i+1]:.2f}, {y_path[i+1]:.2f})")
    time.sleep(0.1)
