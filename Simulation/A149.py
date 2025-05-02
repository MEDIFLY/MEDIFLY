import matplotlib.pyplot as plt
import numpy as np

# Drone state and stability parameters
stability_output = []
drone_velocity = {'x': 1, 'y': 1, 'z': 0}  # Initial velocity
desired_velocity = {'x': 0, 'y': 0, 'z': 0}  # Desired stable state (hovering)
control_gain = 0.5  # Control gain for simulation

# Function to calculate control output for stability
def calculate_stability_control(drone_velocity, desired_velocity, control_gain):
    error_x = desired_velocity['x'] - drone_velocity['x']
    error_y = desired_velocity['y'] - drone_velocity['y']
    error_z = desired_velocity['z'] - drone_velocity['z']
    
    # Control output to minimize error
    control_output_x = control_gain * error_x
    control_output_y = control_gain * error_y
    control_output_z = control_gain * error_z
    
    return control_output_x, control_output_y, control_output_z

# Simulating stability control output over time
time_steps = np.arange(0, 100, 1)  # Time steps for simulation

for t in time_steps:
    control_output_x, control_output_y, control_output_z = calculate_stability_control(drone_velocity, desired_velocity, control_gain)
    
    stability_output.append(np.sqrt(control_output_x**2 + control_output_y**2 + control_output_z**2))  # Stability output (control effort)

# Plotting stability control output
plt.figure(figsize=(10, 6))
plt.plot(time_steps, stability_output, label='Stability Control Output', color='purple')

plt.title("Simulation Control Output for Stability over Time")
plt.xlabel("Time (s)")
plt.ylabel("Control Output (N)")
plt.legend()
plt.grid(True)
plt.show()

class DroneControlSystem:
    def __init__(self, velocity, desired_velocity, control_gain):
        self.velocity = velocity
        self.desired_velocity = desired_velocity
        self.control_gain = control_gain

    def calculate_control_output(self):
        error_x = self.desired_velocity['x'] - self.velocity['x']
        error_y = self.desired_velocity['y'] - self.velocity['y']
        error_z = self.desired_velocity['z'] - self.velocity['z']
        
        # Control output to minimize error
        control_output_x = self.control_gain * error_x
        control_output_y = self.control_gain * error_y
        control_output_z = self.control_gain * error_z
        
        return control_output_x, control_output_y, control_output_z

# Backend logic simulation
drone_control = DroneControlSystem(velocity={'x': 1, 'y': 1, 'z': 0}, desired_velocity={'x': 0, 'y': 0, 'z': 0}, control_gain=0.5)

# Running the control loop for 100 time steps
for t in range(100):
    control_output_x, control_output_y, control_output_z = drone_control.calculate_control_output()
    stability_output = np.sqrt(control_output_x**2 + control_output_y**2 + control_output_z**2)
    
    print(f"Time Step {t+1}: Control Output for Stability: {stability_output}")
    # Here you would use the control output to adjust drone stability in real systems
