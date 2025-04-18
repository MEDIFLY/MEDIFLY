# ----------------------------------------------------
# Algorithm 51: Calculate PID Output Function
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

def calculate_pid_output(error, prev_error, sum_error):
    """Returns the PID control output based on given values."""
    derivative = error - prev_error
    output = kp * error + ki * sum_error + kd * derivative
    return output

# Simulate 5 errors
target_altitude = 10.0
altitudes = [round(random.uniform(8.5, 11.5), 2) for _ in range(5)]
errors = []
pid_outputs = []
sum_error = 0
prev_error = 0

print("🎮 FRONTEND PID OUTPUT CALCULATION:")

for i in range(5):
    error = target_altitude - altitudes[i]
    sum_error += error
    pid_output = calculate_pid_output(error, prev_error, sum_error)

    errors.append(error)
    pid_outputs.append(pid_output)
    print(f"Iteration {i+1}: error={error:.2f}, PID Output={pid_output:.2f}")

    prev_error = error

# 🎨 Plot PID Output
plt.figure(figsize=(10, 5))
plt.plot(range(1, 6), pid_outputs, 'co-', label='PID Output')
plt.axhline(y=0, color='gray', linestyle='--', label='Zero Output Line')
plt.title("Algorithm 51 - PID Output Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("PID Output (Thrust Units)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND HARDWARE PID EXECUTION:")

sum_error = 0
prev_error = 0

for i in range(5):
    actual = altitudes[i]
    error = target_altitude - actual
    sum_error += error
    pid_output = calculate_pid_output(error, prev_error, sum_error)
    print(f"[BACKEND] Iteration {i+1}: Actual={actual:.2f}, PID Output={pid_output:.2f}")
    prev_error = error

print("\n✅ PID Output function ready for integration into thrust control.")
