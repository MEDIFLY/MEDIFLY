# A79.py – Algorithm 79: Environment Sensor Simulation for Real-Time Data

import random
import time
import matplotlib.pyplot as plt

# ------------------------------
# Frontend: Visualization + Plot
# ------------------------------

# Function to visualize environment sensor data
def plot_sensor_data(sensor_data):
    time_steps = list(sensor_data.keys())
    temperature = [sensor_data[step]['temperature'] for step in time_steps]
    humidity = [sensor_data[step]['humidity'] for step in time_steps]
    wind_speed = [sensor_data[step]['wind_speed'] for step in time_steps]
    air_quality = [sensor_data[step]['air_quality'] for step in time_steps]
    
    plt.figure(figsize=(12, 6))

    # Plot each environmental factor over time
    plt.subplot(2, 2, 1)
    plt.plot(time_steps, temperature, label='Temperature (°C)', color='orange')
    plt.title('Temperature Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')

    plt.subplot(2, 2, 2)
    plt.plot(time_steps, humidity, label='Humidity (%)', color='blue')
    plt.title('Humidity Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Humidity (%)')

    plt.subplot(2, 2, 3)
    plt.plot(time_steps, wind_speed, label='Wind Speed (m/s)', color='green')
    plt.title('Wind Speed Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Wind Speed (m/s)')

    plt.subplot(2, 2, 4)
    plt.plot(time_steps, air_quality, label='Air Quality (AQI)', color='red')
    plt.title('Air Quality Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Air Quality Index (AQI)')

    plt.tight_layout()
    plt.show()

# ------------------------------
# Backend: Sensor Data Simulation
# ------------------------------

# Function to simulate environment sensor data (temperature, humidity, wind speed, air quality)
def simulate_environmental_data():
    # Simulating random environmental sensor data for each factor
    temperature = random.uniform(15, 35)  # Random temperature between 15°C and 35°C
    humidity = random.uniform(30, 80)  # Random humidity between 30% and 80%
    wind_speed = random.uniform(0, 15)  # Random wind speed between 0 m/s and 15 m/s
    air_quality = random.randint(50, 200)  # Random AQI between 50 and 200

    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "air_quality": air_quality
    }

# Function to simulate a series of environmental data points over time
def generate_environment_data_simulation(duration=10):
    sensor_data = {}

    for time_step in range(duration):
        print(f"Simulating environmental data for time step {time_step + 1}...")
        sensor_data[time_step] = simulate_environmental_data()
        time.sleep(1)  # Simulate a 1-second interval between data points

    print("✅ Environmental data simulation complete.")
    return sensor_data

# ------------------------------
# Initialization
# ------------------------------

# Simulate environmental data over a 10-second duration
duration = 10  # Simulating for 10 time steps
sensor_data = generate_environment_data_simulation(duration)

# Plot the simulated sensor data
plot_sensor_data(sensor_data)
