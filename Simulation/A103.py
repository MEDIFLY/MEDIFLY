import matplotlib.pyplot as plt
import time

# Initial drone state
altitude = 0
velocity = 0
acceleration = 0

# Control outputs from previous algorithm (for simulation purposes)
control_outputs = [2.5, 2.8, 3.1, 3.0, 2.7]  # Simulated PID outputs

# Constants
mass = 1.5  # in kg
dt = 1  # 1 second per iteration

altitude_log = []
velocity_log = []
iteration_log = []

print("🛠️ Starting Algorithm 103: State Update for Simulation...")

# 🧪 FRONTEND: 5 Iteration Simulation
for i in range(5):
    print(f"\n🔁 Iteration {i+1}")

    force = control_outputs[i]
    acceleration = force / mass
    velocity += acceleration * dt
    altitude += velocity * dt

    print(f"  ➤ Acceleration: {acceleration:.2f} m/s²")
    print(f"  ➤ Velocity: {velocity:.2f} m/s")
    print(f"  ➤ Altitude: {altitude:.2f} m")

    # Log for plotting
    iteration_log.append(i + 1)
    altitude_log.append(altitude)
    velocity_log.append(velocity)

    time.sleep(0.5)

# 📊 Plot Altitude and Velocity
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(iteration_log, altitude_log, marker='o', color='blue', linewidth=2)
plt.title("📈 Altitude Over Time (A103)")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(iteration_log, velocity_log, marker='s', color='orange', linewidth=2)
plt.title("📉 Velocity Over Time (A103)")
plt.xlabel("Iteration")
plt.ylabel("Velocity (m/s)")
plt.grid(True)

plt.tight_layout()
plt.show()

# 🧠 BACKEND: Hardware State Update Function
def update_drone_state(altitude, velocity, control_output, mass, dt):
    acceleration = control_output / mass
    velocity += acceleration * dt
    altitude += velocity * dt
    return altitude, velocity

# Example hardware call
new_alt, new_vel = update_drone_state(5.5, 1.2, 3.0, 1.5, 1)
print("\n⚙️ Backend Updated Altitude:", round(new_alt, 2))
print("⚙️ Backend Updated Velocity:", round(new_vel, 2))
