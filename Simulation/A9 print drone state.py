import time
import random

# === Algorithm 9: Print Drone State ===

# Starting drone state
position = {"x": 0, "y": 0, "z": 0}
velocity = 0.0
battery_level = 100.0  # percentage
flight_mode = "Takeoff"

print("🖨️ Printing Drone State Over 5 Iterations...\n")

for i in range(5):
    print(f"📋 Iteration {i + 1} - Drone State:")

    # === Backend logic: simulate state change ===
    position["z"] += random.uniform(0.8, 1.2)  # simulate upward movement
    velocity = random.uniform(0.5, 2.0)        # simulate velocity change
    battery_level -= random.uniform(0.5, 1.0)  # battery drains

    # === Frontend: print state ===
    print(f"📍 Position -> x: {position['x']:.2f}, y: {position['y']:.2f}, z: {position['z']:.2f} meters")
    print(f"⚙️ Velocity: {velocity:.2f} m/s")
    print(f"🔋 Battery: {battery_level:.2f}%")
    print(f"✈️ Flight Mode: {flight_mode}")
    print("-" * 40)

    time.sleep(1)
