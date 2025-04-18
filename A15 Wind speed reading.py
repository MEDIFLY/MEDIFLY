import random
import matplotlib.pyplot as plt

# ------------------------ FRONTEND: Simulated Wind Speed Readings ------------------------

def simulate_wind_speed_readings():
    print("\n🌬️ Simulated Wind Speed Readings:\n")
    wind_speeds = []

    for i in range(5):  # 5 Iterations
        wind = random.uniform(0.5, 5.5)  # Wind speed in m/s
        wind_speeds.append(wind)
        print(f"💨 Iteration {i + 1}: Wind Speed = {wind:.2f} m/s")

    # Plot the simulated wind speed values
    plt.figure(figsize=(7, 4))
    plt.plot(wind_speeds, marker='s', color='darkorange')
    plt.title("Simulated Wind Speed Readings")
    plt.xlabel("Iteration")
    plt.ylabel("Wind Speed (m/s)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return wind_speeds

# ------------------------ BACKEND: Wind Speed Sensor Placeholder ------------------------

def read_wind_speed_backend():
    # In a real system, you'd connect an anemometer sensor
    # Here we simulate a backend value
    wind_speed = 3.2  # Simulated fixed backend value
    print(f"\n🔧 Backend Sensor Reading: Wind Speed = {wind_speed:.2f} m/s")
    return wind_speed

# ------------------------ Run the Simulation ------------------------

simulate_wind_speed_readings()
read_wind_speed_backend()
