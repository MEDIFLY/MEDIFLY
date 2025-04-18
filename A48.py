# ----------------------------------------------------
# Algorithm 48: Integral of Error (error_z_sum)
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
target_altitude = 10.0

actual_altitudes = []
error_z_list = []
error_z_sum_list = []

error_z_sum = 0  # Initial integral sum

print("🎮 FRONTEND SIMULATION:")
for i in iterations:
    actual_altitude = round(random.uniform(8.5, 11.5), 2)
    error_z = target_altitude - actual_altitude

    actual_altitudes.append(actual_altitude)
    error_z_list.append(error_z)
    
    error_z_sum += error_z  # Keep adding up error
    error_z_sum_list.append(error_z_sum)

    print(f"Iteration {i}: error_z = {error_z:.2f}, error_z_sum = {error_z_sum:.2f}")

# 🎨 Plotting error_z_sum over iterations
plt.figure(figsize=(10, 5))
plt.plot(iterations, error_z_sum_list, 'g^-', label='Integral of Error (error_z_sum)')
plt.title("Algorithm 48 - Accumulated Error (Integral) Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Accumulated Error")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE LOGIC:")
error_z_sum = 0

for i in range(5):
    actual_altitude_hw = actual_altitudes[i]
    error_z = target_altitude - actual_altitude_hw

    error_z_sum += error_z  # Same logic as frontend
    print(f"[BACKEND] Iteration {i+1}: error_z = {error_z:.2f} | error_z_sum = {error_z_sum:.2f}")

print("\n✅ Integral of Error (error_z_sum) accumulated and visualized correctly.")
