import random
import matplotlib.pyplot as plt

# 📦 Sensor Reading Structure
class SensorData:
    def __init__(self):
        self.temperature = []
        self.humidity = []
        self.wind_speed = []
        self.air_quality = []
        self.time_log = []

# 🔁 Backend Logic: Simulate dynamic sensor data
def update_sensor_readings(sensor_data, current_time):
    temp = round(random.uniform(22.0, 35.0), 2)  # °C
    humidity = round(random.uniform(40.0, 80.0), 2)  # %
    wind_speed = round(random.uniform(0.0, 15.0), 2)  # m/s
    air_quality = random.randint(0, 500)  # AQI

    sensor_data.temperature.append(temp)
    sensor_data.humidity.append(humidity)
    sensor_data.wind_speed.append(wind_speed)
    sensor_data.air_quality.append(air_quality)
    sensor_data.time_log.append(current_time)

    print(f"⏱️ Time {current_time}s | 🌡️ Temp: {temp}°C | 💧 Humidity: {humidity}% | 🌬️ Wind: {wind_speed} m/s | 🫁 AQI: {air_quality}")

# 🧠 Frontend: Simulation routine
def simulate_sensor_updates():
    print("📡 Starting Sensor Readings Update...\n")
    sensor_data = SensorData()
    
    for t in range(0, 60, 5):  # Every 5 seconds till 60 seconds
        update_sensor_readings(sensor_data, t)

    return sensor_data

# 🔄 Run simulation
sensor_log = simulate_sensor_updates()

# 📊 Plotting all sensor readings
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.plot(sensor_log.time_log, sensor_log.temperature, marker='o', color='red')
plt.title("🌡️ Temperature over Time")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(sensor_log.time_log, sensor_log.humidity, marker='o', color='blue')
plt.title("💧 Humidity over Time")
plt.xlabel("Time (s)")
plt.ylabel("Humidity (%)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(sensor_log.time_log, sensor_log.wind_speed, marker='o', color='purple')
plt.title("🌬️ Wind Speed over Time")
plt.xlabel("Time (s)")
plt.ylabel("Speed (m/s)")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(sensor_log.time_log, sensor_log.air_quality, marker='o', color='green')
plt.title("🫁 Air Quality Index over Time")
plt.xlabel("Time (s)")
plt.ylabel("AQI")
plt.grid(True)

plt.tight_layout()
plt.show()
