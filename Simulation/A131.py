import csv
import time
import random
import matplotlib.pyplot as plt

class Drone:
    def __init__(self, drone_id="MEDI-FLY-1"):
        self.drone_id = drone_id
        self.position = {'x': 0, 'y': 0, 'z': 25}  # start at 25m height
        self.battery = 100
        self.time_elapsed = 0
        self.log_data = []
        self.emergency = False

    def simulate_flight_step(self):
        # Simulate basic flight
        self.position['x'] += random.randint(1, 5)
        self.position['y'] += random.randint(1, 5)
        self.position['z'] = max(self.position['z'] - random.randint(0, 2), 0)
        self.battery -= random.uniform(2.5, 5.0)
        self.time_elapsed += 1

        # Emergency condition
        if self.battery <= 10 or self.position['z'] == 0:
            self.emergency = True

        # Record flight step
        self.log_data.append({
            'Time': self.time_elapsed,
            'X': self.position['x'],
            'Y': self.position['y'],
            'Z': self.position['z'],
            'Battery': round(self.battery, 2),
            'Status': "EMERGENCY" if self.emergency else "NORMAL"
        })

        print(f"⏱️ Time: {self.time_elapsed}s | 📍 Pos: {self.position} | 🔋 Battery: {round(self.battery,1)}% | Status: {self.log_data[-1]['Status']}")

    def fly(self, steps=10):
        print(f"🛫 Starting flight log for Drone: {self.drone_id}")
        for _ in range(steps):
            self.simulate_flight_step()
            if self.emergency:
                print("🚨 Emergency detected. Logging and aborting flight.")
                break
            time.sleep(0.3)
        self.save_log()

    def save_log(self):
        filename = f"{self.drone_id}_flight_log.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.log_data[0].keys())
            writer.writeheader()
            writer.writerows(self.log_data)
        print(f"\n📁 Flight log saved as: {filename}")
        self.plot_log()

    def plot_log(self):
        times = [entry['Time'] for entry in self.log_data]
        altitudes = [entry['Z'] for entry in self.log_data]

        plt.figure(figsize=(10, 5))
        plt.plot(times, altitudes, marker='o', color='blue')
        plt.title("📊 Drone Altitude Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Altitude (m)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# 🔧 Run the simulation
if __name__ == "__main__":
    drone1 = Drone()
    drone1.fly(steps=20)
import random
import matplotlib.pyplot as plt
import time

class EnvironmentalConditions:
    def __init__(self):
        self.time_data = []
        self.temperature_data = []
        self.humidity_data = []
        self.wind_speed_data = []
        self.air_quality_data = []

    def simulate_conditions(self):
        """Simulate environmental conditions detection over time."""
        for t in range(50):  # Run for 50 iterations
            temperature = random.uniform(15.0, 35.0)  # Simulate temperature in Celsius
            humidity = random.uniform(30.0, 90.0)  # Simulate humidity in percentage
            wind_speed = random.uniform(0.0, 15.0)  # Simulate wind speed in m/s
            air_quality = random.uniform(60.0, 100.0)  # Simulate air quality percentage

            self.time_data.append(t)
            self.temperature_data.append(temperature)
            self.humidity_data.append(humidity)
            self.wind_speed_data.append(wind_speed)
            self.air_quality_data.append(air_quality)

            # Simulate a delay (1 second per iteration)
            time.sleep(0.1)

        print("Environmental conditions detected over time.")

    def plot_conditions(self):
        """Plot environmental conditions data over time."""
        plt.figure(figsize=(10, 6))
        
        plt.subplot(2, 2, 1)
        plt.plot(self.time_data, self.temperature_data, label="Temperature (°C)", color='tab:blue')
        plt.title("Temperature Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(self.time_data, self.humidity_data, label="Humidity (%)", color='tab:green')
        plt.title("Humidity Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(self.time_data, self.wind_speed_data, label="Wind Speed (m/s)", color='tab:orange')
        plt.title("Wind Speed Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(self.time_data, self.air_quality_data, label="Air Quality (%)", color='tab:red')
        plt.title("Air Quality Over Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Air Quality (%)")
        plt.legend()

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    env_conditions = EnvironmentalConditions()
    env_conditions.simulate_conditions()
    env_conditions.plot_conditions()
