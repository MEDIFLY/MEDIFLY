import time
import matplotlib.pyplot as plt

# === Algorithm 8: State Update ===

# Initial state
x = 0
y = 0
z = 0
velocity = 0
acceleration = 0.3  # simulated constant upward acceleration (m/s²)
dt = 1  # time step in seconds

# Store positions for plotting
z_positions = []

print("📍 Starting Drone State Updates During Takeoff...\n")

# 5 iterations of state update
for i in range(5):
    print(f"🌀 Iteration {i + 1}:")

    # === Backend State Update Logic ===
    velocity += acceleration * dt         # v = v + a*t
    z += velocity * dt                    # z = z + v*t

    # Store z for plot
    z_positions.append(z)

    # === Frontend: Print current state ===
    print(f"📦 Position -> x: {x}, y: {y}, z: {z:.2f} meters")
    print(f"⚙️ Velocity: {velocity:.2f} m/s")
    time.sleep(1)
    print()

# === Plotting the height (z) ===
plt.figure(figsize=(8, 5))
plt.plot(z_positions, marker='o', linestyle='-', color='green')
plt.title("Drone Altitude Over Time (Takeoff)")
plt.xlabel("Iteration")
plt.ylabel("Height z (meters)")
plt.grid(True)
plt.tight_layout()
plt.show()
