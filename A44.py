# ----------------------------------------------
# Algorithm 44: Derivative Gain (kd): 0.01
# Frontend: Simulation + Plots
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------

import matplotlib.pyplot as plt

# FRONTEND: Simulating and plotting kd values (5 iterations)
kd_values = []
iterations = [1, 2, 3, 4, 5]

# Simulated frontend values (these could vary based on tuning later)
for i in iterations:
    kd = 0.01  # Fixed derivative gain
    print(f"Iteration {i}: Derivative Gain (kd) set to {kd}")
    kd_values.append(kd)

# Plotting the kd values for visualization
plt.figure(figsize=(8, 4))
plt.plot(iterations, kd_values, marker='o', linestyle='--', color='purple', label='Derivative Gain (kd)')
plt.title("Algorithm 44 - Derivative Gain (kd) Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("kd Value")
plt.ylim(0, 0.02)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# BACKEND: Hardware Integration Logic (for real drone)
# ------------------------------------------------------

# Let's assume the drone's control system has a dictionary where PID values are stored
drone_pid_settings = {}

# Applying derivative gain to the hardware control system for 5 iterations
for i in iterations:
    # Assign the kd value (usually fed into motor controllers or flight controller firmware)
    drone_pid_settings["kd"] = 0.01  # Real drone setting
    print(f"[BACKEND] Iteration {i}: kd set in hardware config => {drone_pid_settings['kd']}")

# Final confirmation
print("\n✅ Derivative Gain (kd) successfully simulated and applied to hardware settings.")
