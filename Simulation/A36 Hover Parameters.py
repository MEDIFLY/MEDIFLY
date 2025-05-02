import matplotlib.pyplot as plt
import numpy as np
import time

# Hover parameter settings
max_hover_altitude = 6.0  # meters
min_hover_altitude = 4.0  # meters
hover_duration = 10       # seconds
timestep = 1              # second

iterations = 5
hover_records = []

print("📡 Simulating Hover Parameters Check:\n")

for i in range(iterations):
    print(f"\n🌀 Iteration {i+1}:")

    heights = []
    times = []

    for t in range(hover_duration):
        current_altitude = np.random.uniform(4.0, 6.0)
        times.append(t)
        heights.append(current_altitude)

        print(f"  Time {t}s → Altitude: {round(current_altitude, 2)} m")

        time.sleep(0.2)

    hover_records.append((times, heights))

# Plotting hover stability zone
for i, (t, h) in enumerate(hover_records):
    plt.plot(t, h, label=f"Iter {i+1}")

plt.axhline(y=max_hover_altitude, color='r', linestyle='--', label="Max Altitude")
plt.axhline(y=min_hover_altitude, color='g', linestyle='--', label="Min Altitude")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Hover Parameter Ranges")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import random
import time

# Define safe hover boundaries
min_hover_altitude = 4.0
max_hover_altitude = 6.0

def hover_status_backend(current_height):
    if min_hover_altitude <= current_height <= max_hover_altitude:
        return "✅ Hover Altitude Safe"
    elif current_height < min_hover_altitude:
        return "⚠️ Altitude Too Low"
    else:
        return "⚠️ Altitude Too High"

# Run backend hover parameter check for 5 iterations
print("\n🛠️ Backend Hover Altitude Validator:\n")
for i in range(5):
    current_height = round(random.uniform(3.5, 6.5), 2)
    result = hover_status_backend(current_height)
    print(f"Iteration {i+1}: Altitude = {current_height} m → {result}")
    time.sleep(0.5)
