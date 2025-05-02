# AI Model 1: IoT Sensor Data Collection
# Includes: 5 Iterations | Frontend (Simulation + Plotting) | Backend (Hardware Logic Placeholder)

import time
import random
import matplotlib.pyplot as plt

# FRONTEND: Simulated Sensor Data Collection & Visualization
def simulate_sensor_data():
    gps_lat = random.uniform(12.90, 12.95)
    gps_lon = random.uniform(77.60, 77.65)
    imu_acc = [random.uniform(-1, 1) for _ in range(3)]
    temperature = random.uniform(25, 35)
    lidar_distance = random.uniform(1, 10)
    return {
        'gps': (gps_lat, gps_lon),
        'imu': imu_acc,
        'temperature': temperature,
        'lidar': lidar_distance
    }

# Noise Reduction (Simple Moving Average Filter)
def filter_noise(data_list):
    return sum(data_list) / len(data_list)

# Store structured sensor data
structured_data = []

# Visualization setup
gps_lat_list, gps_lon_list = [], []
temp_list, lidar_list = [], []

# Run 5 Iterations (as per MEDIFLY structure)
for iteration in range(5):
    print(f"\n📡 Iteration {iteration+1}/5 - Collecting Sensor Data...")

    # FRONTEND: Simulate Data
    data = simulate_sensor_data()

    # Preprocessing: Filter IMU noise
    filtered_imu = [round(filter_noise([acc]), 2) for acc in data['imu']]

    # Structuring Data
    structured = {
        'iteration': iteration + 1,
        'gps': {'lat': round(data['gps'][0], 6), 'lon': round(data['gps'][1], 6)},
        'imu': {'acc_x': filtered_imu[0], 'acc_y': filtered_imu[1], 'acc_z': filtered_imu[2]},
        'temperature': round(data['temperature'], 2),
        'lidar_distance': round(data['lidar'], 2)
    }
    structured_data.append(structured)

    # Store for plots
    gps_lat_list.append(structured['gps']['lat'])
    gps_lon_list.append(structured['gps']['lon'])
    temp_list.append(structured['temperature'])
    lidar_list.append(structured['lidar_distance'])

    print(f"✅ Collected Data: {structured}")
    time.sleep(1)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(gps_lat_list, gps_lon_list, marker='o', color='blue')
plt.title('GPS Coordinates (Simulated Path)')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(range(1, 6), temp_list, label='Temperature (°C)', color='red', marker='o')
plt.plot(range(1, 6), lidar_list, label='Lidar Distance (m)', color='green', marker='x')
plt.title('Sensor Data Over Iterations')
plt.xlabel('Iteration')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# BACKEND: Placeholder for actual sensor integration (To replace simulate_sensor_data)
def read_actual_sensor_data():
    # Example: Replace with real sensor reading code
    # GPS: Serial read
    # IMU: I2C read from MPU6050 or similar
    # Temp: GPIO or I2C sensor like DHT11
    # Lidar: UART or I2C based reading
    return {
        'gps': (0.0, 0.0),  # Replace with actual GPS read
        'imu': [0.0, 0.0, 0.0],  # Replace with IMU data
        'temperature': 0.0,  # Replace with temp sensor
        'lidar': 0.0  # Replace with LIDAR read
    }

# To switch to hardware: replace `simulate_sensor_data()` with `read_actual_sensor_data()`
