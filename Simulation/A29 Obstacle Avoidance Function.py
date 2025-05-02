# ALGORITHM 29: Obstacle Avoidance Function – Combined

import random
import matplotlib.pyplot as plt

# Simulated drone and obstacle positions
drone_positions = []
obstacle_positions = []
avoidance_actions = []

# ---------- Backend: Obstacle Avoidance Logic ----------
print("----- Obstacle Avoidance Execution (Backend) -----")

for i in range(5):
    # Random positions
    drone_x = random.randint(0, 50)
    drone_y = random.randint(0, 50)
    obs_x = drone_x + random.choice([-5, 0, 5])
    obs_y = drone_y + random.choice([-5, 0, 5])

    # Store for plotting
    drone_positions.append((drone_x, drone_y))
    obstacle_positions.append((obs_x, obs_y))

    # Simple avoidance logic
    if abs(drone_x - obs_x) <= 5 and abs(drone_y - obs_y) <= 5:
        action = "Avoided"
    else:
        action = "No Action"

    avoidance_actions.append(action)

    print(f"Iteration {i+1}: Drone at ({drone_x},{drone_y}) | Obstacle at ({obs_x},{obs_y}) => {action}")

# ---------- Frontend: Plotting the Avoidance ----------
plt.figure(figsize=(8, 6))

for i in range(5):
    drone = drone_positions[i]
    obs = obstacle_positions[i]
    color = 'red' if avoidance_actions[i] == "Avoided" else 'green'

    # Drone point
    plt.scatter(drone[0], drone[1], color='blue', label='Drone' if i == 0 else "")
    # Obstacle point
    plt.scatter(obs[0], obs[1], color='black', label='Obstacle' if i == 0 else "")
    # Connect them
    plt.plot([drone[0], obs[0]], [drone[1], obs[1]], linestyle='--', color=color)

plt.title("Algorithm 29: Obstacle Avoidance Visualization")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
