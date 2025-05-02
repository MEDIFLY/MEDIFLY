import random
import matplotlib.pyplot as plt

# Sensor class to simulate the initialization of environmental sensors
class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type
        self.value = 0

    def initialize_sensor(self):
        """Initialize the sensor with a random value within a realistic range."""
        if self.sensor_type == "Temperature":
            self.value = random.uniform(20, 30)  # Initial temperature between 20°C and 30°C
        elif self.sensor_type == "Humidity":
            self.value = random.uniform(40, 60)  # Initial humidity between 40% and 60%
        elif self.sensor_type == "Wind Speed":
            self.value = random.uniform(0, 5)  # Initial wind speed between 0 m/s and 5 m/s
        elif self.sensor_type == "Air Quality":
            self.value = random.uniform(100, 200)  # Initial air quality index between 100 and 200
        print(f"{self.sensor_type} Sensor Initialized with value: {self.value:.2f}")

# --- Main Execution ---
if __name__ == "__main__":
    # Initialize sensors for environmental factors
    temperature_sensor = Sensor("Temperature")
    humidity_sensor = Sensor("Humidity")
    wind_speed_sensor = Sensor("Wind Speed")
    air_quality_sensor = Sensor("Air Quality")
    
    # Initialize all sensors
    temperature_sensor.initialize_sensor()
    humidity_sensor.initialize_sensor()
    wind_speed_sensor.initialize_sensor()
    air_quality_sensor.initialize_sensor()
    
    # Prepare data for plotting
    sensor_names = ["Temperature", "Humidity", "Wind Speed", "Air Quality"]
    sensor_values = [
        temperature_sensor.value,
        humidity_sensor.value,
        wind_speed_sensor.value,
        air_quality_sensor.value
    ]
    
    # Plotting the sensor values
    plt.bar(sensor_names, sensor_values, color='skyblue')
    plt.xlabel('Sensor Type')
    plt.ylabel('Sensor Value')
    plt.title('Environmental Sensor Initialization')
    plt.show()
