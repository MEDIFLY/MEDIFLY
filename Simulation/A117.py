# A117.py – Takeoff Simulation (Frontend + Backend with Plots)
import matplotlib.pyplot as plt
import numpy as np
import random

# Simulation parameters
mass = 2.1  # kg
thrust = 18  # N
g = 9.81  # gravity m/s²
net_force = thrust - (mass * g)
acceleration = net_force / mass  # m/s²
iterations = 5
time_step = 1  # seconds per step
steps_per_iteration = 10

# Store altitude data for all 5 iterations
all_altitudes = []

print("🚀 Starting Takeoff Simulation...\n")

for i in range(iterations):
    velocity = 0
    altitude = 0
    altitudes = []

    print(f"🌀 Iteration {i+1}:")
    for step in range(steps_per_iteration):
        # Simulate wind disturbance
        wind_factor = random.uniform(-0.05, 0.05)
        velocity += (acceleration + wind_factor) * time_step
        altitude += velocity * time_step
        altitudes.append(altitude)

        print(f"⏱️ t={step+1}s → Altitude: {altitude:.2f} m | Velocity: {velocity:.2f} m/s")

    print("--------------------------------------------------")
    all_altitudes.append(altitudes)

# Plotting all 5 iterations
plt.figure(figsize=(10, 6))
for i in range(iterations):
    plt.plot(range(1, steps_per_iteration + 1), all_altitudes[i], label=f"Iteration {i+1}")

plt.title("🚁 Drone Takeoff Simulation - Altitude Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
