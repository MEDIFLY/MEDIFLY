# A68.py – Algorithm 68: Precise Payload Dropping

import numpy as np
import matplotlib.pyplot as plt
import time

# ------------------------------
# Frontend Simulation + Visualization
# ------------------------------

# Step 1: Simulated drone drop points (same as A67)
drop_points = np.array([
    [105.5, 50.0],
    [158.0, 60.0],
    [204.5, 55.0],
    [257.2, 58.0],
    [306.1, 53.0]
])

# Step 2: Simulate drop accuracy (small deviation from actual drop point)
def simulate_drop(drone_drop_point):
    deviation = np.random.uniform(-0.5, 0.5, size=2)  # random deviation
    actual_drop_point = drone_drop_point + deviation
    return actual_drop_point

# Step 3: Run 5 iterations
actual_drops = []
print("\n--- Frontend: Simulated Precise Payload Dropping ---")
for i in range(5):
    target = drop_points[i]
    actual = simulate_drop(target)
    actual_drops.append(actual)
    print(f"Iteration {i+1}: Target Drop Point = {target}, Actual Drop = {actual}")

actual_drops = np.array(actual_drops)

# Step 4: Plot drop points and actual drops
plt.figure(figsize=(8, 5))
plt.plot(drop_points[:, 0], drop_points[:, 1], 'go-', label='Target Drop Points')
plt.plot(actual_drops[:, 0], actual_drops[:, 1], 'rx--', label='Actual Drops')
plt.title("Precise Payload Dropping - Simulation")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------
# Backend Hardware Integration
# ------------------------------

# Step 1: Simulated drop trigger function
def trigger_payload_drop():
    print("→ Servo activated: Releasing medicine payload...")
    time.sleep(1)  # simulate hardware delay
    print("✔ Payload released successfully.")

# Step 2: Check if drone has reached the drop point
def has_reached_drop_point(current_pos, drop_point, tolerance=0.5):
    distance = np.linalg.norm(current_pos - drop_point)
    return distance <= tolerance

# Step 3: Run backend logic
print("\n--- Backend: Precise Payload Drop Execution ---")
simulated_drone_position = np.array([204.6, 55.2])  # very close to drop point
target_drop_point = np.array([204.5, 55.0])

if has_reached_drop_point(simulated_drone_position, target_drop_point):
    trigger_payload_drop()
else:
    print("✖ Drone has not yet reached drop point. Holding drop mechanism.")
