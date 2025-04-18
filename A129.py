import random
import matplotlib.pyplot as plt
import time

class WindSpeedSensor:
    def __init__(self):
        self.wind_speed = 5  # Initial wind speed in m/s
        self.time_data = []  # For plotting wind speed over time
        self.wind_speed_data = []

    def update_wind_speed(self):
        """Simulate wind speed changes over time."""
        self.wind_speed += random.uniform(-0.2, 0.2)  # Small fluctuation in wind speed

    def simulate_wind_speed_reading(self):
        """Simulate wind speed sensor readings over time."""
        for t in range(50):  # Run for 50 iterations
            self.update_wind_speed()
            self.time_data.append(t)
            self.wind_speed_data.append(self.wind_speed)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print(f"Final Wind Speed: {self.wind_speed} m/s")

    def plot_wind_speed(self):
        """Plot wind speed data over time."""
        plt.plot(self.time_data, self.wind_speed_data, label="Wind Speed (m/s)", color='tab:green')
        plt.title("Wind Speed Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    wind_speed_sensor = WindSpeedSensor()
    wind_speed_sensor.simulate_wind_speed_reading()
    wind_speed_sensor.plot_wind_speed()
