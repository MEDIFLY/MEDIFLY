import matplotlib.pyplot as plt
import math
import time

# ---------- Frontend (Simulation + Plot) ----------

print("\n📍 Frontend: Simulating Drone Navigation Method\n")

# Initial and Target GPS coordinates
initial_position = (0, 0)
target_position = (10, 10)

# Drone parameters
speed = 1  # units per step
navigation_path = [initial_position]
current_position = list(initial_position)

# Navigation using simple vector direction
for step in range(15):
    dx = target_position[0] - current_position[0]
    dy = target_position[1] - current_position[1]
    
    distance = math.sqrt(dx**2 + dy**2)
    if distance < 0.5:
        print(f"✅ Drone reached the target at step {step}")
        break

    # Normalize direction
    direction_x = dx / distance
    direction_y = dy / distance

    # Update position
    current_position[0] += direction_x * speed
    current_position[1] += direction_y * speed

    navigation_path.append(tuple(current_position))
    print(f"➡️ Step {step + 1}: Drone at {tuple(round(val, 2) for val in current_position)}")
    time.sleep(0.3)

# Plot the navigation path
x_vals = [point[0] for point in navigation_path]
y_vals = [point[1] for point in navigation_path]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'bo-', label='Navigation Path')
plt.scatter(initial_position[0], initial_position[1], color='green', s=100, label='Start')
plt.scatter(target_position[0], target_position[1], color='red', s=100, label='Target')
plt.title("Algorithm 31: Navigation Method")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# ---------- Backend (Hardware Logic) ----------

def navigation_method_backend(start, target, speed):
    print("\n🔧 Backend: Executing Drone Navigation Method\n")
    path = [start]
    current = list(start)

    for step in range(15):
        dx = target[0] - current[0]
        dy = target[1] - current[1]

        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance < 0.5:
            print(f"✅ Target reached at backend step {step}")
            break

        direction_x = dx / distance
        direction_y = dy / distance

        current[0] += direction_x * speed
        current[1] += direction_y * speed

        path.append(tuple(current))
        print(f"🔹 Backend Step {step + 1}: {tuple(round(val, 2) for val in current)}")
        time.sleep(0.2)

    return path

# Call backend logic
navigation_method_backend((0, 0), (10, 10), speed=1)
