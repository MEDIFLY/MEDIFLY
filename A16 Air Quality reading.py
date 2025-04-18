import random
import matplotlib.pyplot as plt

# ----------------- FRONTEND: Simulated Air Quality Readings -----------------

def simulate_air_quality_readings():
    print("\n🌫️ Simulated Air Quality Index (AQI) Readings:\n")
    air_quality = []

    for i in range(5):
        aqi = random.randint(50, 150)  # Simulate AQI between 50 and 150
        air_quality.append(aqi)
        print(f"🌡️ Iteration {i + 1}: AQI = {aqi}")

    # 📊 Plot the AQI values
    plt.figure(figsize=(6, 4))
    plt.plot(air_quality, marker='^', color='darkcyan', linestyle='--')
    plt.title("Simulated Air Quality Index Readings")
    plt.xlabel("Iteration")
    plt.ylabel("AQI Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return air_quality

# ----------------- BACKEND: Placeholder for Sensor Data -----------------

def read_air_quality_backend():
    # This part simulates backend sensor reading (e.g., MQ135)
    backend_aqi = 92  # Sample hardcoded sensor value
    print(f"\n🔧 Backend Sensor Reading: AQI = {backend_aqi}")
    return backend_aqi

simulate_air_quality_readings()
read_air_quality_backend()

