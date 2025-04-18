import random
import matplotlib.pyplot as plt
import time

class MainExecutionControlSimulation:
    def __init__(self):
        self.time_data = []
        self.execution_status_data = []
        self.simulation_time = 50  # Number of iterations for simulation
        self.execution_status = 1  # 1 means running, 0 means stopped

    def run_simulation(self):
        """Simulate the main execution control loop."""
        for t in range(self.simulation_time):
            # Simulate changes in execution status
            self.execution_status = random.choice([0, 1])  # Randomly stop or run

            # Store data for plotting
            self.time_data.append(t)
            self.execution_status_data.append(self.execution_status)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Main execution control simulation complete.")

    def plot_execution_status(self):
        """Plot the main execution status over time."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.execution_status_data, label="Execution Status", color='tab:purple')
        plt.title("Main Execution Status Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Execution Status (1: Running, 0: Stopped)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    execution_control = MainExecutionControlSimulation()
    execution_control.run_simulation()
    execution_control.plot_execution_status()
