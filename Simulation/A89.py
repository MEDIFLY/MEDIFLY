# A89.py - Return to Base (Frontend + Backend Combined)
import matplotlib.pyplot as plt
import numpy as np
import time

# ---------------- FRONTEND: Visualization ---------------- #

def plot_return_trajectory(positions, home):
    positions = np.array(positions)
    plt.figure(figsize=(6, 6))
    plt.plot(positions[:, 0], positions[:, 1], 'g-', marker='o', label='Drone Path')
    plt.plot(home[0], home[1], 'ro', label='Home Base')
    plt.title('Drone Return Trajectory')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.legend()
    plt.show()

# ---------------- BACKEND: Return Logic ---------------- #

class ReturnToBase:
    def __init__(self):
        self.position = np.array([25.0, -35.0, 50.0])  # Starting position (x, y, z)
        self.home = np.array([0.0, 0.0, 0.0])          # Home base position (x, y, z)
        self.speed = 10.0                              # Movement speed per step
        self.tolerance = 1.0                           # Tolerance distance to consider "arrived"
        self.positions_log = [self.position[:2].copy()]  # Log x, y path for plotting

    def move_step(self):
        direction = self.home - self.position
        distance = np.linalg.norm(direction)

        # Check if drone is close enough to home
        if distance < self.tolerance:
            self.position = self.home  # Snap to home
            self.positions_log.append(self.position[:2].copy())
            return False

        # Calculate step vector and move
        step_vector = (direction / distance) * min(self.speed, distance)
        self.position += step_vector
        self.positions_log.append(self.position[:2].copy())

        print(f"Current Drone Position: {np.round(self.position, 2)}")
        return True

    def execute_return(self):
        print("\n=== Executing Return to Base ===")
        step = 1
        while self.move_step():
            print(f"Step {step} complete.\n")
            step += 1
            time.sleep(0.5)  # Simulate time delay
        print("✅ Drone has reached the base.\n")

    def get_path(self):
        return self.positions_log, self.home[:2]

# ---------------- MAIN EXECUTION ---------------- #

if __name__ == "__main__":
    rtb = ReturnToBase()
    rtb.execute_return()

    path, home_pos = rtb.get_path()
    plot_return_trajectory(path, home_pos)
