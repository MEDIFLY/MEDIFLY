import matplotlib.pyplot as plt
import numpy as np
import time

# Simulation parameters
target_height = 5.0  # meters
tolerance = 0.5
dt = 0.1  # time step (seconds)
simulation_time = 10  # seconds
iterations = 5

# PID parameters
Kp = 1.2
Ki = 0.01
Kd = 0.4

# Simulation loop
for i in range(iterations):
    print(f"\n🌀 PID Hover Simulation Iteration {i+1}")
    
    height = 0
    velocity = 0
    integral = 0
    previous_error = 0

    times = []
    heights = []

    for t in np.arange(0, simulation_time, dt):
        error = target_height - height
        integral += error * dt
        derivative = (error - previous_error) / dt
        thrust = Kp * error + Ki * integral + Kd * derivative

        velocity += thrust * dt
        height += velocity * dt
        previous_error = error

        times.append(t)
        heights.append(height)

        # Show current simulated height
        print(f"Time {round(t,1)}s → Altitude: {round(height,2)} m")

        time.sleep(0.05)

    # Plotting the hover profile
    plt.plot(times, heights, label=f"Iteration {i+1}")

plt.axhline(y=target_height, color='r', linestyle='--', label="Target Height")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Drone Hover Control using PID")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import random

def check_hover_status(current_height, target_height, tolerance):
    if abs(current_height - target_height) <= tolerance:
        return "🟢 Hover Stable"
    elif current_height < target_height:
        return "🔼 Ascending..."
    else:
        return "🔽 Descending..."

# Simulated backend hover control for 5 iterations
print("\n🛠️ Backend Hover Control System Check:")
for i in range(5):
    current_height = round(random.uniform(4.3, 5.7), 2)
    status = check_hover_status(current_height, target_height, tolerance)
    print(f"Iteration {i+1}: Current Height = {current_height} m → {status}")
    time.sleep(0.5)
