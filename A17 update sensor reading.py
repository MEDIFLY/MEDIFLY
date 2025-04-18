import random
import matplotlib.pyplot as plt

# ----------------- FRONTEND: Simulate Sensor Data Updates -----------------

def simulate_sensor_updates():
    print("\n📡 Simulated Environmental Sensor Updates:\n")

    temperatures = []
    humidities = []
    wind_speeds = []
    air_qualities = []

    for i in range(5):
        temp = round(random.uniform(25.0, 35.0), 2)        # Celsius
        humidity = round(random.uniform(30.0, 70.0), 2)     # %
        wind = round(random.uniform(0.0, 15.0), 2)          # km/h
        aqi = random.randint(50, 150)                      # AQI

        temperatures.append(temp)
        humidities.append(humidity)
        wind_speeds.append(wind)
        air_qualities.append(aqi)

        print(f"🔁 Iteration {i + 1}: Temp = {temp}°C | Humidity = {humidity}% | Wind = {wind} km/h | AQI = {aqi}")

    # 📊 Plotting all four in a 2x2 grid
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(temperatures, marker='o', color='red')
    plt.title("Temperature over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("°C")

    plt.subplot(2, 2, 2)
    plt.plot(humidities, marker='s', color='blue')
    plt.title("Humidity over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("%")

    plt.subplot(2, 2, 3)
    plt.plot(wind_speeds, marker='^', color='green')
    plt.title("Wind Speed over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("km/h")

    plt.subplot(2, 2, 4)
    plt.plot(air_qualities, marker='D', color='purple')
    plt.title("Air Quality Index over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("AQI")

    plt.tight_layout()
    plt.show()

    return temperatures, humidities, wind_speeds, air_qualities

# ----------------- BACKEND: Placeholder for Real-Time Update -----------------

def update_sensor_backend():
    print("\n🛠️ Backend Sensor Update Triggered...")
    updated_data = {
        "temperature": 29.8,
        "humidity": 58.5,
        "wind_speed": 7.4,
        "air_quality": 96
    }
    print(f"📥 Updated Sensor Data (Backend): {updated_data}")
    return updated_data

# ----------------- RUN BOTH SIMULATION + BACKEND -----------------

simulate_sensor_updates()
update_sensor_backend()
