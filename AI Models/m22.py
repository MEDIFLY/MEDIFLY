# AI Model 22: UAV Mission Progress Monitoring

import numpy as np
import matplotlib.pyplot as plt

# Simulate UAV mission parameters
mission_time = np.linspace(0, 100, 500)
position = np.sin(mission_time) * 50  # Simulated UAV position
battery_level = 100 - (mission_time * 0.2)  # Battery drain over time
task_completion = np.minimum(mission_time / 100, 1)  # Simulate task completion as time progresses

# Function to monitor UAV performance
def monitor_uav_performance(position, battery_level, task_completion):
    # Predict mission status based on task completion
    if task_completion[-1] == 1.0:
        mission_status = "Mission Completed"
    elif battery_level[-1] < 20:
        mission_status = "Battery Low"
    else:
        mission_status = "Mission In Progress"

    return mission_status

# Simulate mission status monitoring
mission_status = monitor_uav_performance(position, battery_level, task_completion)

# Plot UAV Mission Progress
def plot_mission_progress():
    plt.figure(figsize=(10, 6))

    # Task Completion vs Time Plot
    plt.subplot(2, 1, 1)
    plt.plot(mission_time, task_completion, label="Task Completion", color='blue')
    plt.title("UAV Mission Progress Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Task Completion (%)")
    plt.grid(True)
    plt.legend()

    # Battery Level vs Time Plot
    plt.subplot(2, 1, 2)
    plt.plot(mission_time, battery_level, label="Battery Level", color='green')
    plt.title("UAV Battery Level Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Battery Level (%)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Display Mission Status
print(f"Mission Status: {mission_status}")

# Visualize Mission Progress
plot_mission_progress()
