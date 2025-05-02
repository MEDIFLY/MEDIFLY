import random
import matplotlib.pyplot as plt
import time

class HumiditySensor:
    def __init__(self):
        self.humidity = 50  # Initial humidity in percentage
        self.time_data = []  # For plotting humidity over time
        self.humidity_data = []

    def update_humidity(self):
        """Simulate humidity changes over time."""
        self.humidity += random.uniform(-1.0, 1.0)  # Small fluctuation in humidity

    def simulate_humidity_reading(self):
        """Simulate humidity sensor readings over time."""
        for t in range(50):  # Run for 50 iterations
            self.update_humidity()
            self.time_data.append(t)
            self.humidity_data.append(self.humidity)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print(f"Final Humidity: {self.humidity}%")

    def plot_humidity(self):
        """Plot humidity data over time."""
        plt.plot(self.time_data, self.humidity_data, label="Humidity (%)", color='tab:blue')
        plt.title("Humidity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    humidity_sensor = HumiditySensor()
    humidity_sensor.simulate_humidity_reading()
    humidity_sensor.plot_humidity()
