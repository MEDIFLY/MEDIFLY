# AI Model 13: AI-Based UAV Communication and Feedback System

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulate UAV communication status and feedback signals
n = 100
time = np.linspace(0, 10, n)
uav_distance = np.linspace(0, 1000, n)  # Simulated UAV distance from base station (in meters)
signal_quality = 100 - 0.05 * uav_distance + np.random.normal(0, 2, n)  # Signal quality decreases with distance

# Simulate feedback reception and transmission
feedback_sent = np.sin(time) * 10  # Simulated feedback signals sent to the base station
feedback_received = feedback_sent + np.random.normal(0, 1, n)  # Received feedback with noise

# BACKEND: Adaptive communication decisions based on distance and signal quality
max_signal_strength = 100  # Maximum signal strength (arbitrary units)
adaptive_range = np.clip(signal_quality, 0, max_signal_strength)  # Adaptive communication range

# Print communication status at the final step
print(f"Final Signal Quality: {signal_quality[-1]:.2f}")
print(f"Feedback Sent: {feedback_sent[-1]:.2f}")
print(f"Feedback Received: {feedback_received[-1]:.2f}")

# Plot 1: Signal Quality vs Distance
plt.figure(figsize=(8, 4))
plt.plot(uav_distance, signal_quality, label='Signal Quality', color='blue')
plt.title("Signal Quality vs Distance")
plt.xlabel("Distance (m)")
plt.ylabel("Signal Quality")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Feedback Sent vs Received
plt.figure(figsize=(8, 4))
plt.plot(feedback_sent, label='Feedback Sent', color='green')
plt.plot(feedback_received, label='Feedback Received', color='red')
plt.title("Feedback Signals Sent vs Received")
plt.xlabel("Time (s)")
plt.ylabel("Feedback Signal")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
