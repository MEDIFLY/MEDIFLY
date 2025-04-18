import random
import time
import matplotlib.pyplot as plt

# -------------------- Backend Placeholder Function --------------------
def detect_environmental_conditions_backend():
    """
    This function is a placeholder for real sensor interfacing in hardware.
    In actual integration, it would read from environmental sensors.
    """
    temperature = random.uniform(28.0, 35.0)         # Celsius
    humidity = random.uniform(40.0, 70.0)            # %
    wind_speed = random.uniform(0.5, 5.0)            # m/s
    air_quality = random.randint(50, 150)            # AQI
    return temperature, humidity, wind_speed, air_quality

# -------------------- Frontend Simulation + Plotting --------------------

# Lists to store 5 iteration values
temperatures = []
humidities = []
wind_speeds = []
aqi_values = []

print("🌍 Simulating Environmental Condition Detection for 5 Iterations...\n")

for i in range(5):
    print(f"📡 Iteration {i + 1} Environmental Readings:")

    # Call backend (placeholder) function
    temp, hum, wind, aqi = detect_environmental_conditions_backend()

    print(f"🌡️ Temperature: {temp:.2f} °C")
    print(f"💧 Humidity: {hum:.2f} %")
    print(f"🍃 Wind Speed: {wind:.2f} m/s")
    print(f"🏭 Air Quality Index (AQI): {aqi}")

    # Store for plots
    temperatures.append(temp)
    humidities.append(hum)
    wind_speeds.append(wind)
    aqi_values.append(aqi)

    time.sleep(1)
    print("-" * 50)

# -------------------- Plotting Environmental Conditions --------------------

plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.plot(temperatures, marker='o', color='red')
plt.title('Temperature per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Temperature (°C)')

plt.subplot(2, 2, 2)
plt.plot(humidities, marker='s', color='blue')
plt.title('Humidity per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Humidity (%)')

plt.subplot(2, 2, 3)
plt.plot(wind_speeds, marker='^', color='green')
plt.title('Wind Speed per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Speed (m/s)')

plt.subplot(2, 2, 4)
plt.plot(aqi_values, marker='x', color='purple')
plt.title('Air Quality Index per Iteration')
plt.xlabel('Iteration')
plt.ylabel('AQI')

plt.tight_layout()
plt.show()
