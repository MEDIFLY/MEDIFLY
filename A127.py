import random
import matplotlib.pyplot as plt
import time

class TemperatureSensor:
    def __init__(self):
        self.temperature = 25  # Initial temperature in Celsius
        self.time_data = []  # For plotting temperature over time
        self.temperature_data = []

    def update_temperature(self):
        """Simulate temperature changes over time."""
        self.temperature += random.uniform(-0.5, 0.5)  # Small temperature fluctuations

    def simulate_temperature_reading(self):
        """Simulate temperature sensor readings over time."""
        for t in range(50):  # Run for 50 iterations
            self.update_temperature()
            self.time_data.append(t)
            self.temperature_data.append(self.temperature)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print(f"Final Temperature: {self.temperature}°C")

    def plot_temperature(self):
        """Plot temperature data over time."""
        plt.plot(self.time_data, self.temperature_data, label="Temperature (°C)", color='tab:red')
        plt.title("Temperature Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    temp_sensor = TemperatureSensor()
    temp_sensor.simulate_temperature_reading()
    temp_sensor.plot_temperature()
