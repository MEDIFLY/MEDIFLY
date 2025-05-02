import random
import time
import matplotlib.pyplot as plt

# ------------------ 🌐 Frontend Simulation ------------------

# Simulate 5 temperature readings
temperature_readings = []

print("\n🌡️ Simulated Temperature Readings:\n")

for i in range(5):
    temp = random.uniform(28.0, 35.0)  # Simulated temperature range
    temperature_readings.append(temp)
    print(f"📊 Iteration {i+1}: Temperature = {temp:.2f} °C")
    time.sleep(1)

# Plot the readings
plt.figure(figsize=(6, 4))
plt.plot(temperature_readings, marker='o', color='tomato')
plt.title("Simulated Temperature Readings")
plt.xlabel("Iteration")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------ 🛠️ Backend Placeholder ------------------

def read_temperature_backend():
    """
    Placeholder for real temperature sensor logic (e.g., DHT22 or LM35).
    Returns a simulated value for now.
    """
    return random.uniform(28.0, 35.0)  # Replace with real sensor read
