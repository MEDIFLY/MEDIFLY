import random
import matplotlib.pyplot as plt
import time

class SensorReadingsInitialization:
    def __init__(self):
        self.time_data = []
        self.temperature_data = []
        self.humidity_data = []
        self.wind_speed_data = []
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate initialization of sensor readings for various environmental factors."""
        for t in range(self.simulation_time):
            # Simulate temperature reading (in Celsius)
            temperature = random.uniform(15, 35)  # Temperature range 15 to 35 degrees Celsius

            # Simulate humidity reading (percentage)
            humidity = random.uniform(40, 80)  # Humidity range 40% to 80%

            # Simulate wind speed reading (in meters per second)
            wind_speed = random.uniform(0, 15)  # Wind speed range 0 to 15 m/s

            # Store data for plotting
            self.time_data.append(t)
            self.temperature_data.append(temperature)
            self.humidity_data.append(humidity)
            self.wind_speed_data.append(wind_speed)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Sensor readings initialization complete.")

    def plot_sensor_readings(self):
        """Plot sensor readings (temperature, humidity, and wind speed) over time."""
        plt.figure(figsize=(12, 8))

        # Plot temperature changes
        plt.subplot(3, 1, 1)
        plt.plot(self.time_data, self.temperature_data, label="Temperature (°C)", color='tab:red')
        plt.title("Temperature Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        plt.legend()

        # Plot humidity changes
        plt.subplot(3, 1, 2)
        plt.plot(self.time_data, self.humidity_data, label="Humidity (%)", color='tab:blue')
        plt.title("Humidity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")
        plt.legend()

        # Plot wind speed changes
        plt.subplot(3, 1, 3)
        plt.plot(self.time_data, self.wind_speed_data, label="Wind Speed (m/s)", color='tab:green')
        plt.title("Wind Speed Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    sensor_readings_init = SensorReadingsInitialization()
    sensor_readings_init.run_simulation()
    sensor_readings_init.plot_sensor_readings()
