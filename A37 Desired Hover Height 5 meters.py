import matplotlib.pyplot as plt
import numpy as np
import time

# Desired hover height
desired_hover_height = 5.0
hover_tolerance = 0.5
hover_duration = 10

iterations = 5
hover_height_data = []

print("📡 Simulating Hover at Desired Height (5m):\n")

for i in range(iterations):
    print(f"\n🌀 Iteration {i+1}:")
    time_list = []
    altitude_list = []

    for t in range(hover_duration):
        # Simulate random fluctuation around 5m
        altitude = np.random.normal(loc=desired_hover_height, scale=0.3)
        time_list.append(t)
        altitude_list.append(altitude)
        print(f"  Time {t}s → Altitude: {round(altitude, 2)} m")
        time.sleep(0.2)

    hover_height_data.append((time_list, altitude_list))

# Plot hover performance
for i, (t, h) in enumerate(hover_height_data):
    plt.plot(t, h, label=f"Iter {i+1}")

plt.axhline(y=desired_hover_height, color='b', linestyle='--', label="Desired Height (5m)")
plt.axhline(y=desired_hover_height + hover_tolerance, color='g', linestyle='--', label="Upper Tolerance")
plt.axhline(y=desired_hover_height - hover_tolerance, color='r', linestyle='--', label="Lower Tolerance")

plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Drone Hover Performance Around 5m")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import random
import time

desired_hover_height = 5.0
tolerance = 0.5

def hover_height_feedback(current_height):
    if abs(current_height - desired_hover_height) <= tolerance:
        return "✅ Within Desired Hover Range"
    elif current_height < desired_hover_height:
        return "⬆️ Increase Altitude"
    else:
        return "⬇️ Decrease Altitude"

print("\n🛠️ Backend Hover Control Feedback:\n")
for i in range(5):
    current_height = round(random.uniform(4.3, 5.7), 2)
    result = hover_height_feedback(current_height)
    print(f"Iteration {i+1}: Altitude = {current_height} m → {result}")
    time.sleep(0.5)
