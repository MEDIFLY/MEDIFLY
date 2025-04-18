import matplotlib.pyplot as plt
import numpy as np
import random
import time

# ----------------------------
# PARAMETERS
# ----------------------------
desired_hover_height = 5.0
tolerance = 0.5
iterations = 5
hover_duration = 10

hover_height_data = []

print("🚁 Hover Tolerance Algorithm - Desired Height: 5m ± 0.5m\n")

# ----------------------------
# MAIN LOOP - SIMULATION + FEEDBACK
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")

    time_list = []
    altitude_list = []

    for t in range(hover_duration):
        # Simulate fluctuating altitude (random around 5m)
        current_height = round(np.random.normal(loc=desired_hover_height, scale=0.3), 2)
        time_list.append(t)
        altitude_list.append(current_height)

        # Backend: Control Logic
        if abs(current_height - desired_hover_height) <= tolerance:
            status = "✅ Within Range"
        elif current_height < desired_hover_height:
            status = "⬆️ Increase Altitude"
        else:
            status = "⬇️ Decrease Altitude"

        print(f"  Time {t}s → Altitude: {current_height} m → {status}")
        time.sleep(0.2)

    hover_height_data.append((time_list, altitude_list))

# ----------------------------
# PLOTTING SECTION
# ----------------------------
for i, (t, h) in enumerate(hover_height_data):
    plt.plot(t, h, label=f"Iter {i+1}")

# Desired and tolerance bands
plt.axhline(y=desired_hover_height, color='blue', linestyle='--', label='Desired Height (5m)')
plt.axhline(y=desired_hover_height + tolerance, color='green', linestyle='--', label='+0.5m Tolerance')
plt.axhline(y=desired_hover_height - tolerance, color='red', linestyle='--', label='-0.5m Tolerance')

plt.title("Drone Hover Height with Tolerance")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
