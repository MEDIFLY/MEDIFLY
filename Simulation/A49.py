# ----------------------------------------------------
# Algorithm 49: Hover Control Loop
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random

# =======================
# FRONTEND: Simulation
# =======================

# PID Constants
kp = 0.5
ki = 0.1
kd = 0.01

target_altitude = 10.0

# Initial States
altitudes = []
thrust_outputs = []

error_z_prev = 0
error_z_sum = 0
current_altitude = round(random.uniform(8.0, 12.0), 2)

print("🎮 FRONTEND SIMULATION (Hover Control Loop):")
for i in range(5):  # 5 Iterations
    # Calculate error
    error_z = target_altitude - current_altitude

    # PID Components
    error_z_sum += error_z
    d_error = error_z - error_z_prev
    pid_output = kp * error_z + ki * error_z_sum + kd * d_error

    # Update thrust (for simulation, assume linear effect on altitude)
    thrust = pid_output
    current_altitude += thrust * 0.1  # Altitude influenced by thrust

    # Save and print
    altitudes.append(current_altitude)
    thrust_outputs.append(thrust)

    print(f"Iteration {i+1}: error_z={error_z:.2f}, thrust={thrust:.2f}, new_altitude={current_altitude:.2f}")

    error_z_prev = error_z

# 🎨 Plot Altitude and Thrust Over Time
plt.figure(figsize=(10, 5))
plt.plot(range(1, 6), altitudes, 'bo-', label='Simulated Altitude')
plt.plot(range(1, 6), thrust_outputs, 'r*-', label='PID Thrust Output')
plt.axhline(y=target_altitude, color='g', linestyle='--', label='Target Altitude')
plt.title("Algorithm 49 - Hover Control Loop Simulation")
plt.xlabel("Iteration")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE LOGIC:")
error_z_prev = 0
error_z_sum = 0
altitude_hw = altitudes[0]  # Starting from first simulated value

for i in range(5):
    error_z = target_altitude - altitude_hw
    error_z_sum += error_z
    d_error = error_z - error_z_prev

    pid_output = kp * error_z + ki * error_z_sum + kd * d_error
    thrust = pid_output
    altitude_hw += thrust * 0.1  # Simulating hardware altitude change

    print(f"[BACKEND] Iteration {i+1}: error={error_z:.2f} | PID={pid_output:.2f} | Altitude={altitude_hw:.2f}")

    error_z_prev = error_z

print("\n✅ Hover loop logic executed successfully for both simulation and hardware.")
