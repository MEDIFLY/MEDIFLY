import matplotlib.pyplot as plt
import time
import random

# Thresholds
velocity_threshold = 0.5  # m/s
acceleration_threshold = 0.3  # m/s²

# Logs
iteration_log = []
stability_status = []

# Simulated values for 5 iterations
velocities = [0.45, 0.6, 0.3, 0.2, 0.55]
accelerations = [0.25, 0.35, 0.2, 0.1, 0.4]

print("📊 Starting Algorithm 104: Stability Check...\n")

# ✅ FRONTEND: Check Stability Across 5 Iterations
for i in range(5):
    print(f"🔁 Iteration {i+1}")
    velocity = velocities[i]
    acceleration = accelerations[i]

    is_stable = velocity < velocity_threshold and acceleration < acceleration_threshold
    status = "✅ Stable" if is_stable else "❌ Unstable"

    print(f"  ➤ Velocity = {velocity:.2f} m/s")
    print(f"  ➤ Acceleration = {acceleration:.2f} m/s²")
    print(f"  ➤ Stability: {status}")

    iteration_log.append(i + 1)
    stability_status.append(1 if is_stable else 0)

    time.sleep(0.5)

# 📊 Plotting Stability Status
plt.figure(figsize=(8, 4))
plt.plot(iteration_log, stability_status, marker='o', linestyle='-', color='green')
plt.title("🛰️ Drone Stability Over Iterations (A104)")
plt.xlabel("Iteration")
plt.ylabel("Stability (1 = Stable, 0 = Unstable)")
plt.ylim(-0.1, 1.1)
plt.grid(True)
plt.yticks([0, 1], ["Unstable", "Stable"])
plt.tight_layout()
plt.show()

# ✅ BACKEND: Hardware Check Function
def is_drone_stable(velocity, acceleration, v_thresh=0.5, a_thresh=0.3):
    return velocity < v_thresh and acceleration < a_thresh

# Example Hardware Stability Check
print("\n🧠 Backend Stability Check:")
v_test = 0.4
a_test = 0.25
stable = is_drone_stable(v_test, a_test)
print(f"  ➤ Velocity = {v_test} m/s, Acceleration = {a_test} m/s²")
print(f"  ➤ Hardware Stability: {'✅ Stable' if stable else '❌ Unstable'}")
