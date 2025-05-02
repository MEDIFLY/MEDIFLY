# AI Model 24: Dynamic Landing and Automatic Return to Base

import numpy as np
import matplotlib.pyplot as plt

# Simulated UAV telemetry data
time = np.linspace(0, 100, 500)
battery_level = 100 - (time * 0.3)  # Simulate battery drain
uav_position = np.c_[np.sin(time) * 50, np.cos(time) * 50, np.abs(np.sin(time)) * 100]  # Simulate UAV trajectory

# Define home/base coordinates (target location)
home_location = np.array([0, 0, 0])

# Function to compute return-to-home path
def return_to_home(uav_position, home_location):
    # Calculate straight-line return path (ignoring obstacles for simplicity)
    path_x = np.linspace(uav_position[-1, 0], home_location[0], len(uav_position))
    path_y = np.linspace(uav_position[-1, 1], home_location[1], len(uav_position))
    path_z = np.linspace(uav_position[-1, 2], home_location[2], len(uav_position))

    return np.c_[path_x, path_y, path_z]

# Function to detect low battery and initiate landing
def check_battery_and_land(battery_level):
    if battery_level[-1] < 20:
        return True  # Initiate landing
    return False

# Simulate return-to-home and landing
land = check_battery_and_land(battery_level)
return_path = return_to_home(uav_position, home_location) if land else uav_position

# Plot UAV Return-to-Home and Landing Path
def plot_return_to_home():
    plt.figure(figsize=(10, 6))

    # Plot UAV return-to-home path
    plt.subplot(2, 1, 1)
    plt.plot(uav_position[:, 0], uav_position[:, 1], label="UAV Path")
    plt.plot(return_path[:, 0], return_path[:, 1], label="Return-to-Home Path", linestyle='--')
    plt.scatter(home_location[0], home_location[1], color='red', label="Home Location")
    plt.title("UAV Return-to-Home Path")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.grid(True)
    plt.legend()

    # Plot UAV Altitude vs Time (Landing)
    plt.subplot(2, 1, 2)
    plt.plot(time, uav_position[:, 2], label="UAV Altitude")
    plt.axhline(0, color='black', linestyle='--', label="Ground Level")
    plt.title("UAV Altitude During Return-to-Home")
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Print landing status
landing_status = "Initiating Landing" if land else "Normal Flight"
print(f"Battery Level: {battery_level[-1]:.2f}%")
print(f"Landing Status: {landing_status}")

# Visualize the UAV's Return-to-Home path and landing
plot_return_to_home()
