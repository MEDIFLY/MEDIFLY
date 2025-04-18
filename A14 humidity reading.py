import random
import matplotlib.pyplot as plt

# ------------------------ FRONTEND: Simulated Humidity Readings ------------------------

def simulate_humidity_readings():
    print("\n💧 Simulated Humidity Readings:\n")
    humidity_data = []

    for i in range(5):  # 5 Iterations
        humidity = random.uniform(45.0, 65.0)  # Simulated humidity in %
        humidity_data.append(humidity)
        print(f"📊 Iteration {i + 1}: Humidity = {humidity:.2f} %")

    # Plot the simulated humidity values
    plt.figure(figsize=(7, 4))
    plt.plot(humidity_data, marker='o', color='dodgerblue')
    plt.title("Simulated Humidity Readings")
    plt.xlabel("Iteration")
    plt.ylabel("Humidity (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return humidity_data

# ------------------------ BACKEND: Humidity Sensor Function (Placeholder) ------------------------

def read_humidity_backend():
    # In real hardware, you'd interface with a sensor like DHT22
    # For now, we simulate a fixed value
    humidity_value = 55.0  # Simulated constant for placeholder
    print(f"\n🔧 Backend Sensor Reading: Humidity = {humidity_value:.2f} %")
    return humidity_value

# ------------------------ Run Simulation ------------------------

simulate_humidity_readings()
read_humidity_backend()
