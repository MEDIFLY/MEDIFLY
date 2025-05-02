import matplotlib.pyplot as plt
import random
import time

# ----------------------------
# PARAMETERS
# ----------------------------
iterations = 5
initial_velocity = 0.0  # drone_vz = 0
vz_history_all = []

print("🚁 Vertical Velocity Simulation: drone_vz starts at 0 m/s\n")

# ----------------------------
# MAIN LOOP (Frontend + Backend)
# ----------------------------
for i in range(iterations):
    print(f"\n🔁 Iteration {i+1}:")
    drone_vz = initial_velocity
    vz_list = []

    for t in range(10):
        # Simulate vertical velocity fluctuation
        velocity_change = round(random.uniform(-0.5, 0.5), 2)
        drone_vz = round(drone_vz + velocity_change, 2)

        # Backend Logic
        if abs(drone_vz) <= 0.2:
            status = "✅ Stable (No major vertical motion)"
        elif drone_vz > 0.2:
            status = "⬆️ Ascending"
        else:
            status = "⬇️ Descending"

        print(f"  Time {t}s → Vertical Velocity (drone_vz): {drone_vz} m/s → {status}")
        vz_list.append(drone_vz)
        time.sleep(0.2)

    vz_history_all.append(vz_list)

# ----------------------------
# PLOTTING SECTION
# ----------------------------
for i, vz_list in enumerate(vz_history_all):
    plt.plot(range(len(vz_list)), vz_list, label=f"Iter {i+1}")

plt.axhline(y=0, color='blue', linestyle='--', label='Target drone_vz = 0 m/s')
plt.axhline(y=0.2, color='green', linestyle='--', label='+0.2 Tolerance')
plt.axhline(y=-0.2, color='red', linestyle='--', label='-0.2 Tolerance')

plt.title("Vertical Velocity of Drone (drone_vz)")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
