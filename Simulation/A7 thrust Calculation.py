import time
import random
import matplotlib.pyplot as plt

# === Algorithm 7: Thrust Calculation ===

# Constants
mass = 2.0  # in kg (adjust based on your drone)
gravity = 9.81  # m/s²

# Lists to store thrust values
thrust_values = []

print("🚀 Starting Thrust Calculation for Takeoff...\n")

# 5 Iteration Simulated Thrust Calculation
for i in range(5):
    print(f"🌀 Iteration {i + 1}:")

    # === Frontend Simulation ===
    # Simulate vertical acceleration (between 0.1 to 0.5 m/s²)
    acceleration = round(random.uniform(0.1, 0.5), 2)

    # === Backend Thrust Calculation ===
    thrust = mass * (gravity + acceleration)
    thrust_values.append(thrust)

    print(f"📈 Vertical Acceleration: {acceleration:.2f} m/s²")
    print(f"🧮 Calculated Thrust: {thrust:.2f} N")

    time.sleep(1)
    print()

# === Plotting Thrust Across Iterations ===
plt.figure(figsize=(8, 5))
plt.plot(thrust_values, marker='s', linestyle='-', color='darkorange')
plt.title("Thrust Required During Takeoff")
plt.xlabel("Iteration")
plt.ylabel("Thrust (N)")
plt.grid(True)
plt.tight_layout()
plt.show()
