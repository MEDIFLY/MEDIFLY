# A82.py – Algorithm 82: State Updates for Environmental Simulation

import random
import time
import matplotlib.pyplot as plt

class EnvironmentalSimulation:
    def __init__(self):
        # Initializing environmental state variables
        self.temperature = 25  # Initial temperature in Celsius
        self.humidity = 50  # Initial humidity percentage
        self.wind_speed = 5  # Initial wind speed in m/s

        # Data storage for simulation
        self.temperature_data = []
        self.humidity_data = []
        self.wind_speed_data = []

    # Function to simulate random environmental changes (temperature, humidity, wind speed)
    def update_environmental_conditions(self):
        # Simulate environmental changes within realistic ranges
        self.temperature += random.uniform(-0.5, 0.5)  # Temperature changes by ±0.5°C
        self.humidity += random.uniform(-2, 2)  # Humidity changes by ±2%
        self.wind_speed += random.uniform(-0.5, 0.5)  # Wind speed changes by ±0.5 m/s

        # Keeping the values within realistic bounds
        self.temperature = max(0, min(self.temperature, 45))  # Temperature between 0°C and 45°C
        self.humidity = max(0, min(self.humidity, 100))  # Humidity between 0% and 100%
        self.wind_speed = max(0, min(self.wind_speed, 20))  # Wind speed between 0 m/s and 20 m/s

    # Function to simulate environmental conditions over a given duration
    def simulate_environment(self, duration=10):
        print("Simulating environmental state updates...")
        for time_step in range(duration):
            self.update_environmental_conditions()

            # Record the updated environmental data
            self.temperature_data.append(self.temperature)
            self.humidity_data.append(self.humidity)
            self.wind_speed_data.append(self.wind_speed)

            print(f"Time Step {time_step + 1}: Temperature={self.temperature:.2f}°C, "
                  f"Humidity={self.humidity:.2f}%, Wind Speed={self.wind_speed:.2f} m/s")
            time.sleep(1)  # Simulate a 1-second interval between updates

        print("✅ Environmental state simulation complete.")

    # Function to plot the simulated environmental data
    def plot_environmental_data(self):
        time_steps = range(1, len(self.temperature_data) + 1)

        # Plotting the temperature, humidity, and wind speed over time
        plt.figure(figsize=(10, 6))
        plt.plot(time_steps, self.temperature_data, label='Temperature (°C)', color='red')
        plt.plot(time_steps, self.humidity_data, label='Humidity (%)', color='blue')
        plt.plot(time_steps, self.wind_speed_data, label='Wind Speed (m/s)', color='green')
        plt.title('Environmental Conditions Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Environmental Value')
        plt.legend()
        plt.grid(True)
        plt.show()

# ------------------------------
# Initialization
# ------------------------------

# Create an instance of the EnvironmentalSimulation class
env_simulation = EnvironmentalSimulation()

# Simulate environmental state updates over 10 seconds
env_simulation.simulate_environment(duration=10)

# Plot the environmental data
env_simulation.plot_environmental_data()
