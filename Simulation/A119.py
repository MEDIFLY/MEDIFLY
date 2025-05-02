# A119.py
import numpy as np
import matplotlib.pyplot as plt
import time

# ─────────────────────────────────────
# 🚀 FRONTEND: Time Step Simulation
# ─────────────────────────────────────

# Define simulation parameters
total_time = 20  # seconds
time_step = 0.5  # seconds
iterations = int(total_time / time_step)
time_array = np.arange(0, total_time + time_step, time_step)

# Simulated altitude profile (e.g., a simple linear climb)
altitude_profile = [min(2 * t, 30) for t in time_array]  # Max altitude 30 meters

# ─────────────────────────────────────
# 🔧 BACKEND: Log Time Steps + Hardware-Like Logic
# ─────────────────────────────────────

print("🕒 Time Step Initialization for MEDIFLY Simulation")
print(f"➡️  Total Time: {total_time} seconds")
print(f"➡️  Time Step: {time_step} seconds")
print(f"➡️  Iterations: {iterations}")
print("📡 Starting mission...\n")

# Simulate hardware loop with time steps
for i, t in enumerate(time_array):
    altitude = altitude_profile[i]
    print(f"⏱️  t = {t:.1f}s | Altitude = {altitude:.2f} m")
    time.sleep(0.1)  # Simulate real-time delay (optional)

# ─────────────────────────────────────
# 📊 Plotting Altitude vs Time
# ─────────────────────────────────────

plt.figure(figsize=(10, 6))
plt.plot(time_array, altitude_profile, marker='o', linestyle='-', color='blue', label="Altitude (m)")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("MEDIFLY Altitude Simulation Over Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
