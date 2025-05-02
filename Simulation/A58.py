# ----------------------------------------------------
# Algorithm 58: AI Model for Calculating Optimal Payload Drop Offset
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

# Function to calculate optimal payload drop offset
def calculate_payload_drop_offset(drone_params, payload_drop_params):
    """AI logic to calculate optimal payload drop offset."""
    # Calculate offset based on drone's current altitude, velocity, and wind speed
    wind_offset = drone_params["wind_speed"] * payload_drop_params["wind_factor"]
    altitude_offset = drone_params["altitude"] * payload_drop_params["altitude_factor"]
    velocity_offset = drone_params["velocity"] * payload_drop_params["velocity_factor"]
    
    # Total offset is the sum of all factors
    total_offset = wind_offset + altitude_offset + velocity_offset
    return total_offset

# Simulate the payload drop calculations
offsets = []
for i in range(5):
    # Calculate the drop offset
    offset = calculate_payload_drop_offset(drone_params, payload_drop_params)
    
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
plt.title("AI Model for Calculating Optimal Payload Drop Offset")
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
    # Calculate the drop offset for hardware deployment
    offset = calculate_payload_drop_offset(drone_params, payload_drop_params)
    
    # Simulate changes in drone parameters (to reflect real-time updates)
    drone_params["altitude"] += random.uniform(-0.5, 0.5)  # Altitude fluctuation
    drone_params["velocity"] += random.uniform(-1.0, 1.0)  # Velocity fluctuation
    drone_params["wind_speed"] += random.uniform(-2.0, 2.0)  # Wind speed fluctuation
    
    print(f"[BACKEND] Iteration {i+1}: Payload Drop Offset={offset:.2f} meters, Altitude={drone_params['altitude']:.2f}, Velocity={drone_params['velocity']:.2f}, Wind Speed={drone_params['wind_speed']:.2f}")

print("\n✅ Payload drop offset processed successfully.")
