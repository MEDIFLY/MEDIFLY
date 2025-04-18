import matplotlib.pyplot as plt
import time

# Simulated drone state variables
x = 0
y = 0
z = 0
velocity = 1  # units per second

# Logs for plotting
x_log = []
z_log = []

print("📡 Starting Algorithm 106: Print Drone State in Main Loop\n")

# ✅ FRONTEND: Print Simulated State in Each Iteration
for i in range(5):
    print(f"🔁 Iteration {i+1}")
    print(f"  ➤ Drone Position → X: {x}, Y: {y}, Z: {z}")
    print(f"  ➤ Velocity: {velocity} units/s\n")
    
    # Log for plotting
    x_log.append(x)
    z_log.append(z)
    
    # Update state for next iteration
    x += velocity
    z += velocity
    time.sleep(0.5)

# 📊 Plotting Position vs Altitude
plt.figure(figsize=(8, 4))
plt.plot(x_log, z_log, marker='o', linestyle='--', color='green')
plt.title("🛰️ Drone Position vs Altitude (A106)")
plt.xlabel("X Position")
plt.ylabel("Z Altitude")
plt.grid(True)
plt.tight_layout()
plt.show()

# ✅ BACKEND: Print State Function for Hardware
def print_drone_state(x, y, z, velocity):
    print(f"[HARDWARE LOG] Position → X:{x}, Y:{y}, Z:{z} | Velocity: {velocity} units/s")

# Simulated backend run
print("\n🧠 Backend Hardware Log:")
x, y, z = 0, 0, 0
for i in range(5):
    print_drone_state(x, y, z, velocity)
    x += velocity
    z += velocity
