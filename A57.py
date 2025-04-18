# ----------------------------------------------------
# Algorithm 57: AI Model Flow
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

# Drone State Parameters
sensor_data = {
    "altitude": 10.0,
    "velocity": 0.0,
    "battery_level": 95,
    "wind_speed": 5.0,
}
target_altitude = 10.0

# AI Model Parameters
decision_thresholds = {
    "altitude_threshold": 1.0,  # If altitude difference exceeds 1m, adjust hover.
    "battery_threshold": 20.0,  # If battery drops below 20%, land.
    "wind_threshold": 15.0,     # If wind speed is too high, adjust flight.
}

# Decision making function (AI Model)
def ai_decision_making(sensor_data, decision_thresholds):
    """AI decision-making flow based on sensor data and defined thresholds."""
    # Step 1: Collect sensor data and evaluate against thresholds
    decisions = []
    
    # Step 2: Decision logic based on altitude
    if abs(sensor_data["altitude"] - target_altitude) > decision_thresholds["altitude_threshold"]:
        decisions.append("Adjust Hover")
    
    # Step 3: Decision logic based on battery level
    if sensor_data["battery_level"] < decision_thresholds["battery_threshold"]:
        decisions.append("Land for Charging")
    
    # Step 4: Decision logic based on wind speed
    if sensor_data["wind_speed"] > decision_thresholds["wind_threshold"]:
        decisions.append("Adjust Flight Path")
    
    return decisions

# Simulation loop
decisions_list = []
sensor_data["altitude"] = round(random.uniform(8.0, 12.0), 2)  # Random altitude for simulation
sensor_data["wind_speed"] = round(random.uniform(0.0, 20.0), 2)  # Random wind speed for simulation

for i in range(5):
    # Step 5: AI decision making flow
    decisions = ai_decision_making(sensor_data, decision_thresholds)
    
    # Step 6: Simulate change in sensor data (for flow progression)
    sensor_data["altitude"] += random.uniform(-0.2, 0.2)  # Random change in altitude
    sensor_data["wind_speed"] += random.uniform(-1.0, 1.0)  # Random change in wind speed
    sensor_data["battery_level"] -= 0.5  # Decrease battery level slightly
    
    # Store decisions for visualization
    decisions_list.append(decisions)
    
    print(f"Iteration {i+1}: Decisions={decisions}, Altitude={sensor_data['altitude']:.2f}, Wind Speed={sensor_data['wind_speed']:.2f}, Battery Level={sensor_data['battery_level']:.2f}")

# 🎨 Plotting Decision Flow
plt.figure(figsize=(10, 5))

# Decision Plot
decision_counts = [len(decisions) for decisions in decisions_list]

plt.plot(range(1, 6), decision_counts, 'bo-', label="Number of Decisions")
plt.title("AI Model Flow (Decision Making)")
plt.xlabel("Iteration")
plt.ylabel("Number of Decisions")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: AI Model Flow Processing:")

# Simulate sensor updates and decision flow for hardware
sensor_data["altitude"] = 10.0  # Initial value
sensor_data["battery_level"] = 95  # Initial value

for i in range(5):
    # Step 5: AI decision making flow
    decisions = ai_decision_making(sensor_data, decision_thresholds)
    
    # Step 6: Simulate change in sensor data for hardware
    sensor_data["altitude"] += random.uniform(-0.2, 0.2)  # Random fluctuation in altitude
    sensor_data["wind_speed"] += random.uniform(-1.0, 1.0)  # Random fluctuation in wind speed
    sensor_data["battery_level"] -= 0.5  # Battery decreases over time
    
    print(f"[BACKEND] Iteration {i+1}: Decisions={decisions}, Altitude={sensor_data['altitude']:.2f}, Wind Speed={sensor_data['wind_speed']:.2f}, Battery Level={sensor_data['battery_level']:.2f}")

print("\n✅ AI model flow processed successfully.")
