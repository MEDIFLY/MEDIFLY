import matplotlib.pyplot as plt
import numpy as np

# Drone parameters and position tracking
drone_position = {'x': 0, 'y': 0, 'z': 0}
desired_position = {'x': 50, 'y': 50, 'z': 100}  # Desired position
error_x = []
error_y = []
error_z = []

# Function to calculate position error
def calculate_position_error(drone_position, desired_position):
    error_x_val = desired_position['x'] - drone_position['x']
    error_y_val = desired_position['y'] - drone_position['y']
    error_z_val = desired_position['z'] - drone_position['z']
    
    return error_x_val, error_y_val, error_z_val

# Simulating error calculations over time
time_steps = np.arange(0, 100, 1)  # Time steps for simulation

for t in time_steps:
    # Simulate drone movement towards the target
    drone_position['x'] += 0.5  # Movement speed in x-direction
    drone_position['y'] += 0.4  # Movement speed in y-direction
    drone_position['z'] += 0.3  # Movement speed in z-direction
    
    error_x_val, error_y_val, error_z_val = calculate_position_error(drone_position, desired_position)
    error_x.append(error_x_val)
    error_y.append(error_y_val)
    error_z.append(error_z_val)

# Plotting error over time
plt.figure(figsize=(10, 6))
plt.plot(time_steps, error_x, label='Error in X Position', color='red')
plt.plot(time_steps, error_y, label='Error in Y Position', color='blue')
plt.plot(time_steps, error_z, label='Error in Z Position', color='green')

plt.title("Position Error Calculation over Time")
plt.xlabel("Time (s)")
plt.ylabel("Error (m)")
plt.legend()
plt.grid(True)
plt.show()

class Drone:
    def __init__(self, position, desired_position):
        self.position = position
        self.desired_position = desired_position
        self.error_x = 0
        self.error_y = 0
        self.error_z = 0

    def calculate_position_error(self):
        self.error_x = self.desired_position['x'] - self.position['x']
        self.error_y = self.desired_position['y'] - self.position['y']
        self.error_z = self.desired_position['z'] - self.position['z']
    
    def move_towards_target(self):
        # Move drone towards target to reduce error
        self.position['x'] += 0.5
        self.position['y'] += 0.4
        self.position['z'] += 0.3

    def get_position(self):
        return self.position

    def get_error(self):
        return self.error_x, self.error_y, self.error_z


# Backend logic simulation loop
drone = Drone(position={'x': 0, 'y': 0, 'z': 0}, desired_position={'x': 50, 'y': 50, 'z': 100})

# Running the backend for 100 time steps
for t in range(100):
    drone.move_towards_target()
    drone.calculate_position_error()
    error_x, error_y, error_z = drone.get_error()
    # Here you can pass these error values to the control system for corrections
    print(f"Time Step {t+1}: Error in Position - X: {error_x}, Y: {error_y}, Z: {error_z}")
