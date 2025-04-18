# A90.py - Drone Landing Procedure (Frontend + Backend)
import matplotlib.pyplot as plt
import time
import numpy as np

# ---------------- FRONTEND: Visualization ---------------- #

def plot_landing_trajectory(positions):
    positions = np.array(positions)
    plt.figure(figsize=(6, 6))
    plt.plot(positions[:, 0], positions[:, 1], 'blue', marker='o', label='Landing Path')
    plt.plot(positions[-1, 0], positions[-1, 1], 'ro', label='Landed')
    plt.title('Normal Drone Landing Trajectory')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.legend()
    plt.show()

# ---------------- BACKEND: Logic ---------------- #

class DroneLanding:
    def __init__(self):
        self.position = np.array([30.0, -20.0, 50.0])  # x, y, altitude
        self.altitude_decrease = 2.0  # m/sec
        self.horizontal_stability = 0.5  # x-y correction per step
        self.positions_log = [self.position[:2].copy()]

    def descend(self):
        if self.position[2] <= 0.0:
            return False  # Landed

        # Reduce altitude
        self.position[2] -= self.altitude_decrease
        if self.position[2] < 0.0:
            self.position[2] = 0.0  # Clamp to ground

        # Small x-y adjustments
        self.position[0] += self.horizontal_stability * 0.1
        self.position[1] -= self.horizontal_stability * 0.1

        self.positions_log.append(self.position[:2].copy())
        print(f"Landing... Position: {np.round(self.position, 2)}")
        return True

    def initiate_landing(self):
        print("\n🛬 Initiating Drone Landing Procedure...")
        step = 1
        while self.descend():
            print(f"Landing Step {step} completed.")
            step += 1
            time.sleep(0.3)
        print("✅ Drone has landed safely.\n")

    def get_landing_path(self):
        return self.positions_log

# ---------------- MAIN EXECUTION ---------------- #

if __name__ == "__main__":
    dl = DroneLanding()
    dl.initiate_landing()

    path = dl.get_landing_path()
    plot_landing_trajectory(path)
