# ----------------------------------------------------
# Algorithm 52: Update Drone State for Hover
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random

# =======================
# FRONTEND: Simulation
# =======================

# Drone State Parameters
target_altitude = 10.0
current_altitude = round(random.uniform(8.0, 12.0), 2)
current_velocity = 0.0  # Starting velocity (m/s)

# PID Constants
kp = 0.5
ki = 0.1
kd = 0.01

# Time step (simulation)
dt = 0.1  # seconds (each iteration is 0.1 seconds)

def update_drone_state(pid_output, current_altitude, current_velocity, dt):
    """Update drone altitude and velocity based on PID output (thrust)."""
    # Update velocity based on thrust (simplified dynamics)
    new_velocity = current_velocity + pid_output * dt
    
    # Update altitude based on velocity
    new_altitude = current_altitude + new_velocity * dt

    return new_altitude, new_velocity

# Simulation loop
altitudes = [current_altitude]
velocities = [current_velocity]
errors = []
pid_outputs = []
sum_error = 0
prev_error = 0

print("🎮 FRONTEND: Updating Drone State for Hover:")

for i in range(5):
    error = target_altitude - current_altitude
    sum_error += error
    pid_output = kp * error + ki * sum_error + kd * (error - prev_error)

    # Update state
    current_altitude, current_velocity = update_drone_state(pid_output, current_altitude, current_velocity, dt)

    # Store results for visualization
    altitudes.append(current_altitude)
    velocities.append(current_velocity)
    pid_outputs.append(pid_output)
    errors.append(error)

    print(f"Iteration {i+1}: Altitude={current_altitude:.2f}, Velocity={current_velocity:.2f}, PID={pid_output:.2f}")

    prev_error = error

# 🎨 Plot Altitudes and Velocities
plt.figure(figsize=(10, 5))

# Altitude Plot
plt.subplot(2, 1, 1)
plt.plot(range(1, 6), altitudes[1:], 'bo-', label='Altitude')
plt.axhline(y=target_altitude, color='g', linestyle='--', label='Target Altitude')
plt.title("Drone Altitude over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid(True)

# Velocity Plot
plt.subplot(2, 1, 2)
plt.plot(range(1, 6), velocities[1:], 'ro-', label='Velocity')
plt.title("Drone Velocity over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Drone State Update for Hover:")
current_altitude = altitudes[0]  # Starting altitude from simulation
current_velocity = velocities[0]  # Starting velocity from simulation

for i in range(5):
    error = target_altitude - current_altitude
    sum_error += error
    pid_output = kp * error + ki * sum_error + kd * (error - prev_error)

    # Update state for hardware
    current_altitude, current_velocity = update_drone_state(pid_output, current_altitude, current_velocity, dt)

    print(f"[BACKEND] Iteration {i+1}: Altitude={current_altitude:.2f}, Velocity={current_velocity:.2f}, PID={pid_output:.2f}")

    prev_error = error

print("\n✅ Drone state updated for hover using PID-based adjustments.")
