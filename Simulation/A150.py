import matplotlib.pyplot as plt
import numpy as np

# Simulation of drone state during hover execution
class Drone:
    def __init__(self, initial_position):
        self.position = initial_position  # (x, y, z)
        self.velocity = [0, 0, 0]  # velocity in x, y, z directions
        self.altitude = initial_position[2]
        self.time_step = 1  # time step for simulation in seconds
        self.path = [initial_position]
        
    def update_state(self):
        # Simulating state update (hover logic)
        # Assuming constant velocity for simplicity
        self.position[0] += self.velocity[0] * self.time_step
        self.position[1] += self.velocity[1] * self.time_step
        self.position[2] += self.velocity[2] * self.time_step  # Hover logic (no change in altitude)
        self.path.append(tuple(self.position))

    def display_state(self):
        print(f"Position: {self.position}, Altitude: {self.position[2]}")

# Initialize drone at position (0, 0, 100)
drone = Drone([0, 0, 100])

# Simulate for 100 seconds
for _ in range(100):
    drone.update_state()

# Extract x, y, z coordinates for plotting
x_vals, y_vals, z_vals = zip(*drone.path)

# Plotting the drone path
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="Drone Path")
plt.scatter(x_vals[-1], y_vals[-1], color='red', label="Current Position")
plt.title("Drone Hover Path (State Update)")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.legend()
plt.grid(True)
plt.show()

class DroneBackend:
    def __init__(self):
        self.position = [0, 0, 100]  # Initial position at (x, y, z)
        self.velocity = [0, 0, 0]  # Velocity in (x, y, z)
        self.is_hovering = True  # Assume the drone is hovering for this operation
        self.altitude = 100  # Hovering at 100m
        
    def update_position(self):
        # Simulate state update in backend (can be used for control logic in hardware)
        if self.is_hovering:
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]
            self.position[2] = self.altitude  # Maintain altitude for hover
        return self.position
    
    def check_stability(self):
        # Simulate stability check (for backend control)
        if self.is_hovering and abs(self.velocity[0]) < 0.5 and abs(self.velocity[1]) < 0.5:
            return True  # Hovering is stable
        return False

    def display_status(self):
        print(f"Position: {self.position}, Altitude: {self.position[2]}, Stability: {self.check_stability()}")

# Initialize drone backend for hardware control
drone_backend = DroneBackend()

# Update and check stability
for _ in range(100):
    drone_backend.update_position()
    drone_backend.display_status()
