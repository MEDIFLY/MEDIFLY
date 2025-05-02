import random
import matplotlib.pyplot as plt
import time

class SimulationRoutineExecution:
    def __init__(self):
        self.time_data = []
        self.simulation_step_data = []
        self.simulation_time = 50  # Number of iterations for simulation
        self.step_counter = 0  # Counter for simulation steps

    def run_simulation(self):
        """Simulate the routine execution of the simulation."""
        for t in range(self.simulation_time):
            # Increment simulation step
            self.step_counter += 1

            # Simulate some random changes during the routine
            random_event = random.choice([True, False])
            if random_event:
                self.step_counter += random.randint(1, 5)  # Simulate some extra steps

            # Store data for plotting
            self.time_data.append(t)
            self.simulation_step_data.append(self.step_counter)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Simulation routine execution complete.")

    def plot_simulation_steps(self):
        """Plot simulation steps over time."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.simulation_step_data, label="Simulation Step Count", color='tab:blue')
        plt.title("Simulation Routine Execution Steps Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Simulation Steps")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    routine_execution = SimulationRoutineExecution()
    routine_execution.run_simulation()
    routine_execution.plot_simulation_steps()
