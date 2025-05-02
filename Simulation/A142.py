import random
import matplotlib.pyplot as plt
import time

class StateUpdatesHoverLoop:
    def __init__(self):
        self.time_data = []
        self.position_data = []
        self.altitude_data = []
        self.velocity_data = []
        self.simulation_time = 50  # Number of iterations for simulation
        self.current_position = [0, 0, 0]  # Initial position (x, y, z)
        self.velocity = 0  # Initial velocity (m/s)

    def run_simulation(self):
        """Simulate state updates for hover loop."""
        for t in range(self.simulation_time):
            # Simulate some movement and updates in position and velocity
            self.velocity = random.uniform(0.1, 0.3)  # Simulate velocity changes (m/s)
            self.current_position[2] += random.uniform(-0.1, 0.1)  # Small changes in altitude

            # Store data for plotting
            self.time_data.append(t)
            self.position_data.append(self.current_position[:2])  # Storing only x, y position
            self.altitude_data.append(self.current_position[2])  # Storing only z (altitude)
            self.velocity_data.append(self.velocity)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("State updates in hover loop complete.")

    def plot_state_updates(self):
        """Plot state updates over time."""
        plt.figure(figsize=(8, 5))
        plt.subplot(3, 1, 1)
        plt.plot(self.time_data, [pos[0] for pos in self.position_data], label="X Position", color='tab:blue')
        plt.plot(self.time_data, [pos[1] for pos in self.position_data], label="Y Position", color='tab:orange')
        plt.title("Position (x, y) Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Position (m)")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(self.time_data, self.altitude_data, label="Altitude (z)", color='tab:green')
        plt.title("Altitude (z) Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(self.time_data, self.velocity_data, label="Velocity", color='tab:red')
        plt.title("Velocity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    state_updates = StateUpdatesHoverLoop()
    state_updates.run_simulation()
    state_updates.plot_state_updates()
