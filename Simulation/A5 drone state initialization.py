import time
import random
import matplotlib.pyplot as plt

# === Drone State Initialization ===

# Constants for initial values
INITIAL_POSITION = (0, 0, 0)  # (x, y, z) in meters
INITIAL_VELOCITY = 0.0        # in m/s
MAX_BATTERY = 25.2            # in volts
MIN_BATTERY = 22.0            # in volts

# Lists to store state parameters for plotting
orientations = []
battery_levels = []

print("🚁 Initializing Drone State...\n")

# 5 Iterations
for i in range(5):
    print(f"🌀 Iteration {i + 1} - Initializing Drone State")

    # === Frontend Simulation ===
    x, y, z = INITIAL_POSITION
    yaw = round(random.uniform(-180, 180), 2)
    pitch = round(random.uniform(-90, 90), 2)
    roll = round(random.uniform(-180, 180), 2)
    velocity = INITIAL_VELOCITY
    battery = round(random.uniform(22.0, 25.2), 2)

    orientations.append((yaw, pitch, roll))
    battery_levels.append(battery)

    print(f"📍 Position: x={x}, y={y}, z={z}")
    print(f"🧭 Orientation: Yaw={yaw}°, Pitch={pitch}°, Roll={roll}°")
    print(f"💨 Velocity: {velocity} m/s")
    print(f"🔋 Battery Level: {battery} V")

    # === Backend Check ===
    if battery < MIN_BATTERY:
        print("❌ Battery too low for initialization!")
    elif battery > MAX_BATTERY:
        print("❌ Voltage too high - unsafe!")
    else:
        print("✅ Battery level OK")

    print("✅ Initial drone state recorded.\n")
    time.sleep(1)

# === Plotting ===
# Unpacking orientation values
yaws = [ori[0] for ori in orientations]
pitches = [ori[1] for ori in orientations]
rolls = [ori[2] for ori in orientations]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(battery_levels, marker='o', color='green')
plt.title("Battery Level per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Voltage (V)")

plt.subplot(1, 2, 2)
plt.plot(yaws, label="Yaw", marker='o')
plt.plot(pitches, label="Pitch", marker='s')
plt.plot(rolls, label="Roll", marker='^')
plt.title("Orientation per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Degrees")
plt.legend()

plt.tight_layout()
plt.show()
