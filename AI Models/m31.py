import numpy as np
import matplotlib.pyplot as plt

# Simulate real-time data for energy optimization and load balancing
time = np.linspace(0, 120, 600)  # Flight time (0 to 120 minutes)
altitude = 100 - (time * 0.2)  # Simulated altitude (drops over time)
battery_level = 100 - (time * 0.25)  # Simulated battery consumption (drops over time)
load = np.random.uniform(1, 5, len(time))  # Simulated load (in kg)
wind_speed = np.random.uniform(5, 15, len(time))  # Simulated wind speed (affects energy)
solar_energy = np.sin(time / 10) * 10 + 30  # Simulated solar energy contribution
energy_used = 0.5 * (altitude * load) / 100  # Simplified energy usage model

# Energy optimization and load balancing model
def energy_optimization(altitude, battery_level, load, energy_used, wind_speed, solar_energy):
    # Simulate energy consumption with factors like load, wind speed, and solar energy
    energy_needed = energy_used + (load * wind_speed / 100) - (solar_energy / 100)
    
    # Check if battery is enough
    energy_status = "Battery Sufficient" if np.all(battery_level >= energy_needed) else "Battery Low"
    
    # Simulate load balancing: if load is too high, reduce it
    load_balanced = np.where(load > 4, load * 0.9, load)  # Reduce load by 10% if above 4 kg
    
    return energy_needed, energy_status, load_balanced

# Function to visualize energy optimization and load balancing
def plot_energy_optimization(altitude, battery_level, energy_used, energy_needed, load, load_balanced):
    plt.figure(figsize=(12, 8))

    # Plot altitude vs battery level
    plt.subplot(3, 1, 1)
    plt.plot(time, altitude, label="Altitude (m)", color='blue')
    plt.plot(time, battery_level, label="Battery Level (%)", color='green')
    plt.title("UAV Altitude and Battery Level")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Altitude (m) / Battery Level (%)")
    plt.legend()
    plt.grid(True)

    # Plot energy usage and energy required
    plt.subplot(3, 1, 2)
    plt.plot(time, energy_used, label="Energy Used (kWh)", color='red')
    plt.plot(time, energy_needed, label="Energy Needed (kWh)", color='orange')
    plt.title("Energy Usage and Optimization")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Energy (kWh)")
    plt.legend()
    plt.grid(True)

    # Plot load vs balanced load
    plt.subplot(3, 1, 3)
    plt.plot(time, load, label="Load (kg)", color='purple')
    plt.plot(time, load_balanced, label="Balanced Load (kg)", color='cyan')
    plt.title("Load vs Balanced Load")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Load (kg)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Perform energy optimization and load balancing
energy_needed, energy_status, load_balanced = energy_optimization(altitude, battery_level, load, energy_used, wind_speed, solar_energy)

# Print energy status
print(f"Energy Status: {energy_status}")

# Visualize energy optimization and load balancing
plot_energy_optimization(altitude, battery_level, energy_used, energy_needed, load, load_balanced)
