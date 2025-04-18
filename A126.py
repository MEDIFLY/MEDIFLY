import random
import matplotlib.pyplot as plt
import time

class DroneControlFunctions:
    def __init__(self):
        self.battery = 100  # Full battery at start
        self.altitude = 0   # Starting altitude
        self.wind_speed = 2  # Starting wind speed
        self.temperature = 25  # Starting temperature in Celsius
        self.time_data = []  # For plotting
        self.battery_data = []
        self.altitude_data = []

    def check_battery(self):
        """Simulate battery check during flight."""
        self.battery -= random.uniform(0.1, 0.5)  # Battery drains over time

    def update_altitude(self):
        """Simulate altitude changes during flight."""
        self.altitude += random.uniform(0.5, 1.5)  # Increase altitude gradually

    def update_weather(self):
        """Simulate weather/environment changes."""
        self.wind_speed += random.uniform(-0.5, 0.5)  # Wind speed fluctuation
        self.temperature += random.uniform(-0.2, 0.2)  # Temperature change

    def simulate_flight_operations(self):
        """Simulate the main flight loop with environmental and drone control functions."""
        for t in range(50):  # Simulate for 50 iterations
            self.check_battery()
            self.update_altitude()
            self.update_weather()

            self.time_data.append(t)
            self.battery_data.append(self.battery)
            self.altitude_data.append(self.altitude)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

            if self.battery <= 10:
                print("Battery critically low! Returning to base...")
                break

        print(f"Final Altitude: {self.altitude} meters")
        print(f"Final Battery Status: {self.battery}%")

    def plot_flight_data(self):
        """Plot flight data including battery and altitude over time."""
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.battery_data, label="Battery Level (%)", color='tab:red')
        plt.title("Battery Level Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Battery Level (%)")

        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.altitude_data, label="Altitude (m)", color='tab:blue')
        plt.title("Altitude Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    drone_control = DroneControlFunctions()
    drone_control.simulate_flight_operations()
    drone_control.plot_flight_data()
