# AI Model 18: User Interface and Mission Control Dashboard

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# Simulated UAV data (position, speed, battery level)
uav_position = np.sin(np.linspace(0, 10, 100)) * 50  # UAV position (X-axis)
uav_speed = np.cos(np.linspace(0, 10, 100)) * 10  # UAV speed (m/s)
battery_level = np.linspace(100, 0, 100)  # Battery level percentage

# Function to create the main control panel UI
def create_ui():
    window = tk.Tk()
    window.title("UAV Mission Control Dashboard")
    window.geometry("600x400")

    # Labels for UAV status display
    tk.Label(window, text="UAV Mission Control", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2)
    
    # UAV Status
    tk.Label(window, text="Current Position (m):").grid(row=1, column=0)
    position_display = tk.Label(window, text=f"{uav_position[-1]:.2f} m")
    position_display.grid(row=1, column=1)

    tk.Label(window, text="Current Speed (m/s):").grid(row=2, column=0)
    speed_display = tk.Label(window, text=f"{uav_speed[-1]:.2f} m/s")
    speed_display.grid(row=2, column=1)

    tk.Label(window, text="Battery Level (%):").grid(row=3, column=0)
    battery_display = tk.Label(window, text=f"{battery_level[-1]:.2f}%")
    battery_display.grid(row=3, column=1)

    # Button to update data
    def update_data():
        position_display.config(text=f"{uav_position[-1]:.2f} m")
        speed_display.config(text=f"{uav_speed[-1]:.2f} m/s")
        battery_display.config(text=f"{battery_level[-1]:.2f}%")
        
    update_button = tk.Button(window, text="Update Data", command=update_data)
    update_button.grid(row=4, column=0, columnspan=2)

    # Start the UI
    window.mainloop()

# Function to plot UAV data (real-time visualization)
def plot_uav_data():
    plt.figure(figsize=(10, 6))

    # UAV Position and Speed Plot
    plt.subplot(2, 1, 1)
    plt.plot(uav_position, label='UAV Position', color='blue')
    plt.title("UAV Position Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    plt.grid(True)
    plt.legend()

    # Battery Level Plot
    plt.subplot(2, 1, 2)
    plt.plot(battery_level, label='Battery Level', color='red')
    plt.title("UAV Battery Level Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Battery Level (%)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Create UI and plot data
create_ui()
plot_uav_data()
