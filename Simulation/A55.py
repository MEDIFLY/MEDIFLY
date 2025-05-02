# ----------------------------------------------------
# Algorithm 55: Simulate Time Delay for Hover
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random
import time

# =======================
# FRONTEND: Simulation
# =======================

# Drone State Parameters
target_altitude = 10.0
current_altitude = round(random.uniform(8.0, 12.0), 2)
current_velocity = 0.0  # Starting velocity (m/s)

# Time step and delay simulation (realistic time delay)
dt = 0.1  # seconds (each iteration is 0.1 seconds)
simulated_delay = 0.3  # seconds (simulating delay in hover control)

# Function to simulate the time delay
def simulate_time_delay(delay_time):
    """Simulate a time delay in the hover control system."""
    time.sleep(delay_time)

# Simulation loop
altitudes = [current_altitude]
velocities = [current_velocity]
delays = []

print("🎮 FRONTEND: Simulating Time Delay for Hover:")

for i in range(5):
    # Simulate the time delay
    simulate_time_delay(simulated_delay)
    
    # Simulate small changes in velocity and altitude
    current_velocity += 0.1 * (random.random() - 0.5)  # Random velocity change
    current_altitude += current_velocity * dt
    
    # Store results for visualization
    altitudes.append(current_altitude)
    velocities.append(current_velocity)
    delays.append(simulated_delay)
    
    print(f"Iteration {i+1}: Altitude={current_altitude:.2f}, Velocity={current_velocity:.2f}, Delay={simulated_delay}s")

# 🎨 Plot Altitude and Delay Visualization
plt.figure(figsize=(10, 5))

# Altitude Plot
plt.subplot(2, 1, 1)
plt.plot(range(1, 6), altitudes[1:], 'bo-', label='Altitude')
plt.axhline(y=target_altitude, color='g', linestyle='--', label='Target Altitude')
plt.title("Drone Altitude vs Time")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid(True)

# Delay Visualization Plot
plt.subplot(2, 1, 2)
plt.plot(range(1, 6), delays, 'ro-', label='Simulated Delay')
plt.title("Simulated Time Delay for Hover")
plt.xlabel("Iteration")
plt.ylabel("Delay Time (s)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Simulating Time Delay for Hover:")
current_altitude = altitudes[0]  # Starting altitude from simulation
current_velocity = velocities[0]  # Starting velocity from simulation

for i in range(5):
    # Simulate the time delay
    simulate_time_delay(simulated_delay)
    
    # Simulate small changes in velocity and altitude
    current_velocity += 0.1 * (random.random() - 0.5)  # Random velocity change
    current_altitude += current_velocity * dt
    
    print(f"[BACKEND] Iteration {i+1}: Altitude={current_altitude:.2f}, Velocity={current_velocity:.2f}, Delay={simulated_delay}s")

print("\n✅ Time delay for hover control simulated successfully.")
