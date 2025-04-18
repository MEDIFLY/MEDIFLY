import random
import matplotlib.pyplot as plt
import time

class DronePhysicalParameters:
    def __init__(self):
        self.time_data = []
        self.mass_data = []
        self.size_data = []
        self.drone_mass = 2.5  # Mass of drone in kg
        self.drone_size = 1.0  # Size of drone (scaled value)
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate changes in the drone's mass and size."""
        for t in range(self.simulation_time):
            # Simulate random changes in drone mass (e.g., battery drain, added payload)
            self.drone_mass = max(1.5, random.uniform(2.5, 3.0))

            # Simulate changes in drone size (e.g., wing expansion or contraction)
            self.drone_size = random.uniform(0.8, 1.2)

            # Store data for plotting
            self.time_data.append(t)
            self.mass_data.append(self.drone_mass)
            self.size_data.append(self.drone_size)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Simulation with drone physical parameters complete.")

    def plot_drone_physical_parameters(self):
        """Plot drone mass and size changes over time."""
        plt.figure(figsize=(10, 6))

        # Plot mass changes
        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.mass_data, label="Drone Mass (kg)", color='tab:red')
        plt.title("Drone Mass Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Mass (kg)")
        plt.legend()

        # Plot size changes
        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.size_data, label="Drone Size (scaled)", color='tab:green')
        plt.title("Drone Size Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Size (scaled)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    drone_physical_params = DronePhysicalParameters()
    drone_physical_params.run_simulation()
    drone_physical_params.plot_drone_physical_parameters()
