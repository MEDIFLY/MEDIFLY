# ----------------------------------------------------
# Algorithm 47: Previous Error (error_z_prev)
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random

# =======================
# FRONTEND: Simulation
# =======================

iterations = [1, 2, 3, 4, 5]
target_altitude = 10.0  # Target height in meters

actual_altitudes = []
error_z_list = []
error_z_prev_list = []

error_z_prev = 0  # Start with 0 as no previous error in first iteration

print("🎮 FRONTEND SIMULATION:")
for i in iterations:
    actual_altitude = round(random.uniform(8.5, 11.5), 2)
    error_z = target_altitude - actual_altitude

    actual_altitudes.append(actual_altitude)
    error_z_list.append(error_z)
    error_z_prev_list.append(error_z_prev)

    print(f"Iteration {i}: error_z = {error_z:.2f}, error_z_prev = {error_z_prev:.2f}")

    error_z_prev = error_z  # Update previous error for next iteration

# 🎨 Plot both error_z and error_z_prev
plt.figure(figsize=(10, 5))
plt.plot(iterations, error_z_list, 'bo-', label='Current Error (error_z)')
plt.plot(iterations, error_z_prev_list, 'ro--', label='Previous Error (error_z_prev)')
plt.title("Algorithm 47 - Tracking Previous Error Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Error Value (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE LOGIC:")
error_z_prev = 0  # Initial hardware memory variable

for i in range(5):
    actual_altitude_hw = actual_altitudes[i]
    error_z = target_altitude - actual_altitude_hw

    # Log previous error used before updating
    print(f"[BACKEND] Iteration {i+1}: error_z_prev = {error_z_prev:.2f} -> error_z = {error_z:.2f}")

    # Update previous error for next loop
    error_z_prev = error_z

print("\n✅ Previous error (error_z_prev) tracked correctly for simulation and backend.")
