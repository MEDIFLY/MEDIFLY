import matplotlib.pyplot as plt
import numpy as np
import time

# ---------- 🖼️ FRONTEND (Simulation + Plot) ----------

print("\n📍 Frontend: Simulating Drone Hovering at Target Coordinates\n")

def simulate_hover_position(target_x, target_y, target_z, duration, tolerance):
    time_steps = list(range(duration + 1))
    x_values = []
    y_values = []
    z_values = []

    for t in time_steps:
        current_x = target_x + np.random.uniform(-0.3, 0.3)
        current_y = target_y + np.random.uniform(-0.3, 0.3)
        current_z = target_z + np.random.uniform(-0.2, 0.2)

        x_values.append(current_x)
        y_values.append(current_y)
        z_values.append(current_z)

        print(f"🕒 t={t}s | Pos: ({current_x:.2f}, {current_y:.2f}, {current_z:.2f})")
        time.sleep(0.2)

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x_values, y_values, z_values, marker='o', label='Drone Path')
    ax.scatter([target_x], [target_y], [target_z], color='red', s=100, label='Target Point')

    ax.set_title("Algorithm 34: Hovering at Specified (x, y, z)")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (Altitude in m)")
    ax.legend()
    plt.tight_layout()
    plt.show()

# Call Frontend Hover Simulation
simulate_hover_position(target_x=10.0, target_y=20.0, target_z=5.0, duration=10, tolerance=0.3)

# ---------- 🔧 BACKEND (Hover Logic with Check) ----------

print("\n🔧 Backend: Executing Hover Stability Check at Target Coordinates\n")

def hover_at_coordinates(target_x, target_y, target_z, duration, tolerance):
    stable = True
    for t in range(duration + 1):
        sensor_x = target_x + np.random.uniform(-0.3, 0.3)
        sensor_y = target_y + np.random.uniform(-0.3, 0.3)
        sensor_z = target_z + np.random.uniform(-0.2, 0.2)

        deviation = max(abs(sensor_x - target_x), abs(sensor_y - target_y), abs(sensor_z - target_z))
        print(f"🕒 t={t}s | Current: ({sensor_x:.2f}, {sensor_y:.2f}, {sensor_z:.2f})")

        if deviation > tolerance:
            print("⚠️ Drone position out of tolerance range! Hover unstable.")
            stable = False
        else:
            print("✅ Position within stable hover tolerance.")
        time.sleep(0.2)

    if stable:
        print("\n✅ Drone hovered accurately at target coordinates!")
    else:
        print("\n❌ Hover deviation detected! Stabilization needed.")

# Call backend hover check
hover_at_coordinates(target_x=10.0, target_y=20.0, target_z=5.0, duration=10, tolerance=0.3)
