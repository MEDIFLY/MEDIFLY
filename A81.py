# A81.py – Algorithm 81: Sensor Simulation

import random
import time
import matplotlib.pyplot as plt

class SensorSimulation:
    def __init__(self, sensor_type="Temperature"):
        # Initializing the sensor with a default type of "Temperature"
        self.sensor_type = sensor_type
        self.sensor_data = []

    # Function to simulate data for different sensor types
    def simulate_sensor_data(self):
        if self.sensor_type == "Temperature":
            return random.uniform(15, 35)  # Temperature between 15°C and 35°C
        elif self.sensor_type == "Humidity":
            return random.uniform(30, 80)  # Humidity between 30% and 80%
        elif self.sensor_type == "WindSpeed":
            return random.uniform(0, 15)  # Wind speed between 0 m/s and 15 m/s
        elif self.sensor_type == "AirQuality":
            return random.randint(50, 200)  # Air Quality Index between 50 and 200
        else:
            raise ValueError(f"Unknown sensor type: {self.sensor_type}")

    # Function to simulate the sensor over a given duration
    def generate_sensor_data(self, duration=10):
        print(f"Simulating {self.sensor_type} sensor data...")
        for time_step in range(duration):
            data = self.simulate_sensor_data()
            self.sensor_data.append(data)
            print(f"Time Step {time_step+1}: {data}")
            time.sleep(1)  # Simulate a 1-second interval between readings

        print("✅ Sensor data simulation complete.")

    # Function to plot the simulated sensor data
    def plot_sensor_data(self):
        time_steps = range(1, len(self.sensor_data) + 1)

        plt.figure(figsize=(8, 5))
        plt.plot(time_steps, self.sensor_data, label=f'{self.sensor_type} Data', color='blue')
        plt.title(f'{self.sensor_type} Sensor Data Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel(f'{self.sensor_type} Value')
        plt.legend()
        plt.grid(True)
        plt.show()

# ------------------------------
# Initialization
# ------------------------------

# Create an instance of the SensorSimulation class for "Temperature"
temperature_sensor = SensorSimulation(sensor_type="Temperature")

# Simulate temperature data over 10 seconds
temperature_sensor.generate_sensor_data(duration=10)

# Plot the temperature sensor data
temperature_sensor.plot_sensor_data()

# You can repeat the process for other types of sensors, like Humidity or WindSpeed
# Example:
# humidity_sensor = SensorSimulation(sensor_type="Humidity")
# humidity_sensor.generate_sensor_data(duration=10)
# humidity_sensor.plot_sensor_data()
