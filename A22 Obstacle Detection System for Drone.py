import random
import matplotlib.pyplot as plt

# ---------------- BACKEND: Obstacle Detection Logic ----------------
def generate_obstacles(num_obstacles=5):
    obstacles = []
    for _ in range(num_obstacles):
        x = random.uniform(1, 9)
        y = random.uniform(1, 9)
        distance = round(random.uniform(1, 5), 2)  # in meters
        obstacles.append({'x': x, 'y': y, 'distance': distance})
    return obstacles

def detect_nearby_obstacles(obstacles, threshold=3):
    nearby = [obs for obs in obstacles if obs['distance'] <= threshold]
    return nearby

# ---------------- FRONTEND: Obstacle Detection Plot ----------------
def simulate_obstacle_detection_plot(obstacles, nearby):
    fig, ax = plt.subplots(figsize=(8, 6))
    drone_pos = (5, 5)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Drone Obstacle Detection System", fontsize=14)
    
    # Plot drone
    ax.plot(*drone_pos, 'bo', markersize=12, label="Drone")

    # Plot obstacles
    for obs in obstacles:
        color = 'red' if obs in nearby else 'green'
        ax.plot(obs['x'], obs['y'], 'o', color=color, markersize=10)
        ax.text(obs['x'] + 0.2, obs['y'], f"{obs['distance']}m", fontsize=9)

    ax.legend()
    ax.grid(True)
    plt.show()

# ---------------- EXECUTION ----------------
print("🔍 Scanning for obstacles...")
obstacles = generate_obstacles()
nearby = detect_nearby_obstacles(obstacles)

if nearby:
    print(f"⚠️ Nearby Obstacles Detected (within 3m):")
    for i, obs in enumerate(nearby, 1):
        print(f"  {i}. Location=({round(obs['x'],1)}, {round(obs['y'],1)}), Distance={obs['distance']}m")
else:
    print("✅ No nearby obstacles detected.")

simulate_obstacle_detection_plot(obstacles, nearby)
