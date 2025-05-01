# AI Model 10: Flight Controller Coding and UAV System Integration

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulate controller and IMU data
n = 100
time = np.linspace(0, 10, n)
desired_pitch = np.sin(time) * 10  # Commanded pitch in degrees
imu_pitch = desired_pitch + np.random.normal(0, 2, n)  # Sensor reading with noise

# PID controller initialization
Kp = 1.2
Ki = 0.02
Kd = 0.6

error_sum = 0
last_error = 0
pitch_output = []

for i in range(n):
    error = desired_pitch[i] - imu_pitch[i]
    error_sum += error
    d_error = error - last_error

    output = Kp * error + Ki * error_sum + Kd * d_error
    pitch_output.append(output)
    last_error = error

# Normalize outputs to motor PWM range (1000-2000)
def normalize_pwm(val):
    return int(np.clip(1500 + val * 10, 1000, 2000))

motor_pwm = [normalize_pwm(o) for o in pitch_output]

# BACKEND: Print final motor signal and system status
print(f"Final PWM Command to Motor: {motor_pwm[-1]}")
print(f"Stabilization Output at Final Step: {pitch_output[-1]:.2f}")

# Plot 1: Command vs IMU Reading
plt.figure(figsize=(8, 4))
plt.plot(desired_pitch, label='Desired Pitch', color='blue')
plt.plot(imu_pitch, label='IMU Pitch (Sensor)', color='red', alpha=0.6)
plt.title("Command vs IMU Sensor Pitch")
plt.xlabel("Time Step")
plt.ylabel("Pitch (degrees)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: PID Output (Motor Control)
plt.figure(figsize=(8, 4))
plt.plot(pitch_output, label='PID Output', color='green')
plt.plot(motor_pwm, label='Motor PWM', color='purple', linestyle='--')
plt.title("PID Controller Output and Motor PWM Signal")
plt.xlabel("Time Step")
plt.ylabel("Control Output")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
