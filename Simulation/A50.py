# ----------------------------------------------------
# Algorithm 50: Calculate Error Function
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random

# =======================
# FRONTEND: Simulation
# =======================

def calculate_error(target, actual):
    return target - actual

target_altitude = 10.0
altitude_readings = [round(random.uniform(8.5, 11.5), 2) for _ in range(5)]
errors = []

print("🎮 FRONTEND ERROR CALCULATION:")
for i in range(5):
    error = calculate_error(target_altitude, altitude_readings[i])
    errors.append(error)
    print(f"Iteration {i+1}: actual={altitude_readings[i]:.2f}, error={error:.2f}")

# 🎨 Plot Errors
plt.figure(figsize=(10, 5))
plt.plot(range(1, 6), errors, 'ms--', label='Altitude Error')
plt.axhline(y=0, color='g', linestyle='--', label='Zero Error')
plt.title("Algorithm 50 - Error Between Actual and Target Altitude")
plt.xlabel("Iteration")
plt.ylabel("Error (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE ERROR CHECKING:")
for i in range(5):
    actual = altitude_readings[i]
    error = calculate_error(target_altitude, actual)
    print(f"[BACKEND] Iteration {i+1}: actual={actual:.2f}, error={error:.2f}")

print("\n✅ Error calculation function isolated for reuse in PID systems.")
