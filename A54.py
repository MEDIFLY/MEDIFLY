# ----------------------------------------------------
# Algorithm 54: Check Hover Tolerance
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random

# =======================
# FRONTEND: Simulation
# =======================

# Drone State Parameters
target_altitude = 10.0
tolerance = 0.5  # The tolerance level (± meters)
current_altitude = round(random.uniform(8.0, 12.0), 2)
current_velocity = 0.0  # Starting velocity (m/s)

# Time step (simulation)
dt = 0.1  # seconds (each iteration is 0.1 seconds)

# Function to check if the current altitude is within tolerance
def check_hover_tolerance(current_altitude, target_altitude, tolerance):
    """Check if the drone's current altitude is within the target altitude tolerance."""
    if target_altitude - tolerance <= current_altitude <= target_altitude + tolerance:
        return True
    else:
        return False

# Simulation loop
altitudes = [current_altitude]
velocities = [current_velocity]
tolerances = []
status = []

print("🎮 FRONTEND: Checking Hover Tolerance:")

for i in range(5):
    # Check if the altitude is within tolerance
    is_within_tolerance = check_hover_tolerance(current_altitude, target_altitude, tolerance)
    
    # Update state with a small change (simulating PID correction)
    current_velocity += 0.1 * (random.random() - 0.5)  # Simulate small random velocity change
    current_altitude += current_velocity * dt
    
    # Store results for visualization
    altitudes.append(current_altitude)
    velocities.append(current_velocity)
    tolerances.append(is_within_tolerance)
    status.append("Within Tolerance" if is_within_tolerance else "Out of Tolerance")

    print(f"Iteration {i+1}: Altitude={current_altitude:.2f}, Tolerance Status={status[-1]}")

# 🎨 Plot Altitudes and Tolerance Status
plt.figure(figsize=(10, 5))

# Altitude Plot
plt.subplot(2, 1, 1)
plt.plot(range(1, 6), altitudes[1:], 'bo-', label='Altitude')
plt.axhline(y=target_altitude, color='g', linestyle='--', label='Target Altitude')
plt.axhline(y=target_altitude + tolerance, color='r', linestyle='--', label='Tolerance Limit (+)')
plt.axhline(y=target_altitude - tolerance, color='r', linestyle='--', label='Tolerance Limit (-)')
plt.title("Drone Altitude vs Tolerance")
plt.xlabel("Iteration")
plt.ylabel("Altitude (m)")
plt.legend()
plt.grid(True)

# Tolerance Status Plot
plt.subplot(2, 1, 2)
plt.plot(range(1, 6), [1 if status[i] == "Within Tolerance" else 0 for i in range(5)], 'ro-', label='Tolerance Status')
plt.title("Tolerance Check Status")
plt.xlabel("Iteration")
plt.ylabel("Status (1=Within, 0=Out)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Checking Hover Tolerance:")
current_altitude = altitudes[0]  # Starting altitude from simulation
current_velocity = velocities[0]  # Starting velocity from simulation

for i in range(5):
    is_within_tolerance = check_hover_tolerance(current_altitude, target_altitude, tolerance)
    
    # Update state for hardware
    current_velocity += 0.1 * (random.random() - 0.5)  # Simulate random velocity change
    current_altitude += current_velocity * dt
    
    print(f"[BACKEND] Iteration {i+1}: Altitude={current_altitude:.2f}, Tolerance Status={is_within_tolerance}")

print("\n✅ Hover tolerance checked and status updated for each iteration.")
