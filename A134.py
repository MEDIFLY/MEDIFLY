import random
import matplotlib.pyplot as plt
import time

class HoverControlPID:
    def __init__(self):
        # Initialize PID controller parameters
        self.Kp = 1.0  # Proportional constant
        self.Ki = 0.1  # Integral constant
        self.Kd = 0.01 # Derivative constant
        self.target_height = 10  # Target hover height (m)
        self.current_height = 0  # Initial height (m)
        self.integral = 0
        self.previous_error = 0
        self.time_data = []
        self.height_data = []

    def calculate_pid(self):
        """PID control to maintain hover height."""
        for t in range(50):  # Run for 50 iterations
            error = self.target_height - self.current_height
            self.integral += error
            derivative = error - self.previous_error
            control_signal = self.Kp * error + self.Ki * self.integral + self.Kd * derivative

            # Update height based on control signal (for simulation)
            self.current_height += control_signal * 0.1  # Adjust height with control signal

            # Store data for plotting
            self.time_data.append(t)
            self.height_data.append(self.current_height)

            # Update previous error for next iteration
            self.previous_error = error

            # Simulate a delay (0.1 second per iteration)
            time.sleep(0.1)

        print("Hover control using PID complete.")

    def plot_hover_control(self):
        """Plot the hover height over time."""
        plt.figure(figsize=(8, 6))
        plt.plot(self.time_data, self.height_data, label="Height (m)", color='tab:blue')
        plt.axhline(self.target_height, color='tab:red', linestyle='--', label="Target Height")
        plt.title("Hover Control Using PID")
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    hover_control = HoverControlPID()
    hover_control.calculate_pid()
    hover_control.plot_hover_control()
