# ----------------------------------------------------
# Algorithm 59: AI Model Class for Payload Drop Prediction
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import random
import numpy as np

# =======================
# FRONTEND: Simulation
# =======================

# Drone and Environmental Parameters
drone_params = {
    "altitude": 12.0,  # in meters
    "velocity": 10.0,  # in m/s
    "wind_speed": 5.0,  # in m/s
    "battery_level": 85,  # percentage
    "latitude": 19.0760,  # placeholder for simulation
    "longitude": 72.8777,  # placeholder for simulation
}

# AI Model Parameters for Payload Drop
payload_drop_params = {
    "wind_factor": 0.5,  # how much wind affects payload drop position
    "altitude_factor": 0.3,  # how much altitude affects offset
    "velocity_factor": 0.2,  # how much velocity affects offset
}

# Payload Drop Prediction AI Model Class
class PayloadDropPrediction:
    def __init__(self, wind_factor, altitude_factor, velocity_factor):
        """Initialize the AI Model with factors affecting payload drop."""
        self.wind_factor = wind_factor
        self.altitude_factor = altitude_factor
        self.velocity_factor = velocity_factor

    def calculate_offset(self, drone_params):
        """Calculate the offset for payload drop based on drone parameters."""
        wind_offset = drone_params["wind_speed"] * self.wind_factor
        altitude_offset = drone_params["altitude"] * self.altitude_factor
        velocity_offset = drone_params["velocity"] * self.velocity_factor
        total_offset = wind_offset + altitude_offset + velocity_offset
        return total_offset

# Instantiate the AI Model for Payload Drop Prediction
model = PayloadDropPrediction(payload_drop_params["wind_factor"],
                              payload_drop_params["altitude_factor"],
                              payload_drop_params["velocity_factor"])

# Simulate the payload drop calculations
offsets = []
for i in range(5):
    # Calculate the drop offset using the model class
    offset = model.calculate_offset(drone_params)
    
    # Simulate slight random changes in drone parameters
    drone_params["altitude"] += random.uniform(-0.5, 0.5)  # Altitude change
    drone_params["velocity"] += random.uniform(-1.0, 1.0)  # Velocity change
    drone_params["wind_speed"] += random.uniform(-2.0, 2.0)  # Wind speed change
    
    # Append the calculated offset
    offsets.append(offset)
    
    print(f"Iteration {i+1}: Drop Offset={offset:.2f} meters")

# 🎨 Plotting Payload Drop Offset
plt.figure(figsize=(10, 5))

# Plot drop offsets over iterations
plt.plot(range(1, 6), offsets, 'go-', label="Calculated Payload Drop Offset")
plt.title("AI Model for Payload Drop Prediction")
plt.xlabel("Iteration")
plt.ylabel("Payload Drop Offset (meters)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Payload Drop Offset Processing:")

# Simulate backend logic for real-time calculation of the drop offset
for i in range(5):
    # Calculate the drop offset for hardware deployment using the model
    offset = model.calculate_offset(drone_params)
    
    # Simulate changes in drone parameters (to reflect real-time updates)
    drone_params["altitude"] += random.uniform(-0.5, 0.5)  # Altitude fluctuation
    drone_params["velocity"] += random.uniform(-1.0, 1.0)  # Velocity fluctuation
    drone_params["wind_speed"] += random.uniform(-2.0, 2.0)  # Wind speed fluctuation
    
    print(f"[BACKEND] Iteration {i+1}: Payload Drop Offset={offset:.2f} meters, Altitude={drone_params['altitude']:.2f}, Velocity={drone_params['velocity']:.2f}, Wind Speed={drone_params['wind_speed']:.2f}")

print("\n✅ Payload drop prediction processed successfully.")
