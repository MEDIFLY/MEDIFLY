# AI Model 12: AI-Based Energy Optimization and Load Balancing

import numpy as np
import matplotlib.pyplot as plt

# FRONTEND: Simulate battery and power consumption data
n = 100
time = np.linspace(0, 10, n)
battery_voltage = 12 - 0.05 * time  # Simulated battery voltage decrease over time
battery_current = 2 + 0.1 * np.sin(time)  # Simulated current consumption with slight fluctuations
total_power_consumption = battery_voltage * battery_current  # Power consumption in watts

# Simulated power distribution to motors and sensors
motor_power = np.random.normal(15, 3, n)  # Random power consumption for motors
sensor_power = np.random.normal(5, 1, n)  # Random power consumption for sensors

# BACKEND: Energy optimization and load balancing
total_power_available = 100  # Total available power in watts
motor_load_ratio = motor_power / total_power_consumption
sensor_load_ratio = sensor_power / total_power_consumption

# Calculate adjusted power distribution based on energy levels
adjusted_motor_power = motor_load_ratio * total_power_available
adjusted_sensor_power = sensor_load_ratio * total_power_available

# Print final power distribution
print(f"Total Available Power: {total_power_available} W")
print(f"Adjusted Motor Power: {np.mean(adjusted_motor_power):.2f} W")
print(f"Adjusted Sensor Power: {np.mean(adjusted_sensor_power):.2f} W")

# Plot 1: Battery Voltage and Power Consumption
plt.figure(figsize=(8, 4))
plt.plot(time, battery_voltage, label='Battery Voltage (V)', color='blue')
plt.plot(time, total_power_consumption, label='Total Power Consumption (W)', color='red')
plt.title("Battery Voltage and Power Consumption")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V) / Power (W)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot 2: Power Distribution to Motors and Sensors
plt.figure(figsize=(8, 4))
plt.plot(time, motor_power, label='Motor Power Consumption (W)', color='green')
plt.plot(time, sensor_power, label='Sensor Power Consumption (W)', color='orange')
plt.plot(time, adjusted_motor_power, label='Adjusted Motor Power (W)', linestyle='--', color='darkgreen')
plt.plot(time, adjusted_sensor_power, label='Adjusted Sensor Power (W)', linestyle='--', color='darkorange')
plt.title("Power Distribution to Motors and Sensors")
plt.xlabel("Time (s)")
plt.ylabel("Power (W)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
