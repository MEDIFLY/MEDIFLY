# ---------------------------------------------------------
# 🧠 MEDIFLY Algorithm 101: Error Calculation for Simulation
# ---------------------------------------------------------
# Includes: Frontend (Simulation & Plots) + Backend (Hardware Logic)
# Iteration Count: 5x Error Calculation updates for realism

import matplotlib.pyplot as plt
import numpy as np

# ------------------- Initialization ----------------------
desired_altitude = 50  # meters
actual_altitude_log = [45, 46.5, 47.8, 48.9, 49.5]  # Simulated sensor data
iterations = 5

# ------------------- Frontend Simulation -------------------
error_log = []

print("\n📡 Calculating Altitude Errors Over 5 Iterations:")

for i in range(iterations):
    current_altitude = actual_altitude_log[i]
    error = desired_altitude - current_altitude
    error_log.append(error)
    print(f"Iteration {i+1}: Desired = {desired_altitude}m, Actual = {current_altitude}m, Error = {error:.2f}m")

# ------------------- Plotting ------------------------------
plt.figure(figsize=(10, 5))
plt.plot(range(1, iterations+1), error_log, marker='o', color='crimson', linewidth=2, label='Altitude Error')
plt.axhline(0, color='gray', linestyle='--', label='Zero Error Line')
plt.title('🔍 Altitude Error Over Time')
plt.xlabel('Iteration')
plt.ylabel('Error (meters)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ------------------- Backend Hardware Logic ----------------
def calculate_error(desired, actual):
    """Backend logic for real-time error calculation."""
    return desired - actual

# Simulating hardware callback loop
print("\n🛠️ Backend Hardware Simulation:")
for i in range(iterations):
    sensor_reading = actual_altitude_log[i]  # Replace with hardware sensor in real case
    error_val = calculate_error(desired_altitude, sensor_reading)
    print(f"[Hardware] Iteration {i+1}: Error = {error_val:.2f} meters")
