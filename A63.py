# ----------------------------------------------------
# Algorithm 63: Input Parameter Definition
# Frontend: Simulation + Plot
# Backend: Hardware Logic
# 5 Iterations Included
# ----------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# =======================
# FRONTEND: Simulation
# =======================

# Define the input parameters for payload drop
input_parameters = {
    "drone_weight": 1.5,  # in kg
    "payload_weight": 0.5,  # in kg
    "drop_height": 100.0,  # in meters
    "drop_speed": 10.0,  # in m/s
    "wind_speed": 5.0,  # in m/s
    "temperature": 25.0,  # in Celsius
    "altitude": 150.0,  # in meters
}

# Define function to update input parameters
def update_input_parameters(parameters, update_values):
    """Update the input parameters with new values."""
    for key, value in update_values.items():
        if key in parameters:
            parameters[key] = value
    return parameters

# Simulate the update of input parameters over 5 iterations
updated_parameters = []
for i in range(5):
    # Simulate slight variations in the environment and drone parameters
    update_values = {
        "wind_speed": np.random.uniform(4.0, 7.0),
        "drop_speed": np.random.uniform(8.0, 12.0),
        "temperature": np.random.uniform(20.0, 30.0),
    }
    
    # Update the input parameters
    updated_parameters.append(update_input_parameters(input_parameters, update_values))
    print(f"Iteration {i+1}: Updated Parameters = {updated_parameters[-1]}")

# 🎨 Plot the input parameters over iterations
plt.figure(figsize=(10, 5))

# Plotting the change in wind speed and drop speed
wind_speeds = [param["wind_speed"] for param in updated_parameters]
drop_speeds = [param["drop_speed"] for param in updated_parameters]
plt.plot(range(1, 6), wind_speeds, 'bo-', label="Wind Speed (m/s)")
plt.plot(range(1, 6), drop_speeds, 'ro-', label="Drop Speed (m/s)")

plt.title("Input Parameter Changes Over Iterations")
plt.xlabel("Iteration")
plt.ylabel("Speed (m/s)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# =======================
# BACKEND: Hardware Logic
# =======================

print("\n⚙️ BACKEND: Input Parameter Definition:")

# Simulate backend logic for applying input parameters in real-time hardware
for i in range(5):
    # Apply updated input parameters for hardware execution
    updated_params = updated_parameters[i]
    
    # Simulate the application of parameters (simplified here)
    print(f"[BACKEND] Iteration {i+1}: Updated Parameters = {updated_params}")

print("\n✅ Input Parameters Defined and Updated Successfully.")
