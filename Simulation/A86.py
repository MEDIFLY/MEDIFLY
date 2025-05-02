import matplotlib.pyplot as plt

# --------- Backend: Battery Check Logic ---------
class DroneBatteryChecker:
    def __init__(self, initial_battery=100, threshold=25):
        self.battery_level = initial_battery
        self.battery_threshold = threshold
        self.battery_log = [initial_battery]
        self.status_log = ["OK"]

    def update_battery(self, consumption):
        self.battery_level -= consumption
        if self.battery_level < 0:
            self.battery_level = 0
        self.battery_log.append(self.battery_level)

    def check_battery(self):
        if self.battery_level <= self.battery_threshold:
            status = "LOW"
            print(f"⚠️ Warning! Battery Low: {self.battery_level}%")
        else:
            status = "OK"
            print(f"✅ Battery Status OK: {self.battery_level}%")
        self.status_log.append(status)

    def simulate_battery_check(self, steps=10, consumption_rate=10):
        print("🔋 Starting Battery Check Simulation...\n")
        for step in range(steps):
            print(f"Step {step + 1}")
            self.update_battery(consumption=consumption_rate)
            self.check_battery()
            print("-" * 30)

    def plot_battery_status(self):
        steps = list(range(len(self.battery_log)))
        plt.figure(figsize=(8, 5))
        plt.plot(steps, self.battery_log, marker='o', color='purple', label='Battery Level')
        plt.axhline(y=self.battery_threshold, color='red', linestyle='--', label='Threshold')
        plt.title("Battery Level Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Battery (%)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

# --------- Run Simulation ---------
if __name__ == "__main__":
    checker = DroneBatteryChecker(initial_battery=100, threshold=25)
    checker.simulate_battery_check(steps=12, consumption_rate=8)
    checker.plot_battery_status()
