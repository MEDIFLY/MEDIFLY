import random
import matplotlib.pyplot as plt
import time

class SensorReadings:
    def __init__(self):
        self.time_data = []
        self.temperature_data = []
        self.humidity_data = []
        self.wind_speed_data = []
        self.air_quality_data = []

    def print_readings(self):
        """Print the sensor readings in the main loop."""
        for t in range(50):  # Run for 50 iterations
            temperature = random.uniform(15.0, 35.0)
            humidity = random.uniform(30.0, 90.0)
            wind_speed = random.uniform(0.0, 15.0)
            air_quality = random.uniform(60.0, 100.0)

            # Append to lists
            self.time_data.append(t)
            self.temperature_data.append(temperature)
            self.humidity_data.append(humidity)
            self.wind_speed_data.append(wind_speed)
            self.air_quality_data.append(air_quality)

            # Print the current readings for each sensor
            print(f"Time: {t}s | Temp: {temperature:.2f}°C | Humidity: {humidity:.2f}% | Wind Speed: {wind_speed:.2f}m/s | Air Quality: {air_quality:.2f}%")
            
            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Sensor readings printed in the main loop.")

    def plot_sensor_readings(self):
        """Plot the sensor readings over time."""
        plt.figure(figsize=(10, 6))
        
        plt.subplot(2, 2, 1)
        plt.plot(self.time_data, self.temperature_data, label="Temperature (°C)", color='tab:blue')
        plt.title("Temperature Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(self.time_data, self.humidity_data, label="Humidity (%)", color='tab:green')
        plt.title("Humidity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(self.time_data, self.wind_speed_data, label="Wind Speed (m/s)", color='tab:orange')
        plt.title("Wind Speed Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(self.time_data, self.air_quality_data, label="Air Quality (%)", color='tab:red')
        plt.title("Air Quality Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Air Quality (%)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    sensor_readings = SensorReadings()
    sensor_readings.print_readings()
    sensor_readings.plot_sensor_readings()
