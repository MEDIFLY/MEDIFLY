# AI Model 27: UAV Fault Detection and Recovery System

import numpy as np
import matplotlib.pyplot as plt

# Simulated UAV system status (e.g., motors, battery, GPS)
time = np.linspace(0, 100, 500)
motor_health = np.random.uniform(0.8, 1.0, size=(len(time)))  # Simulate motor health (1 = healthy)
gps_accuracy = np.random.normal(loc=1.0, scale=0.05, size=(len(time)))  # Simulate GPS accuracy
battery_level = 100 - (time * 0.25)  # Simulate battery drain
fault_threshold = 0.2  # Set fault threshold for motor health and GPS accuracy

# Function to detect faults
def detect_faults(motor_health, gps_accuracy, battery_level):
    faults = []
    
    # Check if motor health drops below threshold
    if np.any(motor_health < fault_threshold):
        faults.append("Motor Health Fault")
    
    # Check if GPS accuracy drops below threshold
    if np.any(gps_accuracy < fault_threshold):
        faults.append("GPS Accuracy Fault")
    
    # Check if battery is low
    if battery_level[-1] < 20:
        faults.append("Battery Low")
    
    return faults

# Function to execute fault recovery protocols
def recovery_protocol(faults):
    if "Motor Health Fault" in faults:
        return "Activating backup motor system"
    elif "GPS Accuracy Fault" in faults:
        return "Switching to backup GPS system"
    elif "Battery Low" in faults:
        return "Initiating emergency landing protocol"
    else:
        return "No faults detected, normal operation"

# Function to plot system health
def plot_system_health():
    plt.figure(figsize=(10, 6))

    # Plot motor health over time
    plt.subplot(3, 1, 1)
    plt.plot(time, motor_health, label="Motor Health", color='green')
    plt.axhline(fault_threshold, color='red', linestyle='--', label="Fault Threshold")
    plt.title("Motor Health During Flight")
    plt.xlabel("Time (s)")
    plt.ylabel("Motor Health")
    plt.legend()
    plt.grid(True)

    # Plot GPS accuracy over time
    plt.subplot(3, 1, 2)
    plt.plot(time, gps_accuracy, label="GPS Accuracy", color='blue')
    plt.axhline(fault_threshold, color='red', linestyle='--', label="Fault Threshold")
    plt.title("GPS Accuracy During Flight")
    plt.xlabel("Time (s)")
    plt.ylabel("GPS Accuracy")
    plt.legend()
    plt.grid(True)

    # Plot battery level over time
    plt.subplot(3, 1, 3)
    plt.plot(time, battery_level, label="Battery Level", color='orange')
    plt.axhline(20, color='red', linestyle='--', label="Low Battery Threshold")
    plt.title("Battery Level During Flight")
    plt.xlabel("Time (s)")
    plt.ylabel("Battery Level (%)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Run fault detection and recovery
faults = detect_faults(motor_health, gps_accuracy, battery_level)
recovery_action = recovery_protocol(faults)

# Print fault detection and recovery actions
if faults:
    print("Detected Faults:", faults)
    print("Recovery Action:", recovery_action)
else:
    print("No faults detected. System is operating normally.")

# Visualize system health
plot_system_health()
