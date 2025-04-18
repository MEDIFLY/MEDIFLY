import matplotlib.pyplot as plt
import numpy as np
import time

# ---------- Frontend (Simulation + Plot) ----------

print("\n📍 Frontend: Simulating Hover Function Call\n")

# Hover Function Parameters
def simulate_hover(target_altitude, duration, tolerance):
    time_steps = list(range(duration + 1))
    altitudes = []

    for t in time_steps:
        # Simulate sensor reading with fluctuation
        current_altitude = target_altitude + np.random.uniform(-0.2, 0.2)
        altitudes.append(current_altitude)
        print(f"🕒 t={t}s | Altitude: {current_altitude:.2f} m")
        time.sleep(0.2)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(time_steps, altitudes, marker='o', linestyle='--', color='blue', label='Simulated Altitude')
    plt.axhline(y=target_altitude, color='green', linestyle='-', label='Target Altitude')
    plt.fill_between(time_steps, 
                     [target_altitude - tolerance]*len(time_steps), 
                     [target_altitude + tolerance]*len(time_steps),
                     color='yellow', alpha=0.2, label='Tolerance Band')
    plt.title("Algorithm 33: Hover Function Simulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (meters)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Call frontend simulation
simulate_hover(target_altitude=5.0, duration=10, tolerance=0.3)

# ---------- Backend (Hover Function Logic) ----------

print("\n🔧 Backend: Hover Function Execution\n")

def hover_function(target_altitude, duration, tolerance):
    stable = True
    for t in range(duration + 1):
        sensor_altitude = target_altitude + np.random.uniform(-0.2, 0.2)
        print(f"🕒 Backend t={t}s | Sensor Altitude: {sensor_altitude:.2f} m")

        if abs(sensor_altitude - target_altitude) > tolerance:
            print("⚠️ Altitude out of range! Adjusting thrust...")
            stable = False
        else:
            print("✅ Altitude within acceptable range.")
        time.sleep(0.2)

    if stable:
        print("\n✅ Hover function maintained altitude successfully!")
    else:
        print("\n❌ Hover function encountered instability!")

# Call backend hover logic
hover_function(target_altitude=5.0, duration=10, tolerance=0.3)
