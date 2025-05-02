import random
import matplotlib.pyplot as plt
import time

class SimulationManagement:
    def __init__(self):
        self.time_data = []
        self.battery_data = []
        self.altitude_data = []
        self.battery_level = 100  # Initial battery level (percent)
        self.altitude = 0  # Initial altitude (m)

    def manage_simulation(self):
        """Simulate basic flight operations like battery monitoring and altitude adjustments."""
        for t in range(50):  # Run for 50 iterations
            # Simulate battery drain and altitude increase
            self.battery_level -= random.uniform(0.1, 0.5)
            self.altitude += random.uniform(0.5, 1.5)

            # Ensure battery level stays between 0 and 100
            if self.battery_level < 0:
                self.battery_level = 0
            if self.battery_level > 100:
                self.battery_level = 100

            # Store data for plotting
            self.time_data.append(t)
            self.battery_data.append(self.battery_level)
            self.altitude_data.append(self.altitude)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Simulation management complete.")

    def plot_simulation_data(self):
        """Plot battery level and altitude data over time."""
        plt.figure(figsize=(10, 6))

        # Plot battery level
        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.battery_data, label="Battery Level (%)", color='tab:green')
        plt.title("Battery Level Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Battery Level (%)")
        plt.legend()

        # Plot altitude
        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.altitude_data, label="Altitude (m)", color='tab:orange')
        plt.title("Altitude Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    simulation_manager = SimulationManagement()
    simulation_manager.manage_simulation()
    simulation_manager.plot_simulation_data()
