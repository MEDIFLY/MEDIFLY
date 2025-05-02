# ----------------------------------------------------
# Algorithm 53: Update Error Variables for Hover
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

# Error Variables Initialization
prev_error = 0
sum_error = 0

# Simulation function to update error variables
def update_error_variables(current_altitude, target_altitude, prev_error, sum_error):
    """Update previous error and sum of errors for the next iteration."""
    error = target_altitude - current_altitude
    sum_error += error
    return error, sum_error

# Simulate 5 iterations
errors = []
sum_errors = []
pid_outputs = []
altitudes = [current_altitude]
velocities = [current_velocity]

print("🎮 FRONTEND: Updating Error Variables for Hover:")

for i in range(5):
    # Update error variables
    error, sum_error = update_error_variables(current_altitude, target_altitude, prev_error, sum_error)
    
    # Calculate PID output
    pid_output = kp * error + ki * sum_error + kd * (error - prev_error)
    
    # Update state with PID output
    current_velocity += pid_output * dt
    current_altitude += current_velocity * dt
    
    # Store results
    errors.append(error)
    sum_errors.append(sum_error)
    pid_outputs.append(pid_output)
    altitudes.append(current_altitude)
    velocities.append(current_velocity)

    # Update previous error for the next iteration
    prev_error = error

    print(f"Iteration {i+1}: Error={error:.2f}, Sum Error={sum_error:.2f}, PID Output={pid_output:.2f}")

# 🎨 Plot Error and PID Output
plt.figure(figsize=(10, 5))

# Error Plot
plt.subplot(2, 1, 1)
plt.plot(range(1, 6), errors, 'bo-', label='Error')
plt.title("Error Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Error (m)")
plt.legend()
plt.grid(True)

# Sum Error Plot
plt.subplot(2, 1, 2)
plt.plot(range(1, 6), sum_errors, 'go-', label='Sum Error')
plt.title("Sum of Errors Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Sum of Errors")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Updating Error Variables for Hover:")
prev_error = 0
sum_error = 0
current_altitude = altitudes[0]
current_velocity = velocities[0]

for i in range(5):
    error, sum_error = update_error_variables(current_altitude, target_altitude, prev_error, sum_error)
    
    # Calculate PID output for hardware
    pid_output = kp * error + ki * sum_error + kd * (error - prev_error)
    
    # Update drone state
    current_velocity += pid_output * dt
    current_altitude += current_velocity * dt
    
    print(f"[BACKEND] Iteration {i+1}: Error={error:.2f}, Sum Error={sum_error:.2f}, PID Output={pid_output:.2f}")
    
    # Update previous error for the next iteration
    prev_error = error

print("\n✅ Error variables updated for hover control.")
