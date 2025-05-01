# AI Model 23: Adaptive Failure Recovery and Safety Measures

import numpy as np
import matplotlib.pyplot as plt

# Simulated UAV telemetry data (time, battery level, motor status)
time = np.linspace(0, 100, 500)
battery_level = 100 - (time * 0.2)  # Simulate battery drain
motor_status = np.ones_like(time)  # Simulated motor health status (1 = healthy, 0 = failure)
motor_status[300:] = 0  # Simulate motor failure after time = 60 seconds

# Function to detect failure (e.g., battery low, motor failure)
def detect_failure(battery_level, motor_status):
    if battery_level[-1] < 20:
        return "Battery Low"
    elif np.any(motor_status == 0):
        return "Motor Failure"
    else:
        return "Normal"

# Function to perform recovery actions
def recovery_action(failure_type):
    if failure_type == "Battery Low":
        return "Initiating Emergency Landing"
    elif failure_type == "Motor Failure":
        return "Switching to Backup Motor"
    else:
        return "Continuing Normal Operations"

# Detect failure and initiate recovery action
failure_type = detect_failure(battery_level, motor_status)
recovery = recovery_action(failure_type)

# Plot UAV Battery Level and Motor Health
def plot_failure_recovery():
    plt.figure(figsize=(10, 6))

    # Battery Level vs Time Plot
    plt.subplot(2, 1, 1)
    plt.plot(time, battery_level, label="Battery Level", color='red')
    plt.axhline(y=20, color='black', linestyle='--', label="Low Battery Threshold")
    plt.title("UAV Battery Level and Failure Detection")
    plt.xlabel("Time (s)")
    plt.ylabel("Battery Level (%)")
    plt.grid(True)
    plt.legend()

    # Motor Health vs Time Plot
    plt.subplot(2, 1, 2)
    plt.plot(time, motor_status, label="Motor Health", color='blue')
    plt.axhline(y=0, color='black', linestyle='--', label="Motor Failure")
    plt.title("UAV Motor Health Status")
    plt.xlabel("Time (s)")
    plt.ylabel("Motor Status (1 = Healthy, 0 = Failure)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Print the recovery action taken
print(f"Failure Detected: {failure_type}")
print(f"Recovery Action: {recovery}")

# Visualize Failure Recovery Process
plot_failure_recovery()
