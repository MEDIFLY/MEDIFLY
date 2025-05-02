import matplotlib.pyplot as plt
import random
import time

# ----------------------------
# PARAMETERS
# ----------------------------
iterations = 5
initial_position = 0.0  # drone_z = 0
drone_z_history = []

print("🚁 Vertical Position Simulation: drone_z starts at 0\n")

# ----------------------------
# MAIN LOOP (Frontend + Backend)
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")
    drone_z = initial_position  # Start at 0 each time
    z_positions = []

    for t in range(10):
        # Simulate vertical motion (random noise added)
        change = random.uniform(-0.3, 0.3)
        drone_z = round(drone_z + change, 2)

        # Backend Logic
        if abs(drone_z) <= 0.1:
            status = "✅ Stable near 0m"
        elif drone_z > 0.1:
            status = "⬆️ Rising"
        else:
            status = "⬇️ Dropping"

        print(f"  Time {t}s → Altitude (drone_z): {drone_z} m → {status}")
        z_positions.append(drone_z)
        time.sleep(0.2)

    drone_z_history.append(z_positions)

# ----------------------------
# PLOTTING SECTION
# ----------------------------
for i, z_list in enumerate(drone_z_history):
    plt.plot(range(len(z_list)), z_list, label=f"Iter {i+1}")

plt.axhline(y=0, color='blue', linestyle='--', label='Target (drone_z = 0)')
plt.axhline(y=0.1, color='green', linestyle='--', label='+0.1m Tolerance')
plt.axhline(y=-0.1, color='red', linestyle='--', label='-0.1m Tolerance')

plt.title("Vertical Position of Drone (drone_z)")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
