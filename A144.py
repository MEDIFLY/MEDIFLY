import random
import matplotlib.pyplot as plt
import time

class ErrorVariablesHoverLoop:
    def __init__(self):
        self.time_data = []
        self.altitude_error_data = []
        self.velocity_error_data = []
        self.setpoint = 10  # Desired altitude (m)
        self.velocity_setpoint = 0.5  # Desired velocity (m/s)
        self.simulation_time = 50  # Number of iterations for simulation
        self.current_altitude = 0  # Current altitude (m)
        self.current_velocity = 0  # Current velocity (m/s)

    def run_simulation(self):
        """Simulate error variables for hover loop."""
        for t in range(self.simulation_time):
            # Simulate altitude and velocity errors
            altitude_error = self.setpoint - self.current_altitude
            velocity_error = self.velocity_setpoint - self.current_velocity

            # Store error data for plotting
            self.time_data.append(t)
            self.altitude_error_data.append(altitude_error)
            self.velocity_error_data.append(velocity_error)

            # Simulate changes in altitude and velocity
            self.current_altitude += random.uniform(-0.05, 0.05)
            self.current_velocity += random.uniform(-0.02, 0.02)

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Error variables for hover loop simulation complete.")

    def plot_error_variables(self):
        """Plot error variables (altitude and velocity) over time."""
        plt.figure(figsize=(8, 5))
        plt.subplot(2, 1, 1)
        plt.plot(self.time_data, self.altitude_error_data, label="Altitude Error", color='tab:blue')
        plt.title("Altitude Error Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude Error (m)")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(self.time_data, self.velocity_error_data, label="Velocity Error", color='tab:orange')
        plt.title("Velocity Error Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity Error (m/s)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    error_variables = ErrorVariablesHoverLoop()
    error_variables.run_simulation()
    error_variables.plot_error_variables()
