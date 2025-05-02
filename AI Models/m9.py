# AI Model 9: Sensor Fusion and Kalman Filters for Flight Stability

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulated IMU data with noise
n = 100
true_angle = np.linspace(0, 10, n)  # Simulated true angle over time
gyro_data = true_angle + np.random.normal(0, 0.8, n)  # Noisy gyroscope data
accel_data = true_angle + np.random.normal(0, 1.2, n)  # Noisy accelerometer data

# Kalman filter initialization
angle_estimate = 0
bias = 0
P = np.array([[1, 0], [0, 1]])  # Initial error covariance
Q = np.array([[0.01, 0], [0, 0.03]])  # Process noise covariance
R = 0.5  # Measurement noise covariance

dt = 0.1  # Time step
estimates = []

for i in range(n):
    # Prediction step
    rate = gyro_data[i] - bias
    angle_estimate += dt * rate
    P = P + dt * (np.dot(np.dot(np.array([[1, -dt], [0, 1]]), P), np.array([[1, -dt], [0, 1]]).T)) + Q

    # Update step
    S = P[0, 0] + R
    K = np.array([P[0, 0]/S, P[1, 0]/S])
    y = accel_data[i] - angle_estimate
    angle_estimate = angle_estimate + K[0] * y
    bias = bias + K[1] * y
    P = P - np.outer(K, P[0])

    estimates.append(angle_estimate)

# Plot 1: Comparison of signals
plt.figure(figsize=(8, 4))
plt.plot(true_angle, label='True Angle', linestyle='--', color='black')
plt.plot(gyro_data, label='Gyro (Noisy)', alpha=0.6)
plt.plot(accel_data, label='Accel (Noisy)', alpha=0.6)
plt.plot(estimates, label='Kalman Estimate', linewidth=2, color='green')
plt.title("Sensor Fusion using Kalman Filter")
plt.xlabel("Time Step")
plt.ylabel("Angle (degrees)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# BACKEND: Output final stability result
final_estimate = estimates[-1]
drift_error = true_angle[-1] - final_estimate
print(f"Final Estimated Angle: {final_estimate:.2f}°")
print(f"Drift Error Corrected: {drift_error:.2f}°")
