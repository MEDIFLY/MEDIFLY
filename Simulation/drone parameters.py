import time
import random
import matplotlib.pyplot as plt

# Backend Drone Parameter Check Function
def check_drone_parameters(iteration):
    print(f"\n📦 Drone Parameter Check - Iteration {iteration + 1}")

    max_altitude = random.uniform(90.0, 110.0)  # meters
    max_speed = random.uniform(18.0, 22.0)      # m/s
    payload_capacity = random.uniform(1.8, 2.2)  # kg
    flight_time = random.uniform(28, 32)         # minutes
    battery_voltage = random.uniform(22.0, 25.0)  # volts

    print(f"📏 Max Altitude: {max_altitude:.2f} m")
    print(f"🚀 Max Speed: {max_speed:.2f} m/s")
    print(f"📦 Payload Capacity: {payload_capacity:.2f} kg")
    print(f"⏱️ Flight Time: {flight_time:.2f} mins")
    print(f"🔋 Battery Voltage: {battery_voltage:.2f} V")

    return max_altitude, max_speed, payload_capacity, flight_time, battery_voltage

# Lists to store values for plotting
altitudes = []
speeds = []
payloads = []
flight_times = []
voltages = []

# 5 Iterations
print("🔁 Performing 5 iterations of drone parameter check...")
for i in range(5):
    alt, spd, load, time_, volt = check_drone_parameters(i)
    altitudes.append(alt)
    speeds.append(spd)
    payloads.append(load)
    flight_times.append(time_)
    voltages.append(volt)
    time.sleep(1)

# 📊 Plotting the parameters
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(altitudes, marker='o', color='blue')
plt.title('Max Altitude per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Altitude (m)')

plt.subplot(2, 3, 2)
plt.plot(speeds, marker='s', color='green')
plt.title('Max Speed per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Speed (m/s)')

plt.subplot(2, 3, 3)
plt.plot(payloads, marker='^', color='purple')
plt.title('Payload Capacity per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Payload (kg)')

plt.subplot(2, 3, 4)
plt.plot(flight_times, marker='D', color='orange')
plt.title('Flight Time per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Time (mins)')

plt.subplot(2, 3, 5)
plt.plot(voltages, marker='x', color='red')
plt.title('Battery Voltage per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Voltage (V)')

plt.tight_layout()
plt.show()
