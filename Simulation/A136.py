import random
import matplotlib.pyplot as plt
import time

class SimulationParameters:
    def __init__(self):
        self.time_data = []
        self.environment_data = []
        self.drone_speed = 0  # Initial drone speed (m/s)
        self.environment_factor = 1  # Environment factor (like wind speed)
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate environment factors and drone's speed."""
        for t in range(self.simulation_time):
            # Simulate environment factor (wind speed, temperature, etc.)
            self.environment_factor = random.uniform(0.5, 1.5)

            # Simulate drone speed based on environmental factors
            self.drone_speed = random.uniform(5, 15) * self.environment_factor

            # Store data for plotting
            self.time_data.append(t)
            self.environment_data.append(self.environment_factor)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Simulation with environment parameters complete.")

    def plot_simulation_parameters(self):
        """Plot drone speed over time based on environment factor."""
        plt.figure(figsize=(8, 6))
        plt.plot(self.time_data, self.environment_data, label="Environment Factor", color='tab:blue')
        plt.title("Simulation Parameters Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Environment Factor (Wind Speed, etc.)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    simulation_params = SimulationParameters()
    simulation_params.run_simulation()
    simulation_params.plot_simulation_parameters()
