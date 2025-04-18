# A80.py – Algorithm 80: Environment Sensor Simulation Class

import random
import time
import matplotlib.pyplot as plt

class EnvironmentalSensorSimulation:
    def __init__(self):
        # Initializing the simulation with empty data dictionary
        self.sensor_data = {}

    # Function to simulate individual environmental sensor data
    def simulate_sensor_data(self):
        # Simulating random environmental sensor data for each factor
        temperature = random.uniform(15, 35)  # Random temperature between 15°C and 35°C
        humidity = random.uniform(30, 80)  # Random humidity between 30% and 80%
        wind_speed = random.uniform(0, 15)  # Random wind speed between 0 m/s and 15 m/s
        air_quality = random.randint(50, 200)  # Random AQI between 50 and 200

        return {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "air_quality": air_quality
        }

    # Function to generate environmental data for a set duration
    def generate_sensor_data(self, duration=10):
        for time_step in range(duration):
            print(f"Simulating environmental data for time step {time_step + 1}...")
            self.sensor_data[time_step] = self.simulate_sensor_data()
            time.sleep(1)  # Simulate a 1-second interval between data points

        print("✅ Environmental data simulation complete.")

    # Function to plot the environmental data
    def plot_sensor_data(self):
        time_steps = list(self.sensor_data.keys())
        temperature = [self.sensor_data[step]['temperature'] for step in time_steps]
        humidity = [self.sensor_data[step]['humidity'] for step in time_steps]
        wind_speed = [self.sensor_data[step]['wind_speed'] for step in time_steps]
        air_quality = [self.sensor_data[step]['air_quality'] for step in time_steps]

        plt.figure(figsize=(12, 6))

        # Plot each environmental factor over time
        plt.subplot(2, 2, 1)
        plt.plot(time_steps, temperature, label='Temperature (°C)', color='orange')
        plt.title('Temperature Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Temperature (°C)')

        plt.subplot(2, 2, 2)
        plt.plot(time_steps, humidity, label='Humidity (%)', color='blue')
        plt.title('Humidity Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Humidity (%)')

        plt.subplot(2, 2, 3)
        plt.plot(time_steps, wind_speed, label='Wind Speed (m/s)', color='green')
        plt.title('Wind Speed Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Wind Speed (m/s)')

        plt.subplot(2, 2, 4)
        plt.plot(time_steps, air_quality, label='Air Quality (AQI)', color='red')
        plt.title('Air Quality Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Air Quality Index (AQI)')

        plt.tight_layout()
        plt.show()

# ------------------------------
# Initialization
# ------------------------------

# Create an instance of the EnvironmentalSensorSimulation class
sensor_simulation = EnvironmentalSensorSimulation()

# Simulate environmental data over a 10-second duration
duration = 10  # Simulating for 10 time steps
sensor_simulation.generate_sensor_data(duration)

# Plot the simulated sensor data
sensor_simulation.plot_sensor_data()
