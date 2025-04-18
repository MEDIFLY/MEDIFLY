import matplotlib.pyplot as plt
import numpy as np
import time

# ---------- Frontend (Simulation + Plot) ----------

print("\n📍 Frontend: Simulating Drone Hover at Fixed Altitude\n")

# Hovering Parameters
hover_altitude = 5.0  # meters
hover_duration = 10  # seconds
hover_noise_level = 0.2  # small fluctuations

# Simulate altitude variations over time
time_steps = list(range(hover_duration + 1))
altitude_readings = []

for t in time_steps:
    fluctuation = np.random.uniform(-hover_noise_level, hover_noise_level)
    altitude = hover_altitude + fluctuation
    altitude_readings.append(altitude)
    print(f"🕒 t={t}s | Altitude: {altitude:.2f} meters")
    time.sleep(0.2)

# Plotting hover altitude
plt.figure(figsize=(8, 5))
plt.plot(time_steps, altitude_readings, marker='o', linestyle='--', color='blue', label='Altitude')
plt.axhline(y=hover_altitude, color='green', linestyle='-', label='Target Altitude')
plt.title("Algorithm 32: Hovering at Fixed Altitude")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (meters)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# ---------- Backend (Hardware Logic) ----------

def hover_backend(target_altitude=5.0, duration=10, tolerance=0.3):
    print("\n🔧 Backend: Maintaining Hover at Altitude\n")
    current_time = 0
    stable = True

    while current_time <= duration:
        # Simulated sensor reading with random noise
        sensor_altitude = target_altitude + np.random.uniform(-0.2, 0.2)
        print(f"🕒 Backend t={current_time}s | Sensor Altitude: {sensor_altitude:.2f} m")

        # Check if within acceptable tolerance
        if abs(sensor_altitude - target_altitude) > tolerance:
            print("⚠️ Warning: Altitude out of tolerance! Taking corrective action...")
            stable = False

        time.sleep(0.2)
        current_time += 1

    if stable:
        print("✅ Hover maintained successfully at target altitude.")
    else:
        print("❌ Hover instability detected during duration.")

# Call backend hover function
hover_backend(target_altitude=5.0, duration=10)
