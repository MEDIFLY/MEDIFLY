import random
import matplotlib.pyplot as plt

# --------- Backend: Battery and Return Logic ---------
class BatteryMonitor:
    def __init__(self, battery_threshold=30):
        self.battery_level = 100  # Start at 100%
        self.battery_threshold = battery_threshold
        self.position = [0, 0]
        self.base_position = [0, 0]
        self.path = [self.position.copy()]
        self.returning = False

    def simulate_battery_usage(self):
        usage = random.randint(5, 15)
        self.battery_level -= usage
        self.battery_level = max(self.battery_level, 0)

    def move_randomly(self):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        self.position[0] += dx
        self.position[1] += dy

    def check_battery_and_decide(self):
        if self.battery_level <= self.battery_threshold:
            self.returning = True
            print(f"⚠️ Battery low ({self.battery_level}%). Returning to base...")
        else:
            print(f"Battery OK ({self.battery_level}%). Continuing mission.")

    def move_to_base(self):
        if self.position != self.base_position:
            for i in range(2):
                if self.position[i] > self.base_position[i]:
                    self.position[i] -= 1
                elif self.position[i] < self.base_position[i]:
                    self.position[i] += 1

    def simulate(self, steps=10):
        print("🚁 Starting battery monitoring simulation...\n")
        for step in range(steps):
            print(f"Step {step + 1}")
            self.simulate_battery_usage()
            self.check_battery_and_decide()

            if self.returning:
                self.move_to_base()
            else:
                self.move_randomly()

            print(f"Current Position: {self.position}\n")
            self.path.append(self.position.copy())

    def plot_path(self):
        x_vals = [pos[0] for pos in self.path]
        y_vals = [pos[1] for pos in self.path]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, marker='o', linestyle='--', color='blue', label='Drone Path')
        plt.scatter(self.base_position[0], self.base_position[1], color='green', label='Base')
        plt.scatter(x_vals[-1], y_vals[-1], color='red', label='Final Position')
        plt.title('Battery-Based Return to Base Simulation')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.grid(True)
        plt.show()

# --------- Run Simulation ---------
if __name__ == "__main__":
    monitor = BatteryMonitor(battery_threshold=30)
    monitor.simulate(steps=15)
    monitor.plot_path()
