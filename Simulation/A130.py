import random
import matplotlib.pyplot as plt
import time

class AirQualitySensor:
    def __init__(self):
        self.air_quality = 75  # Initial air quality percentage
        self.time_data = []  # For plotting air quality over time
        self.air_quality_data = []

    def update_air_quality(self):
        """Simulate air quality changes over time."""
        self.air_quality += random.uniform(-2.0, 2.0)  # Small fluctuation in air quality

    def simulate_air_quality_reading(self):
        """Simulate air quality sensor readings over time."""
        for t in range(50):  # Run for 50 iterations
            self.update_air_quality()
            self.time_data.append(t)
            self.air_quality_data.append(self.air_quality)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print(f"Final Air Quality: {self.air_quality}%")

    def plot_air_quality(self):
        """Plot air quality data over time."""
        plt.plot(self.time_data, self.air_quality_data, label="Air Quality (%)", color='tab:red')
        plt.title("Air Quality Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Air Quality (%)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    air_quality_sensor = AirQualitySensor()
    air_quality_sensor.simulate_air_quality_reading()
    air_quality_sensor.plot_air_quality()
