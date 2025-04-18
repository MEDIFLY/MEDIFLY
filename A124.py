import random
import matplotlib.pyplot as plt
import time

class DroneSimulation:
    def __init__(self):
        self.position = {"x": 0, "y": 0, "z": 0}  # Initial position
        self.battery = 100  # Full battery at start
        self.path = []  # To track the drone's path for plotting

    def update_position(self):
        """Simulate position update based on random movement."""
        self.position["x"] += random.uniform(-1, 1)
        self.position["y"] += random.uniform(-1, 1)
        self.position["z"] += random.uniform(-0.5, 0.5)  # Small vertical movement

    def simulate_main_loop(self):
        """Simulate the main loop where position is updated over time."""
        for _ in range(50):  # Run the simulation for 50 iterations
            self.update_position()
            self.path.append((self.position["x"], self.position["y"], self.position["z"]))
            self.battery -= 0.2  # Battery drains over time

            # Simulate a delay as if it's real-time (1 second per iteration)
            time.sleep(0.1)

            if self.battery <= 0:
                print("Battery drained! Returning to home base...")
                break

        print(f"Final Position: {self.position}")
        print(f"Battery status: {self.battery}%")

    def plot_path(self):
        """Plot the drone's path (x, y, z) during the simulation."""
        x_vals, y_vals, z_vals = zip(*self.path)  # Unzip the path into x, y, z coordinates
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x_vals, y_vals, z_vals, label='Drone Path')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        ax.set_zlabel('Z Position')
        ax.set_title('Drone Path During Simulation')
        ax.legend()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    drone_sim = DroneSimulation()
    drone_sim.simulate_main_loop()
    drone_sim.plot_path()
