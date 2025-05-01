# AI Model 21: Real-Time Flight Trajectory Adjustment

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Simulated real-time flight data (time, position, speed, heading)
time = np.linspace(0, 100, 500)
position = np.sin(time) * 50  # Simulated UAV position along X-axis
speed = np.cos(time) * 10    # Simulated UAV speed in m/s
heading = np.sin(time) * 30  # Simulated UAV heading (angle)

# Function to simulate obstacle detection and trajectory adjustment
def real_time_trajectory_adjustment(position, speed, heading):
    # Simulate detecting an obstacle and adjusting the trajectory
    if np.random.rand() > 0.95:  # Simulate obstacle detection with 5% chance
        new_heading = heading + 45  # Adjust heading by 45 degrees
        adjusted_position = position + np.sin(new_heading)
        return adjusted_position, new_heading
    else:
        return position, heading

# Adjust trajectory based on real-time conditions
adjusted_position, adjusted_heading = real_time_trajectory_adjustment(position, speed, heading)

# Interpolate the adjusted trajectory using Cubic Spline
cs = CubicSpline(time, adjusted_position)

# Generate new trajectory with adjusted path
new_time = np.linspace(0, 100, 500)
new_position = cs(new_time)

# Function to visualize real-time trajectory adjustment
def plot_trajectory_adjustment():
    plt.figure(figsize=(10, 6))

    # UAV Position vs Time Plot
    plt.subplot(2, 1, 1)
    plt.plot(time, position, label="Original Position", color='blue')
    plt.plot(new_time, new_position, label="Adjusted Position", color='red', linestyle='dashed')
    plt.title("Real-Time UAV Position Adjustment")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.grid(True)
    plt.legend()

    # UAV Heading vs Time Plot
    plt.subplot(2, 1, 2)
    plt.plot(time, heading, label="Original Heading", color='green')
    plt.plot(new_time, np.sin(new_time) * 30 + 45, label="Adjusted Heading", color='purple', linestyle='dashed')
    plt.title("Real-Time UAV Heading Adjustment")
    plt.xlabel("Time (s)")
    plt.ylabel("Heading (degrees)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Visualize the adjusted trajectory and heading
plot_trajectory_adjustment()
