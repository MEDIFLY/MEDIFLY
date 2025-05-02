import random
import matplotlib.pyplot as plt
import time

class SensorSimulation:
    def __init__(self):
        self.temperature = 25  # Initial temperature in Celsius
        self.humidity = 50     # Initial humidity in percentage
        self.wind_speed = 2    # Initial wind speed in m/s
        self.air_quality = 150 # Initial air quality index
        self.time_data = []    # Time stamps for plotting
        self.sensor_data = {"Temperature": [], "Humidity": [], "Wind Speed": [], "Air Quality": []}

    def update_sensors(self):
        """Simulate sensor updates over time."""
        self.temperature += random.uniform(-0.5, 0.5)  # Slight temperature change
        self.humidity += random.uniform(-2, 2)          # Slight humidity change
        self.wind_speed += random.uniform(-0.2, 0.2)    # Wind speed variation
        self.air_quality += random.uniform(-1, 1)       # Air quality fluctuation

    def simulate_sensor_reading(self):
        """Simulate the main loop for sensor readings over time."""
        for t in range(50):  # Run for 50 iterations
            self.update_sensors()
            self.time_data.append(t)
            self.sensor_data["Temperature"].append(self.temperature)
            self.sensor_data["Humidity"].append(self.humidity)
            self.sensor_data["Wind Speed"].append(self.wind_speed)
            self.sensor_data["Air Quality"].append(self.air_quality)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print(f"Final Sensor Readings: Temperature={self.temperature}°C, Humidity={self.humidity}%, Wind Speed={self.wind_speed} m/s, Air Quality={self.air_quality}")

    def plot_sensor_data(self):
        """Plot sensor data (temperature, humidity, wind speed, air quality) over time."""
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 2, 1)
        plt.plot(self.time_data, self.sensor_data["Temperature"], label="Temperature (°C)", color='tab:red')
        plt.title("Temperature Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")

        plt.subplot(2, 2, 2)
        plt.plot(self.time_data, self.sensor_data["Humidity"], label="Humidity (%)", color='tab:blue')
        plt.title("Humidity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")

        plt.subplot(2, 2, 3)
        plt.plot(self.time_data, self.sensor_data["Wind Speed"], label="Wind Speed (m/s)", color='tab:green')
        plt.title("Wind Speed Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")

        plt.subplot(2, 2, 4)
        plt.plot(self.time_data, self.sensor_data["Air Quality"], label="Air Quality (AQI)", color='tab:orange')
        plt.title("Air Quality Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Air Quality (AQI)")

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    sensor_sim = SensorSimulation()
    sensor_sim.simulate_sensor_reading()
    sensor_sim.plot_sensor_data()
