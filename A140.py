import random
import matplotlib.pyplot as plt
import time

class VerticalPositionInitialization:
    def __init__(self):
        self.time_data = []
        self.position_data_z = []
        self.initial_z_position = 0  # Starting altitude (z-position) in meters
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate initialization of the vertical position (z) of the drone."""
        for t in range(self.simulation_time):
            # Simulate vertical position changes (e.g., rising or hovering)
            self.initial_z_position = max(0, self.initial_z_position + random.uniform(0, 0.5))  # Max height is 100m

            # Store data for plotting
            self.time_data.append(t)
            self.position_data_z.append(self.initial_z_position)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Vertical position initialization complete.")

    def plot_vertical_position(self):
        """Plot vertical position (z) over time."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.position_data_z, label="Vertical Position (z)", color='tab:blue')
        plt.title("Vertical Position Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Position (m)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    vertical_position_init = VerticalPositionInitialization()
    vertical_position_init.run_simulation()
    vertical_position_init.plot_vertical_position()
