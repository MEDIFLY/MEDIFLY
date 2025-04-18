import random
import matplotlib.pyplot as plt
import time

class HoverControlLoopExecution:
    def __init__(self):
        self.time_data = []
        self.altitude_data = []
        self.desired_altitude = 10  # Desired altitude in meters
        self.current_altitude = 0  # Initial altitude
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate hover control loop to maintain desired altitude."""
        for t in range(self.simulation_time):
            # Control loop to maintain desired altitude
            altitude_error = self.desired_altitude - self.current_altitude
            self.current_altitude += random.uniform(-0.1, 0.2) * altitude_error  # Adjust the altitude based on error

            # Store data for plotting
            self.time_data.append(t)
            self.altitude_data.append(self.current_altitude)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Hover control loop execution complete.")

    def plot_hover_control(self):
        """Plot the altitude of the drone during the hover control loop."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.altitude_data, label="Altitude (m)", color='tab:green')
        plt.axhline(y=self.desired_altitude, color='r', linestyle='--', label="Desired Altitude")
        plt.title("Hover Control Loop Altitude Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    hover_control_loop = HoverControlLoopExecution()
    hover_control_loop.run_simulation()
    hover_control_loop.plot_hover_control()
