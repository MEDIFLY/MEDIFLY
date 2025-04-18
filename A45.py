# ----------------------------------------------
# Algorithm 45: Error Variables
# Frontend: Simulation + Plot
# Backend: Hardware Variable Setup
# 5 Iterations Included
# ----------------------------------------------

import matplotlib.pyplot as plt

# ===========================
# FRONTEND: Simulation Setup
# ===========================

iterations = [1, 2, 3, 4, 5]

# Initialize empty lists for visualizing error values
error_z_list = []
error_z_prev_list = []
error_z_sum_list = []

# In a real simulation, we would calculate errors from position
# Here, we'll simulate the process with dummy data

for i in iterations:
    error_z = 0  # Will be calculated later
    error_z_prev = 0  # No previous error in simulation yet
    error_z_sum = 0  # Will accumulate over time

    print(f"Iteration {i}: error_z = {error_z}, error_z_prev = {error_z_prev}, error_z_sum = {error_z_sum}")
    
    error_z_list.append(error_z)
    error_z_prev_list.append(error_z_prev)
    error_z_sum_list.append(error_z_sum)

# 🎨 Plot the initial error variables
plt.figure(figsize=(10, 5))
plt.plot(iterations, error_z_list, 'bo--', label='Current Error (error_z)')
plt.plot(iterations, error_z_prev_list, 'go--', label='Previous Error (error_z_prev)')
plt.plot(iterations, error_z_sum_list, 'ro--', label='Sum of Errors (error_z_sum)')
plt.title("Algorithm 45 - Error Variables Initialization Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Error Value")
plt.ylim(-1, 1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ===========================
# BACKEND: Hardware Variables
# ===========================

# These variables would be declared in your drone control code
# where the flight controller uses them for PID updates

for i in iterations:
    # Simulating hardware-side initialization
    error_z = 0
    error_z_prev = 0
    error_z_sum = 0

    print(f"[BACKEND] Iteration {i}: Initialized error_z={error_z}, error_z_prev={error_z_prev}, error_z_sum={error_z_sum}")

# Final confirmation
print("\n✅ Error variables initialized successfully for both simulation and hardware.")
