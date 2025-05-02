# A88.py - Drone Parameters for Return (Frontend + Backend Combined)
import matplotlib.pyplot as plt

# ---------------- FRONTEND: Visualization ---------------- #

def plot_return_path(start_pos, home_pos):
    x_values = [start_pos[0], home_pos[0]]
    y_values = [start_pos[1], home_pos[1]]

    plt.figure(figsize=(6, 6))
    plt.plot(x_values, y_values, 'b--', marker='o')
    plt.text(start_pos[0], start_pos[1], 'Current Position', fontsize=9, ha='right')
    plt.text(home_pos[0], home_pos[1], 'Home Position', fontsize=9, ha='right')
    plt.title('Drone Return Path')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.show()

# ---------------- BACKEND: Logic ---------------- #

class ReturnDrone:
    def __init__(self):
        self.current_position = [25, -35, 50]  # x, y, altitude
        self.return_position = [0, 0, 0]       # Home base
        self.speed = 10  # units per second
        self.battery_status = 45  # percent

    def display_parameters(self):
        print("=== Drone Return Parameters ===")
        print(f"Current Position  : {self.current_position}")
        print(f"Return Position   : {self.return_position}")
        print(f"Speed             : {self.speed} units/sec")
        print(f"Battery Status    : {self.battery_status}%")
        print("Ready to return to base.\n")

    def get_positions(self):
        return self.current_position, self.return_position

# ---------------- MAIN EXECUTION ---------------- #

if __name__ == "__main__":
    drone = ReturnDrone()
    drone.display_parameters()

    # Visualization
    current_pos, home_pos = drone.get_positions()
    plot_return_path(current_pos, home_pos)
