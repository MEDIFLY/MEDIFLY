import random
import matplotlib.pyplot as plt
import time

class PIDOutputCalculation:
    def __init__(self):
        self.time_data = []
        self.pid_output_data = []
        self.setpoint = 10  # Desired altitude (m)
        self.kp = 1.2  # Proportional gain
        self.ki = 0.8  # Integral gain
        self.kd = 0.3  # Derivative gain
        self.error_sum = 0  # Sum of previous errors for integral term
        self.previous_error = 0  # Previous error for derivative term
        self.current_altitude = 0  # Current altitude (m)
        self.simulation_time = 50  # Number of iterations for simulation

    def run_simulation(self):
        """Simulate PID control output calculation."""
        for t in range(self.simulation_time):
            # Simulate altitude error
            error = self.setpoint - self.current_altitude

            # PID calculations
            self.error_sum += error
            derivative = error - self.previous_error
            pid_output = (self.kp * error) + (self.ki * self.error_sum) + (self.kd * derivative)

            # Update current altitude based on PID output
            self.current_altitude += pid_output * 0.1  # Simulate the altitude change

            # Store data for plotting
            self.time_data.append(t)
            self.pid_output_data.append(pid_output)

            # Update previous error for next iteration
            self.previous_error = error

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("PID output calculation complete.")

    def plot_pid_output(self):
        """Plot PID output over time."""
        plt.figure(figsize=(8, 5))
        plt.plot(self.time_data, self.pid_output_data, label="PID Output", color='tab:purple')
        plt.title("PID Output Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("PID Output")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    pid_output = PIDOutputCalculation()
    pid_output.run_simulation()
    pid_output.plot_pid_output()
