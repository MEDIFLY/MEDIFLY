import time
import random
import matplotlib.pyplot as plt

# === Algorithm 6: Takeoff Loop ===

# Takeoff target height in meters
TARGET_ALTITUDE = 5.0  

# Lists to store altitudes for plotting
altitude_history = []

# Initial altitude
current_altitude = 0.0

print("🛫 Starting Drone Takeoff Loop...\n")

# 5 Iteration Simulated Takeoff Loop
for i in range(5):
    print(f"🌀 Iteration {i + 1}:")

    # === Frontend Simulation ===
    # Simulate altitude increase (random small increment)
    altitude_increase = round(random.uniform(0.8, 1.2), 2)
    current_altitude += altitude_increase
    altitude_history.append(current_altitude)

    print(f"⬆️ Altitude increased by: {altitude_increase:.2f} m")
    print(f"📍 Current Altitude: {current_altitude:.2f} m")

    # === Backend Check ===
    if current_altitude > TARGET_ALTITUDE:
        print("⚠️ Altitude overshoot! Adjusting...")
        current_altitude = TARGET_ALTITUDE
    elif current_altitude >= TARGET_ALTITUDE:
        print("✅ Target altitude reached!")
    else:
        print("🔄 Ascending...")

    time.sleep(1)
    print()

# === Plotting Altitude Rise ===
plt.figure(figsize=(8, 5))
plt.plot(altitude_history, marker='o', linestyle='-', color='dodgerblue')
plt.axhline(y=TARGET_ALTITUDE, color='red', linestyle='--', label='Target Altitude')
plt.title("Drone Altitude During Takeoff Loop")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
