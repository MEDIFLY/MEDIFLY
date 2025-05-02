# ----------------------------------------------------
# Algorithm 46: Current Error (error_z)
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
target_altitude = 10.0  # in meters (our goal)

actual_altitudes = []  # Simulated sensor data
error_z_list = []

print("🎮 FRONTEND SIMULATION:")
for i in iterations:
    actual_altitude = round(random.uniform(8.5, 11.5), 2)  # Simulate noisy altitudes
    error_z = target_altitude - actual_altitude  # Current error

    actual_altitudes.append(actual_altitude)
    error_z_list.append(error_z)

    print(f"Iteration {i}: Target = {target_altitude} m, Actual = {actual_altitude} m => error_z = {error_z:.2f} m")

# 🎨 Plotting error_z
plt.figure(figsize=(10, 5))
plt.plot(iterations, error_z_list, marker='o', linestyle='-', color='blue', label='Current Error (error_z)')
plt.axhline(0, color='gray', linestyle='--')
plt.title("Algorithm 46 - Current Error (error_z) Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Error in Altitude (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE LOGIC:")
for i in iterations:
    # Simulate sensor fetching actual drone height
    actual_altitude_hw = actual_altitudes[i - 1]  # From earlier simulated values
    error_z = target_altitude - actual_altitude_hw

    # In real drone firmware, this value will feed into the PID controller
    print(f"[BACKEND] Iteration {i}: Actual = {actual_altitude_hw} m, Target = {target_altitude} m => error_z = {error_z:.2f} m")

# Confirmation
print("\n✅ Current Error (error_z) calculated and applied to both simulation and hardware logic.")
