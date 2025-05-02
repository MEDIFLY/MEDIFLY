import random
import matplotlib.pyplot as plt
import time

class StabilityCheckHoverLoop:
    def __init__(self):
        self.time_data = []
        self.stability_data = []
        self.stability_threshold = 0.1  # Threshold for stability (m for altitude, m/s for velocity)
        self.simulation_time = 50  # Number of iterations for simulation
        self.current_altitude = 0  # Current altitude (m)
        self.current_velocity = 0  # Current velocity (m/s)

    def run_simulation(self):
        """Simulate stability check for hover loop."""
        for t in range(self.simulation_time):
            # Simulate changes in altitude and velocity
            altitude_change = random.uniform(-0.05, 0.05)
            velocity_change = random.uniform(-0.02, 0.02)

            # Update current altitude and velocity
            self.current_altitude += altitude_change
            self.current_velocity += velocity_change

            # Stability check: compare with threshold
            if abs(altitude_change) < self.stability_threshold and abs(velocity_change) < self.stability_threshold:
                stability = 1  # Stable
            else:
                stability = 0  # Unstable

            # Store stability data for plotting
            self.time_data.append(t)
            self.stability_data.append(stability)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Stability check for hover loop simulation complete.")

    def plot_stability_check(self):
        """Plot stability status over time."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.stability_data, label="Stability Status", color='tab:green')
        plt.title("Stability Check Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Stability (1: Stable, 0: Unstable)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    stability_check = StabilityCheckHoverLoop()
    stability_check.run_simulation()
    stability_check.plot_stability_check()
