import random
import matplotlib.pyplot as plt
import time

# Drone class to simulate environmental sensors and state updates
class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id
        self.temperature = 25  # Initial temperature in Celsius
        self.humidity = 50     # Initial humidity in percentage
        self.wind_speed = 5    # Initial wind speed in m/s
        self.air_quality = 100 # Initial air quality index
        self.time_log = []     # To log the time steps
        self.temp_log = []     # To log the temperature readings
        self.humidity_log = [] # To log the humidity readings
        self.wind_speed_log = [] # To log wind speed
        self.air_quality_log = [] # To log air quality

    def simulate_environmental_factors(self):
        """Simulate environmental factors and update state."""
        print(f"\n🛩️ Drone {self.drone_id}: Simulating Environmental Conditions...")
        
        for t in range(10):  # Simulate for 10 time steps
            # Randomly simulate changes in environmental factors
            self.temperature += random.uniform(-1, 1)  # Temperature change
            self.humidity += random.uniform(-2, 2)     # Humidity change
            self.wind_speed += random.uniform(-0.5, 0.5) # Wind speed change
            self.air_quality += random.uniform(-5, 5)   # Air quality change
            
            # Ensure values remain within realistic limits
            self.temperature = max(min(self.temperature, 40), -10)  # Temperature between -10°C and 40°C
            self.humidity = max(min(self.humidity, 100), 0)         # Humidity between 0% and 100%
            self.wind_speed = max(min(self.wind_speed, 15), 0)      # Wind speed between 0 m/s and 15 m/s
            self.air_quality = max(min(self.air_quality, 500), 0)   # Air quality between 0 and 500
            
            # Log data for plotting
            self.time_log.append(t)
            self.temp_log.append(self.temperature)
            self.humidity_log.append(self.humidity)
            self.wind_speed_log.append(self.wind_speed)
            self.air_quality_log.append(self.air_quality)
            
            time.sleep(1)  # Simulate time passing

    def plot_environmental_data(self):
        """Plot environmental data over time."""
        plt.figure(figsize=(10, 6))

        plt.subplot(2, 2, 1)
        plt.plot(self.time_log, self.temp_log, label="Temperature (°C)", color="red")
        plt.xlabel("Time (s)")
        plt.ylabel("Temperature (°C)")
        plt.title("Temperature Over Time")
        plt.grid(True)

        plt.subplot(2, 2, 2)
        plt.plot(self.time_log, self.humidity_log, label="Humidity (%)", color="blue")
        plt.xlabel("Time (s)")
        plt.ylabel("Humidity (%)")
        plt.title("Humidity Over Time")
        plt.grid(True)

        plt.subplot(2, 2, 3)
        plt.plot(self.time_log, self.wind_speed_log, label="Wind Speed (m/s)", color="green")
        plt.xlabel("Time (s)")
        plt.ylabel("Wind Speed (m/s)")
        plt.title("Wind Speed Over Time")
        plt.grid(True)

        plt.subplot(2, 2, 4)
        plt.plot(self.time_log, self.air_quality_log, label="Air Quality Index", color="purple")
        plt.xlabel("Time (s)")
        plt.ylabel("Air Quality Index")
        plt.title("Air Quality Over Time")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    drone1 = Drone("MEDI-FLY-1")
    
    # Simulate environmental conditions
    drone1.simulate_environmental_factors()
    
    # Plot environmental data
    drone1.plot_environmental_data()
