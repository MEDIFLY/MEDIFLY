import time
import random
import matplotlib.pyplot as plt

# === FRONTEND + BACKEND for Takeoff Parameters ===

# Lists to store values for plotting
takeoff_heights = []
ascent_rates = []

# Constants for safety limits
MAX_SAFE_HEIGHT = 50  # in meters
MAX_ASCENT_RATE = 5   # in m/s

print("🚁 Initializing Takeoff Parameter Check...")

# Perform 5 iterations
for i in range(5):
    print(f"\n📡 Iteration {i + 1} - Takeoff Parameter Setting")

    # === Frontend Simulation ===
    takeoff_height = round(random.uniform(10, 50), 2)  # meters
    ascent_rate = round(random.uniform(1, 5), 2)        # m/s

    takeoff_heights.append(takeoff_height)
    ascent_rates.append(ascent_rate)

    print(f"🎯 Target Takeoff Height: {takeoff_height} meters")
    print(f"📈 Ascent Rate: {ascent_rate} m/s")

    # === Backend Logic (Mock) ===
    if takeoff_height > MAX_SAFE_HEIGHT:
        print("❌ Error: Takeoff height exceeds safety limit!")
    else:
        print("✅ Height within safe limits.")

    if ascent_rate > MAX_ASCENT_RATE:
        print("❌ Error: Ascent rate too high!")
    else:
        print("✅ Ascent rate within safe limits.")

    time.sleep(1)

# === Plotting Simulation Results ===
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(takeoff_heights, marker='o', color='skyblue')
plt.title("Takeoff Height per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Height (m)")

plt.subplot(1, 2, 2)
plt.plot(ascent_rates, marker='s', color='salmon')
plt.title("Ascent Rate per Iteration")
plt.xlabel("Iteration")
plt.ylabel("Rate (m/s)")

plt.tight_layout()
plt.show()
